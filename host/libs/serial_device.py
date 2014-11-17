import os
import serial
import time
import json
import functools

class SerialDevice(serial.Serial):

    def __init__(self, *args, **kwargs):
        try:
            debug = kwargs.pop('debug')
        except KeyError:
            debug = False 
        super(SerialDevice,self).__init__(*args,**kwargs)
        time.sleep(SerialDevice.RESET_SLEEP_T)
        self.deviceInfoDict = None
        self.rspDict = None
        self.cmdDict = None
        self.debug = debug

if __name__ == '__main__':

    debug = False
    dev = FlyHerder(port='/dev/ttyUSB0',timeout=2.0,debug=debug)
