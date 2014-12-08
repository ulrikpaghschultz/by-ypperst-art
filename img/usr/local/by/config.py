files_static_list = [
    "sound/bird_chirping.mp3",
    "sound/birds_cardinal.mp3",
    "sound/birds_efx.mp3",
    "sound/bubble.mp3",
    "sound/buceoa.mp3",
    "sound/cats_cats_meow.mp3",
    "sound/dog_siberian_husky_barks_to_black_shadow.mp3",
    "sound/donkey_braying.mp3",
    "sound/frog_afterrain.mp3",
    "sound/frog_croaking.mp3",
    "sound/gun_fiar.mp3",
    "sound/large_cat_or_beast_growls_edited_human_voice_.mp3",
    "sound/proyectile.mp3",
    "sound/small_dog_bark.mp3",
    "sound/small_fountain.mp3",
    "sound/water_sloshing_and_swirling_around_in_bowl.mp3"
]

devices_static_list = [
    '/dev/input/event8',
    '/dev/input/event9',
    '/dev/input/event10',
    '/dev/input/event11'
]

r0 = devices_static_list[0]
r1 = devices_static_list[1]
r2 = devices_static_list[2]
r3 = devices_static_list[3]
tA = "0008555702"
tB = "0008545568"
tC = "0008555028"
tD = "0008543858"

readers_static_list = {
    r0: {
        tA: files_static_list[0],
        tB: files_static_list[1],
        tC: files_static_list[2],
        tD: files_static_list[3]
        },
    r1: {
        tA: files_static_list[4],
        tB: files_static_list[5],
        tC: files_static_list[6],
        tD: files_static_list[7]
        },
    r2: {
        tA: files_static_list[8],
        tB: files_static_list[9],
        tC: files_static_list[10],
        tD: files_static_list[11]
        },
    r3: {
        tA: files_static_list[12],
        tB: files_static_list[13],
        tC: files_static_list[14],
        tD: files_static_list[15]
        }
}

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
