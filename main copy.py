import urequests
import json
import uasyncio
import utime

def web_page():
    bme = BME280.BME280(i2c=i2c)

    html = (
        """<html><head><meta name="viewport" content="width=device-width, initial-scale=1">
  <link rel="icon" href="data:,"><style>body { text-align: center; font-family: "Trebuchet MS", Arial;}
  table { border-collapse: collapse; width:35%; margin-left:auto; margin-right:auto; }
  th { padding: 12px; background-color: #0043af; color: white; }
  tr { border: 1px solid #ddd; padding: 12px; }
  tr:hover { background-color: #bcbcbc; }
  td { border: none; padding: 12px; }
  .sensor { color:white; font-weight: bold; background-color: #bcbcbc; padding: 1px;
  </style></head><body><h1>ESP with BME280</h1>
  <table><tr><th>MEASUREMENT</th><th>VALUE</th></tr>
  <tr><td>Temp. Celsius</td><td><span class="sensor">"""
        + str(bme.temperature[0])
        + str(bme.temperature[1])
        + """</span></td></tr>
  <tr><td>Temp. Fahrenheit</td><td><span class="sensor">"""
        + str(round((bme.read_temperature() / 100.0) * (9 / 5) + 32, 2))
        + """F</span></td></tr>
  <tr><td>Pressure</td><td><span class="sensor">"""
        + str(bme.pressure[0])
        + str(bme.pressure[1])
        + """</span></td></tr>
  <tr><td>Humidity</td><td><span class="sensor">"""
        + str(bme.humidity[0])
        + str(bme.humidity[1])
        + """</span></td></tr></body></html>"""
    )
    return html


async def send_data():
    if gc.mem_free() < 102000:
        gc.collect()

    print(">>>> send_data:")
    bme = BME280.BME280(i2c=i2c)

    print("_____________")
    print("SENDING DATA:")
    print(f"pressure: {bme.pressure[0]}")
    print(f"humidity: {bme.humidity[0]}")
    print(f"temperature: {bme.temperature[0]}")
    
    sensor_output = {
        "celsius": bme.temperature[0],
        "fahrenheit": round((bme.read_temperature() / 100.0) * (9 / 5) + 32, 2),
        "pressure": bme.pressure[0],
        "humidity": bme.humidity[0],
    }

    res = urequests.post('http://192.168.178.25:8000/sensor-data/send-data/', headers={"Content-Type": "application/json"}, data=json.dumps(sensor_output))

    jsonresults = json.loads(res.content)
    print("RECIEWING DATA:")
    print(jsonresults)
    gc.collect()
    await uasyncio.sleep(60)
        
def server_website(s):
    if gc.mem_free() < 102000:
        gc.collect()
        print("collected")

    try:
        print("start accept")
        conn, addr = s.accept()
        print("done accept")
        conn.settimeout(0)
        print("Got a connection from %s" % str(addr))
        request = conn.recv(1024)
        conn.settimeout(None)
        request = str(request)
        print("Content = %s" % request)
        response = web_page()
        conn.send("HTTP/1.1 200 OK\n")
        conn.send("Content-Type: text/html\n")
        conn.send("Connection: close\n\n")
        conn.sendall(response)
        conn.close()
    except OSError as e:
        conn.close()
        print("Connection closed")



def main():
    # utime.sleep(10)
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.bind(("", 80))
    s.listen(5)

    server_website(s)

    # while True:
        # await uasyncio.gather(*[send_data(), server_website(s)])
        # await uasyncio.gather(*[server_website(s)])

    

# uasyncio.run(main())
main()