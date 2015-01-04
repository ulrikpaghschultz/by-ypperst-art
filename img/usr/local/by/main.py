import config, rfid, sounds

def init():
    config.init()
    sounds.init(config.getErrorSoundFile())
    rfid.init(config.getDeviceNames())

def processTag(device,tag):
    fileName = config.mapReaderTagToSoundFile(device.fn,tag)
    print "Read",device,tag,"playing",fileName
    sounds.play(fileName)

def run():
    rfid.processEvents(processTag)

init()
run()

    
