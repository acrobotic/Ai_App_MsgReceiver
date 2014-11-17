from __future__ import print_function
import serial
import time

RESET_SLEEP_T = 2.0

CMD_GET_MEASUREMENT = 0

RSP_ERROR = 0
RSP_SUCCESS = 1

class SerialDevice(serial.Serial):

    def __init__(self, port, timeout=2.0, debug=False):
        params = {'baudrate': 9600, 'timeout': timeout}
        super(SerialDevice,self).__init__(port,**params)
        time.sleep(RESET_SLEEP_T)
        self.debug=debug

    def sendCmd(self,cmd):
        """
        Send command to colorimeter and receiver response.
        """
        self.write('{0}\n'.format(cmd))
        rsp = self.readline()
        if self.debug:
            print('cmd: ', cmd)
            print('rsp: ', rsp)
        rsp = eval(rsp.strip())
        if rsp[0] == RSP_ERROR:
            raise IOError, 'bad response: {0}'.format(rsp)
        return rsp
        
    def getMeasurement(self):
        """
        Get a measurement from the device. 
        """
        cmd = '[{0}]'.format(CMD_GET_MEASUREMENT)
        rsp = self.sendCmd(cmd)
        pwr = rsp[1]
        ldr = rsp[2]
        return pwr, ldr

    def printMeasurement(self):
        """
        Test function. Gets a measurement and pretty prints it.
        """
        f, t, a = self.getMeasurement()

        print('Frequency:')
        print('  red:    {0:1.2f}'.format(f[0]))
        print('  green:  {0:1.2f}'.format(f[1]))
        print('  blue:   {0:1.2f}'.format(f[2]))
        print('  white:  {0:1.2f}'.format(f[3]))

        print('Transmission:')
        print('  red:    {0:1.2f}'.format(t[0]))
        print('  green:  {0:1.2f}'.format(t[1]))
        print('  blue:   {0:1.2f}'.format(t[2]))
        print('  white:  {0:1.2f}'.format(t[3]))

        print('Absorbance:')
        print('  red:    {0:1.2f}'.format(a[0]))
        print('  green:  {0:1.2f}'.format(a[1]))
        print('  blue:   {0:1.2f}'.format(a[2]))
        print('  white:  {0:1.2f}'.format(a[3]))

# -----------------------------------------------------------------------------
if __name__ == '__main__':

    dev = Device('/dev/tty.usbmodemfd111')
    dev.printMeasurement()
