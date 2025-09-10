from elastic_dal import ElasticDAL
from kafka_consumer import SetConsumer
from processor import Processor
class Manager:
    def __init__(self):
        self.elastic_dal = ElasticDAL()
        self.set_consumer = SetConsumer()
        self.processor = Processor()



    def run_all(self):
        self.set_consumer.get_consumer_events("id_and_text_for_analyzing_and_updating")
        consumer = self.set_consumer.consumer
        for message in consumer:
            doc_id = message.value["file_id"]
            text = message.value["text"]
            self.processor.decode_and_lowercase_lists()
            self.processor.clean_text(text)
            bds_percent = self.processor.get_percent()
            is_bds = self.processor.get_is_bds()
            bds_threat_level = self.processor.get_bds_threat_level()
            self.elastic_dal.update_mapping_and_data(bds_percent,is_bds,bds_threat_level,doc_id)









if __name__ == "__main__":
    manager = Manager()
    #manager.run_all()
    manager.run_all()