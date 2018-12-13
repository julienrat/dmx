#!/usr/bin/python
import time
import dmx

sender = dmx.DMX_Serial("/dev/ttyUSB0")
  
sender.start()
sender.set_data(255,6) #channel 6 Full ON 255
time.sleep(5)
sender.set_data(0,6) #channel 6 Full OFF 0
