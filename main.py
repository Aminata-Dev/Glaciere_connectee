### IMPORTATION DES MODULES

import serial #module permettant de "lire" les ports la carte Arduino
import mysql.connector #pip install mysql-connector-python #module permettant de faire des requêtes SQL
import time #module permettant de mettre le programme en pause
import os #module permettant de travailler avec des dossiers / fichiers
import paho.mqtt.client as mqtt
import shutil, webbrowser #travailler avec des fichiers / ouvrir des sites web


### INITIALISATION


connection = mysql.connector.connect(host='localhost', database='', user='root', password='')
curseur = connection.cursor()
requete_creation_bdd = "CREATE DATABASE IF NOT EXISTS TEMPERATURES" #création de la base de données
curseur.execute(requete_creation_bdd)
connection.close()

#On refait une connection en spécifiant cette fois la base de donnée afin d'y effectuer des actions :
connection = mysql.connector.connect(host='localhost',database='TEMPERATURES',user='root',password='')
curseur = connection.cursor()

curseur.execute("CREATE TABLE IF NOT EXISTS `TEMPERATURES_GLACIERE` ( `id_horodatage`  DATETIME NOT NULL, `temperatures` FLOAT NOT NULL ) ENGINE = InnoDB;")

# print("On vide la table")
# curseur.execute("TRUNCATE `TEMPERATURES_GLACIERE`") #On vide la table ( au cas où elle existe déjà )
# connection.commit() #On soumet la requete

#On crée la fonction ajout_temperature_BDD, qui va nous permettre de creer une requete SQL qui ajoute la temperature dans la base de donnée
def ajout_temperature_BDD(temperature):
    print(f"Ajout de la température {temperature} dans la base de donnée")
    # print(f"INSERT INTO `TEMPERATURES_GLACIERE` ( `id_horodatage`, `temperatures`) VALUES (NOW(),'{temperature}')")
    curseur.execute(f"INSERT INTO `TEMPERATURES_GLACIERE` ( `id_horodatage`, `temperatures`) VALUES ( NOW(),'{temperature}')")
    connection.commit() #On soumet la requete


os.chdir("site") #On change de dossier

files = ['suivi_temperature_glaciere.php', 'style_site.css', 'fond.jpg', 'icone.png']

for file in files:
    try:
        shutil.copy(file, r'C:\xampp\htdocs')
    except shutil.Error: #Si le fichier a deja été déplacé
        pass

print("Ouverture de Xampp...")
os.system(r"c: && cd C:\xampp && xampp_start") #On lance xampp

webbrowser.open("http://localhost/phpmyadmin/sql.php?db=temperatures&table=temperatures_glaciere&pos=0")
webbrowser.open("http://localhost/suivi_temperature_glaciere.php") #On ouvre le site en local

def publication(topic, message): #On publie un topic et un message
    client.publish(topic, message)
    print(f"Publication de la température {message} au topic {topic}")

broker_mqtt = "test.mosquitto.org" #On définit la localisation du broker MQTT ( utilisation du broker test fourni par mosquitto )
client = mqtt.Client("glaciere")
client.connect(broker_mqtt) #Connection au broker

valeur_precedente = None


### MAIN

ARDUINO = "COM3" #On part du principe que la carte Arduino se trouve sur le port 3
ser = serial.Serial(ARDUINO, timeout=1) #On lit le port de la carte Arduino

while True: #Boucle infinie
    ser.flushInput()
    serialValue = ser.readline().strip()
    if len(serialValue) == 5: #On filtre la valeur pour n'avoir que la température
        # if serialValue != valeur_precedente:
            # print(float(serialValue))
        ajout_temperature_BDD(float(serialValue)) #On appelle la fonction afin d'ajouter la température dans la base de donnée
        publication("temperature_glaciere", float(serialValue)) #On appelle la fonction afin d'ajouter la température dans la base de donnée
    # valeur_precedente = serialValue
    time.sleep(1) #On met le programme en pause durant deux secondes, pour éviter d'avoir trop de valeur dans la base de donnée

main()
