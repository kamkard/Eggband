# -*- coding: utf-8 -*-
"""
A script to save to CSV and then plot the data coming from a serial port
Written to monitor the thermocouple.
Author: David Kamkar

Original Author: Sujay HG
"""
import serial # import Serial Library
import serial.tools.list_ports # To find arduino port
import warnings # Warn if
import csv
import numpy  # Import numpy
import matplotlib.pyplot as plt #import matplotlib library
#from drawnow import *
#import random

"""
NOTES:
Put list port section in new script, add baud rate
"""

thermo= []

arduino_conn = [
    p.device
    for p in serial.tools.list_ports.comports()
    if 'Arduino' in p.description
]
if not arduino_conn:
    raise IOError("No Arduino found")
if len(arduino_conn) > 1:
    warnings.warn('Multiple Arduinos found - using the first')

try:
    arduinoData = serial.Serial(arduino_conn, 9600) #Creating our serial object named arduinoData
except:
    print("COM issue!")
    quit()

while True:
    arduinoData.name


"""
plt.ion() #Tell matplotlib you want interactive mode to plot live data
cnt=0

def makeFig(): #Create a function that makes our desired plot
    plt.ylim(0,10000)                                 #Set y min and max values
    plt.title('thermo sensor Data')      #Plot the title
    plt.grid(True)                                  #Turn the grid on
    plt.ylabel('Temp')                            #Set ylabels
    plt.plot(thermo, 'ro-', label='thermo')       #plot the temperature
    plt.legend(loc='upper left')                    #plot the legend
    
while True: # While loop that loops forever
    while (arduinoData.inWaiting()==0): #Wait here until there is data
        pass #do nothing
    arduinoString = arduinoData.readline() #read the line of text from the serial port
 #   arduinoString=random.randint(0,2000)
    print arduinoString
    temp = float( arduinoString)   
         #Convert to floating number and put in temp
    thermo.append(temp)                     #Build our tempF array by appending temp readings
    drawnow(makeFig)                       #Call drawnow to update our live graph
    plt.pause(.000001)                     #Pause Briefly. Important to keep drawnow from crashing
    cnt=cnt+1
    if(cnt>50):                            #If you have 50 or more points, delete the first one from the array
        thermo.pop(0)                       #This allows us to just see the last 50 data points
"""
