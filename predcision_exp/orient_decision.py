#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import numpy as np
import matplotlib.pyplot as plt
import os, sys
import exp_func as exp

from psychopy import visual, logging, core, event,  gui, data
from random import random
from numpy import sin, pi
from numpy.random import vonmises
from scipy import signal, stats
from psychopy.preferences import prefs
prefs.general['audioLib'] = ['pyo'] # use Pyo audiolib for good temporal resolution

from psychopy.sound import Sound

# monitors.getAllMonitors()
#from general_settings import * # reads the variables in one script

# Collect subject data
subjID, threshold = exp.subject_info()

monitor_name = "mundet_screen" # monitor to use (make sure to define monitors in exp_monitors center.

# lets define the monitor if necessary
monitor_pixels = (1366, 768); monitor_width = 47; distance2monitor = 50;
screen = exp.define_monitor(monitor_name, monitor_pixels, monitor_width, distance2monitor)

# Creating a new experimental window
units = "deg" # units to define your stimuli
screen_id = 0
full  = False
Hz = 60
win, Hz, ifi = exp.create_window(monitor_name, units, screen_id, full, Hz)


prefs.general['shutdownKey'] = 'q' # esto aun no se si funciona o como funciona (hay que testearlo)

# Create all the stimuli
# Stimuli parameters

size_stim = 10 # degs
grating_contrast = 0.5

fixation_point = visual.PatchStim(win, color= [1, 1, 1], tex=None,mask='circle', size=0.2, units = "deg")
fixation_point_c = visual.PatchStim(win, color= [-1, -1, -1], tex=None,mask='circle', size=0.3, units = "deg")
fixation_circle =  visual.PatchStim(win, color= [0, 0, 0], tex=None, mask='circle', size=0.5, units = "deg")


# Grating stim
grating = visual.GratingStim(win=win, mask="raisedCos" , size=size_stim, pos=[0,0], sf=2,
                             units = "deg", contrast = grating_contrast, maskParams = {'sd': 3} ) # , color = [1,0,1]

# Contour boundary
stim_contour = visual.Circle(win=win,lineWidth = 5, units="deg", radius=size_stim-5, lineColor=[-1, -1, -1],edges=128)
stim_contour_in = visual.Circle(win=win,lineWidth = 1, units="deg", radius=size_stim-5, lineColor=[1, 1, 1],edges=128)

# Mask components
g1 = visual.GratingStim(win=win, mask="raisedCos" , opacity=0.5, size=size_stim, ori = 135, pos=[0,0], sf=2, units = "deg", contrast = grating_contrast, maskParams = {'sd': 3} ) # , color = [1,0,1]
g2 = visual.GratingStim(win=win, mask="raisedCos" , opacity=0.5, size=size_stim, ori = 45, pos=[0,0], sf=2, units = "deg", contrast = grating_contrast, maskParams = {'sd': 3} ) # , color = [1,0,1]
g3 = visual.GratingStim(win=win, mask="raisedCos" , opacity=0.5, size=size_stim, ori = 90, pos=[0,0], sf=2, units = "deg", contrast = grating_contrast, maskParams = {'sd': 3} ) # , color = [1,0,1]
g4 = visual.GratingStim(win=win, mask="raisedCos" , opacity=0.5, size=size_stim, ori = 135, pos=[0,0], sf=2, units = "deg", contrast = grating_contrast, maskParams = {'sd': 3} ) # , color = [1,0,1]

# Circ. Mask
circ_grating_mask = visual.RadialStim(win=win, mask="raisedCos" , opacity=0.5, size=size_stim, ori = 90, pos=[0,0], radialCycles=8, angularCycles=0, units = "deg", contrast = 0.8, maskParams = {'sd': 3} ) # , color = [1,0,1]

# Response options Diagonal or Cardinal
circle = visual.Circle(win=win,lineWidth = 10, units="deg", radius=1, lineColor=[1, 1, 1],edges=32)
linev = visual.Line(win=win,lineWidth = 10,units="deg",lineColor=[1, 1, 1],start = [0, -1],end = [0, 1])
lineh = visual.Line(win=win,lineWidth = 10,units="deg",lineColor=[1, 1, 1],start = [-1, 0],end = [1, 0],)

# Create stimuli objects

def draw_mask():
    g1.draw(); g2.draw(); g3.draw(); g4.draw()
    return

