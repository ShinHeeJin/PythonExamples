from pika import BlockingConnection, ConnectionParameters, PlainCredentials

credential = PlainCredentials(username="admin", password="admin")
connection = BlockingConnection(ConnectionParameters(host="localhost", port=5672, credentials=credential))
channel = connection.channel()

# create queue
channel.queue_declare(queue="hello")

# publish
channel.basic_publish(exchange="", routing_key="hello", body="Hello World")

# connection close
connection.close()
