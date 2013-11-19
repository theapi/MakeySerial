import os
import serial

os.environ['SDL_VIDEODRIVER'] = 'dummy'
import pygame

pygame.init()
pygame.display.set_mode((1,1))
pygame.mixer.init()


snd_a = pygame.mixer.Sound('./piano/A-min7.wav')
snd_b = pygame.mixer.Sound('./piano/Amin7.wav')
snd_c = pygame.mixer.Sound('./piano/Bmin7.wav')
snd_d = pygame.mixer.Sound('./piano/C-min7.wav')
snd_e = pygame.mixer.Sound('./piano/Cmin7.wav')
snd_f = pygame.mixer.Sound('./piano/D-min7.wav')
snd_g = pygame.mixer.Sound('./piano/Dmin7.wav')
snd_h = pygame.mixer.Sound('./piano/E-min7.wav')
snd_i = pygame.mixer.Sound('./piano/Emin7.wav')
snd_j = pygame.mixer.Sound('./piano/G-min7.wav')
snd_k = pygame.mixer.Sound('./piano/Gmin7.wav')

s = serial.Serial(port='/dev/ttyACM0', baudrate=9600, timeout=1,
                       parity=serial.PARITY_EVEN, rtscts=1)


while True:
    line = s.readline()
    line = line.strip()
    print line

    if line == 'press 215':
        snd_i.play()

    if line == 'press 216':
        snd_j.play()

    if line == 'press 217':
        snd_a.play()

    if line == 'press 218':
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
        snd_h.play()
