readers_static_list = {}

def mapReaderTagToSoundFile(reader,tag):
    tags = readers_static_list[reader]
    if tags==None:
        print "Error: unknown reader:",reader
        return None
    return tags[tag]

def register(reader,tag,file):
    if readers_static_list[reader]==None:
        readers_static_list[reader] = {}
    readers_static_list[reader][tag]  = file

def init():
    register('a','b','c')
