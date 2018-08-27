import sys, serial, argparse
from collections import deque

import matplotlib.pyplot as plt
import matplotlib.animation as animation


class AnalogPlot:
    def __init__(self, strPort, maxLen):
        # open serial port
        self.num_sensors = 1
        self.ser = serial.Serial(strPort, 9600)
        self.deque_items = [deque([0.0]*maxLen) for _ in range(self.num_sensors)]
        self.ax = self.deque_items[0]
        self.maxLen = maxLen

    # add to buffer
    def addToBuf(self, buf, val):
        if len(buf) < self.maxLen:
            buf.append(val)
        else:
            buf.pop()
            buf.appendleft(val)

    # add data
    def add(self, data):
        assert (len(data) == 1)
        for i in range(len(data)):
            self.addToBuf(self.ax, data[i])

    # update plot
    def update(self, frameNum, a0, a1):
        try:
            line = self.ser.readline()
            data = [float(val) for val in line.split()]
            print(data)
            if len(data) == len(self.deque_items):
                self.add(data)
                for i in range(len(self.deque_items)):
                    a0.set_data(range(self.maxLen), self.deque_items[i])
        except KeyboardInterrupt:
            print('exiting')

        return a0, a1

        # clean up

    def close(self):
        # close serial
        self.ser.flush()
        self.ser.close()


def main():
    parser = argparse.ArgumentParser(description="LDR serial")
    parser.add_argument('--port', dest='port', required=True)

    args = parser.parse_args()

    # strPort = '/dev/ttyACM0'
    strPort = args.port

    print('reading from serial port %s...' % strPort)

    analogPlot = AnalogPlot(strPort, 100)

    print('plotting data...')

    # set up animation
    fig = plt.figure()
    ax = plt.axes(xlim=(0, 100), ylim=(0, 1023))
    a0, = ax.plot([], [])
    a1, = ax.plot([], [])
    anim = animation.FuncAnimation(fig, analogPlot.update,
                                   fargs=(a0, a1),
                                   interval=50)
    plt.show()

    analogPlot.close()

    print('exiting.')


# call main
if __name__ == '__main__':
    main()

