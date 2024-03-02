from pymongo.mongo_client import MongoClient
from pymongo.server_api import ServerApi
from dotenv import load_dotenv
import os


class MongoDB:
    def __init__(self):
        # Load environment variables from the .env file
        load_dotenv()

        # Now you can access the environment variables as usual
        mongodb_password = os.getenv('MONGODB_PASSWORD')

        uri = f'mongodb+srv://kimchi:{mongodb_password}@valorwin.j58lbbu.mongodb.net/?retryWrites=true&w=majority&appName=valorwin'

        client = MongoClient(uri, server_api=ServerApi('1'))

        try:
            client.admin.command('ping')
            print("Pinged your deployment. You successfully connected to MongoDB!")
        except Exception as e:
            print(e)
