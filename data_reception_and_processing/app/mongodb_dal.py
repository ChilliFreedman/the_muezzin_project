import os

from pymongo import MongoClient, errors
import gridfs


class MongoDal:
    def __init__(self):

        self.database_name = os.getenv("MONGO_DB_NAME", "muezzin_podcasts")
        self.mongo_host = os.getenv("MONGO_HOST", "localhost")
        self.mongo_port = os.getenv("MONGO_PORT", "27017")
        self.url = f"mongodb://{self.mongo_host}:{self.mongo_port}/"
        self.client = MongoClient(self.url)
        self.db = self.client[self.database_name]
        self.fs = gridfs.GridFS(self.db)



    def insert(self,file_path,file_id_hash_name):
        with open(file_path, 'rb') as file_data:
            file_id = self.fs.put(file_data,_id = file_id_hash_name)

        print(f"File uploaded with file_id: {file_id}")

