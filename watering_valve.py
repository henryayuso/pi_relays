#timer for garden automaic water valve

#importing the GPIO module
import Rpi.GPIO as GPIO

# set up GPIO pin as out put
GPIO.setmode(GPIO.BMC)
GPIO.SETUP(17, GPIO.OUT) # pin used to turn relay one with 3.3v
state = 0

#import date and time module
import datetime
import time

# setting day and time water_valve will turn on and off
MonAmOn = datetime.time(hour = 6) #time on
MonAmOff = datatime.time(hour = 7) #time off
MonPMOn  = datetime.time(hour= 18)
MonPMOff = datetime.time(hour= 19)
TueAMOn  = datetime.time(hour = 6)
TueAMOff = datetime.time(hour = 7)
TuePMOn  = datetime.time(hour = 18)
TuePMOff = datetime.time(hour = 19)
WedAMOn  = datetime.time(hour = 6)
WedAMOff = datetime.time(hour = 7)
WedPMOn  = datetime.time(hour = 18)
WedPMOff = datetime.time(hour = 19)
ThuAMOn  = datetime.time(hour = 6)
ThuAMOff = datetime.time(hour = 7 )
ThuPMOn  = datetime.time(hour = 18)
ThuPMOff = datetime.time(hour = 19)
FriAMOn  = datetime.time(hour = 6)
FriAMOff = datetime.time(hour = 7)
FriPMOn  = datetime.time(hour = 18) 
FriPMOff = datetime.time(hour = 19)
SatAMOn  = datetime.time(hour = 6)
SatAMOff = datetime.time(hour = 7)
SatPMOn  = datetime.time(hour = 18)
SatPMOff = datetime.time(hour = 19)
SunAMOn  = datetime.time(hour = 6)
SunAMOff = datetime.time(hour = 7)
SunPMOn  = datetime.time(hour = 18)
SunPMOff = datetime.time(hour = 19)

# putting all the time in an array
onTimeAMOn = [MonAMOn, TueAMOn, WedAMOn, ThuAMOn, FriAMOn, SatAMOn, SunPMOn]
OnTimePM = [MonPMOn, TuePMOn, WedPMOn, ThuPMOn, FriPMOn, SatPMOn, SunPMOn]
OffTimeAM = [MonAMOff, TueAMOff, WedAMOff, ThuAMOff, FriAMOff, SatAMOff, SunAMOff]

# Start the loop that will run until you stop the program or turn off your Raspberry Pi.
 
while True:
    button = GPIO.input(17)
    #print('ttt')
    global state
    if button == 0:
        #print('button', button)
        state = 1
        #print('state', state)
    if state == 1:
        time.sleep(0.5)
        GPIO.output(24, True)
        GPIO.output(27, True)
        time.sleep(3600) #3600
        state = 0
        GPIO.output(24, False)
        GPIO.output(27, False)
 
 
 
    # get the current time in hours, minutes and seconds
    currTime = datetime.datetime.now()
    #print(currTime)
    # get the current day of the week (0=Monday, 1=Tuesday, 2=Wednesday...)
    currDay = datetime.date.today().weekday()
 
        #Check to see if it's time to run the appliance for the AM hours
    while (currTime.hour &gt;= OnTimeAM[currDay].hour and currTime.hour &lt;= OffTimeAM[currDay].hour): # set the GPIO pin to HIGH GPIO.output(24, True) GPIO.output(27, True) time.sleep(60) currTime = datetime.datetime.now() currDay = datetime.date.today().weekday() else: if (currTime.hour &gt;= OffTimeAM[currDay].hour - 1):
            GPIO.output(24, False)
            GPIO.output(27, False)
 
 
 
    #Check to see if it's time to run the appliance for the PM hours
    while (currTime.hour &gt;= OnTimePM[currDay].hour and currTime.hour &lt;= OffTimePM[currDay].hour): GPIO.output(24, True) GPIO.output(27, True) time.sleep(60) currDay = datetime.date.today().weekday() currTime = datetime.datetime.now() else: if (currTime.hour &gt;= OffTimePM[currDay].hour - 1):
            GPIO.output(24, False)
            GPIO.output(27, False)


