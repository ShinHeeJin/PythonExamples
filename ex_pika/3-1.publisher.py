import time
import uuid

from pika import BlockingConnection, ConnectionParameters, PlainCredentials
from pika.spec import BasicProperties

credential = PlainCredentials(username="admin", password="admin")
connection = BlockingConnection(ConnectionParameters(host="localhost", port=5672, credentials=credential))
channel = connection.channel()

# Exchange
exhange_name = "test-exchange"
channel.exchange_declare(exchange=exhange_name, exchange_type="topic")

# Publishing
while True:

    time.sleep(3)
    headers = {"CorrelationData": str(uuid.uuid4())}
    properties = BasicProperties(headers=headers)

    channel.basic_publish(
        exchange=exhange_name, routing_key="myapp.person.1234", body="홍길동", properties=properties
    )
