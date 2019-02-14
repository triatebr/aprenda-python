# Programa : Sensor de temperatura DHT22 com Raspberry Pi B+
# Autor : Lucas de Barros
# Data: 10/09/2018
 
# Carrega as bibliotecas
import Adafruit_DHT
import RPi.GPIO as GPIO
import time
import requests
import json
 
# Define o tipo de sensor
sensor = Adafruit_DHT.DHT22
 
GPIO.setmode(GPIO.BOARD)
 
#Define o pino de alimentação de energia do projeto
#jumper vermelho (Pin# 02)

#Define o pino 'TERRA' da placa
#jumper preto (Pin# 06)

# Define a GPIO conectada ao pino de dados do sensor
#jumper amarelo (Pin# 22)
pino_sensor = 25   
 
while True:

    humidity, temperature = Adafruit_DHT.read_retry(sensor, pino_sensor)
    humidade = '{0:.0f}'.format(humidity)           #formatar a humidade sem casas decimais
    temperatura = '{0:.0f}'.format(temperature)     #formatar a temperatura sem casas decimais
    hora = time.strftime('%H:%M')
    date = time.strftime('%d/%m/%Y')
    latitude = '15'
    longitude = '15'
    smartcontract = '0x5e8d0eedbd53b89a693c57273590dfff5c70bb67'
    data =  { "data": date, "externalIdentifier": "string","hora": hora,"humidity": humidade, "latitude": latitude,"longitude": longitude,"smartContractAddress": smartcontract, "temperature": temperatura }
    data_header = {"accept": "application/json","Content-Type": "application/json"} 
    json_data = json.dumps(data)
    r = requests.post('http://agrichain.tech:8080/rest/eth/setData',data=json_data,headers = data_header)
    print ("Data: ", date ,"Time: ", hora, ' Temp: {0:0.2f}ºc  Humidity: {1:0.2f}%'.format(temperature, humidity), ' smartContract : 0xd495a69094548889ef7be8c6487b2d05bc974396')
    print("status :",r.status_code)
    time.sleep(60)
