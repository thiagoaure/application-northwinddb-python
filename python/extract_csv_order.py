import pandas as pd
import os
import json
from datetime import datetime

def extract_order_details():
    try:
        orderData = pd.read_csv("data\order_details.csv")
        orderRecords = orderData.to_dict('records')
        orderPath = f'data\csv\order_details\{datetime.now().date()}'

        if not os.path.exists(orderPath):
            os.makedirs(orderPath)
            with open(f"{orderPath}\order_details.json", "w") as json_file:
                json.dump(orderRecords, json_file)
    except Exception as e:
        print(f"Error: extract_order_details {str(e)}, {type(e)}, {orderData}")