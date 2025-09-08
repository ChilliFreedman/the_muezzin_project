from elasticserch_dal import ElasticDAL
from kafka_consumer import SetConsumer
from datetime import datetime
class Manager:
    def __init__(self):
        self.set_consumer = SetConsumer()
        self.elas_dal = ElasticDAL()


    def run_functions(self):
        self.set_consumer.get_consumer_events("file_path_and_basic_metadata")
        consumer = self.set_consumer.consumer
        self.elas_dal.create_index()
        for message in consumer:
            #get the metadata from topic
            metadata_dict = message.value["metadata_dict"]
            #convert metadata_dict["file_creation_timestamp"] to date type (from str)
            date_string = metadata_dict["file_creation_timestamp"]
            metadata_dict["file_creation_timestamp"] = datetime.strptime(date_string, "%Y-%m-%d %H:%M:%S")
            file_name = message.value["metadata_dict"]["file_name"]
            #get id with hash func of file name
            doc_id = hash(file_name)
            #insert id and metadata doc
            self.elas_dal.insert_doc(doc_id,metadata_dict)




if __name__ == "__main__":
    manager = Manager()
    manager.run_functions()