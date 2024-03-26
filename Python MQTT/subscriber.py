import paho.mqtt.client as mqtt
import paho.mqtt.enums as enums

def on_message(client: mqtt.Client, user_data, message: mqtt.MQTTMessage):
    print(message.payload.decode(), " on topic ", message.topic)

subscriber = mqtt.Client(client_id = "Subscriber",
                         callback_api_version = enums.CallbackAPIVersion.VERSION1)
subscriber.on_message = on_message
subscriber.connect("test.mosquitto.org")
subscriber.loop_start()
subscriber.subscribe("Escapist Topic")
input("Press Enter to stop...\n")
subscriber.loop_stop()
subscriber.disconnect()