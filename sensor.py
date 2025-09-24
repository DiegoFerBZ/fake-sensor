import time
import random
import paho.mqtt.client as mqtt

ADAFRUIT_IO_USERNAME = ""  
ADAFRUIT_IO_KEY = "" 
FEED_SISTOLICA = "p-sistolica"
FEED_DIASTOLICA = "p-diastolica"

client = mqtt.Client()
client.username_pw_set(ADAFRUIT_IO_USERNAME, ADAFRUIT_IO_KEY)
client.connect("io.adafruit.com", 1883, 60)

while True:
    sistolica = random.randint(100, 140) 
    diastolica = random.randint(60, 90) 

    print(f"Enviando presión arterial: {sistolica}/{diastolica} mmHg")

    client.publish(f"{ADAFRUIT_IO_USERNAME}/feeds/{FEED_SISTOLICA}", sistolica)
    client.publish(f"{ADAFRUIT_IO_USERNAME}/feeds/{FEED_DIASTOLICA}", diastolica)

    time.sleep(10)
