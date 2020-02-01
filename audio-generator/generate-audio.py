from struct import pack
from math import sin, pi
import wave
import random
import pygame


# RATE = 44100
# freq = 2000


# wv = wave.open(str(freq) + "Hz.wav", 'w')
# wv.setparams((2,2,RATE,0,'NONE','not compressed'))
# maxVol = 2**15-1.0
# stereoMultiplier = 1.0
# wvData = bytes("", 'utf-8')
# for i in range(0, RATE*3):
#     wvData += pack('f',maxVol*sin(i*freq/RATE)*(1-stereoMultiplier))
#     wvData += pack('f',maxVol*sin(i*freq/RATE)*(stereoMultiplier))

# wv.writeframes(wvData)
# wv.close()

pygame.mixer.init(frequency=44000, size=-16, channels=2, buffer=4096)
m = pygame.mixer.Sound("../../audio-files/Audio-files-for-ETA/audiocheck.net_sin_200Hz_-3dBFS_0.25s.wav")
n = pygame.mixer.Sound("../../audio-files/Audio-files-for-ETA/audiocheck.net_sin_200Hz_-3dBFS_0.25s.wav")

# pygame.mixer.Channel(1).play(m,-1)
# pygame.mixer.Channel(2).play(n,-1)

channel0 = m.play()
channel0.set_volume(1.0, 0.0)

channel1 = n.play()
channel1.set_volume(0.0, 1.0)