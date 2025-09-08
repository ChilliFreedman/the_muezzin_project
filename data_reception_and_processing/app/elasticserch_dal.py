from elasticsearch import Elasticsearch,helpers
from utils.checking_logs import Logger
import os
class ElasticDAL:
    def __init__(self):
        self.host = os.getenv("ELASTIC_HOST", "http://localhost:9200")
        self.index = os.getenv("ELASTIC_INDEX", "metadata")
        self.es = Elasticsearch(self.host)
        self.logger = Logger.get_logger()

    def create_index(self):
        try:
            if not self.es.indices.exists(index=self.index):
                mapping = {
                    "mappings": {
                        "properties": {
                            "id": {"type": "keyword"},
                            "file_name": {"type": "text"},
                            "file_size_bytes": {"type": "integer"},
                            "file_creation_timestamp": {"type": "date"}
                        }
                    }
                }

                self.es.indices.create(index=self.index, body=mapping)
                self.logger.info({"message": f"Index '{self.index}' created"})
                return
            self.logger.info({"message": f"Index '{self.index}' already exists"})

        except Exception as e:
            self.logger.exception(f"In file 'elasticserch_dal' in func create_index an unexpected error occurred: {e}")

    def insert_doc(self, doc_id, doc: dict):
        try:
            return self.es.index(index=self.index, id=doc_id, document=doc)
        except Exception as e:
            self.logger.exception(f"In file 'elasticserch_dal' in func insert_doc an unexpected error occurred: {e}")
if __name__ == "__main__":

    dal = ElasticDAL()
    print(dal.create_index())
