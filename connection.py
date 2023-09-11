import pymongo
from dotenv import load_dotenv, find_dotenv
import os

load_dotenv(find_dotenv())
password = os.environ.get('MONGODB_PASSWORD')
connection_string = f'mongodb+srv://golammostofa10001:{password}@cluster0.yaxxsxd.mongodb.net/'


def create_connection():
    client = pymongo.MongoClient(connection_string)
    return client

