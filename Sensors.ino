 #define BLYNK_PRINT Serial
 #include <ESP8266WiFi.h>
 #include <BlynkSimpleEsp8266.h>

 #define BLYNK_TEMPLATE_ID "TMPL3P_301-FD"
 #define BLYNK_TEMPLATE_NAME "MMCOE HackSprint"
 #define BLYNK_AUTH_TOKEN "2ayuBvz0AzD73C1u1L3Y_tJWkqR-yzQS"
 
 char auth[] = BLYNK_AUTH_TOKEN;
 char ssid[] = "Tushar's Galaxy M12";
 char pass[] = "yptb0262";
 
 #include <SimpleDHT.h>  
 //   for DHT11,   
 //   VCC: 5V or 3V  
 //   GND: GND  
 //   DATA: 2  
 //   for soil moisture,
 //   Analog Output (AO): A0
 int pinDHT11 = 4;  
 const int sensor_pin = A0;  /* Connect Soil moisture analog sensor pin to A0 of NodeMCU */
 SimpleDHT11 dht11(pinDHT11); 
 
 void setup()  
 {  
   Serial.begin(9600);  
   Blynk.begin(auth, ssid, pass, "blynk.cloud", 8080);
   pinMode(pinDHT11, INPUT);
   pinMode(sensor_pin, INPUT);
//   Serial.println("TEMPERATURE AND HUMIDITY");  
//   timer.setInterval(1000L, sendSensor);
 }  
 void loop()   
 {  
  Blynk.run();
  /*DHT INTERFACING */
  byte temperature = 0;  
  byte humidity = 0;  
  int err = SimpleDHTErrSuccess;  
  if ((err = dht11.read(&temperature, &humidity, NULL)) != SimpleDHTErrSuccess) {  
   Serial.print("Read DHT11 failed, err="); Serial.println(err);delay(1000);  
   return;  
  }  
  Serial.print((int)temperature); Serial.print(" *C, ");   
  Serial.print((int)humidity); Serial.println(" H");  
  // DHT11 sampling rate is 1HZ.  
  Blynk.virtualWrite(V0, (int)temperature);
  Blynk.virtualWrite(V1, (int)humidity);
  
  /*SOIL SENSOR INTERFACING */
  float moisture_percentage;

  moisture_percentage = ( 100.00 - ( (analogRead(sensor_pin)/1023.00) * 100.00 ) );

  Serial.print("Soil Moisture(in Percentage) = ");
  Serial.print(moisture_percentage);
  Serial.println("%");
  Blynk.virtualWrite(V2, moisture_percentage);
  delay(1500);  
 }  
