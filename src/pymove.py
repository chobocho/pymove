# pymove.py

import win32api
import win32con
import sys

mVersion = "V0.627_20170622"

def clickMouseLeft(x,y):
    win32api.SetCursorPos((x,y))
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN,x,y,0,0)
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP,x,y,0,0)

def clickMouseRight(x,y):
    win32api.SetCursorPos((x,y))
    win32api.mouse_event(win32con.MOUSEEVENTF_RIGHTDOWN,x,y,0,0)
    win32api.mouse_event(win32con.MOUSEEVENTF_RIGHTUP,x,y,0,0)

def moveMouseXY(x,y):
    win32api.SetCursorPos((x,y))


def readDataFile(filename):
    ''' Example of data file
        L 1 2
        R 2 3
        M 3 4
    '''
    with open(filename, 'r') as fp:
        cmdlines = fp.readlines()
    return cmdlines


def parseCommand(cmdlines):
    cmdlist = []
    for c in cmdlines:
        cmd = c.strip().split(" ")
        cmdlist.append(cmd)
    return cmdlist

cmdTable = { 
   'L':clickMouseLeft,
   'R':clickMouseRight,
   'M':moveMouseXY
}

def process(cmdlist):
    for c in cmdlist:
        cmdTable[c[0]](int(c[1]), int(c[2]))

def main(filename):
    cmdlines = readDataFile(filename)
    cmdlist = parseCommand(cmdlines)
    process(cmdlist)

def printHelp():
    print "\n[Help]"
    print "Usage : pymove filename"

if __name__ == '__main__':
    if (len(sys.argv) < 2) or ('-h' in sys.argv[1:]):
        printHelp()
    else:
        main(sys.argv[1])
    print mVersion
