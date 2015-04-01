# print "hello1"
import serial
import string
import time


nbTime = 10

while nbTime > 0 :
    # print "hello1"

    ser = serial.Serial('/dev/tty.usbmodem1421', 115200, timeout=3)
    # print "hello2"

    s = ser.read(1000)
    # print ""
    # print ""
    # print ""
    # print s

    ssPos = string.find(s, '------------------------Sector 0-------------------------')
    # print ""
    # print ssPos
    # print ""
    print ""
    start = 489
    emailPart1 = s[ssPos + start: ssPos + start + 7]
    emailPart2 = s[ssPos + start + 67: ssPos + start + 67 + 16]
    emailPart3 = s[ssPos + start + 67 + 76: ssPos + start + 67 + 76 + 16]
    print emailPart1 + emailPart2 + emailPart3
    print ""
    # print ""
    time.sleep(2)
    
    ser.flush()

    # print "hello3"
    ser.close()
    # print "hello4"
    
    nbTime-=1
    
    # print nbTime
    
    
