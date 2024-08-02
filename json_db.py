from __future__ import annotations

import os
import json
from typing import List
from .db import DB




class JsonDB(DB):

    def __init__(self, db_name: str, tables: List[str] = None):
        self.tables = tables
        self.db: dict = {"count": [], "id_track": []}
        self.db_name = db_name
        self.file_path = self.get_path()
        self.load_db()

    def save(self):
        with open(file=self.file_path, mode="w") as f:
            json.dump(self.db, f, indent=4)
        return True
    def get_path(self):
        path = os.path.dirname(os.path.abspath(__file__))
        return os.path.join(path, 'data', self.db_name)
    def load_db(self):
        if not os.path.exists(self.file_path):
            with open(file=self.file_path, mode="w+") as f:
                json.dump(self.db, f, indent=4)
        else:
            with open(self.file_path, 'r+') as file:
                self.db = json.load(file)
        if self.tables:
            for table in self.tables:
                self.add_table(table)
        self.save()
        return


    def __str__(self):
        return str(json.dumps(self.db, indent=4))

    def initialize_count(self, table_name: str):
        self.db["count"].append({"id": table_name, "count": 0})
        return True

    def get_count(self, table_name: str):
        data = self.get_by_id("count", table_name)
        if not data:
            return False
        return data.get("count")

    def increase_counter(self, table_name: str):
        count = self.get_count(table_name)
        return self.update_by_query("count", {"id": table_name}, {"count": count + 1})
    def decrease_counter(self, table_name: str):
        count = self.get_count(table_name)
        return self.update_by_query("count", {"id": table_name}, {"count": count - 1})

    def get_id(self, table_name):
        return self.get_count(table_name) + 1

    def _table_exists(self, table_name: str, show_message: bool = True):
        if table_name not in self.db:
            if show_message: print(f"invalid table: {table_name}")
            return False
        return True


    def _duplicate_check(self, table_name: str, data: dict):
        for pre_exist_data in self.db[table_name]:
            print(pre_exist_data)
            if data["id"] == pre_exist_data.get("id"):
                print(f"data already exist in table: {table_name} for the id: {data['id']}")
                return True
        return False

    def add(self, table_name: str, data: dict):
        if not self._table_exists(table_name):
            return False
        # if self._duplicate_check(table_name, data):
        #     return False
        id = self.get_count(table_name)
        data.update({"id": id})
        self.db[table_name].append(data)
        self.increase_counter(table_name)
        self.save()
        return True


    def add_many(self, table_name: str, data_list: List[dict]):
        if not self._table_exists(table_name):
            return False
        for data in data_list:
            # if self._duplicate_check(table_name, data):
            #     return False
            self.db[table_name].append(data)
            self.increase_counter(table_name)
            self.save()
        return True

    def get_table(self, table_name: str):
        if not self._table_exists(table_name):
            return []
        return self.db[table_name]

    def add_table(self, table_name: str):
        if self._table_exists(table_name, show_message=False):
            print(f"table: {table_name} already exist...")
            return False
        self.db[table_name] = []
        self.initialize_count(table_name)
        self.save()
        return


    def get_all(self, table_name: str):
        return self.db.get(table_name, [])


    def get_by_id(self, table_name: str, pk: int | str):
        if not self._table_exists(table_name):
            return False
        for data in self.db[table_name]:
            if data.get("id") == pk:
                return data
        return {}


    def get_by_quantity(self, table_name: str, quantity: int):
        if not self._table_exists(table_name):
            return False
        return self.db[table_name][:quantity] if len(self.db[table_name]) >= quantity else []


    def get_by_query(self, table_name: str, query: dict):
        result = []
        if table_name not in self.db:
            print(f"{table_name} table is not present")
            return result
        for data in self.get_table(table_name):
            if all([data.get(key) == value for key, value in query.items()]):
                result.append(data)
        return result


    def update_by_id(self, table_name: str, pk: int, data: dict):
        if not self._table_exists(table_name):
            return False
        for details in self.db[table_name]:
            if details.get("id") == pk:
                details.update(data)
                self.save()
                return True
        return False


    def update_by_query(self, table_name: str, query: dict, data: dict):
        if not self._table_exists(table_name):
            return False
        for details in self.db[table_name]:
            if all([details.get(key) == value for key, value in query.items()]):
                details.update(data)
                self.save()
                return True
        return False


    def delete_by_id(self, table_name: str, pk: int):
        if not self._table_exists(table_name):
            return False
        for i, data in enumerate(self.db[table_name]):
            if data.get("id") == pk:
                self.db[table_name].pop(i)
                # self.decrease_counter(table_name=table_name)
                self.save()
                return True
        return False


    def delete_all_table_details(self):
        for details in self.db.values():
            details.clear()
        self.save()

    def delete_all(self):
        self.db = {}
        self.save()