def fixation():
    fixation_circle.draw()
    fixation_point_c.draw()
    fixation_point.draw()
    return

def draw_contour():
    stim_contour.draw()
    stim_contour_in.draw()
    return

# Response options (cardinal/diagonal)
def resp_option(ori, rgb, pos): # response option object
    lineh.ori = ori
    lineh.pos = pos
    linev.ori = ori
    linev.pos = pos
    lineh.lineColor = rgb
    linev.lineColor = rgb
    circle.lineColor = rgb
    circle.pos = pos
    circle.draw()
    linev.draw()
    lineh.draw()
    return


# Create the sounds that I am going to use
#lowf_s = Sound(600, sampleRate=44100, secs=0.1, stereo=True ,loops=0,hamming=True)
medf_s = Sound(800, sampleRate=44100, secs=0.1, stereo=True ,loops=0,hamming=True)
#highf_s = Sound(1000, sampleRate=44100, secs=0.1, stereo=True ,loops=0,hamming=True)

# Experimental condition preparation

nstim = 8 # number of gratings per sequence
ntrials_per_cond = 1 # number of repetitions per trial type
stim_time = 250 # in miliseconds
stim_frames = round(250/ifi[0])
ISI1_frames = round(500/ifi[0])
ISI2_frames = round(500/ifi[0])
ISI1s_frames = round(100/ifi[0])
ISI2s_frames = round(500/ifi[0]) # 
#mask_frames = round(100/ifi[0])
Clock = core.Clock()

# response mapping (shuffled in each experiment )
resp_maps = np.array([0, 45]) # 0 -> cardinal; 45 -> diagonal
np.random.shuffle(resp_maps) # first response option (cardignal or diagonal) will be placed at left, and second at right 



stimList = []
for cond in [-1, 1]:#0.5, 1.0, 1.5, 2.0, 2.5]:
   for diff in [threshold,threshold*1.5]: # two levels of difficulty. Both orientations equally likely. Or Threshold.
       for n_reps in [2]: # nreps = [2, 3]
           #for ntrials in [ntrials_per_cond]: # you dont need to append this to the matrix
            stimList.append(
                         {'cond':cond, 'diff': diff, 'n_reps': n_reps} #
                        )

# set path of stim file
outfile = os.path.join(os.getcwd(),"stim_matrix") # os.sep

if os.path.isfile(outfile + ".npy"): # check if file exist, otherwise, create a new one.
    orientations = np.load(outfile + ".npy")
else: # This is the procedure to generate the trials matrix. I RECOMEND TO RUN THIS MANUALLY TO VISUALIZE THE RESULTS ONLINE
    from create_stimuli import stim_creation
    orientations = stim_creation(nstim)

# collapse the circular angles on one side of the circle to make the analyses easier (see that 45 is equal to 225
# degrees when drawing grating orientations)
orientations[orientations < 0] += np.deg2rad(180)
decision_var = signal.sawtooth(4 * ((orientations)), 0.5)  # DU decision variable
decision_var_T = np.mean(decision_var, 1)
decision_var_std = np.std(decision_var, 1)
orientation_var_std = stats.circstd((orientations), axis=1)

ExpClockStart = Clock.getTime()


#trials = data.TrialHandler(stimList, 2)

trials = data.TrialHandler(stimList, ntrials_per_cond, method='random') # when calling next trial it continues to the next randomly ordered trial

staircase = data.StairHandler(startVal = threshold,
                          stepType = 'lin', stepSizes=[0.1 ,0.05, 0.025], # this determines the number of reversals and therefore the number of trials
                          nUp=1, nDown=2,  # will home in on the 80% threshold
                          minVal = 0, maxVal = 0.7,
                          nTrials=20)

for thisIncrement in staircase:  # will continue the staircase until it terminates!
    # set location of stimuli
    cond = np.random.choice([-1,1])  # will be cardinal or diagonal
   
#for thisTrial in trials: # you have to reset the trials variable in order to redo the trials sequence

     #thisTrial = trials.getFutureTrial(2) # you can force a particular trial using this function
