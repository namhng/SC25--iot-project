WIFI_SSID = '{YourSSID}'
WIFI_PASS = '{YourWiFIPassword}'
INFLUXDB_URL = 'http://{INFLUXDB_ADDRESS}:{PORT}/api/v2/write?org={your-org}&bucket={your-bucket}&precision=s'
INFLUXDB_TOKEN = '{TOKEN}'
INFLUXDB_HEADERS = {
    "Authorization": "Token " + INFLUXDB_TOKEN,
    "Content-Type": "text/plain"
}
