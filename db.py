from abc import ABC, abstractmethod
from typing import List


class DB(ABC):

    @abstractmethod
    def get_count(self, table_name: str):
        """returns robot id"""
    @abstractmethod
    def get_id(self, table_name: str):
        pass


    @abstractmethod
    def load_db(self):
        """returns the new db object"""

    @abstractmethod
    def save(self):
        pass


    @abstractmethod
    def add_table(self, table_name: str):
        pass

    @abstractmethod
    def get_table(self, table_name: str):
        pass

    @abstractmethod
    def add(self, table_name: str, data: dict):
        """adds the data"""

    @abstractmethod
    def add_many(self, table_name: str, data_list: List[dict]):
        """adds the data"""

    @abstractmethod
    def get_all(self, table_name: str):
        """"""

    @abstractmethod
    def get_by_id(self, table_name: str, pk: int):
        """"""

    @abstractmethod
    def get_by_quantity(self, table_name: str, quantity: int):
        """"""

    @abstractmethod
    def get_by_query(self, table_name: str, query: dict):
        """"""

    @abstractmethod
    def update_by_id(self, table_name: str, pk: int, data: dict):
        """"""

    @abstractmethod
    def update_by_query(self, table_name: str, query: dict, data: dict):
        """"""

    @abstractmethod
    def delete_by_id(self, table_name: str, pk: int):
        """"""

    @abstractmethod
    def delete_all(self):
        """"""

    @abstractmethod
    def delete_all_table_details(self):
        pass
