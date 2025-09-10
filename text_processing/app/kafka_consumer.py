from kafka import KafkaConsumer
import json
import os
from utils.checking_logs import Logger
class SetConsumer:

    def __init__(self):
        self.consumer = None
        self.logger = Logger.get_logger()

    def get_consumer_events(self,topic):
        try:

            kafka_url = os.getenv('KAFKA_URL', 'localhost')
            kafka_port = os.getenv('KAFKA_PORT', '9092')
            bootstrap_servers = [f'{kafka_url}:{kafka_port}']
            consumer = KafkaConsumer(topic,
                                     group_id='my-group',
                                     value_deserializer=lambda m: json.loads(m.decode('ascii')),
                                     bootstrap_servers=bootstrap_servers)#,consumer_timeout_ms=10000)



            self.consumer = consumer
            self.logger.info("In file 'kafka_consumer' the config was successful")
        except Exception as e:
            self.logger.exception(f"In file 'kafka_consumer' an unexpected error occurred: {e}")

    def print_messages(self):
        for message in self.consumer:
            print("%s:%d:%d: key=%s value=%s" % (message.topic, message.partition,
                                                 message.offset, message.key,
                                                 message.value))
#test to see how the data returns from topic
    def get_messages_in_list(self):

        for message in self.consumer:

                print(message.value["file_id"])
                print(message.value["text"])


if __name__ == "__main__":
    set_consumer = SetConsumer()
    set_consumer.get_consumer_events("id_and_text_for_analyzing_and_updating")
    #set_consumer.print_messages()
    set_consumer.get_messages_in_list()
