try:
    import BME280
    import gc
    import usocket as socket
except:
    import socket

from time import sleep

from machine import Pin, I2C
import network
import esp
esp.osdebug(None)

gc.collect()


# ESP32 - Pin assignment
# i2c = I2C(scl=Pin(22), sda=Pin(21), freq=10000)
# ESP8266 - Pin assignment
i2c = I2C(scl=Pin(5), sda=Pin(4), freq=10000)

import secrets
ssid = secrets.SSID
password = secrets.PASSWORD

station = network.WLAN(network.STA_IF)
station.active(True)
station.connect(ssid, password)

while station.isconnected() == False:
    pass

print('Connection successful')
print(station.ifconfig())
