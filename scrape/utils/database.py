from pymongo.mongo_client import MongoClient
from pymongo.server_api import ServerApi
from dotenv import load_dotenv
import os

from models.Map import Map


class MongoDB:
    def __init__(self):
        self.connect()

    def connect(self):
        # Load environment variables from the .env file
        load_dotenv()

        # Now you can access the environment variables as usual
        mongodb_password = os.getenv('MONGODB_PASSWORD')

        uri = f'mongodb+srv://kimchi:{mongodb_password}@valorwin.j58lbbu.mongodb.net/?retryWrites=true&w=majority&appName=valorwin'

        self.client = MongoClient(uri, server_api=ServerApi('1'))

    def add_map_data(self, map):
        map_name = map.map_name
        map_outcome = map.map_outcome

        for round in map.rounds:
            self.add_entry({'team_loadout': round.team_loadout,
                            'enemy_loadout': round.enemy_loadout,
                            'team_score': round.team_score,
                            'enemy_score': round.enemy_score,
                            'round_outcome': round.round_outcome,
                            'map_name': map.map_name,
                            'map_outcome': map.map_outcome})

    def add_entry(self, round_dict):
        db = self.client['econ']
        collection = db['round_data']

        insert_result = collection.insert_one(round_dict)
