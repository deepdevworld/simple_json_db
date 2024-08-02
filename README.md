# SIMPLE JSON DB



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

## Get Table Data

```.py 
db.get_all(table_name="user") 
```

## Get Data By Id

```.py 
db.get_by_id(table_name="user", pk=1)
```





