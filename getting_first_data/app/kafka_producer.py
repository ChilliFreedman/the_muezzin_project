from kafka import KafkaProducer
import json
import os
class SetKafkaProducer:

    def __init__(self):
        self.producer = None

    def producer_config(self):
        kafka_url = os.getenv('KAFKA_URL', 'localhost')
        kafka_port = os.getenv('KAFKA_PORT', '9092')
        bootstrap_servers = [f'{kafka_url}:{kafka_port}']
        producer = KafkaProducer(bootstrap_servers=bootstrap_servers,
                                 value_serializer=lambda x:
                                 json.dumps(x).encode('utf-8'))

        self.producer = producer


    def producer_publish(self,topic,message):
        self.producer.send(topic,message)

    def producer_flush(self):
        self.producer.flush()

