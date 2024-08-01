from json_db import JsonDB


db = JsonDB(db_name="demo.json", tables=["user", "location"])
db.add("user", {"name": "sushil"})
print(db.get_all(table_name="user"))
# db.delete_by_id("user", pk=1)