# Automatic Treat Dispenser

Nam Hoang (nh223av)

## Project Overview
For this course,  I chose to create an automatic treat dispenser with IoT functionalities. The dispenser in itself consists of an IR motion sensor, an ultrasonic ranging module, a servo motor, and last but not least the microcontroller Raspberry Pi Pico WH. The system is constructed on a breadboard and is powered by a breadboard power supply with a 9V battery during testing and prototyping.
In addition to the device itself, the system as a whole also uses InfluxDB and Grafana to process the data collected by the microcontroller (a variation of the TIG stack, if you will). The microcontroller sends the data directly through REST API to InfluxDB and stores the data, which then is visualized through a dashboard in Grafana.

The project time from start to finish can vary greatly depending on the experience and familiarity of both microcontrollers ( and its components) and Docker, but as a whole an approximation would be between three to ten hours.

## Objective
The goal of this project is primarily to track the eating habits by tracking how often candies/ treats are requested. As I do not own any pets, I can not sadly use them as an excuse to meticulously analyze the eating habits, but I figure placing this in a common space in an office or in a shared apartment can offer valuable insights, e.g., theory if snacking habits increase during stressful times.

As I was rather well acquainted with Docker and Grafana, I decided to host the server on my laptop as the data for me personally would only be relevant when I am already working on my laptop and therefore can have the services running in the background during my usual studies or personal work. 

Since my studies are primarily focussed on just software, this project helped me understand the interaction between software and hardware better. 
Futhermore, the project for me also served as a prototype for future enhancements to the candy dispenser such as integrating a minigame which has to be completed before candy will be dispensed, e.g., a trivia question that has to be answered correctly.

## Material
For this course, I decided to go for a more extensive kit option that was recommended by the lecturers that contained all the material needed and other parts (680 SEK). A price breakdown if one decided to order each part individually is shown in the following:

