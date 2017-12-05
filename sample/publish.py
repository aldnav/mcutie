import paho.mqtt.client as mqtt

mqttc = mqtt.Client('python_pub')
mqttc.connect('localhost', 1883)
print('ping')
mqttc.publish('mcutie/init', 'Starting...')
mqttc.loop(2)
