import os
import psycopg2
import json
from datetime import datetime, date
from config_connection import db_config_read
from constants import TABLE_NAMES

table_names = [item.value for item in TABLE_NAMES]
table_names.remove("order_details")

def extract_db_data():
    strDate = datetime.now().date() 
    for table_name in table_names:
        try:
            cnn = psycopg2.connect(**db_config_read)
            cur = cnn.cursor()
            cur.execute(f"SELECT * FROM {table_name}")
            results = cur.fetchall()

            column_names = [desc[0] for desc in cur.description]

            data = []
            for row in results:
                row_data = {}
                for i, value in enumerate(row):
                    if isinstance(value, memoryview):
                        encoded_image = bytes(value).decode("utf-8")
                        row_data[column_names[i]] = encoded_image
                    elif isinstance(value, (datetime, date)):
                        formated_date = str(value)
                        row_data[column_names[i]] = formated_date
                    else:
                        row_data[column_names[i]] = value

                data.append(row_data)
        except Exception as e:
            print(f"Error processing table {table_name} - extract_db_data: {str(e)}")
        finally:
            cur.close()
            cnn.close()

        tablePath = f'data\postgres\{table_name}\{strDate}'
        if not os.path.exists(tablePath):
            os.makedirs(tablePath)
            with open(f"{tablePath}\{table_name}.json", "w") as json_file:
                json.dump(data, json_file)
    