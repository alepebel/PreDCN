#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Apr 25 18:25:05 2019

@author: alex
"""



prefs.general['audioLib'] 

from psychopy.preferences import prefs
prefs.general['audioLib'] = ['pyo']

from psychopy.sound import Sound

med.play()
prefs.general['audioLib'] = ['pygame']

low = Sound(600, sampleRate=44100, secs=0.1, stereo=True ,loops=0,  blockSize=128, preBuffer=-1)
med = Sound(800, sampleRate=44100, secs=0.1, stereo=True )
high = Sound(1000, sampleRate=44100, secs=0.1, stereo=True )

med = Sound(800, sampleRate=44100, secs=0.1, stereo=True )


low = Sound(600, sampleRate=44100, secs=0.1, stereo=True ,loops=0,hamming=True) 
high = Sound(1000, sampleRate=44100, secs=0.1, stereo=True,loops=0,hamming=True )

low.play()

high.play()

med.play() 
high.play()

standard # you can verify that the audiolib has changed

import 
psychopy.sound.backend_sounddevice.SoundDeviceSound(value='C', secs=0.5, octave=4, stereo=-1, volume=1.0, loops=0, sampleRate=None, blockSize=128, preBuffer=-1, hamming=True, startTime=0, stopTime=-1, name='', autoLog=True)