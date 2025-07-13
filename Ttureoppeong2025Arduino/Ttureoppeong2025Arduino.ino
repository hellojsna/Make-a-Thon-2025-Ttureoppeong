#include <ESP8266WiFi.h>
#include <ESP8266WebServer.h>

const char* ssid = "HelloJsNa-NodeMCU";
const char* password = "ciNqoz-mekjah!@#$";

IPAddress local_ip(192,168,4,2);
IPAddress gateway(192,168,4,1);
IPAddress subnet(255,255,255,0);

ESP8266WebServer server(80);

void handleGetLevelSensor() {
  int sensorValue = analogRead(A0);
  server.sendHeader("Access-Control-Allow-Origin", "*");
  server.sendHeader("Access-Control-Max-Age", "10000");
  server.sendHeader("Access-Control-Allow-Methods", "PUT,POST,GET,OPTIONS");
  server.sendHeader("Access-Control-Allow-Headers", "*");
  server.send(200, "text/plain", String(sensorValue));
}

void setup() {
  Serial.begin(9600);

  delay(1000);

  WiFi.softAP(ssid, password);

  Serial.print("Hello, Js Na! - AP \"");
  Serial.print(ssid);
  Serial.println("\" 시작됨");
  Serial.print("IP:\t");
  Serial.println(WiFi.softAPIP());

  server.on("/api/getLevelSensor", handleGetLevelSensor);

  server.begin();
  Serial.println("HTTP 서버 시작됨");
}

void loop() {
  server.handleClient();
  delay(10);
}
