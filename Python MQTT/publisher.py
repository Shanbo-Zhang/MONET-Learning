import paho.mqtt.client as mqtt
import paho.mqtt.enums as enums

def on_publish(client: mqtt.Client, user_data, mid: int):
    print("Data Published ^_^")

publisher = mqtt.Client(client_id="publisher",callback_api_version=enums.CallbackAPIVersion.VERSION1)
publisher.on_publish = on_publish
publisher.connect("test.mosquitto.org")
publisher.publish("Escapist Topic", "^_^ First MQTT")