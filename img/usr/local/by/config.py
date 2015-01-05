from random import seed, shuffle

test_files_static_list = [
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

undefined_sound_file = "sound/dyr_fly_buzz_on_window.mp3"

left_files_static_list = [
    "sound/historie_A_B_C.mp3",
    "sound/historie_Da_Humpernikkel_var_paa_biblioteket.mp3",
    "sound/historie_Da_solen_blev_vaek01.mp3",
    "sound/historie_Historien_om_Bastian_og_myrerne.mp3",
    "sound/historie_Tael_til_ti01.mp3",
    "sound/natur_Jutland_Winter_Underwater_No_Pops.mp3",
    "sound/natur_Myles_Thompson_Bulbjerg.mp3",
    "sound/natur_2011_05_16A_Joyce_WA_01_strream_like_downpour.mp3",
    "sound/natur_2011_05_16A_Joyce_WA_04_Pacific_Chours_Frogs_evening_ambi.mp3",
    "sound/natur_2011_05_16A_Joyce_WA_08_Trickling_Stream_W_Birds_Dawn.mp3",
    "sound/musik_14_Luftballon.mp3",
    "sound/musik_Nanna_1.mp3",
    "sound/musik_Nanna_Schelde_Lullaby.mp3",
    "sound/musik_The_Land_The_Sea_demo.mp3",
    "sound/musik_You_Look_So_Much_Fairer_Now_That_Youre_Fading.mp3",
    "sound/musik_01_No_1.mp3",
    "sound/musik_02_No_2.mp3",
    "sound/musik_04_Farvernes_landskab.mp3",
    "sound/musik_04_No_4.mp3",
    "sound/musik_05_Hele_verden_er_vores.mp3",

    "sound/lyd_Underwater_W_Shingle.mp3",
    "sound/lyd_VB03_36_02_Laugh_Girls_Giggling.mp3",
    "sound/lyd_musical_accent_glockenspiel_chime_bright.mp3",
    "sound/lyd_musical_electric_guitar_dry_bb_sus4.mp3",
    "sound/lyd_musical_piano_mysterious_arpeggio_descend.mp3",
    "sound/lyd_musical_violin_g_major_scale_up_hold_last_note_vibrato.mp3",

    "sound/dyr_Cows_1.mp3",
    "sound/dyr_Lion_Growling.mp3",
    "sound/lyd_freesfx_jingle.mp3",
    "sound/lyd_freesfx_walk.mp3"
]

right_files_static_list  = [
    "sound/natur_Thunder_and_Rain_1.mp3",
    "sound/natur_Thy_Dawn_Chorus.mp3",
    "sound/historie_Historien_om_en_faetter.mp3",
    "sound/historie_Hvad_bor_julemanden_i_01.mp3",
    "sound/historie_Hvad_har_du_lavet_i_dag_01.mp3",
    "sound/historie_Mistelkatten.mp3",
    "sound/historie_Tael_til_100_01.mp3",
    "sound/natur_2011_05_16A_Joyce_WA_10_Winter_Wren_SFX.mp3",
    "sound/natur_2011_05_16B_Joyce_WA_04_Stream_in_Forest_W_Birds-44k.mp3",
    "sound/natur_2011_05_16C_Beach_02_Ocean_Waves.mp3",
    "sound/musik_01_Som_sendt_fra_himlen.mp3",
    "sound/musik_05_Dr_Dingeling_2003_Digital_Remaster.mp3",
    "sound/musik_05_Roede_Gummistoevler.mp3",
    "sound/musik_07_Min_lille_sveske_2003_Digital_Remaster.mp3",
    "sound/musik_13_Godnat_Godnat_Godnat.mp3",
    "sound/musik_05_No_5.mp3",
    "sound/musik_06_I_skovens_dybe_stille_ro.mp3",
    "sound/musik_07_No_7.mp3",
    "sound/musik_14_Med_store_undrende_oejne.mp3",
    "sound/musik_15_Gi_os_lyset_tilbage.mp3",

    "sound/lyd_Underwater_W_Shingle.mp3",
    "sound/lyd_VB03_36_02_Laugh_Girls_Giggling.mp3",
    "sound/lyd_musical_accent_glockenspiel_chime_bright.mp3",
    "sound/lyd_musical_electric_guitar_dry_bb_sus4.mp3",
    "sound/lyd_musical_piano_mysterious_arpeggio_descend.mp3",
    "sound/lyd_musical_violin_g_major_scale_up_hold_last_note_vibrato.mp3",

    "sound/dyr_Pigs_1.mp3",
    "sound/dyr_birds_efx.mp3",
    "sound/dyr_cats_cats_meow.mp3",
    "sound/lyd_Trampoline_Fun.mp3"
]

# Select list and shuffle statically & determinstically
files_static_list = right_files_static_list
seed(87)
shuffle(files_static_list)

devices_static_list = [
    '/dev/input/event0',
    '/dev/input/event1',
    '/dev/input/event2',
]

T1  = "0008977370"
T2  = "0009007256"
T3  = "0008985253"
T4  = "0008532161"
T5  = "0008535523"
T6  = "0008988208"
T7  = "0008546521"
T8  = "0008536013"
T9  = "0008461114"
T10 = "0008467439"

tags_static_list = [ T1, T2, T3, T4, T5, T6, T7, T8, T9, T10 ]

def register(reader,tag,file):
    if not reader in readers_static_list:
        readers_static_list[reader] = {}
    readers_static_list[reader][tag]  = file

readers_static_list = {}
file_index = 0
for reader in devices_static_list:
    for tag in tags_static_list:
        register(reader,tag,files_static_list[file_index%len(files_static_list)])
        file_index = file_index + 1

def mapReaderTagToSoundFile(reader,tag):
    if not reader in readers_static_list:
        print "Error: unknown reader:",reader
        return undefined_sound_file
    tags = readers_static_list[reader]
    if not tag in tags:
        print "Error: unknown tag:",reader
        return undefined_sound_file
    return tags[tag]

def getErrorSoundFile():
    return undefined_sound_file

def getDeviceNames():
    return devices_static_list

def init():
    print "Configuration",readers_static_list
