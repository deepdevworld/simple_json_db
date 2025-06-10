# SIMPLE JSON DB

I built a lightweight JSON-based database using Python, designed for simple, schema-less data storage without external dependencies. The database leverages Python's built-in json module to store and retrieve data in a human-readable format, supporting basic CRUD (Create, Read, Update, Delete) operations.

Key features include:

File-based persistence – Data is saved to a JSON file for durability.

Simple API – Easy-to-use methods for managing records.

No rigid schema – Flexible storage for dictionaries and lists.

Portability – Database files can be easily shared or migrated.


## Setup DB
* Import the package
```.py 
from  simple_json_db import JsonDB
```
* Initialized the object

The "demo.json" will be created inside the data folder

```.py 
db = JsonDB(db_name="demo.json")    
```

## Add Table

```.py 
db.add_table(table_name="user")    
```

## Add Data

```.py 
db.add(table_name="user", data={"name": "alex"})    
```

## Add Many Data

```.py 
db.add(table_name="user", data_list=[{"name": "alex"}, {"name": "bixby"}])    
```

## Get Table Data

```.py 
db.get_all(table_name="user") 
```

## Get Data By Id

```.py 
db.get_by_id(table_name="user", pk=1)
```

## Get Table Data By Query

```.py 
db.get_by_query(table_name="user", query={"name": "alex"}) 
```






