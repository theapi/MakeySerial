import os
import serial

os.environ['SDL_VIDEODRIVER'] = 'dummy'
import pygame

pygame.init()
pygame.display.set_mode((1,1))
pygame.mixer.init()

#noise = pygame.mixer.Sound("/usr/share/sounds/alsa/Noise.wav")
snd_a = pygame.mixer.Sound("/usr/share/sounds/alsa/Rear_Center.wav")
snd_b = pygame.mixer.Sound("/usr/share/sounds/alsa/Front_Center.wav")
snd_c = pygame.mixer.Sound("/usr/share/sounds/alsa/Side_Left.wav")
snd_d = pygame.mixer.Sound("/usr/share/sounds/alsa/Side_Right.wav")

playing_snd_a = False
playing_snd_b = False
playing_snd_c = False
playing_snd_d = False
playing_snd_e = False
playing_snd_f = False
playing_snd_g = False

s = serial.Serial(port='/dev/ttyACM0', baudrate=9600, timeout=1,
                       parity=serial.PARITY_EVEN, rtscts=1)

#noise.play()

while True:
    line = s.readline()
    line = line.strip()

    if line == 'press 218':

        if not playing_snd_a:
            snd_a.play(-1)
            playing_snd_a = True
            print 'playing UP'
        else:
            snd_a.stop()
            playing_snd_a = False
            print 'stopped UP'

    if line == 'press 217':

        if not playing_snd_b:
            snd_b.play(-1)
            playing_snd_b = True
            print 'playing DOWN'
        else:
            snd_b.stop()
            playing_snd_b = False
            print 'stopped DOWN'

    if line == 'press 216':

        if not playing_snd_c:
            snd_c.play(-1)
            playing_snd_c = True
            print 'playing LEFT'
        else:
            snd_c.stop()
            playing_snd_c = False
            print 'stopped LEFT'

    if line == 'press 215':

        if not playing_snd_d:
            snd_d.play(-1)
            playing_snd_d = True
            print 'playing RIGHT'
        else:
            snd_d.stop()
            playing_snd_d = False
            print 'stopped RIGHT'


