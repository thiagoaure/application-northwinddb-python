from datetime import datetime
import json
from config_connection import db_config_mongo
from constants import TABLE_NAMES

client = db_config_mongo
db = client["northwind_mongodb"]

table_names = [item.value for item in TABLE_NAMES]

def insert_data_mongodb():
    try:
        for table_name in table_names:
            if table_name == "order_details":
                pathTable = f"data\csv\{table_name}\{datetime.now().date()}\{table_name}.json"
            else:
                pathTable = f"data\postgres\{table_name}\{datetime.now().date()}\{table_name}.json"
            with open(pathTable, "r") as file:
                data = json.load(file)
                if len(data) == 0 or data is None:
                    print(f"Não contém dados novos na tabela {table_name}")
                else:
                    collection = db[table_name]
                    collection.insert_many(data)
    except Exception as e:
         print(f"Error processing table {table_name} - insert_data_mongodb: {str(e)} ")

