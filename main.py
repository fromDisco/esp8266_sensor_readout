import urequests
import json
import uasyncio as asyncio
import utime
import server
import webpage

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

    res = urequests.post('http://192.168.178.37:8000/sensor-data/send-data/', headers={"Content-Type": "application/json"}, data=json.dumps(sensor_output))

    jsonresults = json.loads(res.content)
    print("RECIEWING DATA:")
    print(jsonresults)
    gc.collect()
        

# Create web server application
app = server.webserver()

# Index page
@app.route('/')
async def index(request, response):
    # Start HTTP response with content-type text/html
    response.start_html()
    web_page = webpage.web_page()
    # Send actual HTML page
    await response.send(web_page)


async def main():
    asyncio.create_task(app.run(host='0.0.0.0', port=8081))
    await asyncio.sleep(0)

    while True:
        asyncio.create_task(send_data())
        await asyncio.sleep(60)

asyncio.run(main())