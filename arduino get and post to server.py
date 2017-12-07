import serial
import requests
#initialize the serial port variable
arduino = serial.Serial('com9', 9600, timeout=.1)
while True:
        #get the data from serial port
	data = arduino.readline()[0:-2] 
	if data:
		print((data))
		#client=requests.post("http://wrektangle.herokuapp.com/api/binRegister",{"bincap":data})
                #Post the request to the server sending data in JSON format
		client=requests.post("http://192.168.43.76:8800/api/binRegister",{"bincap":data})
