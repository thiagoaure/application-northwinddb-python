from datetime import datetime
import json
import os
from config_connection import db_config_mongo
from constants import TABLE_NAMES

client = db_config_mongo
db = client["northwind_mongodb"]

table_names = [item.value for item in TABLE_NAMES]

def read_mongo():
    try:
        for table_name in table_names:

            collection = db[table_name]
            cur = collection.find()

            dataList = []
            for data in cur:
                data.pop("_id", None)
                dataList.append(dict(data))
                
            tablePath = f'data\mongoDb\{table_name}\{datetime.now().date()}'
            if not os.path.exists(tablePath):
                os.makedirs(tablePath)
                with open(f"{tablePath}\{table_name}.json", "w") as json_file:
                    json.dump(dataList, json_file)
                    
    except Exception as e:
        print(f"Error processing table {table_name} - read_mongo: {str(e)} ")