#    cond = thisTrial['cond']
#    diff =  thisTrial['diff']
  #  print(cond)
  #  print(diff)

    ExpClockTrial = Clock.getTime()
    # decision variable in this trial
    x =  cond*(thisIncrement)
    print(x)
   # x = -0.5
    #sel_trials = decision_var_T[np.where((decision_var_T > x-0.001) & (decision_var_T < x+0.001))] # to return an array and not tuple
    sel_trials = np.where((decision_var_T > x-0.025) & (decision_var_T < x+0.025))
    trial_sel_idx = np.random.choice(sel_trials[0]) # selecting orientation vector for this trial.
    t_orient = orientations[trial_sel_idx,]
    decision_avg = decision_var_T[trial_sel_idx]

    # Initialize some default paratemers for this trial
    thisResp=None
    col_resp = [1, 1, 1]
    trialClockStart = Clock.getTime()


    for i_si in range(ISI1_frames): # first period before the first beep
        fixation()
        win.flip()

    medf_s.play() # reproduce 1st auditory cue

    for i_si in range(ISI1s_frames): # second period before the second beep
        fixation()
        win.flip()

    medf_s.play() # reproduce 2nd auditory cue (here it is always the same)
    
    for i_si in range(ISI2s_frames): # second period before the contour
        fixation()
        win.flip()
        

    for i_si in range(ISI2_frames): # second period before the trial starts (response mapping cues)
        fixation()         
        draw_contour()
        win.flip()

    # Draw the stimuli
    for istim in range(nstim+2): # 2 stim for the masks sandwiching
        event.clearEvents()
        if (istim == 0) | (istim == nstim+1):
           for frame in range(stim_frames):  # drawing stim frames
                if frame < stim_frames - 1:  # the last frame should be empty
                    draw_mask()
                    fixation()
                    draw_contour()
                    win.flip()
                    respClockStart = Clock.getTime()
        else:
            grating.ori =  np.rad2deg(t_orient[istim-1]) # change orientation for each stim
            grating.phase = np.random.rand()

            for frame in range(stim_frames): # drawing stim frames
                if frame < stim_frames - 1:  # the last frame should be empty
                    grating.draw()
                    fixation()
                    draw_contour()
                    win.flip()
            fixation()
            win.flip()
    
    draw_mask()
    fixation()
    draw_contour()
    resp_option(resp_maps[0], np.array([-1,-1,-1]), np.array([-7,0])) 
    resp_option(resp_maps[1], np.array([-1,-1,-1]), np.array([7,0]))      
    win.flip()
    
    # Get responses
    while thisResp == None:
            thisResp = exp.getResponse(["left", "right"], Clock) # you have to pass a clock function

    rt_deci = thisResp[0] -  respClockStart
    print(rt_deci) # you can make a function of this to assign the correctness
    
    if thisResp[1] == 'left':
        resp_ang = resp_maps[0] # assign response selected
        
    elif thisResp[1] == 'right':
        resp_ang = resp_maps[1]
        
    if (x > 0 and resp_ang == 45) or (x < 0 and  resp_ang == 0):
        correct = 1  # correct
        print("correct")
    else:
        print("incorrect")
        correct = -1  # incorrect
     
    staircase.addData(correct)
#    dataFile.write('%i,%.3f,%i\n' %(targetSide, thisIncrement, thisResp))    
    #trials.data.add('correct', correct)
    #trials.data.add('rt_deci', rt_deci)


    # Add a time out before selecting the level of confidence. This chunk of code is not completelu necesary
    #resp_option(resp_ang, col_resp)
    #fixation() # text - Choose your level of confidence
    #exp.draw_this_text(win, "Cómo estás de segur@ en tu respuesta?", -3)
    #win.flip()
    #event.waitKeys()

    
        #trials.data.add('rt_confi', rt_confi)

    #respTimeStart = Clock.getTime()


print(staircase.reversalIntensities)
approxThreshold = np.average(staircase.reversalIntensities[-6:])
approxThreshold 
# tienes que salvar el
# subj, threshold, mean decision info, decisorientation of each grating, orientation of each

resp_option(resp_maps[0], np.array([-1,-1,-1]), np.array([-7,0])) 
resp_option(resp_maps[1], np.array([-1,-1,-1]), np.array([7,0]))      

# IN ORDER TO MEASURE THE NUMBER OF FRAMES DROPPED
#from __future__ import division, print_function
# haz log tambien de los flip time stamps
# Set the log module to report warnings to the standard output window
# (default is errors only).
logging.console.setLevel(logging.WARNING)
import matplotlib.pyplot as plt
plt.plot(win.frameIntervals)
plt.show()
print('Overall, %i frames were dropped.' % win.nDroppedFrames)

