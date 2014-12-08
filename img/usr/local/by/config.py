readers_static_list = {}
devices_static_list = [
    '/dev/input/event8',
    '/dev/input/event9',
    '/dev/input/event10',
    '/dev/input/event11'
]

def mapReaderTagToSoundFileo(reader,tag):
    tags = readers_static_list[reader]
    if tags==None:
        print "Error: unknown reader:",reader
        return None
    return tags[tag]

def register(reader,tag,file):
    if readers_static_list[reader]==None:
        readers_static_list[reader] = {}
    readers_static_list[reader][tag]  = file

def getDeviceNames():
    return devices_static_list

def init():
    register('a','b','c')
