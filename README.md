# SimpleDMX
## Requirements / Dependencies
before using this script, please install pyserial
```
sudo pip install pyseral
```
## Hardward compatibility
FTDI to RS485 cheap dongle :

https://fr.aliexpress.com/item/USB-to-TTL-RS485-Serial-Converter-Adapter-FTDI-Module-FT232RL-SN75176-double-function-double/32771847720.html?spm=a2g0w.search0104.3.15.63586239S7KSon&ws_ab_test=searchweb0_0,searchweb201602_2_10065_10068_319_10892_317_10696_453_10084_454_10083_10618_10304_10307_10820_10821_538_537_10302_536_10843_10059_10884_10887_100031_321_322_10103,searchweb201603_51,ppcSwitch_0&algo_expid=6957aa39-4868-4f8d-ac7f-b10f610a4a24-2&algo_pvid=6957aa39-4868-4f8d-ac7f-b10f610a4a24


## Hardware issues 

https://stevenbreuls.com/2013/05/diy-usb-dmx-dongle-interface-for-under-10/

## Usage

```
import dmx
sender = dmx.DMX_Serial("/dev/ttyUSB0")
sender.start()
sender.set_data(255,6) # value // channel
```
