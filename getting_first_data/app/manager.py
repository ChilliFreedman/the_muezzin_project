from time import sleep
from reading_files import ReadFiles
from creating_metadata import SetMetadata
from combining_data_into_json import DataToJson
from kafka_producer import SetKafkaProducer
class Manager:
    def __init__(self):
        self.read_files = ReadFiles()
    def run_all_functions(self):
        all_paths = self.read_files.get_all_file_paths()
        for file_path in all_paths:
            set_metadata = SetMetadata(file_path)
            metadata_dict = set_metadata.get_metadata()
            data_to_json = DataToJson(file_path, metadata_dict)
            all_data = data_to_json.combin_to_json()
            kafka_producer = SetKafkaProducer()
            kafka_producer.producer_config()
            kafka_producer.producer_publish("file_path_and_basic_metadata",all_data)
            kafka_producer.producer_flush()
            #sleep(60)
            # print(file_path)
            # print(metadata_dict)
            # print(all_data)

if __name__ == "__main__":
    manager = Manager()
    manager.run_all_functions()