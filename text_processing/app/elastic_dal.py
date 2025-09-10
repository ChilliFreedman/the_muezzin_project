from elasticsearch import Elasticsearch,helpers
from utils.checking_logs import Logger
import os
class ElasticDAL:
    def __init__(self):
        self.host = os.getenv("ELASTIC_HOST", "http://localhost:9200")
        self.index = os.getenv("ELASTIC_INDEX", "metadata")
        self.es = Elasticsearch(self.host)
        self.logger = Logger.get_logger()


    def update_mapping_and_data(self,bds_percent:float,is_bds:bool,bds_threat_level:str,doc_id):
        new_mapping = {
            "properties": {
                "bds_percent": {"type": "float"},
                "is_bds": {"type": "boolean"},
                "bds_threat_level": {"type": "keyword"}
            }
        }
        try:
            self.es.indices.put_mapping(index=self.index, body=new_mapping)
            self.logger.info(f"Mapping updated successfully for index '{self.index}'.")
        except Exception as e:
            self.logger.exception(f"Error updating mapping: {e}")

        update_body = {"doc":{"bds_percent":bds_percent,
                              "is_bds":is_bds,
                              "bds_threat_level":bds_threat_level}}
        self.es.update(index=self.index,id= doc_id,body= update_body)

if __name__ == "__main__":

    dal = ElasticDAL()

