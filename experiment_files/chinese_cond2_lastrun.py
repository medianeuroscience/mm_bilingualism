#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
This experiment was created using PsychoPy2 Experiment Builder (v1.90.1),
    on Fri Feb  8 13:55:03 2019
If you publish work using this script please cite the PsychoPy publications:
    Peirce, JW (2007) PsychoPy - Psychophysics software in Python.
        Journal of Neuroscience Methods, 162(1-2), 8-13.
    Peirce, JW (2009) Generating stimuli for neuroscience using PsychoPy.
        Frontiers in Neuroinformatics, 2:10. doi: 10.3389/neuro.11.010.2008
"""

from __future__ import absolute_import, division
from psychopy import locale_setup, sound, gui, visual, core, data, event, logging, clock
from psychopy.constants import (NOT_STARTED, STARTED, PLAYING, PAUSED,
                                STOPPED, FINISHED, PRESSED, RELEASED, FOREVER)
import numpy as np  # whole numpy lib is available, prepend 'np.'
from numpy import (sin, cos, tan, log, log10, pi, average,
                   sqrt, std, deg2rad, rad2deg, linspace, asarray)
from numpy.random import random, randint, normal, shuffle
import os  # handy system and path functions
import sys  # to get file system encoding

# Ensure that relative paths start from the same directory as this script
_thisDir = os.path.dirname(os.path.abspath(__file__))
os.chdir(_thisDir)

# Store info about the experiment session
expName = 'chinese_cond2'  # from the Builder filename that created this script
expInfo = {'participant': '', 'session': '001'}
dlg = gui.DlgFromDict(dictionary=expInfo, title=expName)
if dlg.OK == False:
    core.quit()  # user pressed cancel
expInfo['date'] = data.getDateStr()  # add a simple timestamp
expInfo['expName'] = expName

# Data file name stem = absolute path + name; later add .psyexp, .csv, .log, etc
filename = _thisDir + os.sep + u'data/%s_%s_%s' % (expInfo['participant'], expName, expInfo['date'])

# An ExperimentHandler isn't essential but helps with data saving
thisExp = data.ExperimentHandler(name=expName, version='',
    extraInfo=expInfo, runtimeInfo=None,
    originPath='/Users/jacobfisher/projects/inprogress/mm_bilingualism/experiment_files/chinese_cond2.psyexp',
    savePickle=True, saveWideText=True,
    dataFileName=filename)
# save a log file for detail verbose info
logFile = logging.LogFile(filename+'.log', level=logging.EXP)
logging.console.setLevel(logging.WARNING)  # this outputs to the screen, not a file

endExpNow = False  # flag for 'escape' or other condition => quit the exp

# Start Code - component code to be run before the window creation

# Setup the Window
win = visual.Window(
    size=[1680, 1050], fullscr=True, screen=0,
    allowGUI=False, allowStencil=False,
    monitor='testMonitor', color=[1,1,1], colorSpace='rgb',
    blendMode='avg', useFBO=True)
# store frame rate of monitor if we can measure it
expInfo['frameRate'] = win.getActualFrameRate()
if expInfo['frameRate'] != None:
    frameDur = 1.0 / round(expInfo['frameRate'])
else:
    frameDur = 1.0 / 60.0  # could not measure, so guess

# Initialize components for Routine "instr"
instrClock = core.Clock()
text_8 = visual.TextStim(win=win, name='text_8',
    text='Welcome!',
    font='Arial',
    pos=(0, 0), height=0.1, wrapWidth=None, ori=0, 
    color='black', colorSpace='rgb', opacity=1,
    depth=0.0);
text_9 = visual.TextStim(win=win, name='text_9',
    text='In this experiment you will complete a word matching task.',
    font='Arial',
    pos=(0, 0), height=0.1, wrapWidth=None, ori=0, 
    color='black', colorSpace='rgb', opacity=1,
    depth=-1.0);
text_10 = visual.TextStim(win=win, name='text_10',
    text='In the task, you will see a series of pictures paired with words.',
    font='Arial',
    pos=(0, 0), height=0.1, wrapWidth=None, ori=0, 
    color='black', colorSpace='rgb', opacity=1,
    depth=-2.0);
text_13 = visual.TextStim(win=win, name='text_13',
    text='Each pair will look like this.',
    font='Arial',
    pos=(0, 0), height=0.1, wrapWidth=None, ori=0, 
    color='black', colorSpace='rgb', opacity=1,
    depth=-3.0);

# Initialize components for Routine "match_prac1"
match_prac1Clock = core.Clock()
image_2 = visual.ImageStim(
    win=win, name='image_2',units='pix', 
    image='sin', mask=None,
    ori=0, pos=[-200, 0], size=[300, 300],
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=0.0)
text_12 = visual.TextStim(win=win, name='text_12',
    text='default text',
    font='Arial',
    pos=(.2, 0), height=0.1, wrapWidth=None, ori=0, 
    color='black', colorSpace='rgb', opacity=1,
    depth=-1.0);

# Initialize components for Routine "instr_2"
instr_2Clock = core.Clock()
text_14 = visual.TextStim(win=win, name='text_14',
    text='Each pair will be either a correct or incorrect match.',
    font='Arial',
    pos=(0, 0), height=0.1, wrapWidth=None, ori=0, 
    color='black', colorSpace='rgb', opacity=1,
    depth=0.0);
text_15 = visual.TextStim(win=win, name='text_15',
    text='You should press "z" if the match is correct.',
    font='Arial',
    pos=(0, 0), height=0.1, wrapWidth=None, ori=0, 
    color='green', colorSpace='rgb', opacity=1,
    depth=-1.0);
text_16 = visual.TextStim(win=win, name='text_16',
    text='You should press "x" if the match is incorrect.',
    font='Arial',
    pos=(0, 0), height=0.1, wrapWidth=None, ori=0, 
    color='red', colorSpace='rgb', opacity=1,
    depth=-2.0);
text_17 = visual.TextStim(win=win, name='text_17',
    text="Let's do a practice round.",
    font='Arial',
    pos=(0, 0), height=0.1, wrapWidth=None, ori=0, 
    color='black', colorSpace='rgb', opacity=1,
    depth=-3.0);

# Initialize components for Routine "match_2"
match_2Clock = core.Clock()
image_3 = visual.ImageStim(
    win=win, name='image_3',units='pix', 
    image='sin', mask=None,
    ori=0, pos=[-200, 0], size=[300,300],
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=0.0)
text_18 = visual.TextStim(win=win, name='text_18',
    text='default text',
    font='Arial',
    pos=(.2, 0), height=0.1, wrapWidth=None, ori=0, 
    color='black', colorSpace='rgb', opacity=1,
    depth=-1.0);


# Initialize components for Routine "instr_3"
instr_3Clock = core.Clock()
text_20 = visual.TextStim(win=win, name='text_20',
    text='Great job!',
    font='Arial',
    pos=(0, 0), height=0.1, wrapWidth=None, ori=0, 
    color='black', colorSpace='rgb', opacity=1,
    depth=0.0);
text_22 = visual.TextStim(win=win, name='text_22',
    text='During the matching task you will also listen to an audiobook.',
    font='Arial',
    pos=(0, 0), height=0.1, wrapWidth=None, ori=0, 
    color='black', colorSpace='rgb', opacity=1,
    depth=-1.0);
text_21 = visual.TextStim(win=win, name='text_21',
    text='The audiobook will either be in English or in Mandarin Chinese.',
    font='Arial',
    pos=(0, 0), height=0.1, wrapWidth=None, ori=0, 
    color='black', colorSpace='rgb', opacity=1,
    depth=-2.0);
text_23 = visual.TextStim(win=win, name='text_23',
    text='Pay attention to the audiobook, because you will be asked questions about it later.',
    font='Arial',
    pos=(0, 0), height=0.1, wrapWidth=None, ori=0, 
    color='black', colorSpace='rgb', opacity=1,
    depth=-3.0);
text_24 = visual.TextStim(win=win, name='text_24',
    text="Okay! Let's get going.",
    font='Arial',
    pos=(0, 0), height=0.1, wrapWidth=None, ori=0, 
    color='black', colorSpace='rgb', opacity=1,
    depth=-4.0);

# Initialize components for Routine "audiobook_1"
audiobook_1Clock = core.Clock()
globalClock = core.MonotonicClock()
matchClock = core.Clock()
bookClock = core.Clock()

msg='doh!'#if this comes up we forgot to update the msg!

myCount = 0
text_3 = visual.TextStim(win=win, name='text_3',
    text='The matching task will begin soon',
    font='Arial',
    pos=(0, 0), height=0.1, wrapWidth=None, ori=0, 
    color='black', colorSpace='rgb', opacity=1,
    depth=-1.0);

# Initialize components for Routine "match"
matchClock = core.Clock()
image = visual.ImageStim(
    win=win, name='image',units='pix', 
    image='sin', mask=None,
    ori=0, pos=[-200, 0], size=1.0,
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=0.0)
text = visual.TextStim(win=win, name='text',
    text='default text',
    font='Arial',
    pos=(.2, 0), height=0.1, wrapWidth=None, ori=0, 
    color='black', colorSpace='rgb', opacity=1,
    depth=-1.0);


# Initialize components for Routine "feedback"
feedbackClock = core.Clock()
text_2 = visual.TextStim(win=win, name='text_2',
    text='default text',
    font='Arial',
    pos=(0, 0), height=0.1, wrapWidth=None, ori=0, 
    color='black', colorSpace='rgb', opacity=1,
    depth=0.0);


# Initialize components for Routine "end_loop"
end_loopClock = core.Clock()
text_4 = visual.TextStim(win=win, name='text_4',
    text='This round is now complete',
    font='Arial',
    pos=(0, 0), height=0.1, wrapWidth=None, ori=0, 
    color='black', colorSpace='rgb', opacity=1,
    depth=0.0);


# Initialize components for Routine "Finish"
FinishClock = core.Clock()
text_5 = visual.TextStim(win=win, name='text_5',
    text='Thank you for participating!',
    font='Arial',
    pos=(0, 0), height=0.1, wrapWidth=None, ori=0, 
    color='black', colorSpace='rgb', opacity=1,
    depth=0.0);
text_6 = visual.TextStim(win=win, name='text_6',
    text='You will now complete the survey portion of the experiment',
    font='Arial',
    pos=(0, 0), height=0.1, wrapWidth=None, ori=0, 
    color='black', colorSpace='rgb', opacity=1,
    depth=-1.0);
text_7 = visual.TextStim(win=win, name='text_7',
    text='An experimenter will come by to assist you',
    font='Arial',
    pos=(0, 0), height=0.1, wrapWidth=None, ori=0, 
    color='black', colorSpace='rgb', opacity=1,
    depth=-2.0);

# Create some handy timers
globalClock = core.Clock()  # to track the time since experiment started
routineTimer = core.CountdownTimer()  # to track time remaining of each (non-slip) routine 

# ------Prepare to start Routine "instr"-------
t = 0
instrClock.reset()  # clock
frameN = -1
continueRoutine = True
routineTimer.add(21.000000)
# update component parameters for each repeat
# keep track of which components have finished
instrComponents = [text_8, text_9, text_10, text_13]
for thisComponent in instrComponents:
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED

# -------Start Routine "instr"-------
while continueRoutine and routineTimer.getTime() > 0:
    # get current time
    t = instrClock.getTime()
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *text_8* updates
    if t >= 0.0 and text_8.status == NOT_STARTED:
        # keep track of start time/frame for later
        text_8.tStart = t
        text_8.frameNStart = frameN  # exact frame index
        text_8.setAutoDraw(True)
    frameRemains = 0.0 + 3- win.monitorFramePeriod * 0.75  # most of one frame period left
    if text_8.status == STARTED and t >= frameRemains:
        text_8.setAutoDraw(False)
    
    # *text_9* updates
    if t >= 3 and text_9.status == NOT_STARTED:
        # keep track of start time/frame for later
        text_9.tStart = t
        text_9.frameNStart = frameN  # exact frame index
        text_9.setAutoDraw(True)
    frameRemains = 3 + 6- win.monitorFramePeriod * 0.75  # most of one frame period left
    if text_9.status == STARTED and t >= frameRemains:
        text_9.setAutoDraw(False)
    
    # *text_10* updates
    if t >= 9 and text_10.status == NOT_STARTED:
        # keep track of start time/frame for later
        text_10.tStart = t
        text_10.frameNStart = frameN  # exact frame index
        text_10.setAutoDraw(True)
    frameRemains = 9 + 6- win.monitorFramePeriod * 0.75  # most of one frame period left
    if text_10.status == STARTED and t >= frameRemains:
        text_10.setAutoDraw(False)
    
    # *text_13* updates
    if t >= 15 and text_13.status == NOT_STARTED:
        # keep track of start time/frame for later
        text_13.tStart = t
        text_13.frameNStart = frameN  # exact frame index
        text_13.setAutoDraw(True)
    frameRemains = 15 + 6- win.monitorFramePeriod * 0.75  # most of one frame period left
    if text_13.status == STARTED and t >= frameRemains:
        text_13.setAutoDraw(False)
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in instrComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # check for quit (the Esc key)
    if endExpNow or event.getKeys(keyList=["escape"]):
        core.quit()
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "instr"-------
for thisComponent in instrComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)

# set up handler to look after randomisation of conditions etc
trials_3 = data.TrialHandler(nReps=1, method='random', 
    extraInfo=expInfo, originPath=-1,
    trialList=data.importConditions('images.xlsx', selection='[2]'),
    seed=None, name='trials_3')
thisExp.addLoop(trials_3)  # add the loop to the experiment
thisTrial_3 = trials_3.trialList[0]  # so we can initialise stimuli with some values
# abbreviate parameter names if possible (e.g. rgb = thisTrial_3.rgb)
if thisTrial_3 != None:
    for paramName in thisTrial_3:
        exec('{} = thisTrial_3[paramName]'.format(paramName))

for thisTrial_3 in trials_3:
    currentLoop = trials_3
    # abbreviate parameter names if possible (e.g. rgb = thisTrial_3.rgb)
    if thisTrial_3 != None:
        for paramName in thisTrial_3:
            exec('{} = thisTrial_3[paramName]'.format(paramName))
    
    # ------Prepare to start Routine "match_prac1"-------
    t = 0
    match_prac1Clock.reset()  # clock
    frameN = -1
    continueRoutine = True
    routineTimer.add(3.000000)
    # update component parameters for each repeat
    image_2.setImage(images)
    text_12.setText(name)
    # keep track of which components have finished
    match_prac1Components = [image_2, text_12]
    for thisComponent in match_prac1Components:
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    
    # -------Start Routine "match_prac1"-------
    while continueRoutine and routineTimer.getTime() > 0:
        # get current time
        t = match_prac1Clock.getTime()
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *image_2* updates
        if t >= 0.0 and image_2.status == NOT_STARTED:
            # keep track of start time/frame for later
            image_2.tStart = t
            image_2.frameNStart = frameN  # exact frame index
            image_2.setAutoDraw(True)
        frameRemains = 0.0 + 3- win.monitorFramePeriod * 0.75  # most of one frame period left
        if image_2.status == STARTED and t >= frameRemains:
            image_2.setAutoDraw(False)
        
        # *text_12* updates
        if t >= 0.0 and text_12.status == NOT_STARTED:
            # keep track of start time/frame for later
            text_12.tStart = t
            text_12.frameNStart = frameN  # exact frame index
            text_12.setAutoDraw(True)
        frameRemains = 0.0 + 3- win.monitorFramePeriod * 0.75  # most of one frame period left
        if text_12.status == STARTED and t >= frameRemains:
            text_12.setAutoDraw(False)
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in match_prac1Components:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # check for quit (the Esc key)
        if endExpNow or event.getKeys(keyList=["escape"]):
            core.quit()
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # -------Ending Routine "match_prac1"-------
    for thisComponent in match_prac1Components:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    thisExp.nextEntry()
    
# completed 1 repeats of 'trials_3'


# ------Prepare to start Routine "instr_2"-------
t = 0
instr_2Clock.reset()  # clock
frameN = -1
continueRoutine = True
routineTimer.add(24.000000)
# update component parameters for each repeat
# keep track of which components have finished
instr_2Components = [text_14, text_15, text_16, text_17]
for thisComponent in instr_2Components:
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED

# -------Start Routine "instr_2"-------
while continueRoutine and routineTimer.getTime() > 0:
    # get current time
    t = instr_2Clock.getTime()
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *text_14* updates
    if t >= 0.0 and text_14.status == NOT_STARTED:
        # keep track of start time/frame for later
        text_14.tStart = t
        text_14.frameNStart = frameN  # exact frame index
        text_14.setAutoDraw(True)
    frameRemains = 0.0 + 6- win.monitorFramePeriod * 0.75  # most of one frame period left
    if text_14.status == STARTED and t >= frameRemains:
        text_14.setAutoDraw(False)
    
    # *text_15* updates
    if t >= 6 and text_15.status == NOT_STARTED:
        # keep track of start time/frame for later
        text_15.tStart = t
        text_15.frameNStart = frameN  # exact frame index
        text_15.setAutoDraw(True)
    frameRemains = 6 + 6- win.monitorFramePeriod * 0.75  # most of one frame period left
    if text_15.status == STARTED and t >= frameRemains:
        text_15.setAutoDraw(False)
    
    # *text_16* updates
    if t >= 12 and text_16.status == NOT_STARTED:
        # keep track of start time/frame for later
        text_16.tStart = t
        text_16.frameNStart = frameN  # exact frame index
        text_16.setAutoDraw(True)
    frameRemains = 12 + 6- win.monitorFramePeriod * 0.75  # most of one frame period left
    if text_16.status == STARTED and t >= frameRemains:
        text_16.setAutoDraw(False)
    
    # *text_17* updates
    if t >= 18 and text_17.status == NOT_STARTED:
        # keep track of start time/frame for later
        text_17.tStart = t
        text_17.frameNStart = frameN  # exact frame index
        text_17.setAutoDraw(True)
    frameRemains = 18 + 6- win.monitorFramePeriod * 0.75  # most of one frame period left
    if text_17.status == STARTED and t >= frameRemains:
        text_17.setAutoDraw(False)
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in instr_2Components:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # check for quit (the Esc key)
    if endExpNow or event.getKeys(keyList=["escape"]):
        core.quit()
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "instr_2"-------
for thisComponent in instr_2Components:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)

# set up handler to look after randomisation of conditions etc
trials_4 = data.TrialHandler(nReps=1, method='random', 
    extraInfo=expInfo, originPath=-1,
    trialList=data.importConditions('images.xlsx', selection='[4]'),
    seed=None, name='trials_4')
thisExp.addLoop(trials_4)  # add the loop to the experiment
thisTrial_4 = trials_4.trialList[0]  # so we can initialise stimuli with some values
# abbreviate parameter names if possible (e.g. rgb = thisTrial_4.rgb)
if thisTrial_4 != None:
    for paramName in thisTrial_4:
        exec('{} = thisTrial_4[paramName]'.format(paramName))

for thisTrial_4 in trials_4:
    currentLoop = trials_4
    # abbreviate parameter names if possible (e.g. rgb = thisTrial_4.rgb)
    if thisTrial_4 != None:
        for paramName in thisTrial_4:
            exec('{} = thisTrial_4[paramName]'.format(paramName))
    
    # ------Prepare to start Routine "match_2"-------
    t = 0
    match_2Clock.reset()  # clock
    frameN = -1
    continueRoutine = True
    routineTimer.add(3.000000)
    # update component parameters for each repeat
    image_3.setImage(images)
    text_18.setText(name)
    matchClock.reset()
    thisExp.addData('begin_global', globalClock.getTime())
    thisExp.addData('begin_routine', matchClock.getTime())
    
    
    key_resp_2 = event.BuilderKeyResponse()
    # keep track of which components have finished
    match_2Components = [image_3, text_18, key_resp_2]
    for thisComponent in match_2Components:
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    
    # -------Start Routine "match_2"-------
    while continueRoutine and routineTimer.getTime() > 0:
        # get current time
        t = match_2Clock.getTime()
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *image_3* updates
        if t >= 0.0 and image_3.status == NOT_STARTED:
            # keep track of start time/frame for later
            image_3.tStart = t
            image_3.frameNStart = frameN  # exact frame index
            image_3.setAutoDraw(True)
        frameRemains = 0.0 + 3.0- win.monitorFramePeriod * 0.75  # most of one frame period left
        if image_3.status == STARTED and t >= frameRemains:
            image_3.setAutoDraw(False)
        
        # *text_18* updates
        if t >= 0.0 and text_18.status == NOT_STARTED:
            # keep track of start time/frame for later
            text_18.tStart = t
            text_18.frameNStart = frameN  # exact frame index
            text_18.setAutoDraw(True)
        frameRemains = 0.0 + 3.0- win.monitorFramePeriod * 0.75  # most of one frame period left
        if text_18.status == STARTED and t >= frameRemains:
            text_18.setAutoDraw(False)
        
        
        # *key_resp_2* updates
        if t >= 0.0 and key_resp_2.status == NOT_STARTED:
            # keep track of start time/frame for later
            key_resp_2.tStart = t
            key_resp_2.frameNStart = frameN  # exact frame index
            key_resp_2.status = STARTED
            # keyboard checking is just starting
            win.callOnFlip(key_resp_2.clock.reset)  # t=0 on next screen flip
            event.clearEvents(eventType='keyboard')
        frameRemains = 0.0 + 3.0- win.monitorFramePeriod * 0.75  # most of one frame period left
        if key_resp_2.status == STARTED and t >= frameRemains:
            key_resp_2.status = STOPPED
        if key_resp_2.status == STARTED:
            theseKeys = event.getKeys(keyList=['z', 'x'])
            
            # check for quit:
            if "escape" in theseKeys:
                endExpNow = True
            if len(theseKeys) > 0:  # at least one key was pressed
                if key_resp_2.keys == []:  # then this was the first keypress
                    key_resp_2.keys = theseKeys[0]  # just the first key pressed
                    key_resp_2.rt = key_resp_2.clock.getTime()
                    # was this 'correct'?
                    if (key_resp_2.keys == str(corrAns)) or (key_resp_2.keys == corrAns):
                        key_resp_2.corr = 1
                    else:
                        key_resp_2.corr = 0
                    # a response ends the routine
                    continueRoutine = False
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in match_2Components:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # check for quit (the Esc key)
        if endExpNow or event.getKeys(keyList=["escape"]):
            core.quit()
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # -------Ending Routine "match_2"-------
    for thisComponent in match_2Components:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    thisExp.addData('end_global', globalClock.getTime())
    thisExp.addData('end_routine', matchClock.getTime())
    
    if not key_resp_2.keys :
        msg="Failed to respond"
    elif key_resp_2.corr :#stored on last run routine
        msg="Correct!"
    else:
        msg="Wrong."
    # check responses
    if key_resp_2.keys in ['', [], None]:  # No response was made
        key_resp_2.keys=None
        # was no response the correct answer?!
        if str(corrAns).lower() == 'none':
           key_resp_2.corr = 1  # correct non-response
        else:
           key_resp_2.corr = 0  # failed to respond (incorrectly)
    # store data for trials_4 (TrialHandler)
    trials_4.addData('key_resp_2.keys',key_resp_2.keys)
    trials_4.addData('key_resp_2.corr', key_resp_2.corr)
    if key_resp_2.keys != None:  # we had a response
        trials_4.addData('key_resp_2.rt', key_resp_2.rt)
    thisExp.nextEntry()
    
# completed 1 repeats of 'trials_4'


# ------Prepare to start Routine "instr_3"-------
t = 0
instr_3Clock.reset()  # clock
frameN = -1
continueRoutine = True
routineTimer.add(32.000000)
# update component parameters for each repeat
# keep track of which components have finished
instr_3Components = [text_20, text_22, text_21, text_23, text_24]
for thisComponent in instr_3Components:
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED

# -------Start Routine "instr_3"-------
while continueRoutine and routineTimer.getTime() > 0:
    # get current time
    t = instr_3Clock.getTime()
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *text_20* updates
    if t >= 0.0 and text_20.status == NOT_STARTED:
        # keep track of start time/frame for later
        text_20.tStart = t
        text_20.frameNStart = frameN  # exact frame index
        text_20.setAutoDraw(True)
    frameRemains = 0.0 + 6- win.monitorFramePeriod * 0.75  # most of one frame period left
    if text_20.status == STARTED and t >= frameRemains:
        text_20.setAutoDraw(False)
    
    # *text_22* updates
    if t >= 6 and text_22.status == NOT_STARTED:
        # keep track of start time/frame for later
        text_22.tStart = t
        text_22.frameNStart = frameN  # exact frame index
        text_22.setAutoDraw(True)
    frameRemains = 6 + 6- win.monitorFramePeriod * 0.75  # most of one frame period left
    if text_22.status == STARTED and t >= frameRemains:
        text_22.setAutoDraw(False)
    
    # *text_21* updates
    if t >= 12 and text_21.status == NOT_STARTED:
        # keep track of start time/frame for later
        text_21.tStart = t
        text_21.frameNStart = frameN  # exact frame index
        text_21.setAutoDraw(True)
    frameRemains = 12 + 6- win.monitorFramePeriod * 0.75  # most of one frame period left
    if text_21.status == STARTED and t >= frameRemains:
        text_21.setAutoDraw(False)
    
    # *text_23* updates
    if t >= 18 and text_23.status == NOT_STARTED:
        # keep track of start time/frame for later
        text_23.tStart = t
        text_23.frameNStart = frameN  # exact frame index
        text_23.setAutoDraw(True)
    frameRemains = 18 + 8- win.monitorFramePeriod * 0.75  # most of one frame period left
    if text_23.status == STARTED and t >= frameRemains:
        text_23.setAutoDraw(False)
    
    # *text_24* updates
    if t >= 26 and text_24.status == NOT_STARTED:
        # keep track of start time/frame for later
        text_24.tStart = t
        text_24.frameNStart = frameN  # exact frame index
        text_24.setAutoDraw(True)
    frameRemains = 26 + 6- win.monitorFramePeriod * 0.75  # most of one frame period left
    if text_24.status == STARTED and t >= frameRemains:
        text_24.setAutoDraw(False)
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in instr_3Components:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # check for quit (the Esc key)
    if endExpNow or event.getKeys(keyList=["escape"]):
        core.quit()
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "instr_3"-------
for thisComponent in instr_3Components:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)

# set up handler to look after randomisation of conditions etc
trials_2 = data.TrialHandler(nReps=1, method='random', 
    extraInfo=expInfo, originPath=-1,
    trialList=data.importConditions('sounds.xlsx', selection='[0,4]'),
    seed=None, name='trials_2')
thisExp.addLoop(trials_2)  # add the loop to the experiment
thisTrial_2 = trials_2.trialList[0]  # so we can initialise stimuli with some values
# abbreviate parameter names if possible (e.g. rgb = thisTrial_2.rgb)
if thisTrial_2 != None:
    for paramName in thisTrial_2:
        exec('{} = thisTrial_2[paramName]'.format(paramName))

for thisTrial_2 in trials_2:
    currentLoop = trials_2
    # abbreviate parameter names if possible (e.g. rgb = thisTrial_2.rgb)
    if thisTrial_2 != None:
        for paramName in thisTrial_2:
            exec('{} = thisTrial_2[paramName]'.format(paramName))
    
    # ------Prepare to start Routine "audiobook_1"-------
    t = 0
    audiobook_1Clock.reset()  # clock
    frameN = -1
    continueRoutine = True
    routineTimer.add(10.000000)
    # update component parameters for each repeat
    bookClock.reset()
    thisExp.addData('begin_book', globalClock.getTime())
    
    book = sound.Sound(sounds)
    book.play()
    
    myCount = myCount + 1
    # keep track of which components have finished
    audiobook_1Components = [text_3]
    for thisComponent in audiobook_1Components:
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    
    # -------Start Routine "audiobook_1"-------
    while continueRoutine and routineTimer.getTime() > 0:
        # get current time
        t = audiobook_1Clock.getTime()
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        
        # *text_3* updates
        if t >= 0.0 and text_3.status == NOT_STARTED:
            # keep track of start time/frame for later
            text_3.tStart = t
            text_3.frameNStart = frameN  # exact frame index
            text_3.setAutoDraw(True)
        frameRemains = 0.0 + 10- win.monitorFramePeriod * 0.75  # most of one frame period left
        if text_3.status == STARTED and t >= frameRemains:
            text_3.setAutoDraw(False)
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in audiobook_1Components:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # check for quit (the Esc key)
        if endExpNow or event.getKeys(keyList=["escape"]):
            core.quit()
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # -------Ending Routine "audiobook_1"-------
    for thisComponent in audiobook_1Components:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    
    
    # set up handler to look after randomisation of conditions etc
    trials = data.TrialHandler(nReps=5, method='random', 
        extraInfo=expInfo, originPath=-1,
        trialList=data.importConditions('images.xlsx'),
        seed=None, name='trials')
    thisExp.addLoop(trials)  # add the loop to the experiment
    thisTrial = trials.trialList[0]  # so we can initialise stimuli with some values
    # abbreviate parameter names if possible (e.g. rgb = thisTrial.rgb)
    if thisTrial != None:
        for paramName in thisTrial:
            exec('{} = thisTrial[paramName]'.format(paramName))
    
    for thisTrial in trials:
        currentLoop = trials
        # abbreviate parameter names if possible (e.g. rgb = thisTrial.rgb)
        if thisTrial != None:
            for paramName in thisTrial:
                exec('{} = thisTrial[paramName]'.format(paramName))
        
        # ------Prepare to start Routine "match"-------
        t = 0
        matchClock.reset()  # clock
        frameN = -1
        continueRoutine = True
        routineTimer.add(3.000000)
        # update component parameters for each repeat
        image.setSize([300,300])
        image.setImage(images)
        text.setText(name)
        matchClock.reset()
        thisExp.addData('begin_global', globalClock.getTime())
        thisExp.addData('begin_routine', matchClock.getTime())
        
        
        key_resp_1 = event.BuilderKeyResponse()
        # keep track of which components have finished
        matchComponents = [image, text, key_resp_1]
        for thisComponent in matchComponents:
            if hasattr(thisComponent, 'status'):
                thisComponent.status = NOT_STARTED
        
        # -------Start Routine "match"-------
        while continueRoutine and routineTimer.getTime() > 0:
            # get current time
            t = matchClock.getTime()
            frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
            # update/draw components on each frame
            
            # *image* updates
            if t >= 0.0 and image.status == NOT_STARTED:
                # keep track of start time/frame for later
                image.tStart = t
                image.frameNStart = frameN  # exact frame index
                image.setAutoDraw(True)
            frameRemains = 0.0 + 3.0- win.monitorFramePeriod * 0.75  # most of one frame period left
            if image.status == STARTED and t >= frameRemains:
                image.setAutoDraw(False)
            
            # *text* updates
            if t >= 0.0 and text.status == NOT_STARTED:
                # keep track of start time/frame for later
                text.tStart = t
                text.frameNStart = frameN  # exact frame index
                text.setAutoDraw(True)
            frameRemains = 0.0 + 3.0- win.monitorFramePeriod * 0.75  # most of one frame period left
            if text.status == STARTED and t >= frameRemains:
                text.setAutoDraw(False)
            
            
            # *key_resp_1* updates
            if t >= 0.0 and key_resp_1.status == NOT_STARTED:
                # keep track of start time/frame for later
                key_resp_1.tStart = t
                key_resp_1.frameNStart = frameN  # exact frame index
                key_resp_1.status = STARTED
                # keyboard checking is just starting
                win.callOnFlip(key_resp_1.clock.reset)  # t=0 on next screen flip
                event.clearEvents(eventType='keyboard')
            frameRemains = 0.0 + 3.0- win.monitorFramePeriod * 0.75  # most of one frame period left
            if key_resp_1.status == STARTED and t >= frameRemains:
                key_resp_1.status = STOPPED
            if key_resp_1.status == STARTED:
                theseKeys = event.getKeys(keyList=['z', 'x'])
                
                # check for quit:
                if "escape" in theseKeys:
                    endExpNow = True
                if len(theseKeys) > 0:  # at least one key was pressed
                    if key_resp_1.keys == []:  # then this was the first keypress
                        key_resp_1.keys = theseKeys[0]  # just the first key pressed
                        key_resp_1.rt = key_resp_1.clock.getTime()
                        # was this 'correct'?
                        if (key_resp_1.keys == str(corrAns)) or (key_resp_1.keys == corrAns):
                            key_resp_1.corr = 1
                        else:
                            key_resp_1.corr = 0
                        # a response ends the routine
                        continueRoutine = False
            
            # check if all components have finished
            if not continueRoutine:  # a component has requested a forced-end of Routine
                break
            continueRoutine = False  # will revert to True if at least one component still running
            for thisComponent in matchComponents:
                if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                    continueRoutine = True
                    break  # at least one component has not yet finished
            
            # check for quit (the Esc key)
            if endExpNow or event.getKeys(keyList=["escape"]):
                core.quit()
            
            # refresh the screen
            if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                win.flip()
        
        # -------Ending Routine "match"-------
        for thisComponent in matchComponents:
            if hasattr(thisComponent, "setAutoDraw"):
                thisComponent.setAutoDraw(False)
        thisExp.addData('end_global', globalClock.getTime())
        thisExp.addData('end_routine', matchClock.getTime())
        
        if not key_resp_1.keys :
            msg="Failed to respond"
        elif key_resp_1.corr :#stored on last run routine
            msg="Correct!"
        else:
            msg="Wrong."
        # check responses
        if key_resp_1.keys in ['', [], None]:  # No response was made
            key_resp_1.keys=None
            # was no response the correct answer?!
            if str(corrAns).lower() == 'none':
               key_resp_1.corr = 1  # correct non-response
            else:
               key_resp_1.corr = 0  # failed to respond (incorrectly)
        # store data for trials (TrialHandler)
        trials.addData('key_resp_1.keys',key_resp_1.keys)
        trials.addData('key_resp_1.corr', key_resp_1.corr)
        if key_resp_1.keys != None:  # we had a response
            trials.addData('key_resp_1.rt', key_resp_1.rt)
        
        # ------Prepare to start Routine "feedback"-------
        t = 0
        feedbackClock.reset()  # clock
        frameN = -1
        continueRoutine = True
        routineTimer.add(1.000000)
        # update component parameters for each repeat
        text_2.setText(msg)
        
        # keep track of which components have finished
        feedbackComponents = [text_2]
        for thisComponent in feedbackComponents:
            if hasattr(thisComponent, 'status'):
                thisComponent.status = NOT_STARTED
        
        # -------Start Routine "feedback"-------
        while continueRoutine and routineTimer.getTime() > 0:
            # get current time
            t = feedbackClock.getTime()
            frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
            # update/draw components on each frame
            
            # *text_2* updates
            if t >= 0.0 and text_2.status == NOT_STARTED:
                # keep track of start time/frame for later
                text_2.tStart = t
                text_2.frameNStart = frameN  # exact frame index
                text_2.setAutoDraw(True)
            frameRemains = 0.0 + 1.0- win.monitorFramePeriod * 0.75  # most of one frame period left
            if text_2.status == STARTED and t >= frameRemains:
                text_2.setAutoDraw(False)
            if bookClock.getTime() > 480:
                trials.finished=True
                book.stop()
            
            # check if all components have finished
            if not continueRoutine:  # a component has requested a forced-end of Routine
                break
            continueRoutine = False  # will revert to True if at least one component still running
            for thisComponent in feedbackComponents:
                if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                    continueRoutine = True
                    break  # at least one component has not yet finished
            
            # check for quit (the Esc key)
            if endExpNow or event.getKeys(keyList=["escape"]):
                core.quit()
            
            # refresh the screen
            if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                win.flip()
        
        # -------Ending Routine "feedback"-------
        for thisComponent in feedbackComponents:
            if hasattr(thisComponent, "setAutoDraw"):
                thisComponent.setAutoDraw(False)
        
        thisExp.nextEntry()
        
    # completed 5 repeats of 'trials'
    
    
    # ------Prepare to start Routine "end_loop"-------
    t = 0
    end_loopClock.reset()  # clock
    frameN = -1
    continueRoutine = True
    routineTimer.add(10.000000)
    # update component parameters for each repeat
    
    # keep track of which components have finished
    end_loopComponents = [text_4]
    for thisComponent in end_loopComponents:
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    
    # -------Start Routine "end_loop"-------
    while continueRoutine and routineTimer.getTime() > 0:
        # get current time
        t = end_loopClock.getTime()
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *text_4* updates
        if t >= 0.0 and text_4.status == NOT_STARTED:
            # keep track of start time/frame for later
            text_4.tStart = t
            text_4.frameNStart = frameN  # exact frame index
            text_4.setAutoDraw(True)
        frameRemains = 0.0 + 10- win.monitorFramePeriod * 0.75  # most of one frame period left
        if text_4.status == STARTED and t >= frameRemains:
            text_4.setAutoDraw(False)
        
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in end_loopComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # check for quit (the Esc key)
        if endExpNow or event.getKeys(keyList=["escape"]):
            core.quit()
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # -------Ending Routine "end_loop"-------
    for thisComponent in end_loopComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    
    thisExp.nextEntry()
    
# completed 1 repeats of 'trials_2'


# ------Prepare to start Routine "Finish"-------
t = 0
FinishClock.reset()  # clock
frameN = -1
continueRoutine = True
routineTimer.add(18.000000)
# update component parameters for each repeat
# keep track of which components have finished
FinishComponents = [text_5, text_6, text_7]
for thisComponent in FinishComponents:
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED

# -------Start Routine "Finish"-------
while continueRoutine and routineTimer.getTime() > 0:
    # get current time
    t = FinishClock.getTime()
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *text_5* updates
    if t >= 0 and text_5.status == NOT_STARTED:
        # keep track of start time/frame for later
        text_5.tStart = t
        text_5.frameNStart = frameN  # exact frame index
        text_5.setAutoDraw(True)
    frameRemains = 0 + 6- win.monitorFramePeriod * 0.75  # most of one frame period left
    if text_5.status == STARTED and t >= frameRemains:
        text_5.setAutoDraw(False)
    
    # *text_6* updates
    if t >= 6 and text_6.status == NOT_STARTED:
        # keep track of start time/frame for later
        text_6.tStart = t
        text_6.frameNStart = frameN  # exact frame index
        text_6.setAutoDraw(True)
    frameRemains = 6 + 6- win.monitorFramePeriod * 0.75  # most of one frame period left
    if text_6.status == STARTED and t >= frameRemains:
        text_6.setAutoDraw(False)
    
    # *text_7* updates
    if t >= 12 and text_7.status == NOT_STARTED:
        # keep track of start time/frame for later
        text_7.tStart = t
        text_7.frameNStart = frameN  # exact frame index
        text_7.setAutoDraw(True)
    frameRemains = 12 + 6- win.monitorFramePeriod * 0.75  # most of one frame period left
    if text_7.status == STARTED and t >= frameRemains:
        text_7.setAutoDraw(False)
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in FinishComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # check for quit (the Esc key)
    if endExpNow or event.getKeys(keyList=["escape"]):
        core.quit()
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "Finish"-------
for thisComponent in FinishComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)





# these shouldn't be strictly necessary (should auto-save)
thisExp.saveAsWideText(filename+'.csv')
thisExp.saveAsPickle(filename)
logging.flush()
# make sure everything is closed down
thisExp.abort()  # or data files will save again on exit
win.close()
core.quit()
