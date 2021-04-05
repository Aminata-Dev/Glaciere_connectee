#J'utilise l'application MQTTool pour récupérer la température ( host = test.mosquitto.org / Port = 1883 / topic = temperature_glaciere )
import paho.mqtt.client as mqtt
import random, time

def publication(topic, message): #On publie un topic et un message
    client.publish(topic, message)
    print(f"Publication '{message}' au topic '{topic}'")
    time.sleep(1)

broker_mqtt = "test.mosquitto.org" #On définit la localisation du broker MQTT ( utilisation du broker test fourni par mosquitto )
client = mqtt.Client("temperature_interieure")
client.connect(broker_mqtt) #Connection au broker

for i in range(10):
    temperature_au_hasard = random.choice([20.95, 21.01, 22.54]) #( En attendant de récupérer le microprocesseur )
    publication("temperature_glaciere", temperature_au_hasard)