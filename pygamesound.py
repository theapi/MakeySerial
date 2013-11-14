import os
import serial

os.environ['SDL_VIDEODRIVER'] = 'dummy'
import pygame

pygame.init()
pygame.display.set_mode((1,1))
pygame.mixer.init()

noise = pygame.mixer.Sound("/usr/share/sounds/alsa/Noise.wav")
snd_a = pygame.mixer.Sound("/usr/share/sounds/alsa/Rear_Center.wav")
snd_b = pygame.mixer.Sound("/usr/share/sounds/alsa/Front_Center.wav")
snd_c = pygame.mixer.Sound("/usr/share/sounds/alsa/Side_Left.wav")
snd_d = pygame.mixer.Sound("/usr/share/sounds/alsa/Side_Right.wav")

s = serial.Serial(port='/dev/ttyACM0', baudrate=9600, timeout=1,
                       parity=serial.PARITY_EVEN, rtscts=1)

noise.play()

while True:
    line = s.readline()
    line = line.strip()

    if line == 'press 218':
        print 'UP'
        snd_a.play()

    if line == 'press 217':
        print 'DOWN'
        snd_b.play()

    if line == 'press 216':
        print 'LEFT'
        snd_c.play()

    if line == 'press 215':
        print 'RIGHT'
        snd_d.play()


