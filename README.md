# SimpleDMX

```
import dmx
sender = dmx.DMX_Serial("/dev/ttyUSB0")
sender.start()
sender.set_data(255,6) # value // channel
```
