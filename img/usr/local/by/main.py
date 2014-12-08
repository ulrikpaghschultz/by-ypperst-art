import config, rfid, sounds

def init():
    config.init()
    sounds.init()
    rfid.init(config.getDeviceNames())
