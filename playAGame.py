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
        mcp.pullup(pin, 1)
        mcp.config(pin, mcp.INPUT)

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
    pinVal = mcp.input(pin) 
    val = pinVal >> pin
    #print "pin {} returns {} is {}".format(pin, pinVal, val)
    return val

def checkInputs(mcp, minSwitch, maxSwitch):
    for pin in range(minSwitch, maxSwitch):
        if getInputVal(mcp, pin) == 0:
            #print "input %d is on" % pin
            return pin
    return False

def getInput(mcp):
    answer = False
    while(not answer): 
        answer = checkInputs(mcp, 8, 16)
    return answer - 9

if __name__ == '__main__':
    interval = 0.05
    mcp = Adafruit_MCP230XX(address = 0x20, num_gpios = 16, busnum = 1)

    #mcp.pullup(7, 1)
    #mcp.config(7, mcp.INPUT)
    #print "answer = %d" % (mcp.input(7) >> 7)

    initOutputs(mcp, 0, 7)
    initInputs(mcp, 8, 16)

    print "Make your move."
    print "You moved at column %d" % (getInput(mcp) + 1)

    #while (not checkInputs(mcp, 8, 16)):
    #    time.sleep(0.1)

        #lightSweepUp(7, interval, mcp)
        #lightSweepDown(7, interval, mcp)