| Part		| Cost 		| 	Link 		| Description	 |
|----------|----------|----------|----------|
| Raspberry Pi Pico WH    |  99 SEK        |  [electrokit](https://www.electrokit.com/raspberry-pi-pico-wh?srsltid=AfmBOooyRyaHb14HhGaeidTHA0Z_myYrwMB6XcYtzSqHnTZK_JG6wuC24dQ&gQT=2)         | Affordable microcontroller that can hold instructions for other parts and can store & send data.         | 
| Breadboard    |     59 SEK     |  [electrokit](https://www.electrokit.com/kopplingsdack-730-anslutningar)        |    For building and testing electronic circuits without soldering, ideal for prototyping      
| Servo Motor (SG90)  |    69 SEK      |   [electrokit](https://www.electrokit.com/en/servo-msr-1.3-9-360)       | A motor that precisely rotates to a specific angle.        |          |
| PIR Sensor (HC-SR501)   |      55 SEK    |   [electrokit](https://www.electrokit.com/en/pir-rorelsedetektor-hc-sr501)       |   Detects movement of temperature that is compared to surrounding area, if its higher the output is activated       |          |
| Ultrasonic Distance Sensor (HC-SR04)    |     59 SEK     |   [electrokit](https://www.electrokit.com/en/avstandsmatare-ultraljud-hc-sr04-2-400cm)        |   A sensor that uses sound waves to measure the distance to nearby objects.       |          |
| 9V Battery    |     16 SEK     |   [electrokit](https://www.electrokit.com/en/batteri-9v-6f22)        |   Serves as the power supply for the different components       |          |
| Breadboard Power Supply  (HW- 131)  |    (79 SEK)      |   [electrokit alternative](https://www.electrokit.com/en/stromforsorjning-for-kopplingsdack-3.3/5v-usb-c)        |   A breadboard powersupply that can provide more power than the standalone Pico. Seems to not be available as a standalone purchase, but was included in my kit I bought.       |          |
| Jumper Wires / Ribbon Cables    |    79 SEK      |    [electrokit](https://www.electrokit.com/en/kopplingstrad-byglar-for-kopplingsdack)       |   Flexible wires used to connect components on a breadboard or between boards.       |          |
| Optional: Dispenser Materials / Server   |      flexible    |   -		       |  Material cost for the dispenser itself and the choice of server, depends on user.     |          |
| Optional: LED + 220 Ohm Resistor |5 SEK |          |   Used for making sure that my device is working without seeing the inputs when not plugged into my laptop, as my onboard LED did not work.  The resistor limits to current flowing through the LED.  |          |
| Optional: Capacitor | 5 SEK |     [electrokit](https://www.electrokit.com/en/el.lyt-10uf-100v-105c-8x12mm-bipolar)      |   Helps with the sudden power spikes incurred by the servo movement.    |          |
| Micro USB Cable  | free |           |   Used to upload the relevant files to the microcontroller. Most likely is included in your microcontroller purchase or available at home.       |          |
|   |**Total:    515  SEK**  |           |          |          |


## Computer Setup
The tools necessary to work with the microcontroller, ordered by step order:

 - Visual Studio Code
 - Node.js
 - Pymakr extenstion
 - Micropython firmware

### Install Visual Studio Code
To make life easier, you probably want to use an IDE to help programming. A popular option is [Visual Studio Code](https://code.visualstudio.com/), that is available for every common OS.

### Install Node.js
It is necessary to install [Node.js](https://nodejs.org/en/download/) since it is a dependency for Pymakr to work and thus available in the IDE.

### Install Pymakr extension in VS Code
**(Note: This extension is deprecated and no longer maintained, but it was one of the  first recommendations by the lecturer's this year. I started with it and did not feel like changing as it served its purpose without problems for me.)**

To make the microcontroller interactable within the IDE,  the [Pymakr extension for VS Code](https://marketplace.visualstudio.com/items?itemName=pycom.Pymakr) was used. A baseline tutorial can be found [here](https://github.com/pycom/pymakr-vsc/blob/HEAD/GET_STARTED.md)

### Update microcontroller firmware
Download the most recent firmware [here](https://micropython.org/download/RPI_PICO_W/). Before plugging the board into USB hold down the BOOTSEL button. This will make the Pico act like a storage device similar to a USB. Navigate to it, open it, and drop the firmware into the "folder". The board will automatically disconnect and if it does so will be ready to use afterwards.



## Putting Everything Together

### Hardware
The process in itself is rather easy as it is the same repeated process, but due to the various components might seem daunting. As an overview, a mock diagram is shown below (uses different power board supply). Following the diagram should lead to the desired result, but here are the written out steps:

![Untitled Sketch 2_bb](https://github.com/user-attachments/assets/df453b2b-7b71-4c0d-ba00-6425198238c7)

 1. Plug in the breadboard power supply into the breadboard so the (+) and (-) pins of the power supply aligns with the respective ones in the breadboard.
 2. Plug in the Pico in the desired position. The placement is largely preference, but some are more advantageous than others, i.e., USB slot facing away from board so it is easier to access.
 3. Connect the components pins with ribbon cables and/or jumper wires.
 4. Plug in the VCC pins (red wires in this case) into the red rail (+) of the breadboard and GRND pins (blue/black) into the GRND rail.
 5. Take the output pin and plug them into a desired GPIO slot of the Pico.
 6. Repeat for each component.
 7. Plug in the 9V battery into the breadboard power supply.

### Power Consumption

Unfortunately, I do not have the resources, be it either equipment or time, to do a proper analysis of the usage of my system. As a whole the system, was not designed to be used over a long period of time, but rather only when im actively using my laptop at home, which usually is only in shorter time frames. Ideally, it would be powered by a 9-12V DC wall socket, as this is the maximum the breadboard power supply supports. One could lower the consumption of the sensors and servo by actually turning them off via a relay or through MOSFETS until the cooldown time has expired. This is especially relevant for the ultrasonic sensor and the servo, as they still draw current even if not actively used. A minor addition, I did later on was to add a capacitor to one of the rails where the servo is powered to balance the sudden spikes of current when the servo is used.

### Platform
As previosly outlined in the Objective section, I am using a variation of the common TIG stack (T- Telegraf, I- InfluxDB, G- Grafana) that was introduced to the course. Traditionally, this method uses MQTT to transmit data, but for my project I opted to skip this step and ended up with just an IG stack, I guess. Instead, when transmitting data I use REST API through WIFI to directly send new data to InfluxDB which is later explained in more detail.
InfluxDB is an ideal database for this project as it was designed for specifically time series data, which means that it is suitable for high write rates and timestamped data. Unfortunately, I had to learn its query language **Flux**, which is common for many database really.  As I was hosting these services on docker, it is important that it also saves data in efficient manner which InfluxDB also excels in.

### The Code
Coding as a whole is rather straightforward with some experience, as we essentially just read sensor data. Beginners should not fret though as the sensor and servo motors are well documented and reading the data itself are just a few lines of code.

The ultrasonic sensor and the servo motor did require some custom functions to work, but first the general structure.

In general, the structure of the project is as follows:

    boot.py
    keys.py
    main.py

`boot.py` is run when the system powers on and is only run **once**, which makes it the ideal file to have the code to connect to your WiFi-network.

`keys.py` contains any information that is supposed to be confidential such as authorization tokens and WiFi information. 

`main.py` is the heart of the operation. It contains the instructions to make the dispenser operate.

#### Detailed Code Sections
`boot.py`

 
The following code section is copied from a template that was given to us to connect to WiFi.  It is fairly boilerplate, and the code itself does not need adjustments, to make it work for you own connection, `keys.py` must have the correct values to be able to connect to your network.
       
    import keys
    import network
    import time
    import ntptime
    
    def connect():
        wlan = network.WLAN(network.STA_IF)         # Put modem on Station mode
        if not wlan.isconnected():                  # Check if already connected
            print('connecting to network...')
            wlan.active(True)                       # Activate network interface
            # set power mode to get WiFi power-saving off (if needed)
            wlan.config(pm = 0xa11140)
            wlan.connect(keys.WIFI_SSID, keys.WIFI_PASS)  # Your WiFi Credential
            print('Waiting for connection...', end='')
            # Check if it is connected otherwise wait
            while not wlan.isconnected() and wlan.status() >= 0:
                print('.', end='')
                time.sleep(1)
        # Print the IP assigned by router
        ip = wlan.ifconfig()[0]
        print('\nConnected on {}'.format(ip))
        return ip
    
    def http_get(url = 'http://detectportal.firefox.com/'):
        import socket                           # Used by HTML get request
        import time                             # Used for delay
        _, _, host, path = url.split('/', 3)    # Separate URL request
        addr = socket.getaddrinfo(host, 80)[0][-1]  # Get IP address of host
        s = socket.socket()                     # Initialise the socket
        s.connect(addr)                         # Try connecting to host address
        # Send HTTP request to the host with specific path
        s.send(bytes('GET /%s HTTP/1.0\r\nHost: %s\r\n\r\n' % (path, host), 'utf8'))    
        time.sleep(1)                           # Sleep for a second
        rec_bytes = s.recv(10000)               # Receve response
        print(rec_bytes)                        # Print the response
        s.close()                               # Close connection
    
    # WiFi Connection
    try:
        print("HelloBoot")
        ip = connect()
    except KeyboardInterrupt:
        print("Keyboard interrupt")
    
    # HTTP request
    try:                                         
        http_get()
    except (Exception, KeyboardInterrupt) as err:
        print("No Internet", err)

I also added a small section that is run to make the Pico use the correct time for correct data logging.

    try:
    ntptime.settime()
    print("Time synced!")
except Exception as e:
    print("Failed to sync time:", e)

`key.py`
For the WiFi configuration make sure to have the correct values for your network SSID and password (case sensitive).

    WIFI_SSID= "YOUR WIFI NAME"
    WIFI_PASSWORD= "yourPassword"
For the later REST API calls, I also included the URL to my influxDB, an authorization token and a header which is necessary for HTTP requests:

    INFLUXDB_URL = '{myInfluxdbAddress}:{myInfluxDBport}/api/v2/write?org={my-org}&bucket={my-bucket}&precision=s'
     INFLUXDB_TOKEN = '{my-token}' 
     INFLUXDB_HEADERS = { "Authorization": "Token "+ INFLUXDB_TOKEN , "Content-Type": "text/plain" }
    
The address is my local IP address of the device that its being hosted on, the rest are declared in the `docker-compose`file which is explained later.

`main.py`

As mentioned before this contains the instructions for the dispenser. 

Here is the breakdown:
We first import relevant functions, declare variables such as cooldown and check timers, and initialize the parts with the corresponding GPIO pins.

    from machine import Pin, PWM
	import urequests
	import keys

	import time

	CD_TIMER=10
	US_TIMER = 600
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

We then declare some functions, `servoAngle(pos,servo)` , requires the desired angle as a parameter and which servo to use.

    def servoAngle(pos,servo):
	    pos = max(0, min(180, pos))
	    # Convert angle to duty cycle (16-bit)
	    duty = int((pos / 180) * 6552) + 1638
	    servo.duty_u16(duty)

`ultra.py` is responsible to get the correct distance readings:

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

We then declare some functions to make our microcontroller send data to the InfluxDB, the prints statements can be of course skipped, but are very useful for debugging:

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
    
Before the operation loop, we do one final initialization of the hardware itself. We reset the servo angle and make sure it can operate. Furthermore the PIR sensor requires some startup time (15-40 seconds) to operate properly.

    print("Initiliaze")    
	ledPin.value(1)
	time.sleep(1)
	servoAngle(85,servo)#
	ledPin.value(0)
	time.sleep(30)
	cooldown = False
	last_tie = 0 
	print("Ready!")  

The main loop that is responsible for operation:

    
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

It takes the current time and makes sure that the cooldown period is over. If the dispenser is ready to operate it waits until it detects movement  which in turn triggers a quick movement by the servo. The operation is finished by sending an entry to the InfluxDB by calling `send_to_influx(x,y,z)` with the relevant data.
The distance sensor works on a seperate timer and independent from the motion sensor. Whenever it reaches its seperate `US_TIMER`, it measures the distance and sends the data with the same function as outlined above.

While testing this code, I made use of several print statements and had my Pico plugged into my laptop via USB, as the values are printed to the terminal. When everything is working fine, the files can be uploaded to the Pico and disconnected from the laptop/ IDE. 

## Transmitting the data/ connectivity

When starting the course, I was curious to learn about different connectivity methods such as LoRa and The Things Internet, but I was disappointed when I found out an additional sensor was required that costs around 150 SEK. As I already, spent a significant amount of money I opted to do a different option, which was WiFi.  It is set up once and is done, as long as the WiFi configurations don't change. As I used this project as a prototype for future expansion, WiFi is an especially good choice as there won't be anything to worry about in the future, be it handling more sizeable or complex data.

This device is also intended to be used with a constant power supply since the system itself is so power hungry, there is also no concern on how often we transmit data.

Looking at the function that sends the data again:

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
`data` is structured in the following way:

 - `measurements` is the key we will later use to fetch the data through
   queries. 
 -  `tags` can be used if more complex data down the line is
   required making future categorization easier. 
   - `value` contains the
   actual value for our sensors, it is either a float value for our
   ultrasonic sensor as it measures the distance or just 1 when the PIR
   sensor detects motion. 
   - `timestamp` is important to filter the values
   for data visualization and /or aggregation.

The rest of the response takes values that were declared in the `keys.py`file.

## Presenting the Data

### **Visualization**
Set up [Grafana](https://hackmd.io/@lnu-iot/BkwDAimvn#Setting-up-Grafana), and then create a dashboard.
	 For this project I opted to use a gauge to display the status of the content and if the dispenser needs refilling. The motion sensor values are aggregated in a per hour basis. The dashboard can be seen here:

![iot_dashboard](https://github.com/user-attachments/assets/b62f3d8d-90bb-4396-b486-9e700032f9ee)

  
 ### Getting the relevant data: 
 Add a new Visualization to the dashboard and make sure the data source is the name of your InfluxDB name.
	 For the **content gauge**, the following query in Flux was used. It just fetches the data we have send and filters what was created an hour ago:
	 

    from(bucket: "telegraf")
	  |> range(start: -1h)
	  |> filter(fn: (r) => r._measurement == "distance_cm")
	  |> filter(fn: (r) => r.sensor == "ultrasonic")
	  |> filter(fn: (r) => r._field == "value")
	  |> last()

Then on the right hand side choose the Gauge Visualization, and add the desired threshold values  (if labels are wanted, add value mappings as well).

![iot_gauge](https://github.com/user-attachments/assets/ed7b62f1-9a23-4371-b2fc-61e13701aab4)

For the **usage statistic**, the following query was used with the bar chart visualization chosen.

    from(bucket: "telegraf")
	  |> range(start: 0)
	  |> filter(fn: (r) => r._measurement == "motion_event")
	  |> filter(fn: (r) => r.sensor == "pir")
	  |> filter(fn: (r) => r._field == "value")
	  |> aggregateWindow(every: 1h, fn: count, createEmpty: false)
	  |> yield(name: "hourly_motion_count")
It fetches the data just like before, but this time  we use `aggregateWindow` to set a per time frame we are interested in.

![iot_bar](https://github.com/user-attachments/assets/8891d5e8-9a92-44b9-add1-87a99498e8c3)

## Finalizing the Design

As previously alluded to in the Materials section, it is up to the creator how the dispenser itself is going to look like and what material to use. If a 3d printer is available, one can design their own dispenser. Unfortunately, for me I had no access to one and therefore opted to use very cheap materials I had at hand. Those were **plastic bottles, cardboard, rubber bands and duct tape.**
The dispenser storage is made from a cut up plastic bottle with a hole at the top to "seat" the ultrasonic sensor.

The servo motor uses some cardboard to control the flow of the candy:

![iot_product](https://github.com/user-attachments/assets/d897ce6d-89fc-4804-8d22-03300216c3bc)

All in all, I am happy with how the project turned out as it was largely just a prototype to get the hang of how hardware and software interact with each other. It was especially intriguing to experiment with the sensitivity of the sensors and reading up on their respective sensitivities and what factors, e.g., temperature, power, can influence the sensor's capabilities to work. 
![IoT](https://github.com/user-attachments/assets/c9cdfe1c-6aa7-43e3-862c-250faa2230f1)
