import serial
import os

ser = serial.Serial("/dev/ttyACM0")
__location__ = os.path.realpath(os.path.join(os.getcwd(), os.path.dirname(__file__)))


try:
    while True:
        volt = ser.readline().strip("\n")
        print(volt)
        output = open(os.path.join(__location__, "output.csv"), "a")
        output.write(volt)
        output.close()

except IOError as (errno,strerror):
    print "I/O error({0}): {1}".format(errno, strerror)
