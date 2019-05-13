#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from psychopy import visual

def fixation(win)
    fixation_point = visual.PatchStim(win, color=[1, 1, 1], tex=None, mask='circle', size=0.2, units="deg")
    fixation_point_c = visual.PatchStim(win, color=[-1, -1, -1], tex=None, mask='circle', size=0.3, units="deg")
    fixation_circle = visual.PatchStim(win, color=[0, 0, 0], tex=None, mask='circle', size=0.5, units="deg")
    return

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
    linev = visual.Line(win=win,lineWidth = 10,units="deg",lineColor=[1, 1, 1],start = [0, -1],end = [0, 1],ori = 20)
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
    def resp_option(ori, rgb): # response option object
        lineh.ori = ori
        linev.ori = ori
        lineh.lineColor = rgb
        linev.lineColor = rgb
        circle.lineColor = rgb
        circle.draw()
        linev.draw()
        lineh.draw()
        return




t_orient

card = card.flatten()
neutral = t_orient.flatten()
diag
card
neutral

kappa_angle = 20

def vonmises_kde(data, kappa, n_bins=100):
    from scipy.special import i0
    bins = np.linspace(-np.pi, np.pi, n_bins)
    x = np.linspace(-np.pi, np.pi, n_bins)
    # integrate vonmises kernels
    kde = np.exp(kappa*np.cos(x[:, None]-data[None, :])).sum(1)/(2*np.pi*i0(kappa))
    kde /= np.trapz(kde, x=bins)
    return bins, kde



deg_x = np.arange(0, 181, step=45)
deg_y = np.arange(0, 0.015, step=3)

fig, axes = plt.subplots(3,1)
plt.setp(axes, xticks=deg_x, yticks=deg_y)
axes[0].hist(np.rad2deg(card), 100, color = "red" ,alpha = 0.3, density=True, ec="k")

plt.sca(axes[2])
[plt.axvline(_x, linewidth=1, color='black') for _x in deg_x]
axes[2].hist(np.rad2deg(diag), 100, color = "cyan",alpha = 0.3, density=True,  ec="k")
axes[1].hist(np.rad2deg(neutral), 100, color = "grey",alpha = 0.3, density=True,  ec="k")

axes[1].hist(np.rad2deg(card), 100, color = "cyan",alpha = 0.3, density=True,  ec="k")
axes[1].hist(np.rad2deg(diag), 100, color = "red",alpha = 0.3, density=True,  ec="k")


fig, axes = plt.subplots(nrows=3, ncols=4)

# Set the ticks and ticklabels for all axes
plt.setp(axes, xticks=[0.1, 0.5, 0.9], xticklabels=['a', 'b', 'c'],
        yticks=[1, 2, 3])


fig = plt.figure()
#x = np.linspace(np.pi, 2*np.pi, 1000)

ax1 = fig.add_subplot(311)

ax1.hist(np.rad2deg(card), 100, color = "red" ,alpha = 0.3, density=True, ec="k")
ax1.xticks(deg_x)
[plt.axvline(_x, linewidth=1, color='black') for _x in deg_x]


y = np.sin(x)
ax1.plot(x,y)
ax1.set_title('Sine Curve')


ax2 = fig.add_subplot(222)
y = np.cos(x)
ax2.plot(x,y)
ax2.set_title('Cosine Curve')


ax3 = fig.add_subplot(223)
y = np.sin(x)
ax3.plot(x,y)
ax3.set_title('Tangent Curve')




## STAIRCASES


from __future__ import print_function
from builtins import next
from builtins import range
from psychopy import visual, core, data, event
from numpy.random import shuffle
import copy, time #from the std python libs

#create some info to store with the data
info={}
info['startPoints']=[1.5,3,6]
info['nTrials']=10
info['observer']='jwp'

win=visual.Window([400,400])
#---------------------
#create the stimuli
#---------------------

#create staircases
stairs=[]
for thisStart in info['startPoints']:
    #we need a COPY of the info for each staircase 
    #(or the changes here will be made to all the other staircases)
    thisInfo = copy.copy(info)
    #now add any specific info for this staircase
    thisInfo['thisStart']=thisStart #we might want to keep track of this
    thisStair = data.StairHandler(startVal=thisStart, 
        extraInfo=thisInfo,
        nTrials=50, nUp=1, nDown=3,
        minVal = 0.5, maxVal=8, 
        stepSizes=[4,4,2,2,1,1])
    stairs.append(thisStair)
    
for trialN in range(info['nTrials']):
    shuffle(stairs) #this shuffles 'in place' (ie stairs itself is changed, nothing returned)
    #then loop through our randomised order of staircases for this repeat
    for thisStair in stairs:
        thisIntensity = next(thisStair)
        print('start=%.2f, current=%.4f' %(thisStair.extraInfo['thisStart'], thisIntensity))
        
        #---------------------
        #run your trial and get an input
        #---------------------
        keys = event.waitKeys() #(we can simulate by pushing left for 'correct')
        if 'left' in keys: wasCorrect=True
        else: wasCorrect = False
        
        thisStair.addData(wasCorrect) #so that the staircase adjusts itself
        
    #this trial (of all staircases) has finished
#all trials finished
        
#save data (separate pickle and txt files for each staircase)
dateStr = time.strftime("%b_%d_%H%M", time.localtime())#add the current time
for thisStair in stairs:
    #create a filename based on the subject and start value
    filename = "%s start%.2f %s" %(thisStair.extraInfo['observer'], thisStair.extraInfo['thisStart'], dateStr)
    thisStair.saveAsPickle(filename)
    thisStair.saveAsText(filename)   
    
    
    stairs[2].intensities
    stairs[0].extraInfo
    
    dir(stairs[0]) # to see hidden subattributes..