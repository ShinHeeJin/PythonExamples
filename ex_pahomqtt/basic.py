# doc : https://pypi.org/project/paho-mqtt/#client
from typing import Any

import paho.mqtt.client as mqtt
from paho.mqtt.client import MQTTMessage


def on_connect(client: mqtt.Client, userdata: Any, flags, rc):
    """
    The callback for when the client receives a CONNACK response from the server.
    """
    pass


def on_message(client: mqtt.Client, userdata: Any, msg: MQTTMessage):
    """
    The callback for when a PUBLISH message is received from the server.
    """
    pass


def on_disconnect(client: mqtt.Client, userdata: Any, rc):
    pass


def on_log(client: mqtt.Client, userdata: Any, level, string):
    pass


client = mqtt.Client()
client.on_connect = on_connect
client.on_message = on_message
client.on_disconnect = on_disconnect
client.on_log = on_log

client.username_pw_set(username="chammqtt", password="cham#1q84$mqtt")
client.connect(host="localhost", port=1883, keepalive=60)

# connect 이후 subscribe 해야한다.
client.subscribe("test/#")

client.loop_forever()
client.publish("test", "bar", qos=1)
