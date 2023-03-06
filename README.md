# esp8266_sensor_readout

This is a first try to read sensor data and send it to a rest API endpoint. 

Its really in an early state.

## TODO:
- add uasycio, because s.accept() in main.py is blocking the execution of the sensor post request.
- add chaching to file, when rest API isn't available.
- clean up code
