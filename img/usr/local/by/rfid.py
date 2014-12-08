from evdev import InputDevice, categorize, ecodes
from select import select

buffer={}
inputDevices=None

def init(deviceNames):
    global inputDevices
    inputDevices=map(InputDevice,deviceNames)

def code2text(code):
    if code==11:
        return '0'
    elif code==28:
        return ''
    elif code<=10 and code>1:
        return chr(ord('0')+code-1)
    else:
        return None

def processEvent(device,e,processTag):
    global buffer
    if not device in buffer:
        buffer[device] = ''
    if e.type==ecodes.EV_KEY:
        c=categorize(e)
        if c.keystate==1:
            s=c.scancode
            t=code2text(s)
            if t=='':
                processTag(device,buffer[device])
                buffer[device] = ''
            elif t!=None:
                buffer[device] = buffer[device]+t

def processEvents(processTag):
    print 'Ready'
    while True:
        readyDevices,_,_=select(inputDevices,[],[])
        for dev in readyDevices:
            for event in dev.read():
                processEvent(dev,event,processTag)

def processTagInternalTest(device,tag):
    print 'Reader',device,'read',tag

def test(deviceNames):
    setDeviceNames(deviceNames)
    processEvents(processTagInternalTest)
