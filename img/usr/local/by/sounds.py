import pygame

def init(initialFile):
    pygame.mixer.init()
    play(initialFile)

def play(file):
    if pygame.mixer.music.get_busy():
        return
    pygame.mixer.music.load(file)
    pygame.mixer.music.play()

