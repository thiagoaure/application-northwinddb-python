from pymongo import MongoClient


db_config_read = {
    "database": "northwind",
    "user": "northwind_user",
    "password": "thewindisblowing"
}

db_config_mongo = MongoClient(
    host="localhost",
    port=27017,
    username="northwind_user_mongodb",
    password="mongodb2022"
)
