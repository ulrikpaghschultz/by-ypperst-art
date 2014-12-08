import pygame

def init():
    pygame.mixer.init()

def play(file):
    if pygame.mixer.music.get_busy():
        return
    pygame.mixer.music.load(file)
    pygame.mixer.music.play()

