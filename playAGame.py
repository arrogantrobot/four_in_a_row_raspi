#!/usr/bin/env python

import sys
sys.path.append("./Adafruit-Raspberry-Pi-Python-Code/Adafruit_MCP230xx")
import time
from Adafruit_MCP230xx import Adafruit_MCP230XX

ON = 1
OFF = 0

def initOutputs(mcp, startPin, stopPin):
    for pin in range(startPin, stopPin):   
        print "Setting up pin %d for output." % pin
        mcp.config(pin, mcp.OUTPUT)

def initInputs(mcp, startPin, stopPin):
    for pin in range(startPin, stopPin):
        print "Setting pin %d to input." % pin
        mcp.config(pin, mcp.INPUT)
        mcp.pullup(pin, 1)

def lightSweepUp(mcp, maxNum, sleepDuration):
    for output in range(maxNum - 1):
        mcp.output(output, ON)
        time.sleep(sleepDuration)
        mcp.output(output, OFF)

def lightSweepDown(mcp, maxNum, sleepDuration):
    outputs = range(maxNum)
    outputs.remove(0)
    for output in reversed(outputs):
        mcp.output(output, ON)
        time.sleep(sleepDuration)
        mcp.output(output, OFF)

def getInputVal(mcp, pin):
    val = mcp.input(pin) >> pin - 8
    print "pin {} is {}".format(pin, val)
    return val

def checkInputs(mcp, minSwitch, maxSwitch):
    for pin in range(minSwitch, maxSwitch):
        if getInputVal(mcp, pin):
            print "input %d is on" % pin
            return True
    return False

if __name__ == '__main__':
    interval = 0.05
    mcp = Adafruit_MCP230XX(address = 0x20, num_gpios = 16, busnum = 1)
    initOutputs(mcp, 0, 7)
    initInputs(mcp, 8, 16)
    while (not checkInputs(mcp, 8, 16)):
        sleep(0.1)

        #lightSweepUp(7, interval, mcp)
        #lightSweepDown(7, interval, mcp)
