import BME280
from boot import i2c

def web_page():
    bme = BME280.BME280(i2c=i2c)

    html = "HTTP/1.0 200 NA\r\nContent-Type: text/html\r\n\r\n\r\n"
    html += (
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

