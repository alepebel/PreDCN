# A list with the main experimental functions

from psychopy import visual, logging, core, event,  gui, data
from psychopy import monitors
from psychopy import data, gui
from psychopy.tools.filetools import fromFile, toFile

def subject_info():

    try:  # try to get a previous parameters file
        expInfo = fromFile('lastParams.pickle')
    except:  # if not there then use a default set
        expInfo = {'observer':'test', 'threshold':0.3}
    expInfo['dateStr'] = data.getDateStr()  # add the current time

    threshold = expInfo['threshold']

    # present a dialogue to change params
    dlg = gui.DlgFromDict(expInfo, title='Orientation decisions', fixed=['dateStr'])
    if dlg.OK:
        toFile('lastParams.pickle', expInfo)  # save params to file for next time
    else:
        core.quit()  # the user hit cancel so exit
#!/usr/bin/env python3
# -*- coding: utf-8 -*-

    # make a text file to save data
    fileName = expInfo['observer'] + expInfo['dateStr']
    dataFile = open(fileName+'.csv', 'w')  # a simple text file with 'comma-separated-values'
    dataFile.write('targetSide,threshold,correct\n')
    return expInfo, threshold


def define_monitor(monitor_name, monitor_pixels, monitor_width, distance2monitor ):
    # Lets define the monitor characteristics
    screen = monitors.Monitor(name=monitor_name)
    screen.setSizePix(monitor_pixels)
    screen.setWidth(monitor_width)
    screen.setDistance(distance2monitor)
    screen.saveMon()
    #monitors.getAllMonitors()
    print("The monitor that you are using has "  + str(screen.getSizePix()) + " pixels, a with of " + str(monitor_width) + " cm and subjects seats at " + str(distance2monitor) + " cm"   )
    return screen

def create_window(monitor_name, units, screen_id, full, Hz):
    # Lets open a window and define monitor used
    win = visual.Window(monitor= monitor_name, units=units, screen=screen_id, useRetina=True,fullscr=full)
    ifi = win.getMsPerFrame(nFrames=60, showVisual=False, msg='', msDelay=0.0) # inter flip interval in order to calculate the time of each refresh

    if Hz == "auto": # if the monitor is not very reliable it might fail
        Hz = win.getActualFrameRate(nIdentical=20, nMaxFrames=80,nWarmUpFrames=10)
        Hz = round(Hz)

    # Threshold to evaluate dropped frames
    win.refreshThreshold = 1/Hz+ 0.004
    #win.recordFrameIntervals = True
    return win, Hz, ifi


def draw_this_text(win, text, height):
    out = visual.TextStim(win, pos=[0, height], height = 0)
    out.wrapWidth = 20
   # out.setHeight = height
    out.text = text
    out.draw()

# These two functions have been programmed by D. Linares.
def getResponse(keys, Clock):
    allKeys = event.getKeys(timeStamped=Clock)
    if len(allKeys) > 0:
        allK = [allKeys[0][0]]
        t = allKeys[0][1]
        for thisKey in allK:
            for k in keys:
                if thisKey == k:
                    return ([t, k])
                if thisKey in ["q", "escape"]:
                    win.quit()
                    core.quit()

def waitResponse(keys):
    thisResp = None
    while thisResp == None:
        allKeys = event.waitKeys()
        for thisKey in allKeys:
            for k in keys:
                if thisKey == k:
                    return (k)
            if thisKey in ['q', 'escape']:
                win.quit()
                core.quit()