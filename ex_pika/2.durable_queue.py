from pika import BlockingConnection, ConnectionParameters, PlainCredentials
from pika.delivery_mode import DeliveryMode
from pika.spec import BasicProperties

credential = PlainCredentials(username="admin", password="admin")
connection = BlockingConnection(ConnectionParameters(host="localhost", port=5672, credentials=credential))
channel = connection.channel()

# create queue - Durability : Durable
# 해당 queue를 Disk에 Write 하여 서버를 On/Off 하여도 정보 유지
channel.queue_declare(queue="hello", durable=True)

# publish
channel.basic_publish(
    exchange="",
    routing_key="hello",
    body="hello",
    properties=BasicProperties(delivery_mode=DeliveryMode.Persistent),
)

# connection close
connection.close()
