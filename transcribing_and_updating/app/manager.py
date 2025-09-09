from elastic_dal import ElasticDAL
from mongo_dal import MongoDal
from transcribe_WAV_file import Convert
from kafka_consumer import SetConsumer
class Manager:
    def __init__(self):
        self.convert = Convert()
        self.mongodal = MongoDal()
        self.elastidal = ElasticDAL()
        self.set_consumer = SetConsumer()



    def run_all(self,):
        list_file_id = self.mongodal.get_all_id()
        for file_id in list_file_id:
            grid_out = self.mongodal.fs.get(file_id)
            #print(f"grid_out!!! {grid_out}")
            text = self.convert.convert_with_path(grid_out)
            self.elastidal.update_mapping_and_data(text,file_id)

    def run_with_consumer(self):
        self.set_consumer.get_consumer_events("file_id_topic")
        consumer = self.set_consumer.consumer
        for message in consumer:
            file_id = message.value["file_id"]
            grid_out = self.mongodal.fs.get(file_id)
            # print(f"grid_out!!! {grid_out}")
            text = self.convert.convert_with_path(grid_out)
            self.elastidal.update_mapping_and_data(text, file_id)




if __name__ == "__main__":
    manager = Manager()
    #manager.run_all()
    manager.run_with_consumer()