import os
from utils.checking_logs import Logger
from pymongo import MongoClient, errors
import gridfs

class MongoDal:
    def __init__(self):
        self.logger = Logger.get_logger()

        try:

            self.database_name = os.getenv("MONGO_DB_NAME", "muezzin_podcasts")
            self.mongo_host = os.getenv("MONGO_HOST", "localhost")
            self.mongo_port = os.getenv("MONGO_PORT", "27017")
            self.url = f"mongodb://{self.mongo_host}:{self.mongo_port}/"
            self.client = MongoClient(self.url)
            self.db = self.client[self.database_name]
            self.fs = gridfs.GridFS(self.db)
            self.logger.info("In file 'mongodb_dal' the config was successful")
        except Exception as e:
            self.logger.exception(f"In file 'mongodb_dal' by the config an unexpected error occurred: {e}")




    def insert(self,file_path,file_id_hash_name):
        try:
            if self.fs.exists({"id":file_id_hash_name}):
                self.logger.info(f"already exists {file_id_hash_name}")
                return
            with open(file_path, 'rb') as file_data:
                file_id = self.fs.put(file_data,_id = file_id_hash_name)
            self.logger.info(f"File uploaded with file_id: {file_id}")
            self.logger.info("In file 'mongodb_dal' the insert file was successful")
        except Exception as e:
            self.logger.exception(f"In file 'mongodb_dal' in func insert an unexpected error occurred: {e}")




if __name__ == "__main__":
    mongodal = MongoDal()

