from pymongo import MongoClient, collection

connection_string = "mongodb://localhost:27017/?readPreference=primary&appname=MongoDB%20Compass&ssl=false"
client = MongoClient(connection_string)
print(client.list_database_names)

db = client.get_database('inventory')

collection = db.get_collection('items')

document = {'item': "canvas", "qty": 100, "tags": ['cotton'], "size":"h"}

# connection_string = "mongodb//172.20.0.1:27017/scrappingdb"
# client = MongoClient(connection_string)
# print(client.list_database_names)

# mongodb://localhost:27017/?readPreference=primary&appname=MongoDB%20Compass&ssl=false









    # pop= driver.find_element_by_class_name("[id='popover-x']")
# id="popover-foreground"


# 172.20.0.1 

# mongodb://127.0.0.1:27017/?compressors=disabled&gssapiServiceName=mongodb

# popover-x

# class="popover-x ita-popover-x"