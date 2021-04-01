const int LM35 = A0; // Entrée analogique/numérique pour brancher le capteur LM35


#include <Wire.h>
#include "rgb_lcd.h"

rgb_lcd lcd;

const int colorR = 0;
const int colorG = 10;
const int colorB = 245;



// Fonction d’initialisation parcourue une seule fois
void setup()
{
  // Initialisation de la liaison serie
  Serial.begin(9600); 
  Serial.println("Ce programme mesure la temperature");
  // set up the LCD's number of columns and rows:
    lcd.begin(16, 2);

    lcd.setRGB(colorR, colorG, colorB);

    // Print a message to the LCD.
    lcd.print("Temperature");

    delay(1000);



 
} // fin setup
//------------------------------------------------------------
// Fonction Principale parcourue en boucle
//------------------------------------------------------------
void loop()
{ 
  float TC; // Pour afficher la valeur de la température
  int N; // pour stocker la valeur numérisée 
  N = analogRead(LM35); // lecture du capteur LM35
  
   
  TC = N*5.0/1023*100 ;  // calcul de TC en degres Celsius.
  
  
  //AFFICHAGE
   
    Serial.println(TC);
    delay(2000);

    lcd.setCursor(0, 1);
    // print the number of seconds since reset:
    lcd.print(TC);

    delay(100);


    
} //fin loop
