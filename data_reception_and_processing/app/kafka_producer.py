from kafka import KafkaProducer
import json
import os
from utils.checking_logs import Logger
class SetKafkaProducer:

    def __init__(self):
        self.producer = None
        self.logger = Logger.get_logger()

    def producer_config(self):
        try:

            kafka_url = os.getenv('KAFKA_URL', 'localhost')
            kafka_port = os.getenv('KAFKA_PORT', '9092')
            bootstrap_servers = [f'{kafka_url}:{kafka_port}']
            producer = KafkaProducer(bootstrap_servers=bootstrap_servers,
                                     value_serializer=lambda x:
                                     json.dumps(x).encode('utf-8'))

            self.producer = producer
            self.logger.info("In file 'kafka_producer' the producer config  was successful")
        except Exception as e:
            self.logger.exception(f"In file 'kafka_producer' in func 'producer_config' an unexpected error occurred: {e}")


    def producer_publish(self,topic,message):
        try:
            self.producer.send(topic,message)
            self.logger.info("In file 'kafka_producer' the producer publish  was successful")
        except Exception as e:
            self.logger.exception(f"In file 'kafka_producer' in func 'producer_publish' an unexpected error occurred: {e}")


    def producer_flush(self):
        self.producer.flush()

