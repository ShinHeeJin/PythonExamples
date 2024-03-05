from pika import BlockingConnection, ConnectionParameters, PlainCredentials
from pika.adapters.blocking_connection import BlockingChannel
from pika.spec import Basic, BasicProperties

credential = PlainCredentials(username="admin", password="admin")
connection = BlockingConnection(ConnectionParameters(host="localhost", port=5672, credentials=credential))
channel = connection.channel()

# 임시 Queue 생성
result = channel.queue_declare(queue="", exclusive=True)
queue_name = result.method.queue

# 특정 패턴에 해당하는 메시지만 받도록 바인딩
channel.queue_bind(exchange="test-exchange", queue=queue_name, routing_key="myapp.person.*")


# 콜백함수 정의
def callback(ch: BlockingChannel, method: Basic.Deliver, properties: BasicProperties, body: bytes):

    print("-" * 100)
    print(f"{method.routing_key=}")  # myapp.person.1234
    print(f"{method.consumer_tag=}")  # ctag1.abceacc3343b4ec5999cffcbaab0e02a
    print(f"{method.delivery_tag=}")  # 1
    print(f"{method.exchange=}")  # test-exchange
    print(f"{body=}")  # b'\xed\x99\x8d\xea\xb8\xb8\xeb\x8f\x99'

    headers = properties.headers
    correlation_id = headers.get("CorrelationData", None)
    print(f"{correlation_id=}")  # 3e998099-e8ae-4468-9e50-87ad86fff27f

    person_id = method.routing_key.split(".")[-1]
    print(f"{person_id=}")  # 1234


# Comsume
channel.basic_consume(queue=queue_name, on_message_callback=callback, auto_ack=True)


# Loop
channel.start_consuming()
