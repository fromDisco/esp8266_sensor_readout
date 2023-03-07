# esp8266_sensor_readout
sends data to following django rest api
[https://github.com/fromDisco/django_rest_sensors](https://github.com/fromDisco/django_rest_sensors)https://github.com/fromDisco/django_rest_sensorshttps://github.com/fromDisco/django_rest_sensors


This is a first try to read sensor data and send it to a REST API endpoint. 

Its really in an early state.

## TODO:
- add uasycio, because s.accept() in main.py is blocking the execution the post request of the sensor to the REST API.
- add chaching to file, when rest API isn't available / send chache as soon as REST API is available again.
- clean up code
