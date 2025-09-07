from kafka import KafkaConsumer
import json
import os
class SetConsumer:

    def __init__(self):
        self.consumer = None

    def get_consumer_events(self,topic):
        kafka_url = os.getenv('KAFKA_URL', 'localhost')
        kafka_port = os.getenv('KAFKA_PORT', '9092')
        bootstrap_servers = [f'{kafka_url}:{kafka_port}']


        consumer = KafkaConsumer(topic,
                                 group_id='my-group',
                                 value_deserializer=lambda m: json.loads(m.decode('ascii')),
                                 bootstrap_servers=bootstrap_servers,
                                 consumer_timeout_ms=10000)

        self.consumer = consumer

    def print_messages(self):
        for message in self.consumer:
            print("%s:%d:%d: key=%s value=%s" % (message.topic, message.partition,
                                                 message.offset, message.key,
                                                 message.value))


if __name__ == "__main__":
    set_consumer = SetConsumer()
    set_consumer.get_consumer_events("file_path_and_basic_metadata")
    set_consumer.print_messages()
