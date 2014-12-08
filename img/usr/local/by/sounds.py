import pygame

def init():
    pygame.mixer.init()

def play(file):
    pygame.mixer.music.load(file)
    pygame.mixer.music.play()

