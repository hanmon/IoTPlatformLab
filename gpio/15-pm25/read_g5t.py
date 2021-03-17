#!/usr/bin/env python3

from pms5003 import PMS5003
import time

pms5003 = PMS5003(
    device='/dev/ttyAMA0',
    baudrate=9600,
    pin_enable=22,
    pin_reset=27
)

try:
    while True:
        data = pms5003.read()
        print("===========================")
        #print("size=1.0: ", data.pm_ug_per_m3(size=1.0))
        print("size=2.5: ", data.pm_ug_per_m3(size=2.5))
        #print("size=10: ", data.pm_ug_per_m3(size=10))
        time.sleep(1)

except KeyboardInterrupt:
    pass
