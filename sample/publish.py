import paho.mqtt.client as mqtt

mqttc = mqtt.Client('python_pub')
mqttc.connect('test.mosquitto.org', 1883)
mqttc.publish('mcutie/init', 'Starting...')
mqttc.loop(2)
