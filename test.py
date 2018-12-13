#!/usr/bin/python
import time
import dmx

sender = dmx.DMX_Serial("/dev/ttyUSB0")
  
sender.start()
sender.set_data(255,6)
while True:
    for u in range (0,255):
        sender.set_data(u,4)
        time.sleep(0.005)
    sender.set_data(105,5)
    time.sleep( 0.5)
    for u in range (0,255):
        sender.set_data(255-u,4)
        time.sleep(0.005)
    sender.set_data(0,5)
    #sender.set_data(0,4)
    time.sleep( 0.5)
