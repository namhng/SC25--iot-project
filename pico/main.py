
from machine import Pin, PWM
import urequests
import keys

import time

CD_TIMER=5
US_TIMER = 10
last_time=0
check_time=0

#Parts Initialization
onboardLED =Pin(25,Pin.OUT)
trigger= Pin(13,Pin.OUT)
echo = Pin(12, Pin.IN)
sensorPin = Pin(28,Pin.IN)
ledPin = Pin(15,Pin.OUT)
servo=PWM(Pin(16))
servo.freq(50)

time.sleep_ms(1000)

#hardware functions
def servoAngle(pos,servo):
    pos = max(0, min(180, pos))
    duty = int((pos / 180) * 6552) + 1638
    servo.duty_u16(duty)

def ultra():
    trigger.low()
    time.sleep_us(2)
    trigger.high()
    time.sleep_us(5)
    trigger.low()

    timeout = 30000  # 30 ms timeout
    start = time.ticks_us()
    
    # Wait for echo to go HIGH
    while echo.value() == 0:
        if time.ticks_diff(time.ticks_us(), start) > timeout:
            print("Timeout waiting for echo HIGH")
            return -1
    signaloff = time.ticks_us()

    # Wait for echo to go LOW
    start = time.ticks_us()
    while echo.value() == 1:
        if time.ticks_diff(time.ticks_us(), start) > timeout:
            print("Timeout waiting for echo LOW")
            return -1
    signalon = time.ticks_us()

    timepassed = signalon - signaloff
    distance = (timepassed * 0.03343) / 2
    return distance


#Connectivity functions

def send_to_influx(measurements, value,tags=""):
    timestamp = str(int(time.time()))
    data = f"{measurements}{',' + tags if tags else ''} value={value} {timestamp}"
    try:
        response = urequests.post(keys.INFLUXDB_URL, headers=keys.INFLUXDB_HEADERS, data=data)
        if response:
            print("Sent data: ", data)
            print("Response status: ", response.status_code)
            print("Response content: " , response.text)
            response.close()
        else:
            print("No response from InfluxDB")
        
    except Exception as e:
        print("Failed to send to InfluxDB", e)



#Process Start
print("Initiliaze")    
ledPin.value(1)
time.sleep(1)
servoAngle(85,servo)#
ledPin.value(0)
time.sleep(3)
cooldown = False
last_tie = 0 
print("Ready!")  


while True:
    current_time = time.time()
    ledPin.value(1)
    time.sleep(0.5)
    ledPin.value(0)
    if cooldown and (current_time - last_time >= CD_TIMER):
        cooldown = False
        print("Cooldown ended. Ready to dispense.") 

    if not cooldown and sensorPin.value() == 1:
        ledPin.value(1)  #Set led turn on
        servoAngle(140,servo)
        cooldown = True
        time.sleep(0.1)
        servoAngle(90, servo)
        ledPin.value(0)
        send_to_influx("motion_event", 1, tags="sensor=pir")
        last_time = time.time()
    if current_time - check_time >= US_TIMER:
            #print("Checking distance with ultrasonic sensor...")
            distance = ultra()
            if distance != -1:
                print("Distance to object:", distance, "cm")
                send_to_influx("distance_cm", distance, tags="sensor=ultrasonic")
            else:
                print("Ultrasonic reading failed.")
            check_time = current_time

    # Print sensor value for debugginga
    # print("Sensor value:", sensorPin.value())
    time.sleep(1)
         
    
