import serial

""" 
ser = serial.Serial("COM3", 9600)   first param: serial device    second param: baudrate

ser.port = 'COM3'       Specify/define a serial device port

data = ser.read()  read a single byte from serial device

data = ser.read(size = 5)  read n number of bytes from serial device

data = ser.readline() read one line

ser.read(ser.in_waiting)  read data from serial device while something is being written over it

ser.write() write data to serial port

ser.open() opens up the specified port

ser.close() closes the specified port

"""


print("TEST")