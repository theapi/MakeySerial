import serial
if __name__ == '__main__':

    s = serial.Serial(port='/dev/ttyACM0', baudrate=9600, timeout=1,
                       parity=serial.PARITY_EVEN, rtscts=1)
    while True:
        print(s.readline())
