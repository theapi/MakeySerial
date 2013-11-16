import os
import serial

os.environ['SDL_VIDEODRIVER'] = 'dummy'
import pygame

pygame.init()
pygame.display.set_mode((1,1))
pygame.mixer.init()


snd_a = pygame.mixer.Sound('./bongos/1.wav')
snd_b = pygame.mixer.Sound('./bongos/2.wav')
snd_c = pygame.mixer.Sound('./bongos/3.wav')
snd_d = pygame.mixer.Sound('./bongos/4.wav')
snd_e = pygame.mixer.Sound('./bongos/5.wav')
snd_f = pygame.mixer.Sound('./bongos/6.wav')
snd_g = pygame.mixer.Sound('./bongos/7.wav')
snd_h = pygame.mixer.Sound('./bongos/8.wav')

s = serial.Serial(port='/dev/ttyACM0', baudrate=9600, timeout=1,
                       parity=serial.PARITY_EVEN, rtscts=1)


while True:
    line = s.readline()
    line = line.strip()
    print line
    if line == 'press 218':
        snd_a.play()

    if line == 'press 217':
        snd_b.play()

    if line == 'press 119':
        snd_c.play()

    if line == 'press 97':
        snd_d.play()

    if line == 'press 115':
        snd_e.play()

    if line == 'press 100':
        snd_f.play()

    if line == 'press 102':
        snd_g.play()

    if line == 'press 103':
        snd_f.play()