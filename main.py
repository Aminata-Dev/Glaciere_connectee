### MODULES

import serial #module permettant de "lire" les ports la carte Arduino
import mysql.connector #pip install mysql-connector-python #module permettant de faire des requêtes SQL
import time #module permettant de mettre le programme en pause
import os #module permettant de travailler avec des dossiers / fichiers

connection = mysql.connector.connect(host='localhost',database='',user='root',password='')
curseur = connection.cursor()
requete_creation_bdd = "CREATE DATABASE IF NOT EXISTS TEMPERATURES"
curseur.execute(requete_creation_bdd)
connection.close()

#On refait une connection en spécifiant cette fois la base de donnée afin d'y effectuer des actions :
connection = mysql.connector.connect(host='localhost',database='TEMPERATURES',user='root',password='')
curseur = connection.cursor()

curseur.execute("CREATE TABLE IF NOT EXISTS `TEMPERATURES_GLACIERE` ( `id_horodatage`  DATETIME NOT NULL, `temperatures` FLOAT NOT NULL ) ENGINE = InnoDB;")

print("On vide la table")
curseur.execute("TRUNCATE `TEMPERATURES_GLACIERE`") #On vide la table ( au cas où elle existe déjà )
connection.commit() #On soumet la requete

#On crée la fonction ajout_temperature_BDD, qui va nous permettre de creer une requete SQL qui ajoute la temperature dans la base de donnée
def ajout_temperature_BDD(temperature):
    print(f"Ajout de la température {temperature} dans la base de donnée")
    # print(f"INSERT INTO `TEMPERATURES_GLACIERE` ( `id_horodatage`, `temperatures`) VALUES (NOW(),'{temperature}')")
    curseur.execute(f"INSERT INTO `TEMPERATURES_GLACIERE` ( `id_horodatage`, `temperatures`) VALUES ( NOW(),'{temperature}')")
    connection.commit() #On soumet la requete

### main

ARDUINO = "COM3" #On part du principe que la carte Arduino se trouve sur le port 3
ser = serial.Serial(ARDUINO, timeout=1) #On lit le port de la carte Arduino
valeur_precedente = None #On initialise la variable valeur_precedente

while True: #Boucle infinie
    ser.flushInput()
    serialValue = ser.readline().strip()
    if len(serialValue) == 5: #On filtre la valeur pour n'avoir que la température
        # if serialValue != valeur_precedente:
        # print(float(serialValue))
        ajout_temperature_BDD(float(serialValue)) #On appelle la fonction afin d'ajouter la température dans la base de donnée
    valeur_precedente = serialValue
    time.sleep(2) #On met le programme en pause durant deux secondes, pour éviter d'avoir trop de valeur dans la base de donnée

main()

# webbrowser.open("http://localhost/phpmyadmin/sql.php?db=temperatures&table=temperatures_glaciere&pos=0")