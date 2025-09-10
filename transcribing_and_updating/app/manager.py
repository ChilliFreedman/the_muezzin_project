from elastic_dal import ElasticDAL
from mongo_dal import MongoDal
from transcribe_WAV_file import Convert
from kafka_consumer import SetConsumer
from kafka_producer import SetKafkaProducer
class Manager:
    def __init__(self):
        self.convert = Convert()
        self.mongo_dal = MongoDal()
        self.elastic_dal = ElasticDAL()
        self.set_consumer = SetConsumer()



    def run_all(self,):
        list_file_id = self.mongo_dal.get_all_id()
        for file_id in list_file_id:
            grid_out = self.mongo_dal.fs.get(file_id)
            #print(f"grid_out!!! {grid_out}")
            text = self.convert.convert_with_path(grid_out)
            self.elastic_dal.update_mapping_and_data(text,file_id)

    def run_with_consumer(self):
        self.set_consumer.get_consumer_events("file_id_topic")
        consumer = self.set_consumer.consumer
        for message in consumer:
            file_id = message.value["file_id"]
            grid_out = self.mongo_dal.fs.get(file_id)
            # print(f"grid_out!!! {grid_out}")
            text = self.convert.convert_with_path(grid_out)
            self.elastic_dal.update_mapping_and_data(text, file_id)
            message_to_kafka = {"file_id":file_id,"text":text}
            kafka_producer = SetKafkaProducer()
            kafka_producer.producer_config()
            kafka_producer.producer_publish("id_and_text_for_analyzing_and_updating", message_to_kafka)
            kafka_producer.producer_flush()




if __name__ == "__main__":
    manager = Manager()
    #manager.run_all()
    manager.run_with_consumer()