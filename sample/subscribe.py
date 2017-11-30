import paho.mqtt.client as mqtt

def on_connect(client, userdata, flags, rc):
    print('Connected. Result code: ', str(rc))
    client.subscribe('mcutie/init')

def on_message(client, userdata, msg):
    print('Topic: ', msg.topic, '\nMessage:', msg.payload)

client = mqtt.Client()
client.on_connect = on_connect
client.on_message = on_message

client.connect('localhost', 1883, 60)
client.loop_forever()
