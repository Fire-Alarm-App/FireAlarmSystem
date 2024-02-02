# Simulates the Smart Fire Alarm that sends an MQTT Message 
# to the Backend when a Fire is detected
 
import paho.mqtt.client as mqtt
import paho.mqtt.publish as publish # publish dependency
import time # for testing

# Constants
FIRE_ALARM_ER_TOPIC = "ER/bcsotty"
PWA_PUSH_URL = "http://localhost:3000/notify"
BROKER_HOST = "localhost"
CLIENT_USERNAME = "bcsotty"
CLIENT_PASSWORD = "correct"
MQTTMessage = "ALERT. THERE IS A FIRE. EVACUATE IMMEDIATELY"

# BROKER_HOST = "mqtt.eclipseprojects.io"
    
# The callback for when the client receives a CONNACK response from the server.
def on_connect(client, userdata, flags, rc):
    if(rc == 5):
        print("Authentication Error on Broker")
        exit()
    print("Connected to Broker with result code "+str(rc))
    # Subscribing in on_connect() means that if we lose the connection and
    # reconnect then subscriptions will be renewed.
    print(f"Sending: {MQTTMessage} to topic {FIRE_ALARM_ER_TOPIC}")
    publish.single(FIRE_ALARM_ER_TOPIC, MQTTMessage, hostname = BROKER_HOST, auth={'username':CLIENT_USERNAME, 'password':CLIENT_PASSWORD})

# The callback for when a PUBLISH message is received from the server.
def on_message(client, userdata, msg):
    print(msg.topic+" "+str(msg.payload))
    # When a message is received, a response is published
    # publish_response(FIRE_ALARM_ER_TOPIC, "Hello again, from Simple-Client-Publish", "mqtt.eclipseprojects.io")

def main():

    client = mqtt.Client()
    client.on_connect = on_connect
    client.on_message = on_message
    # Set Username and Password
    client.username_pw_set(username=CLIENT_USERNAME, password=CLIENT_PASSWORD )
    # Connect to broker
    client.connect("localhost", 1883)

    while True: 
        client.loop()
        time.sleep(5)
        publish.single(FIRE_ALARM_ER_TOPIC, MQTTMessage, hostname = BROKER_HOST, auth={'username':CLIENT_USERNAME, 'password':CLIENT_PASSWORD})


if __name__ == "__main__":
    main()