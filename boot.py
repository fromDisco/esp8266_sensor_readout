import gc
from utime import sleep
import network
import usocket as socket
from machine import Pin, I2C
import esp
import BME280

esp.osdebug(0)

gc.collect()

# ESP32 - Pin assignment
# i2c = I2C(scl=Pin(22), sda=Pin(21), freq=10000)
# ESP8266 - Pin assignment
i2c = I2C(scl=Pin(5), sda=Pin(4), freq=10000)

# import the SSID and PASSWORD fron secrets.py
import secrets
ssid = secrets.SSID
password = secrets.PASSWORD

station = network.WLAN(network.STA_IF)
station.active(True)
station.connect(ssid, password)

# while station.isconnected() == False:
#     pass

print('Connection successful')
print(station.ifconfig())
gc.collect()