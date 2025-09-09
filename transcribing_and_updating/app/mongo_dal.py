import os
from utils.checking_logs import Logger
from pymongo import MongoClient, errors
import gridfs

from transcribe_WAV_file import Convert
class MongoDal:
    def __init__(self):
        self.logger = Logger.get_logger()
        self.convert = Convert()
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


    def get_all_id(self):
        file_ids = []
        for grid_out in self.fs.find():
            file_ids.append(grid_out._id)
        return file_ids

if __name__ == "__main__":
    mongodal = MongoDal()
