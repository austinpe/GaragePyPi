import wiringpi2 as wp2
from time import sleep
wp2.wiringPiSetup()

#initalize pin7 to output
garagepin = 7 #bcm gpio4 #header7
wp2.digitalWrite(garagepin, 1)
wp2.pinMode(garagepin, 1)

magpin = 1 #bcm gpio18 #header12
wp2.pinMode(magpin, 0)
wp2.pullUpDnControl(magpin, 2)

def garagebutton():
    global garagepin
    wp2.digitalWrite(garagepin, 0)
    sleep(1)
    wp2.digitalWrite(garagepin, 1)
    print "Button Pressed!")

def relayon():
    global garagepin
    wp2.digitalWrite(garagepin, 0)
    print "Relay On"

def relayoff():
    global garagepin
    wp2.digitalWrite(garagepin, 1)
    print "Relay Off"

def checkstate():
    global magpin
    if wp2.digitalRead(magpin):
        print "Open!"
    else:
        print "Closed!"

#at end
wp2.pinMode(garagepin, 0)
wp2.digitalWrite(garagepin, 0)
