from elasticsearch import Elasticsearch,helpers
import os
class ElasticDAL:
    def __init__(self):
        self.host = os.getenv("ELASTIC_HOST", "http://localhost:9200")
        self.index = os.getenv("ELASTIC_INDEX", "metadata")
        self.es = Elasticsearch(self.host)

    def create_index(self):

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
            return {"message": f"Index '{self.index}' created"}
        return {"message": f"Index '{self.index}' already exists"}

    def insert_doc(self, doc_id, doc: dict):

        return self.es.index(index=self.index, id=doc_id, document=doc)

if __name__ == "__main__":


    dal = ElasticDAL()
    print(dal.create_index())
