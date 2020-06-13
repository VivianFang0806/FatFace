#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
This experiment was created using PsychoPy3 Experiment Builder (v2020.1.2),
    on Fri Jun 12 15:06:13 2020
If you publish work using this script the most relevant publication is:

    Peirce J, Gray JR, Simpson S, MacAskill M, Höchenberger R, Sogo H, Kastman E, Lindeløv JK. (2019) 
        PsychoPy2: Experiments in behavior made easy Behav Res 51: 195. 
        https://doi.org/10.3758/s13428-018-01193-y

"""

from __future__ import absolute_import, division

from psychopy import locale_setup
from psychopy import prefs
from psychopy import sound, gui, visual, core, data, event, logging, clock
from psychopy.constants import (NOT_STARTED, STARTED, PLAYING, PAUSED,
                                STOPPED, FINISHED, PRESSED, RELEASED, FOREVER)

import numpy as np  # whole numpy lib is available, prepend 'np.'
from numpy import (sin, cos, tan, log, log10, pi, average,
                   sqrt, std, deg2rad, rad2deg, linspace, asarray)
from numpy.random import random, randint, normal, shuffle
import os  # handy system and path functions
import sys  # to get file system encoding

from psychopy.hardware import keyboard



# Ensure that relative paths start from the same directory as this script
_thisDir = os.path.dirname(os.path.abspath(__file__))
os.chdir(_thisDir)

# Store info about the experiment session
psychopyVersion = '2020.1.2'
expName = 'FatFace_exp2'  # from the Builder filename that created this script
expInfo = {'participant': '', 'gender': '', 'age': '', 'session': '001'}
dlg = gui.DlgFromDict(dictionary=expInfo, sortKeys=False, title=expName)
if dlg.OK == False:
    core.quit()  # user pressed cancel
expInfo['date'] = data.getDateStr()  # add a simple timestamp
expInfo['expName'] = expName
expInfo['psychopyVersion'] = psychopyVersion

# Data file name stem = absolute path + name; later add .psyexp, .csv, .log, etc
filename = _thisDir + os.sep + u'data/%s_%s_%s' % (expInfo['participant'], expName, expInfo['date'])

# An ExperimentHandler isn't essential but helps with data saving
thisExp = data.ExperimentHandler(name=expName, version='',
    extraInfo=expInfo, runtimeInfo=None,
    originPath='/Users/josephine/Documents/research/FatFaceIllusion/program/Exp2/FatFace_exp2_lastrun.py',
    savePickle=True, saveWideText=True,
    dataFileName=filename)
# save a log file for detail verbose info
logFile = logging.LogFile(filename+'.log', level=logging.EXP)
logging.console.setLevel(logging.WARNING)  # this outputs to the screen, not a file

endExpNow = False  # flag for 'escape' or other condition => quit the exp
frameTolerance = 0.001  # how close to onset before 'same' frame

# Start Code - component code to be run before the window creation

# Setup the Window
win = visual.Window(
    size=[1280, 800], fullscr=True, screen=0, 
    winType='pyglet', allowGUI=False, allowStencil=False,
    monitor='testMonitor', color=[0,0,0], colorSpace='rgb',
    blendMode='avg', useFBO=True, 
    units='height')
# store frame rate of monitor if we can measure it
expInfo['frameRate'] = win.getActualFrameRate()
if expInfo['frameRate'] != None:
    frameDur = 1.0 / round(expInfo['frameRate'])
else:
    frameDur = 1.0 / 60.0  # could not measure, so guess

# create a default keyboard (e.g. to check for escape)
defaultKeyboard = keyboard.Keyboard()

# Initialize components for Routine "Instruction"
InstructionClock = core.Clock()
InstrText = visual.TextStim(win=win, name='InstrText',
    text='Welcome to our experiment!\n\nIn our experiment, two faces will presented on the Screen, one is on top and another one is at the bottome. \nPlace indicate which face looks fatter by clicking on it as quick as you can.\n\nPress "Space" to go to the practical session.',
    font='Arial',
    pos=(0, 0), height=0.05, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=0.0);
InstrKey = keyboard.Keyboard()

# Initialize components for Routine "Practise"
PractiseClock = core.Clock()
Fixation0 = visual.ShapeStim(
    win=win, name='Fixation0', vertices='cross',
    size=(0.1, 0.1),
    ori=0, pos=(0, 0),
    lineWidth=1, lineColor=[1,1,1], lineColorSpace='rgb',
    fillColor=[1,1,1], fillColorSpace='rgb',
    opacity=1, depth=0.0, interpolate=True)
Upper_image = visual.ImageStim(
    win=win,
    name='Upper_image', 
    image='sin', mask=None,
    ori=0, pos=(0, 0.16), size=None,
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=-1.0)
Lower_image = visual.ImageStim(
    win=win,
    name='Lower_image', 
    image='sin', mask=None,
    ori=0, pos=(0, -0.16), size=None,
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=-2.0)
PracMouse = event.Mouse(win=win)
x, y = [None, None]
PracMouse.mouseClock = core.Clock()

# Initialize components for Routine "Blank500"
Blank500Clock = core.Clock()
BlankTest = visual.TextStim(win=win, name='BlankTest',
    text=None,
    font='Arial',
    pos=(0, 0), height=0.1, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=0.0);

# Initialize components for Routine "Break"
BreakClock = core.Clock()
BreakText = visual.TextStim(win=win, name='BreakText',
    text='The practise part is over.\n\nPress "Space" to go to the next part.',
    font='Arial',
    pos=(0, 0), height=0.05, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=0.0);
Prac_Key = keyboard.Keyboard()

# Initialize components for Routine "AsianS"
AsianSClock = core.Clock()
import random
AScondition = random.choice(('conditionList/AS_list1.xlsx','conditionList/AS_list2.xlsx'))

thisExp.addData('AScondition_file', AScondition)
Fixation = visual.ShapeStim(
    win=win, name='Fixation', vertices='cross',
    size=(0.1, 0.1),
    ori=0, pos=(0, 0),
    lineWidth=1, lineColor=[1,1,1], lineColorSpace='rgb',
    fillColor=[1,1,1], fillColorSpace='rgb',
    opacity=1, depth=-1.0, interpolate=True)
AS_image_1 = visual.ImageStim(
    win=win,
    name='AS_image_1', 
    image='sin', mask=None,
    ori=0, pos=(0, 0.16), size=None,
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=-2.0)
AS_image_2 = visual.ImageStim(
    win=win,
    name='AS_image_2', 
    image='sin', mask=None,
    ori=0, pos=(0, -0.16), size=None,
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=-3.0)
ASMouse = event.Mouse(win=win)
x, y = [None, None]
ASMouse.mouseClock = core.Clock()

# Initialize components for Routine "Blank500"
Blank500Clock = core.Clock()
BlankTest = visual.TextStim(win=win, name='BlankTest',
    text=None,
    font='Arial',
    pos=(0, 0), height=0.1, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=0.0);

# Initialize components for Routine "BlackS"
BlackSClock = core.Clock()
import random
BScondition = random.choice(('conditionList/BS_list1.xlsx','conditionList/BS_list2.xlsx'))

thisExp.addData('BScondition_file', BScondition)
Fixation5 = visual.ShapeStim(
    win=win, name='Fixation5', vertices='cross',
    size=(0.1, 0.1),
    ori=0, pos=(0, 0),
    lineWidth=1, lineColor=[1,1,1], lineColorSpace='rgb',
    fillColor=[1,1,1], fillColorSpace='rgb',
    opacity=1, depth=-1.0, interpolate=True)
BS_image_1 = visual.ImageStim(
    win=win,
    name='BS_image_1', 
    image='sin', mask=None,
    ori=0, pos=(0, 0.16), size=None,
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=-2.0)
BS_image_2 = visual.ImageStim(
    win=win,
    name='BS_image_2', 
    image='sin', mask=None,
    ori=0, pos=(0, -0.16), size=None,
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=-3.0)
BSMouse = event.Mouse(win=win)
x, y = [None, None]
BSMouse.mouseClock = core.Clock()

# Initialize components for Routine "Blank500"
Blank500Clock = core.Clock()
BlankTest = visual.TextStim(win=win, name='BlankTest',
    text=None,
    font='Arial',
    pos=(0, 0), height=0.1, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=0.0);

# Initialize components for Routine "BlackD"
BlackDClock = core.Clock()
import random
BDcondition = random.choice(('conditionList/BD_list1.xlsx','conditionList/BD_list2.xlsx'))

thisExp.addData('BDcondition_file', BDcondition)
Fixation6 = visual.ShapeStim(
    win=win, name='Fixation6', vertices='cross',
    size=(0.1, 0.1),
    ori=0, pos=(0, 0),
    lineWidth=1, lineColor=[1,1,1], lineColorSpace='rgb',
    fillColor=[1,1,1], fillColorSpace='rgb',
    opacity=1, depth=-1.0, interpolate=True)
BD_image_1 = visual.ImageStim(
    win=win,
    name='BD_image_1', 
    image='sin', mask=None,
    ori=0, pos=(0, 0.16), size=None,
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=-2.0)
BD_image_2 = visual.ImageStim(
    win=win,
    name='BD_image_2', 
    image='sin', mask=None,
    ori=0, pos=(0, -0.16), size=None,
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=-3.0)
BDmouse = event.Mouse(win=win)
x, y = [None, None]
BDmouse.mouseClock = core.Clock()

# Initialize components for Routine "Blank500"
Blank500Clock = core.Clock()
BlankTest = visual.TextStim(win=win, name='BlankTest',
    text=None,
    font='Arial',
    pos=(0, 0), height=0.1, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=0.0);

# Initialize components for Routine "AsianD"
AsianDClock = core.Clock()
import random
ADcondition = random.choice(('conditionList/AD_list1.xlsx','conditionList/AD_list2.xlsx'))

thisExp.addData('ADcondition_file', ADcondition)
Fixation2 = visual.ShapeStim(
    win=win, name='Fixation2', vertices='cross',
    size=(0.1, 0.1),
    ori=0, pos=(0, 0),
    lineWidth=1, lineColor=[1,1,1], lineColorSpace='rgb',
    fillColor=[1,1,1], fillColorSpace='rgb',
    opacity=1, depth=-1.0, interpolate=True)
AD_image_1 = visual.ImageStim(
    win=win,
    name='AD_image_1', 
    image='sin', mask=None,
    ori=0, pos=(0, 0.16), size=None,
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=-2.0)
AD_imgae_2 = visual.ImageStim(
    win=win,
    name='AD_imgae_2', 
    image='sin', mask=None,
    ori=0, pos=(0, -0.16), size=None,
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=-3.0)
ADMouse = event.Mouse(win=win)
x, y = [None, None]
ADMouse.mouseClock = core.Clock()

# Initialize components for Routine "Blank500"
Blank500Clock = core.Clock()
BlankTest = visual.TextStim(win=win, name='BlankTest',
    text=None,
    font='Arial',
    pos=(0, 0), height=0.1, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=0.0);

# Initialize components for Routine "CaucasianS"
CaucasianSClock = core.Clock()
import random
CScondition = random.choice(('conditionList/CS_list1.xlsx','conditionList/CS_list2.xlsx'))

thisExp.addData('CScondition_file', CScondition)
Fixation3 = visual.ShapeStim(
    win=win, name='Fixation3', vertices='cross',
    size=(0.1, 0.1),
    ori=0, pos=(0, 0),
    lineWidth=1, lineColor=[1,1,1], lineColorSpace='rgb',
    fillColor=[1,1,1], fillColorSpace='rgb',
    opacity=1, depth=-1.0, interpolate=True)
CS_image_1 = visual.ImageStim(
    win=win,
    name='CS_image_1', 
    image='sin', mask=None,
    ori=0, pos=(0, 0.16), size=None,
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=-2.0)
CS_image_2 = visual.ImageStim(
    win=win,
    name='CS_image_2', 
    image='sin', mask=None,
    ori=0, pos=(0, -0.16), size=None,
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=-3.0)
CSMouse = event.Mouse(win=win)
x, y = [None, None]
CSMouse.mouseClock = core.Clock()

# Initialize components for Routine "Blank500"
Blank500Clock = core.Clock()
BlankTest = visual.TextStim(win=win, name='BlankTest',
    text=None,
    font='Arial',
    pos=(0, 0), height=0.1, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=0.0);

# Initialize components for Routine "CaucasianD"
CaucasianDClock = core.Clock()
import random
CDcondition = random.choice(('conditionList/CD_list1.xlsx','conditionList/CD_list2.xlsx'))

thisExp.addData('CDcondition_file', CDcondition)
Fixation4 = visual.ShapeStim(
    win=win, name='Fixation4', vertices='cross',
    size=(0.1, 0.1),
    ori=0, pos=(0, 0),
    lineWidth=1, lineColor=[1,1,1], lineColorSpace='rgb',
    fillColor=[1,1,1], fillColorSpace='rgb',
    opacity=1, depth=-1.0, interpolate=True)
CD_image_1 = visual.ImageStim(
    win=win,
    name='CD_image_1', 
    image='sin', mask=None,
    ori=0, pos=(0, 0.16), size=None,
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=-2.0)
CD_image_2 = visual.ImageStim(
    win=win,
    name='CD_image_2', 
    image='sin', mask=None,
    ori=0, pos=(0, -0.16), size=None,
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=-3.0)
CDMouse = event.Mouse(win=win)
x, y = [None, None]
CDMouse.mouseClock = core.Clock()

# Initialize components for Routine "Blank500"
Blank500Clock = core.Clock()
BlankTest = visual.TextStim(win=win, name='BlankTest',
    text=None,
    font='Arial',
    pos=(0, 0), height=0.1, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=0.0);

# Initialize components for Routine "End"
EndClock = core.Clock()
text = visual.TextStim(win=win, name='text',
    text='Thank you!',
    font='Arial',
    pos=(0, 0), height=0.1, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=0.0);

# Create some handy timers
globalClock = core.Clock()  # to track the time since experiment started
routineTimer = core.CountdownTimer()  # to track time remaining of each (non-slip) routine 

# ------Prepare to start Routine "Instruction"-------
continueRoutine = True
# update component parameters for each repeat
InstrKey.keys = []
InstrKey.rt = []
_InstrKey_allKeys = []
# keep track of which components have finished
InstructionComponents = [InstrText, InstrKey]
for thisComponent in InstructionComponents:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
InstructionClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
frameN = -1

# -------Run Routine "Instruction"-------
while continueRoutine:
    # get current time
    t = InstructionClock.getTime()
    tThisFlip = win.getFutureFlipTime(clock=InstructionClock)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *InstrText* updates
    if InstrText.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        InstrText.frameNStart = frameN  # exact frame index
        InstrText.tStart = t  # local t and not account for scr refresh
        InstrText.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(InstrText, 'tStartRefresh')  # time at next scr refresh
        InstrText.setAutoDraw(True)
    
    # *InstrKey* updates
    waitOnFlip = False
    if InstrKey.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        InstrKey.frameNStart = frameN  # exact frame index
        InstrKey.tStart = t  # local t and not account for scr refresh
        InstrKey.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(InstrKey, 'tStartRefresh')  # time at next scr refresh
        InstrKey.status = STARTED
        # keyboard checking is just starting
        waitOnFlip = True
        win.callOnFlip(InstrKey.clock.reset)  # t=0 on next screen flip
        win.callOnFlip(InstrKey.clearEvents, eventType='keyboard')  # clear events on next screen flip
    if InstrKey.status == STARTED and not waitOnFlip:
        theseKeys = InstrKey.getKeys(keyList=['space'], waitRelease=False)
        _InstrKey_allKeys.extend(theseKeys)
        if len(_InstrKey_allKeys):
            InstrKey.keys = _InstrKey_allKeys[-1].name  # just the last key pressed
            InstrKey.rt = _InstrKey_allKeys[-1].rt
            # a response ends the routine
            continueRoutine = False
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in InstructionComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "Instruction"-------
for thisComponent in InstructionComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
thisExp.addData('InstrText.started', InstrText.tStartRefresh)
thisExp.addData('InstrText.stopped', InstrText.tStopRefresh)
# check responses
if InstrKey.keys in ['', [], None]:  # No response was made
    InstrKey.keys = None
thisExp.addData('InstrKey.keys',InstrKey.keys)
if InstrKey.keys != None:  # we had a response
    thisExp.addData('InstrKey.rt', InstrKey.rt)
thisExp.addData('InstrKey.started', InstrKey.tStartRefresh)
thisExp.addData('InstrKey.stopped', InstrKey.tStopRefresh)
thisExp.nextEntry()
# the Routine "Instruction" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# set up handler to look after randomisation of conditions etc
Prac_Loop = data.TrialHandler(nReps=1, method='random', 
    extraInfo=expInfo, originPath=-1,
    trialList=data.importConditions('Prac_Order.xlsx'),
    seed=None, name='Prac_Loop')
thisExp.addLoop(Prac_Loop)  # add the loop to the experiment
thisPrac_Loop = Prac_Loop.trialList[0]  # so we can initialise stimuli with some values
# abbreviate parameter names if possible (e.g. rgb = thisPrac_Loop.rgb)
if thisPrac_Loop != None:
    for paramName in thisPrac_Loop:
        exec('{} = thisPrac_Loop[paramName]'.format(paramName))

for thisPrac_Loop in Prac_Loop:
    currentLoop = Prac_Loop
    # abbreviate parameter names if possible (e.g. rgb = thisPrac_Loop.rgb)
    if thisPrac_Loop != None:
        for paramName in thisPrac_Loop:
            exec('{} = thisPrac_Loop[paramName]'.format(paramName))
    
    # ------Prepare to start Routine "Practise"-------
    continueRoutine = True
    # update component parameters for each repeat
    Upper_image.setImage(UImage)
    Lower_image.setImage(LImage)
    # setup some python lists for storing info about the PracMouse
    PracMouse.clicked_name = []
    PracMouse.clicked_pos = []
    gotValidClick = False  # until a click is received
    # keep track of which components have finished
    PractiseComponents = [Fixation0, Upper_image, Lower_image, PracMouse]
    for thisComponent in PractiseComponents:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    PractiseClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
    frameN = -1
    
    # -------Run Routine "Practise"-------
    while continueRoutine:
        # get current time
        t = PractiseClock.getTime()
        tThisFlip = win.getFutureFlipTime(clock=PractiseClock)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *Fixation0* updates
        if Fixation0.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            Fixation0.frameNStart = frameN  # exact frame index
            Fixation0.tStart = t  # local t and not account for scr refresh
            Fixation0.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(Fixation0, 'tStartRefresh')  # time at next scr refresh
            Fixation0.setAutoDraw(True)
        if Fixation0.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > Fixation0.tStartRefresh + 0.5-frameTolerance:
                # keep track of stop time/frame for later
                Fixation0.tStop = t  # not accounting for scr refresh
                Fixation0.frameNStop = frameN  # exact frame index
                win.timeOnFlip(Fixation0, 'tStopRefresh')  # time at next scr refresh
                Fixation0.setAutoDraw(False)
        
        # *Upper_image* updates
        if Upper_image.status == NOT_STARTED and tThisFlip >= 0.5-frameTolerance:
            # keep track of start time/frame for later
            Upper_image.frameNStart = frameN  # exact frame index
            Upper_image.tStart = t  # local t and not account for scr refresh
            Upper_image.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(Upper_image, 'tStartRefresh')  # time at next scr refresh
            Upper_image.setAutoDraw(True)
        if Upper_image.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > Upper_image.tStartRefresh + 3-frameTolerance:
                # keep track of stop time/frame for later
                Upper_image.tStop = t  # not accounting for scr refresh
                Upper_image.frameNStop = frameN  # exact frame index
                win.timeOnFlip(Upper_image, 'tStopRefresh')  # time at next scr refresh
                Upper_image.setAutoDraw(False)
        
        # *Lower_image* updates
        if Lower_image.status == NOT_STARTED and tThisFlip >= 0.5-frameTolerance:
            # keep track of start time/frame for later
            Lower_image.frameNStart = frameN  # exact frame index
            Lower_image.tStart = t  # local t and not account for scr refresh
            Lower_image.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(Lower_image, 'tStartRefresh')  # time at next scr refresh
            Lower_image.setAutoDraw(True)
        if Lower_image.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > Lower_image.tStartRefresh + 3-frameTolerance:
                # keep track of stop time/frame for later
                Lower_image.tStop = t  # not accounting for scr refresh
                Lower_image.frameNStop = frameN  # exact frame index
                win.timeOnFlip(Lower_image, 'tStopRefresh')  # time at next scr refresh
                Lower_image.setAutoDraw(False)
        # *PracMouse* updates
        if PracMouse.status == NOT_STARTED and t >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            PracMouse.frameNStart = frameN  # exact frame index
            PracMouse.tStart = t  # local t and not account for scr refresh
            PracMouse.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(PracMouse, 'tStartRefresh')  # time at next scr refresh
            PracMouse.status = STARTED
            PracMouse.mouseClock.reset()
            prevButtonState = PracMouse.getPressed()  # if button is down already this ISN'T a new click
        if PracMouse.status == STARTED:  # only update if started and not finished!
            buttons = PracMouse.getPressed()
            if buttons != prevButtonState:  # button state changed?
                prevButtonState = buttons
                if sum(buttons) > 0:  # state changed to a new click
                    # check if the mouse was inside our 'clickable' objects
                    gotValidClick = False
                    for obj in [Upper_image,Lower_image]:
                        if obj.contains(PracMouse):
                            gotValidClick = True
                            PracMouse.clicked_name.append(obj.name)
                            PracMouse.clicked_pos.append(obj.pos)
                    if gotValidClick:  # abort routine on response
                        continueRoutine = False
        
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in PractiseComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # -------Ending Routine "Practise"-------
    for thisComponent in PractiseComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    Prac_Loop.addData('Fixation0.started', Fixation0.tStartRefresh)
    Prac_Loop.addData('Fixation0.stopped', Fixation0.tStopRefresh)
    Prac_Loop.addData('Upper_image.started', Upper_image.tStartRefresh)
    Prac_Loop.addData('Upper_image.stopped', Upper_image.tStopRefresh)
    Prac_Loop.addData('Lower_image.started', Lower_image.tStartRefresh)
    Prac_Loop.addData('Lower_image.stopped', Lower_image.tStopRefresh)
    # store data for Prac_Loop (TrialHandler)
    x, y = PracMouse.getPos()
    buttons = PracMouse.getPressed()
    if sum(buttons):
        # check if the mouse was inside our 'clickable' objects
        gotValidClick = False
        for obj in [Upper_image,Lower_image]:
            if obj.contains(PracMouse):
                gotValidClick = True
                PracMouse.clicked_name.append(obj.name)
                PracMouse.clicked_pos.append(obj.pos)
    Prac_Loop.addData('PracMouse.x', x)
    Prac_Loop.addData('PracMouse.y', y)
    Prac_Loop.addData('PracMouse.leftButton', buttons[0])
    Prac_Loop.addData('PracMouse.midButton', buttons[1])
    Prac_Loop.addData('PracMouse.rightButton', buttons[2])
    if len(PracMouse.clicked_name):
        Prac_Loop.addData('PracMouse.clicked_name', PracMouse.clicked_name[0])
    if len(PracMouse.clicked_pos):
        Prac_Loop.addData('PracMouse.clicked_pos', PracMouse.clicked_pos[0])
    Prac_Loop.addData('PracMouse.started', PracMouse.tStart)
    Prac_Loop.addData('PracMouse.stopped', PracMouse.tStop)
    # the Routine "Practise" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    
    # ------Prepare to start Routine "Blank500"-------
    continueRoutine = True
    routineTimer.add(0.500000)
    # update component parameters for each repeat
    # keep track of which components have finished
    Blank500Components = [BlankTest]
    for thisComponent in Blank500Components:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    Blank500Clock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
    frameN = -1
    
    # -------Run Routine "Blank500"-------
    while continueRoutine and routineTimer.getTime() > 0:
        # get current time
        t = Blank500Clock.getTime()
        tThisFlip = win.getFutureFlipTime(clock=Blank500Clock)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *BlankTest* updates
        if BlankTest.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            BlankTest.frameNStart = frameN  # exact frame index
            BlankTest.tStart = t  # local t and not account for scr refresh
            BlankTest.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(BlankTest, 'tStartRefresh')  # time at next scr refresh
            BlankTest.setAutoDraw(True)
        if BlankTest.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > BlankTest.tStartRefresh + 0.5-frameTolerance:
                # keep track of stop time/frame for later
                BlankTest.tStop = t  # not accounting for scr refresh
                BlankTest.frameNStop = frameN  # exact frame index
                win.timeOnFlip(BlankTest, 'tStopRefresh')  # time at next scr refresh
                BlankTest.setAutoDraw(False)
        
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in Blank500Components:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # -------Ending Routine "Blank500"-------
    for thisComponent in Blank500Components:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    Prac_Loop.addData('BlankTest.started', BlankTest.tStartRefresh)
    Prac_Loop.addData('BlankTest.stopped', BlankTest.tStopRefresh)
    thisExp.nextEntry()
    
# completed 1 repeats of 'Prac_Loop'


# ------Prepare to start Routine "Break"-------
continueRoutine = True
# update component parameters for each repeat
Prac_Key.keys = []
Prac_Key.rt = []
_Prac_Key_allKeys = []
# keep track of which components have finished
BreakComponents = [BreakText, Prac_Key]
for thisComponent in BreakComponents:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
BreakClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
frameN = -1

# -------Run Routine "Break"-------
while continueRoutine:
    # get current time
    t = BreakClock.getTime()
    tThisFlip = win.getFutureFlipTime(clock=BreakClock)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *BreakText* updates
    if BreakText.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        BreakText.frameNStart = frameN  # exact frame index
        BreakText.tStart = t  # local t and not account for scr refresh
        BreakText.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(BreakText, 'tStartRefresh')  # time at next scr refresh
        BreakText.setAutoDraw(True)
    
    # *Prac_Key* updates
    waitOnFlip = False
    if Prac_Key.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        Prac_Key.frameNStart = frameN  # exact frame index
        Prac_Key.tStart = t  # local t and not account for scr refresh
        Prac_Key.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(Prac_Key, 'tStartRefresh')  # time at next scr refresh
        Prac_Key.status = STARTED
        # keyboard checking is just starting
        waitOnFlip = True
        win.callOnFlip(Prac_Key.clock.reset)  # t=0 on next screen flip
        win.callOnFlip(Prac_Key.clearEvents, eventType='keyboard')  # clear events on next screen flip
    if Prac_Key.status == STARTED and not waitOnFlip:
        theseKeys = Prac_Key.getKeys(keyList=['space'], waitRelease=False)
        _Prac_Key_allKeys.extend(theseKeys)
        if len(_Prac_Key_allKeys):
            Prac_Key.keys = _Prac_Key_allKeys[-1].name  # just the last key pressed
            Prac_Key.rt = _Prac_Key_allKeys[-1].rt
            # a response ends the routine
            continueRoutine = False
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in BreakComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "Break"-------
for thisComponent in BreakComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
thisExp.addData('BreakText.started', BreakText.tStartRefresh)
thisExp.addData('BreakText.stopped', BreakText.tStopRefresh)
# check responses
if Prac_Key.keys in ['', [], None]:  # No response was made
    Prac_Key.keys = None
thisExp.addData('Prac_Key.keys',Prac_Key.keys)
if Prac_Key.keys != None:  # we had a response
    thisExp.addData('Prac_Key.rt', Prac_Key.rt)
thisExp.addData('Prac_Key.started', Prac_Key.tStartRefresh)
thisExp.addData('Prac_Key.stopped', Prac_Key.tStopRefresh)
thisExp.nextEntry()
# the Routine "Break" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# set up handler to look after randomisation of conditions etc
BlockTrail = data.TrialHandler(nReps=1, method='random', 
    extraInfo=expInfo, originPath=-1,
    trialList=data.importConditions('BlockOrder.xlsx'),
    seed=None, name='BlockTrail')
thisExp.addLoop(BlockTrail)  # add the loop to the experiment
thisBlockTrail = BlockTrail.trialList[0]  # so we can initialise stimuli with some values
# abbreviate parameter names if possible (e.g. rgb = thisBlockTrail.rgb)
if thisBlockTrail != None:
    for paramName in thisBlockTrail:
        exec('{} = thisBlockTrail[paramName]'.format(paramName))

for thisBlockTrail in BlockTrail:
    currentLoop = BlockTrail
    # abbreviate parameter names if possible (e.g. rgb = thisBlockTrail.rgb)
    if thisBlockTrail != None:
        for paramName in thisBlockTrail:
            exec('{} = thisBlockTrail[paramName]'.format(paramName))
    
    # set up handler to look after randomisation of conditions etc
    AS_Loop = data.TrialHandler(nReps=AS_rep, method='random', 
        extraInfo=expInfo, originPath=-1,
        trialList=data.importConditions(AScondition),
        seed=None, name='AS_Loop')
    thisExp.addLoop(AS_Loop)  # add the loop to the experiment
    thisAS_Loop = AS_Loop.trialList[0]  # so we can initialise stimuli with some values
    # abbreviate parameter names if possible (e.g. rgb = thisAS_Loop.rgb)
    if thisAS_Loop != None:
        for paramName in thisAS_Loop:
            exec('{} = thisAS_Loop[paramName]'.format(paramName))
    
    for thisAS_Loop in AS_Loop:
        currentLoop = AS_Loop
        # abbreviate parameter names if possible (e.g. rgb = thisAS_Loop.rgb)
        if thisAS_Loop != None:
            for paramName in thisAS_Loop:
                exec('{} = thisAS_Loop[paramName]'.format(paramName))
        
        # ------Prepare to start Routine "AsianS"-------
        continueRoutine = True
        # update component parameters for each repeat
        AS_image_1.setImage(Upper_Image)
        AS_image_2.setImage(Lower_Image)
        # setup some python lists for storing info about the ASMouse
        ASMouse.clicked_name = []
        ASMouse.clicked_pos = []
        gotValidClick = False  # until a click is received
        # keep track of which components have finished
        AsianSComponents = [Fixation, AS_image_1, AS_image_2, ASMouse]
        for thisComponent in AsianSComponents:
            thisComponent.tStart = None
            thisComponent.tStop = None
            thisComponent.tStartRefresh = None
            thisComponent.tStopRefresh = None
            if hasattr(thisComponent, 'status'):
                thisComponent.status = NOT_STARTED
        # reset timers
        t = 0
        _timeToFirstFrame = win.getFutureFlipTime(clock="now")
        AsianSClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
        frameN = -1
        
        # -------Run Routine "AsianS"-------
        while continueRoutine:
            # get current time
            t = AsianSClock.getTime()
            tThisFlip = win.getFutureFlipTime(clock=AsianSClock)
            tThisFlipGlobal = win.getFutureFlipTime(clock=None)
            frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
            # update/draw components on each frame
            
            # *Fixation* updates
            if Fixation.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                Fixation.frameNStart = frameN  # exact frame index
                Fixation.tStart = t  # local t and not account for scr refresh
                Fixation.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(Fixation, 'tStartRefresh')  # time at next scr refresh
                Fixation.setAutoDraw(True)
            if Fixation.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > Fixation.tStartRefresh + 0.5-frameTolerance:
                    # keep track of stop time/frame for later
                    Fixation.tStop = t  # not accounting for scr refresh
                    Fixation.frameNStop = frameN  # exact frame index
                    win.timeOnFlip(Fixation, 'tStopRefresh')  # time at next scr refresh
                    Fixation.setAutoDraw(False)
            
            # *AS_image_1* updates
            if AS_image_1.status == NOT_STARTED and tThisFlip >= 0.5-frameTolerance:
                # keep track of start time/frame for later
                AS_image_1.frameNStart = frameN  # exact frame index
                AS_image_1.tStart = t  # local t and not account for scr refresh
                AS_image_1.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(AS_image_1, 'tStartRefresh')  # time at next scr refresh
                AS_image_1.setAutoDraw(True)
            if AS_image_1.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > AS_image_1.tStartRefresh + 3-frameTolerance:
                    # keep track of stop time/frame for later
                    AS_image_1.tStop = t  # not accounting for scr refresh
                    AS_image_1.frameNStop = frameN  # exact frame index
                    win.timeOnFlip(AS_image_1, 'tStopRefresh')  # time at next scr refresh
                    AS_image_1.setAutoDraw(False)
            
            # *AS_image_2* updates
            if AS_image_2.status == NOT_STARTED and tThisFlip >= 0.5-frameTolerance:
                # keep track of start time/frame for later
                AS_image_2.frameNStart = frameN  # exact frame index
                AS_image_2.tStart = t  # local t and not account for scr refresh
                AS_image_2.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(AS_image_2, 'tStartRefresh')  # time at next scr refresh
                AS_image_2.setAutoDraw(True)
            if AS_image_2.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > AS_image_2.tStartRefresh + 3-frameTolerance:
                    # keep track of stop time/frame for later
                    AS_image_2.tStop = t  # not accounting for scr refresh
                    AS_image_2.frameNStop = frameN  # exact frame index
                    win.timeOnFlip(AS_image_2, 'tStopRefresh')  # time at next scr refresh
                    AS_image_2.setAutoDraw(False)
            # *ASMouse* updates
            if ASMouse.status == NOT_STARTED and t >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                ASMouse.frameNStart = frameN  # exact frame index
                ASMouse.tStart = t  # local t and not account for scr refresh
                ASMouse.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(ASMouse, 'tStartRefresh')  # time at next scr refresh
                ASMouse.status = STARTED
                ASMouse.mouseClock.reset()
                prevButtonState = ASMouse.getPressed()  # if button is down already this ISN'T a new click
            if ASMouse.status == STARTED:  # only update if started and not finished!
                buttons = ASMouse.getPressed()
                if buttons != prevButtonState:  # button state changed?
                    prevButtonState = buttons
                    if sum(buttons) > 0:  # state changed to a new click
                        # check if the mouse was inside our 'clickable' objects
                        gotValidClick = False
                        for obj in [AS_image_1,AS_image_2]:
                            if obj.contains(ASMouse):
                                gotValidClick = True
                                ASMouse.clicked_name.append(obj.name)
                                ASMouse.clicked_pos.append(obj.pos)
                        if gotValidClick:  # abort routine on response
                            continueRoutine = False
            
            # check for quit (typically the Esc key)
            if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
                core.quit()
            
            # check if all components have finished
            if not continueRoutine:  # a component has requested a forced-end of Routine
                break
            continueRoutine = False  # will revert to True if at least one component still running
            for thisComponent in AsianSComponents:
                if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                    continueRoutine = True
                    break  # at least one component has not yet finished
            
            # refresh the screen
            if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                win.flip()
        
        # -------Ending Routine "AsianS"-------
        for thisComponent in AsianSComponents:
            if hasattr(thisComponent, "setAutoDraw"):
                thisComponent.setAutoDraw(False)
        AS_Loop.addData('Fixation.started', Fixation.tStartRefresh)
        AS_Loop.addData('Fixation.stopped', Fixation.tStopRefresh)
        AS_Loop.addData('AS_image_1.started', AS_image_1.tStartRefresh)
        AS_Loop.addData('AS_image_1.stopped', AS_image_1.tStopRefresh)
        AS_Loop.addData('AS_image_2.started', AS_image_2.tStartRefresh)
        AS_Loop.addData('AS_image_2.stopped', AS_image_2.tStopRefresh)
        # store data for AS_Loop (TrialHandler)
        x, y = ASMouse.getPos()
        buttons = ASMouse.getPressed()
        if sum(buttons):
            # check if the mouse was inside our 'clickable' objects
            gotValidClick = False
            for obj in [AS_image_1,AS_image_2]:
                if obj.contains(ASMouse):
                    gotValidClick = True
                    ASMouse.clicked_name.append(obj.name)
                    ASMouse.clicked_pos.append(obj.pos)
        AS_Loop.addData('ASMouse.x', x)
        AS_Loop.addData('ASMouse.y', y)
        AS_Loop.addData('ASMouse.leftButton', buttons[0])
        AS_Loop.addData('ASMouse.midButton', buttons[1])
        AS_Loop.addData('ASMouse.rightButton', buttons[2])
        if len(ASMouse.clicked_name):
            AS_Loop.addData('ASMouse.clicked_name', ASMouse.clicked_name[0])
        if len(ASMouse.clicked_pos):
            AS_Loop.addData('ASMouse.clicked_pos', ASMouse.clicked_pos[0])
        AS_Loop.addData('ASMouse.started', ASMouse.tStart)
        AS_Loop.addData('ASMouse.stopped', ASMouse.tStop)
        # the Routine "AsianS" was not non-slip safe, so reset the non-slip timer
        routineTimer.reset()
        
        # ------Prepare to start Routine "Blank500"-------
        continueRoutine = True
        routineTimer.add(0.500000)
        # update component parameters for each repeat
        # keep track of which components have finished
        Blank500Components = [BlankTest]
        for thisComponent in Blank500Components:
            thisComponent.tStart = None
            thisComponent.tStop = None
            thisComponent.tStartRefresh = None
            thisComponent.tStopRefresh = None
            if hasattr(thisComponent, 'status'):
                thisComponent.status = NOT_STARTED
        # reset timers
        t = 0
        _timeToFirstFrame = win.getFutureFlipTime(clock="now")
        Blank500Clock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
        frameN = -1
        
        # -------Run Routine "Blank500"-------
        while continueRoutine and routineTimer.getTime() > 0:
            # get current time
            t = Blank500Clock.getTime()
            tThisFlip = win.getFutureFlipTime(clock=Blank500Clock)
            tThisFlipGlobal = win.getFutureFlipTime(clock=None)
            frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
            # update/draw components on each frame
            
            # *BlankTest* updates
            if BlankTest.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                BlankTest.frameNStart = frameN  # exact frame index
                BlankTest.tStart = t  # local t and not account for scr refresh
                BlankTest.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(BlankTest, 'tStartRefresh')  # time at next scr refresh
                BlankTest.setAutoDraw(True)
            if BlankTest.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > BlankTest.tStartRefresh + 0.5-frameTolerance:
                    # keep track of stop time/frame for later
                    BlankTest.tStop = t  # not accounting for scr refresh
                    BlankTest.frameNStop = frameN  # exact frame index
                    win.timeOnFlip(BlankTest, 'tStopRefresh')  # time at next scr refresh
                    BlankTest.setAutoDraw(False)
            
            # check for quit (typically the Esc key)
            if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
                core.quit()
            
            # check if all components have finished
            if not continueRoutine:  # a component has requested a forced-end of Routine
                break
            continueRoutine = False  # will revert to True if at least one component still running
            for thisComponent in Blank500Components:
                if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                    continueRoutine = True
                    break  # at least one component has not yet finished
            
            # refresh the screen
            if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                win.flip()
        
        # -------Ending Routine "Blank500"-------
        for thisComponent in Blank500Components:
            if hasattr(thisComponent, "setAutoDraw"):
                thisComponent.setAutoDraw(False)
        AS_Loop.addData('BlankTest.started', BlankTest.tStartRefresh)
        AS_Loop.addData('BlankTest.stopped', BlankTest.tStopRefresh)
        thisExp.nextEntry()
        
    # completed AS_rep repeats of 'AS_Loop'
    
    
    # set up handler to look after randomisation of conditions etc
    BS_Loop = data.TrialHandler(nReps=BS_rep, method='random', 
        extraInfo=expInfo, originPath=-1,
        trialList=data.importConditions(BScondition),
        seed=None, name='BS_Loop')
    thisExp.addLoop(BS_Loop)  # add the loop to the experiment
    thisBS_Loop = BS_Loop.trialList[0]  # so we can initialise stimuli with some values
    # abbreviate parameter names if possible (e.g. rgb = thisBS_Loop.rgb)
    if thisBS_Loop != None:
        for paramName in thisBS_Loop:
            exec('{} = thisBS_Loop[paramName]'.format(paramName))
    
    for thisBS_Loop in BS_Loop:
        currentLoop = BS_Loop
        # abbreviate parameter names if possible (e.g. rgb = thisBS_Loop.rgb)
        if thisBS_Loop != None:
            for paramName in thisBS_Loop:
                exec('{} = thisBS_Loop[paramName]'.format(paramName))
        
        # ------Prepare to start Routine "BlackS"-------
        continueRoutine = True
        # update component parameters for each repeat
        BS_image_1.setImage(Upper_Image)
        BS_image_2.setImage(Lower_Image)
        # setup some python lists for storing info about the BSMouse
        BSMouse.clicked_name = []
        BSMouse.clicked_pos = []
        gotValidClick = False  # until a click is received
        # keep track of which components have finished
        BlackSComponents = [Fixation5, BS_image_1, BS_image_2, BSMouse]
        for thisComponent in BlackSComponents:
            thisComponent.tStart = None
            thisComponent.tStop = None
            thisComponent.tStartRefresh = None
            thisComponent.tStopRefresh = None
            if hasattr(thisComponent, 'status'):
                thisComponent.status = NOT_STARTED
        # reset timers
        t = 0
        _timeToFirstFrame = win.getFutureFlipTime(clock="now")
        BlackSClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
        frameN = -1
        
        # -------Run Routine "BlackS"-------
        while continueRoutine:
            # get current time
            t = BlackSClock.getTime()
            tThisFlip = win.getFutureFlipTime(clock=BlackSClock)
            tThisFlipGlobal = win.getFutureFlipTime(clock=None)
            frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
            # update/draw components on each frame
            
            # *Fixation5* updates
            if Fixation5.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                Fixation5.frameNStart = frameN  # exact frame index
                Fixation5.tStart = t  # local t and not account for scr refresh
                Fixation5.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(Fixation5, 'tStartRefresh')  # time at next scr refresh
                Fixation5.setAutoDraw(True)
            if Fixation5.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > Fixation5.tStartRefresh + 0.5-frameTolerance:
                    # keep track of stop time/frame for later
                    Fixation5.tStop = t  # not accounting for scr refresh
                    Fixation5.frameNStop = frameN  # exact frame index
                    win.timeOnFlip(Fixation5, 'tStopRefresh')  # time at next scr refresh
                    Fixation5.setAutoDraw(False)
            
            # *BS_image_1* updates
            if BS_image_1.status == NOT_STARTED and tThisFlip >= 0.5-frameTolerance:
                # keep track of start time/frame for later
                BS_image_1.frameNStart = frameN  # exact frame index
                BS_image_1.tStart = t  # local t and not account for scr refresh
                BS_image_1.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(BS_image_1, 'tStartRefresh')  # time at next scr refresh
                BS_image_1.setAutoDraw(True)
            if BS_image_1.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > BS_image_1.tStartRefresh + 3-frameTolerance:
                    # keep track of stop time/frame for later
                    BS_image_1.tStop = t  # not accounting for scr refresh
                    BS_image_1.frameNStop = frameN  # exact frame index
                    win.timeOnFlip(BS_image_1, 'tStopRefresh')  # time at next scr refresh
                    BS_image_1.setAutoDraw(False)
            
            # *BS_image_2* updates
            if BS_image_2.status == NOT_STARTED and tThisFlip >= 0.5-frameTolerance:
                # keep track of start time/frame for later
                BS_image_2.frameNStart = frameN  # exact frame index
                BS_image_2.tStart = t  # local t and not account for scr refresh
                BS_image_2.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(BS_image_2, 'tStartRefresh')  # time at next scr refresh
                BS_image_2.setAutoDraw(True)
            if BS_image_2.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > BS_image_2.tStartRefresh + 3-frameTolerance:
                    # keep track of stop time/frame for later
                    BS_image_2.tStop = t  # not accounting for scr refresh
                    BS_image_2.frameNStop = frameN  # exact frame index
                    win.timeOnFlip(BS_image_2, 'tStopRefresh')  # time at next scr refresh
                    BS_image_2.setAutoDraw(False)
            # *BSMouse* updates
            if BSMouse.status == NOT_STARTED and t >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                BSMouse.frameNStart = frameN  # exact frame index
                BSMouse.tStart = t  # local t and not account for scr refresh
                BSMouse.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(BSMouse, 'tStartRefresh')  # time at next scr refresh
                BSMouse.status = STARTED
                BSMouse.mouseClock.reset()
                prevButtonState = BSMouse.getPressed()  # if button is down already this ISN'T a new click
            if BSMouse.status == STARTED:  # only update if started and not finished!
                buttons = BSMouse.getPressed()
                if buttons != prevButtonState:  # button state changed?
                    prevButtonState = buttons
                    if sum(buttons) > 0:  # state changed to a new click
                        # check if the mouse was inside our 'clickable' objects
                        gotValidClick = False
                        for obj in [BS_image_1,BS_image_2]:
                            if obj.contains(BSMouse):
                                gotValidClick = True
                                BSMouse.clicked_name.append(obj.name)
                                BSMouse.clicked_pos.append(obj.pos)
                        if gotValidClick:  # abort routine on response
                            continueRoutine = False
            
            # check for quit (typically the Esc key)
            if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
                core.quit()
            
            # check if all components have finished
            if not continueRoutine:  # a component has requested a forced-end of Routine
                break
            continueRoutine = False  # will revert to True if at least one component still running
            for thisComponent in BlackSComponents:
                if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                    continueRoutine = True
                    break  # at least one component has not yet finished
            
            # refresh the screen
            if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                win.flip()
        
        # -------Ending Routine "BlackS"-------
        for thisComponent in BlackSComponents:
            if hasattr(thisComponent, "setAutoDraw"):
                thisComponent.setAutoDraw(False)
        BS_Loop.addData('Fixation5.started', Fixation5.tStartRefresh)
        BS_Loop.addData('Fixation5.stopped', Fixation5.tStopRefresh)
        BS_Loop.addData('BS_image_1.started', BS_image_1.tStartRefresh)
        BS_Loop.addData('BS_image_1.stopped', BS_image_1.tStopRefresh)
        BS_Loop.addData('BS_image_2.started', BS_image_2.tStartRefresh)
        BS_Loop.addData('BS_image_2.stopped', BS_image_2.tStopRefresh)
        # store data for BS_Loop (TrialHandler)
        x, y = BSMouse.getPos()
        buttons = BSMouse.getPressed()
        if sum(buttons):
            # check if the mouse was inside our 'clickable' objects
            gotValidClick = False
            for obj in [BS_image_1,BS_image_2]:
                if obj.contains(BSMouse):
                    gotValidClick = True
                    BSMouse.clicked_name.append(obj.name)
                    BSMouse.clicked_pos.append(obj.pos)
        BS_Loop.addData('BSMouse.x', x)
        BS_Loop.addData('BSMouse.y', y)
        BS_Loop.addData('BSMouse.leftButton', buttons[0])
        BS_Loop.addData('BSMouse.midButton', buttons[1])
        BS_Loop.addData('BSMouse.rightButton', buttons[2])
        if len(BSMouse.clicked_name):
            BS_Loop.addData('BSMouse.clicked_name', BSMouse.clicked_name[0])
        if len(BSMouse.clicked_pos):
            BS_Loop.addData('BSMouse.clicked_pos', BSMouse.clicked_pos[0])
        BS_Loop.addData('BSMouse.started', BSMouse.tStart)
        BS_Loop.addData('BSMouse.stopped', BSMouse.tStop)
        # the Routine "BlackS" was not non-slip safe, so reset the non-slip timer
        routineTimer.reset()
        
        # ------Prepare to start Routine "Blank500"-------
        continueRoutine = True
        routineTimer.add(0.500000)
        # update component parameters for each repeat
        # keep track of which components have finished
        Blank500Components = [BlankTest]
        for thisComponent in Blank500Components:
            thisComponent.tStart = None
            thisComponent.tStop = None
            thisComponent.tStartRefresh = None
            thisComponent.tStopRefresh = None
            if hasattr(thisComponent, 'status'):
                thisComponent.status = NOT_STARTED
        # reset timers
        t = 0
        _timeToFirstFrame = win.getFutureFlipTime(clock="now")
        Blank500Clock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
        frameN = -1
        
        # -------Run Routine "Blank500"-------
        while continueRoutine and routineTimer.getTime() > 0:
            # get current time
            t = Blank500Clock.getTime()
            tThisFlip = win.getFutureFlipTime(clock=Blank500Clock)
            tThisFlipGlobal = win.getFutureFlipTime(clock=None)
            frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
            # update/draw components on each frame
            
            # *BlankTest* updates
            if BlankTest.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                BlankTest.frameNStart = frameN  # exact frame index
                BlankTest.tStart = t  # local t and not account for scr refresh
                BlankTest.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(BlankTest, 'tStartRefresh')  # time at next scr refresh
                BlankTest.setAutoDraw(True)
            if BlankTest.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > BlankTest.tStartRefresh + 0.5-frameTolerance:
                    # keep track of stop time/frame for later
                    BlankTest.tStop = t  # not accounting for scr refresh
                    BlankTest.frameNStop = frameN  # exact frame index
                    win.timeOnFlip(BlankTest, 'tStopRefresh')  # time at next scr refresh
                    BlankTest.setAutoDraw(False)
            
            # check for quit (typically the Esc key)
            if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
                core.quit()
            
            # check if all components have finished
            if not continueRoutine:  # a component has requested a forced-end of Routine
                break
            continueRoutine = False  # will revert to True if at least one component still running
            for thisComponent in Blank500Components:
                if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                    continueRoutine = True
                    break  # at least one component has not yet finished
            
            # refresh the screen
            if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                win.flip()
        
        # -------Ending Routine "Blank500"-------
        for thisComponent in Blank500Components:
            if hasattr(thisComponent, "setAutoDraw"):
                thisComponent.setAutoDraw(False)
        BS_Loop.addData('BlankTest.started', BlankTest.tStartRefresh)
        BS_Loop.addData('BlankTest.stopped', BlankTest.tStopRefresh)
        thisExp.nextEntry()
        
    # completed BS_rep repeats of 'BS_Loop'
    
    
    # set up handler to look after randomisation of conditions etc
    BD_Loop = data.TrialHandler(nReps=BD_rep, method='random', 
        extraInfo=expInfo, originPath=-1,
        trialList=data.importConditions(BDcondition),
        seed=None, name='BD_Loop')
    thisExp.addLoop(BD_Loop)  # add the loop to the experiment
    thisBD_Loop = BD_Loop.trialList[0]  # so we can initialise stimuli with some values
    # abbreviate parameter names if possible (e.g. rgb = thisBD_Loop.rgb)
    if thisBD_Loop != None:
        for paramName in thisBD_Loop:
            exec('{} = thisBD_Loop[paramName]'.format(paramName))
    
    for thisBD_Loop in BD_Loop:
        currentLoop = BD_Loop
        # abbreviate parameter names if possible (e.g. rgb = thisBD_Loop.rgb)
        if thisBD_Loop != None:
            for paramName in thisBD_Loop:
                exec('{} = thisBD_Loop[paramName]'.format(paramName))
        
        # ------Prepare to start Routine "BlackD"-------
        continueRoutine = True
        # update component parameters for each repeat
        BD_image_1.setImage(Upper_Image)
        BD_image_2.setImage(Lower_Image)
        # setup some python lists for storing info about the BDmouse
        BDmouse.clicked_name = []
        BDmouse.clicked_pos = []
        gotValidClick = False  # until a click is received
        # keep track of which components have finished
        BlackDComponents = [Fixation6, BD_image_1, BD_image_2, BDmouse]
        for thisComponent in BlackDComponents:
            thisComponent.tStart = None
            thisComponent.tStop = None
            thisComponent.tStartRefresh = None
            thisComponent.tStopRefresh = None
            if hasattr(thisComponent, 'status'):
                thisComponent.status = NOT_STARTED
        # reset timers
        t = 0
        _timeToFirstFrame = win.getFutureFlipTime(clock="now")
        BlackDClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
        frameN = -1
        
        # -------Run Routine "BlackD"-------
        while continueRoutine:
            # get current time
            t = BlackDClock.getTime()
            tThisFlip = win.getFutureFlipTime(clock=BlackDClock)
            tThisFlipGlobal = win.getFutureFlipTime(clock=None)
            frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
            # update/draw components on each frame
            
            # *Fixation6* updates
            if Fixation6.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                Fixation6.frameNStart = frameN  # exact frame index
                Fixation6.tStart = t  # local t and not account for scr refresh
                Fixation6.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(Fixation6, 'tStartRefresh')  # time at next scr refresh
                Fixation6.setAutoDraw(True)
            if Fixation6.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > Fixation6.tStartRefresh + 0.5-frameTolerance:
                    # keep track of stop time/frame for later
                    Fixation6.tStop = t  # not accounting for scr refresh
                    Fixation6.frameNStop = frameN  # exact frame index
                    win.timeOnFlip(Fixation6, 'tStopRefresh')  # time at next scr refresh
                    Fixation6.setAutoDraw(False)
            
            # *BD_image_1* updates
            if BD_image_1.status == NOT_STARTED and tThisFlip >= 0.5-frameTolerance:
                # keep track of start time/frame for later
                BD_image_1.frameNStart = frameN  # exact frame index
                BD_image_1.tStart = t  # local t and not account for scr refresh
                BD_image_1.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(BD_image_1, 'tStartRefresh')  # time at next scr refresh
                BD_image_1.setAutoDraw(True)
            if BD_image_1.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > BD_image_1.tStartRefresh + 3-frameTolerance:
                    # keep track of stop time/frame for later
                    BD_image_1.tStop = t  # not accounting for scr refresh
                    BD_image_1.frameNStop = frameN  # exact frame index
                    win.timeOnFlip(BD_image_1, 'tStopRefresh')  # time at next scr refresh
                    BD_image_1.setAutoDraw(False)
            
            # *BD_image_2* updates
            if BD_image_2.status == NOT_STARTED and tThisFlip >= 0.5-frameTolerance:
                # keep track of start time/frame for later
                BD_image_2.frameNStart = frameN  # exact frame index
                BD_image_2.tStart = t  # local t and not account for scr refresh
                BD_image_2.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(BD_image_2, 'tStartRefresh')  # time at next scr refresh
                BD_image_2.setAutoDraw(True)
            if BD_image_2.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > BD_image_2.tStartRefresh + 3-frameTolerance:
                    # keep track of stop time/frame for later
                    BD_image_2.tStop = t  # not accounting for scr refresh
                    BD_image_2.frameNStop = frameN  # exact frame index
                    win.timeOnFlip(BD_image_2, 'tStopRefresh')  # time at next scr refresh
                    BD_image_2.setAutoDraw(False)
            # *BDmouse* updates
            if BDmouse.status == NOT_STARTED and t >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                BDmouse.frameNStart = frameN  # exact frame index
                BDmouse.tStart = t  # local t and not account for scr refresh
                BDmouse.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(BDmouse, 'tStartRefresh')  # time at next scr refresh
                BDmouse.status = STARTED
                BDmouse.mouseClock.reset()
                prevButtonState = BDmouse.getPressed()  # if button is down already this ISN'T a new click
            if BDmouse.status == STARTED:  # only update if started and not finished!
                buttons = BDmouse.getPressed()
                if buttons != prevButtonState:  # button state changed?
                    prevButtonState = buttons
                    if sum(buttons) > 0:  # state changed to a new click
                        # check if the mouse was inside our 'clickable' objects
                        gotValidClick = False
                        for obj in [BD_image_1,BD_image_2]:
                            if obj.contains(BDmouse):
                                gotValidClick = True
                                BDmouse.clicked_name.append(obj.name)
                                BDmouse.clicked_pos.append(obj.pos)
                        if gotValidClick:  # abort routine on response
                            continueRoutine = False
            
            # check for quit (typically the Esc key)
            if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
                core.quit()
            
            # check if all components have finished
            if not continueRoutine:  # a component has requested a forced-end of Routine
                break
            continueRoutine = False  # will revert to True if at least one component still running
            for thisComponent in BlackDComponents:
                if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                    continueRoutine = True
                    break  # at least one component has not yet finished
            
            # refresh the screen
            if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                win.flip()
        
        # -------Ending Routine "BlackD"-------
        for thisComponent in BlackDComponents:
            if hasattr(thisComponent, "setAutoDraw"):
                thisComponent.setAutoDraw(False)
        BD_Loop.addData('Fixation6.started', Fixation6.tStartRefresh)
        BD_Loop.addData('Fixation6.stopped', Fixation6.tStopRefresh)
        BD_Loop.addData('BD_image_1.started', BD_image_1.tStartRefresh)
        BD_Loop.addData('BD_image_1.stopped', BD_image_1.tStopRefresh)
        BD_Loop.addData('BD_image_2.started', BD_image_2.tStartRefresh)
        BD_Loop.addData('BD_image_2.stopped', BD_image_2.tStopRefresh)
        # store data for BD_Loop (TrialHandler)
        x, y = BDmouse.getPos()
        buttons = BDmouse.getPressed()
        if sum(buttons):
            # check if the mouse was inside our 'clickable' objects
            gotValidClick = False
            for obj in [BD_image_1,BD_image_2]:
                if obj.contains(BDmouse):
                    gotValidClick = True
                    BDmouse.clicked_name.append(obj.name)
                    BDmouse.clicked_pos.append(obj.pos)
        BD_Loop.addData('BDmouse.x', x)
        BD_Loop.addData('BDmouse.y', y)
        BD_Loop.addData('BDmouse.leftButton', buttons[0])
        BD_Loop.addData('BDmouse.midButton', buttons[1])
        BD_Loop.addData('BDmouse.rightButton', buttons[2])
        if len(BDmouse.clicked_name):
            BD_Loop.addData('BDmouse.clicked_name', BDmouse.clicked_name[0])
        if len(BDmouse.clicked_pos):
            BD_Loop.addData('BDmouse.clicked_pos', BDmouse.clicked_pos[0])
        BD_Loop.addData('BDmouse.started', BDmouse.tStart)
        BD_Loop.addData('BDmouse.stopped', BDmouse.tStop)
        # the Routine "BlackD" was not non-slip safe, so reset the non-slip timer
        routineTimer.reset()
        
        # ------Prepare to start Routine "Blank500"-------
        continueRoutine = True
        routineTimer.add(0.500000)
        # update component parameters for each repeat
        # keep track of which components have finished
        Blank500Components = [BlankTest]
        for thisComponent in Blank500Components:
            thisComponent.tStart = None
            thisComponent.tStop = None
            thisComponent.tStartRefresh = None
            thisComponent.tStopRefresh = None
            if hasattr(thisComponent, 'status'):
                thisComponent.status = NOT_STARTED
        # reset timers
        t = 0
        _timeToFirstFrame = win.getFutureFlipTime(clock="now")
        Blank500Clock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
        frameN = -1
        
        # -------Run Routine "Blank500"-------
        while continueRoutine and routineTimer.getTime() > 0:
            # get current time
            t = Blank500Clock.getTime()
            tThisFlip = win.getFutureFlipTime(clock=Blank500Clock)
            tThisFlipGlobal = win.getFutureFlipTime(clock=None)
            frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
            # update/draw components on each frame
            
            # *BlankTest* updates
            if BlankTest.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                BlankTest.frameNStart = frameN  # exact frame index
                BlankTest.tStart = t  # local t and not account for scr refresh
                BlankTest.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(BlankTest, 'tStartRefresh')  # time at next scr refresh
                BlankTest.setAutoDraw(True)
            if BlankTest.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > BlankTest.tStartRefresh + 0.5-frameTolerance:
                    # keep track of stop time/frame for later
                    BlankTest.tStop = t  # not accounting for scr refresh
                    BlankTest.frameNStop = frameN  # exact frame index
                    win.timeOnFlip(BlankTest, 'tStopRefresh')  # time at next scr refresh
                    BlankTest.setAutoDraw(False)
            
            # check for quit (typically the Esc key)
            if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
                core.quit()
            
            # check if all components have finished
            if not continueRoutine:  # a component has requested a forced-end of Routine
                break
            continueRoutine = False  # will revert to True if at least one component still running
            for thisComponent in Blank500Components:
                if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                    continueRoutine = True
                    break  # at least one component has not yet finished
            
            # refresh the screen
            if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                win.flip()
        
        # -------Ending Routine "Blank500"-------
        for thisComponent in Blank500Components:
            if hasattr(thisComponent, "setAutoDraw"):
                thisComponent.setAutoDraw(False)
        BD_Loop.addData('BlankTest.started', BlankTest.tStartRefresh)
        BD_Loop.addData('BlankTest.stopped', BlankTest.tStopRefresh)
        thisExp.nextEntry()
        
    # completed BD_rep repeats of 'BD_Loop'
    
    
    # set up handler to look after randomisation of conditions etc
    AD_Loop = data.TrialHandler(nReps=AD_rep, method='random', 
        extraInfo=expInfo, originPath=-1,
        trialList=data.importConditions(ADcondition),
        seed=None, name='AD_Loop')
    thisExp.addLoop(AD_Loop)  # add the loop to the experiment
    thisAD_Loop = AD_Loop.trialList[0]  # so we can initialise stimuli with some values
    # abbreviate parameter names if possible (e.g. rgb = thisAD_Loop.rgb)
    if thisAD_Loop != None:
        for paramName in thisAD_Loop:
            exec('{} = thisAD_Loop[paramName]'.format(paramName))
    
    for thisAD_Loop in AD_Loop:
        currentLoop = AD_Loop
        # abbreviate parameter names if possible (e.g. rgb = thisAD_Loop.rgb)
        if thisAD_Loop != None:
            for paramName in thisAD_Loop:
                exec('{} = thisAD_Loop[paramName]'.format(paramName))
        
        # ------Prepare to start Routine "AsianD"-------
        continueRoutine = True
        # update component parameters for each repeat
        AD_image_1.setImage(Upper_Image)
        AD_imgae_2.setImage(Lower_Image)
        # setup some python lists for storing info about the ADMouse
        ADMouse.clicked_name = []
        ADMouse.clicked_pos = []
        gotValidClick = False  # until a click is received
        # keep track of which components have finished
        AsianDComponents = [Fixation2, AD_image_1, AD_imgae_2, ADMouse]
        for thisComponent in AsianDComponents:
            thisComponent.tStart = None
            thisComponent.tStop = None
            thisComponent.tStartRefresh = None
            thisComponent.tStopRefresh = None
            if hasattr(thisComponent, 'status'):
                thisComponent.status = NOT_STARTED
        # reset timers
        t = 0
        _timeToFirstFrame = win.getFutureFlipTime(clock="now")
        AsianDClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
        frameN = -1
        
        # -------Run Routine "AsianD"-------
        while continueRoutine:
            # get current time
            t = AsianDClock.getTime()
            tThisFlip = win.getFutureFlipTime(clock=AsianDClock)
            tThisFlipGlobal = win.getFutureFlipTime(clock=None)
            frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
            # update/draw components on each frame
            
            # *Fixation2* updates
            if Fixation2.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                Fixation2.frameNStart = frameN  # exact frame index
                Fixation2.tStart = t  # local t and not account for scr refresh
                Fixation2.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(Fixation2, 'tStartRefresh')  # time at next scr refresh
                Fixation2.setAutoDraw(True)
            if Fixation2.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > Fixation2.tStartRefresh + 0.5-frameTolerance:
                    # keep track of stop time/frame for later
                    Fixation2.tStop = t  # not accounting for scr refresh
                    Fixation2.frameNStop = frameN  # exact frame index
                    win.timeOnFlip(Fixation2, 'tStopRefresh')  # time at next scr refresh
                    Fixation2.setAutoDraw(False)
            
            # *AD_image_1* updates
            if AD_image_1.status == NOT_STARTED and tThisFlip >= 0.5-frameTolerance:
                # keep track of start time/frame for later
                AD_image_1.frameNStart = frameN  # exact frame index
                AD_image_1.tStart = t  # local t and not account for scr refresh
                AD_image_1.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(AD_image_1, 'tStartRefresh')  # time at next scr refresh
                AD_image_1.setAutoDraw(True)
            if AD_image_1.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > AD_image_1.tStartRefresh + 3-frameTolerance:
                    # keep track of stop time/frame for later
                    AD_image_1.tStop = t  # not accounting for scr refresh
                    AD_image_1.frameNStop = frameN  # exact frame index
                    win.timeOnFlip(AD_image_1, 'tStopRefresh')  # time at next scr refresh
                    AD_image_1.setAutoDraw(False)
            
            # *AD_imgae_2* updates
            if AD_imgae_2.status == NOT_STARTED and tThisFlip >= 0.5-frameTolerance:
                # keep track of start time/frame for later
                AD_imgae_2.frameNStart = frameN  # exact frame index
                AD_imgae_2.tStart = t  # local t and not account for scr refresh
                AD_imgae_2.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(AD_imgae_2, 'tStartRefresh')  # time at next scr refresh
                AD_imgae_2.setAutoDraw(True)
            if AD_imgae_2.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > AD_imgae_2.tStartRefresh + 3-frameTolerance:
                    # keep track of stop time/frame for later
                    AD_imgae_2.tStop = t  # not accounting for scr refresh
                    AD_imgae_2.frameNStop = frameN  # exact frame index
                    win.timeOnFlip(AD_imgae_2, 'tStopRefresh')  # time at next scr refresh
                    AD_imgae_2.setAutoDraw(False)
            # *ADMouse* updates
            if ADMouse.status == NOT_STARTED and t >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                ADMouse.frameNStart = frameN  # exact frame index
                ADMouse.tStart = t  # local t and not account for scr refresh
                ADMouse.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(ADMouse, 'tStartRefresh')  # time at next scr refresh
                ADMouse.status = STARTED
                ADMouse.mouseClock.reset()
                prevButtonState = ADMouse.getPressed()  # if button is down already this ISN'T a new click
            if ADMouse.status == STARTED:  # only update if started and not finished!
                buttons = ADMouse.getPressed()
                if buttons != prevButtonState:  # button state changed?
                    prevButtonState = buttons
                    if sum(buttons) > 0:  # state changed to a new click
                        # check if the mouse was inside our 'clickable' objects
                        gotValidClick = False
                        for obj in [AD_image_1,AD_imgae_2]:
                            if obj.contains(ADMouse):
                                gotValidClick = True
                                ADMouse.clicked_name.append(obj.name)
                                ADMouse.clicked_pos.append(obj.pos)
                        if gotValidClick:  # abort routine on response
                            continueRoutine = False
            
            # check for quit (typically the Esc key)
            if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
                core.quit()
            
            # check if all components have finished
            if not continueRoutine:  # a component has requested a forced-end of Routine
                break
            continueRoutine = False  # will revert to True if at least one component still running
            for thisComponent in AsianDComponents:
                if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                    continueRoutine = True
                    break  # at least one component has not yet finished
            
            # refresh the screen
            if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                win.flip()
        
        # -------Ending Routine "AsianD"-------
        for thisComponent in AsianDComponents:
            if hasattr(thisComponent, "setAutoDraw"):
                thisComponent.setAutoDraw(False)
        AD_Loop.addData('Fixation2.started', Fixation2.tStartRefresh)
        AD_Loop.addData('Fixation2.stopped', Fixation2.tStopRefresh)
        AD_Loop.addData('AD_image_1.started', AD_image_1.tStartRefresh)
        AD_Loop.addData('AD_image_1.stopped', AD_image_1.tStopRefresh)
        AD_Loop.addData('AD_imgae_2.started', AD_imgae_2.tStartRefresh)
        AD_Loop.addData('AD_imgae_2.stopped', AD_imgae_2.tStopRefresh)
        # store data for AD_Loop (TrialHandler)
        x, y = ADMouse.getPos()
        buttons = ADMouse.getPressed()
        if sum(buttons):
            # check if the mouse was inside our 'clickable' objects
            gotValidClick = False
            for obj in [AD_image_1,AD_imgae_2]:
                if obj.contains(ADMouse):
                    gotValidClick = True
                    ADMouse.clicked_name.append(obj.name)
                    ADMouse.clicked_pos.append(obj.pos)
        AD_Loop.addData('ADMouse.x', x)
        AD_Loop.addData('ADMouse.y', y)
        AD_Loop.addData('ADMouse.leftButton', buttons[0])
        AD_Loop.addData('ADMouse.midButton', buttons[1])
        AD_Loop.addData('ADMouse.rightButton', buttons[2])
        if len(ADMouse.clicked_name):
            AD_Loop.addData('ADMouse.clicked_name', ADMouse.clicked_name[0])
        if len(ADMouse.clicked_pos):
            AD_Loop.addData('ADMouse.clicked_pos', ADMouse.clicked_pos[0])
        AD_Loop.addData('ADMouse.started', ADMouse.tStart)
        AD_Loop.addData('ADMouse.stopped', ADMouse.tStop)
        # the Routine "AsianD" was not non-slip safe, so reset the non-slip timer
        routineTimer.reset()
        
        # ------Prepare to start Routine "Blank500"-------
        continueRoutine = True
        routineTimer.add(0.500000)
        # update component parameters for each repeat
        # keep track of which components have finished
        Blank500Components = [BlankTest]
        for thisComponent in Blank500Components:
            thisComponent.tStart = None
            thisComponent.tStop = None
            thisComponent.tStartRefresh = None
            thisComponent.tStopRefresh = None
            if hasattr(thisComponent, 'status'):
                thisComponent.status = NOT_STARTED
        # reset timers
        t = 0
        _timeToFirstFrame = win.getFutureFlipTime(clock="now")
        Blank500Clock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
        frameN = -1
        
        # -------Run Routine "Blank500"-------
        while continueRoutine and routineTimer.getTime() > 0:
            # get current time
            t = Blank500Clock.getTime()
            tThisFlip = win.getFutureFlipTime(clock=Blank500Clock)
            tThisFlipGlobal = win.getFutureFlipTime(clock=None)
            frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
            # update/draw components on each frame
            
            # *BlankTest* updates
            if BlankTest.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                BlankTest.frameNStart = frameN  # exact frame index
                BlankTest.tStart = t  # local t and not account for scr refresh
                BlankTest.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(BlankTest, 'tStartRefresh')  # time at next scr refresh
                BlankTest.setAutoDraw(True)
            if BlankTest.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > BlankTest.tStartRefresh + 0.5-frameTolerance:
                    # keep track of stop time/frame for later
                    BlankTest.tStop = t  # not accounting for scr refresh
                    BlankTest.frameNStop = frameN  # exact frame index
                    win.timeOnFlip(BlankTest, 'tStopRefresh')  # time at next scr refresh
                    BlankTest.setAutoDraw(False)
            
            # check for quit (typically the Esc key)
            if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
                core.quit()
            
            # check if all components have finished
            if not continueRoutine:  # a component has requested a forced-end of Routine
                break
            continueRoutine = False  # will revert to True if at least one component still running
            for thisComponent in Blank500Components:
                if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                    continueRoutine = True
                    break  # at least one component has not yet finished
            
            # refresh the screen
            if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                win.flip()
        
        # -------Ending Routine "Blank500"-------
        for thisComponent in Blank500Components:
            if hasattr(thisComponent, "setAutoDraw"):
                thisComponent.setAutoDraw(False)
        AD_Loop.addData('BlankTest.started', BlankTest.tStartRefresh)
        AD_Loop.addData('BlankTest.stopped', BlankTest.tStopRefresh)
        thisExp.nextEntry()
        
    # completed AD_rep repeats of 'AD_Loop'
    
    
    # set up handler to look after randomisation of conditions etc
    CS_Loop = data.TrialHandler(nReps=CS_rep, method='random', 
        extraInfo=expInfo, originPath=-1,
        trialList=data.importConditions(CScondition),
        seed=None, name='CS_Loop')
    thisExp.addLoop(CS_Loop)  # add the loop to the experiment
    thisCS_Loop = CS_Loop.trialList[0]  # so we can initialise stimuli with some values
    # abbreviate parameter names if possible (e.g. rgb = thisCS_Loop.rgb)
    if thisCS_Loop != None:
        for paramName in thisCS_Loop:
            exec('{} = thisCS_Loop[paramName]'.format(paramName))
    
    for thisCS_Loop in CS_Loop:
        currentLoop = CS_Loop
        # abbreviate parameter names if possible (e.g. rgb = thisCS_Loop.rgb)
        if thisCS_Loop != None:
            for paramName in thisCS_Loop:
                exec('{} = thisCS_Loop[paramName]'.format(paramName))
        
        # ------Prepare to start Routine "CaucasianS"-------
        continueRoutine = True
        # update component parameters for each repeat
        CS_image_1.setImage(Upper_Image)
        CS_image_2.setImage(Lower_Image)
        # setup some python lists for storing info about the CSMouse
        CSMouse.clicked_name = []
        CSMouse.clicked_pos = []
        gotValidClick = False  # until a click is received
        # keep track of which components have finished
        CaucasianSComponents = [Fixation3, CS_image_1, CS_image_2, CSMouse]
        for thisComponent in CaucasianSComponents:
            thisComponent.tStart = None
            thisComponent.tStop = None
            thisComponent.tStartRefresh = None
            thisComponent.tStopRefresh = None
            if hasattr(thisComponent, 'status'):
                thisComponent.status = NOT_STARTED
        # reset timers
        t = 0
        _timeToFirstFrame = win.getFutureFlipTime(clock="now")
        CaucasianSClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
        frameN = -1
        
        # -------Run Routine "CaucasianS"-------
        while continueRoutine:
            # get current time
            t = CaucasianSClock.getTime()
            tThisFlip = win.getFutureFlipTime(clock=CaucasianSClock)
            tThisFlipGlobal = win.getFutureFlipTime(clock=None)
            frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
            # update/draw components on each frame
            
            # *Fixation3* updates
            if Fixation3.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                Fixation3.frameNStart = frameN  # exact frame index
                Fixation3.tStart = t  # local t and not account for scr refresh
                Fixation3.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(Fixation3, 'tStartRefresh')  # time at next scr refresh
                Fixation3.setAutoDraw(True)
            if Fixation3.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > Fixation3.tStartRefresh + 0.5-frameTolerance:
                    # keep track of stop time/frame for later
                    Fixation3.tStop = t  # not accounting for scr refresh
                    Fixation3.frameNStop = frameN  # exact frame index
                    win.timeOnFlip(Fixation3, 'tStopRefresh')  # time at next scr refresh
                    Fixation3.setAutoDraw(False)
            
            # *CS_image_1* updates
            if CS_image_1.status == NOT_STARTED and tThisFlip >= 0.5-frameTolerance:
                # keep track of start time/frame for later
                CS_image_1.frameNStart = frameN  # exact frame index
                CS_image_1.tStart = t  # local t and not account for scr refresh
                CS_image_1.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(CS_image_1, 'tStartRefresh')  # time at next scr refresh
                CS_image_1.setAutoDraw(True)
            if CS_image_1.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > CS_image_1.tStartRefresh + 3-frameTolerance:
                    # keep track of stop time/frame for later
                    CS_image_1.tStop = t  # not accounting for scr refresh
                    CS_image_1.frameNStop = frameN  # exact frame index
                    win.timeOnFlip(CS_image_1, 'tStopRefresh')  # time at next scr refresh
                    CS_image_1.setAutoDraw(False)
            
            # *CS_image_2* updates
            if CS_image_2.status == NOT_STARTED and tThisFlip >= 0.5-frameTolerance:
                # keep track of start time/frame for later
                CS_image_2.frameNStart = frameN  # exact frame index
                CS_image_2.tStart = t  # local t and not account for scr refresh
                CS_image_2.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(CS_image_2, 'tStartRefresh')  # time at next scr refresh
                CS_image_2.setAutoDraw(True)
            if CS_image_2.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > CS_image_2.tStartRefresh + 3-frameTolerance:
                    # keep track of stop time/frame for later
                    CS_image_2.tStop = t  # not accounting for scr refresh
                    CS_image_2.frameNStop = frameN  # exact frame index
                    win.timeOnFlip(CS_image_2, 'tStopRefresh')  # time at next scr refresh
                    CS_image_2.setAutoDraw(False)
            # *CSMouse* updates
            if CSMouse.status == NOT_STARTED and t >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                CSMouse.frameNStart = frameN  # exact frame index
                CSMouse.tStart = t  # local t and not account for scr refresh
                CSMouse.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(CSMouse, 'tStartRefresh')  # time at next scr refresh
                CSMouse.status = STARTED
                CSMouse.mouseClock.reset()
                prevButtonState = CSMouse.getPressed()  # if button is down already this ISN'T a new click
            if CSMouse.status == STARTED:  # only update if started and not finished!
                buttons = CSMouse.getPressed()
                if buttons != prevButtonState:  # button state changed?
                    prevButtonState = buttons
                    if sum(buttons) > 0:  # state changed to a new click
                        # check if the mouse was inside our 'clickable' objects
                        gotValidClick = False
                        for obj in [CS_image_1,CS_image_2]:
                            if obj.contains(CSMouse):
                                gotValidClick = True
                                CSMouse.clicked_name.append(obj.name)
                                CSMouse.clicked_pos.append(obj.pos)
                        if gotValidClick:  # abort routine on response
                            continueRoutine = False
            
            # check for quit (typically the Esc key)
            if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
                core.quit()
            
            # check if all components have finished
            if not continueRoutine:  # a component has requested a forced-end of Routine
                break
            continueRoutine = False  # will revert to True if at least one component still running
            for thisComponent in CaucasianSComponents:
                if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                    continueRoutine = True
                    break  # at least one component has not yet finished
            
            # refresh the screen
            if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                win.flip()
        
        # -------Ending Routine "CaucasianS"-------
        for thisComponent in CaucasianSComponents:
            if hasattr(thisComponent, "setAutoDraw"):
                thisComponent.setAutoDraw(False)
        CS_Loop.addData('Fixation3.started', Fixation3.tStartRefresh)
        CS_Loop.addData('Fixation3.stopped', Fixation3.tStopRefresh)
        CS_Loop.addData('CS_image_1.started', CS_image_1.tStartRefresh)
        CS_Loop.addData('CS_image_1.stopped', CS_image_1.tStopRefresh)
        CS_Loop.addData('CS_image_2.started', CS_image_2.tStartRefresh)
        CS_Loop.addData('CS_image_2.stopped', CS_image_2.tStopRefresh)
        # store data for CS_Loop (TrialHandler)
        x, y = CSMouse.getPos()
        buttons = CSMouse.getPressed()
        if sum(buttons):
            # check if the mouse was inside our 'clickable' objects
            gotValidClick = False
            for obj in [CS_image_1,CS_image_2]:
                if obj.contains(CSMouse):
                    gotValidClick = True
                    CSMouse.clicked_name.append(obj.name)
                    CSMouse.clicked_pos.append(obj.pos)
        CS_Loop.addData('CSMouse.x', x)
        CS_Loop.addData('CSMouse.y', y)
        CS_Loop.addData('CSMouse.leftButton', buttons[0])
        CS_Loop.addData('CSMouse.midButton', buttons[1])
        CS_Loop.addData('CSMouse.rightButton', buttons[2])
        if len(CSMouse.clicked_name):
            CS_Loop.addData('CSMouse.clicked_name', CSMouse.clicked_name[0])
        if len(CSMouse.clicked_pos):
            CS_Loop.addData('CSMouse.clicked_pos', CSMouse.clicked_pos[0])
        CS_Loop.addData('CSMouse.started', CSMouse.tStart)
        CS_Loop.addData('CSMouse.stopped', CSMouse.tStop)
        # the Routine "CaucasianS" was not non-slip safe, so reset the non-slip timer
        routineTimer.reset()
        
        # ------Prepare to start Routine "Blank500"-------
        continueRoutine = True
        routineTimer.add(0.500000)
        # update component parameters for each repeat
        # keep track of which components have finished
        Blank500Components = [BlankTest]
        for thisComponent in Blank500Components:
            thisComponent.tStart = None
            thisComponent.tStop = None
            thisComponent.tStartRefresh = None
            thisComponent.tStopRefresh = None
            if hasattr(thisComponent, 'status'):
                thisComponent.status = NOT_STARTED
        # reset timers
        t = 0
        _timeToFirstFrame = win.getFutureFlipTime(clock="now")
        Blank500Clock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
        frameN = -1
        
        # -------Run Routine "Blank500"-------
        while continueRoutine and routineTimer.getTime() > 0:
            # get current time
            t = Blank500Clock.getTime()
            tThisFlip = win.getFutureFlipTime(clock=Blank500Clock)
            tThisFlipGlobal = win.getFutureFlipTime(clock=None)
            frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
            # update/draw components on each frame
            
            # *BlankTest* updates
            if BlankTest.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                BlankTest.frameNStart = frameN  # exact frame index
                BlankTest.tStart = t  # local t and not account for scr refresh
                BlankTest.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(BlankTest, 'tStartRefresh')  # time at next scr refresh
                BlankTest.setAutoDraw(True)
            if BlankTest.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > BlankTest.tStartRefresh + 0.5-frameTolerance:
                    # keep track of stop time/frame for later
                    BlankTest.tStop = t  # not accounting for scr refresh
                    BlankTest.frameNStop = frameN  # exact frame index
                    win.timeOnFlip(BlankTest, 'tStopRefresh')  # time at next scr refresh
                    BlankTest.setAutoDraw(False)
            
            # check for quit (typically the Esc key)
            if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
                core.quit()
            
            # check if all components have finished
            if not continueRoutine:  # a component has requested a forced-end of Routine
                break
            continueRoutine = False  # will revert to True if at least one component still running
            for thisComponent in Blank500Components:
                if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                    continueRoutine = True
                    break  # at least one component has not yet finished
            
            # refresh the screen
            if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                win.flip()
        
        # -------Ending Routine "Blank500"-------
        for thisComponent in Blank500Components:
            if hasattr(thisComponent, "setAutoDraw"):
                thisComponent.setAutoDraw(False)
        CS_Loop.addData('BlankTest.started', BlankTest.tStartRefresh)
        CS_Loop.addData('BlankTest.stopped', BlankTest.tStopRefresh)
        thisExp.nextEntry()
        
    # completed CS_rep repeats of 'CS_Loop'
    
    
    # set up handler to look after randomisation of conditions etc
    CD_Loop = data.TrialHandler(nReps=CD_rep, method='random', 
        extraInfo=expInfo, originPath=-1,
        trialList=data.importConditions(CDcondition),
        seed=None, name='CD_Loop')
    thisExp.addLoop(CD_Loop)  # add the loop to the experiment
    thisCD_Loop = CD_Loop.trialList[0]  # so we can initialise stimuli with some values
    # abbreviate parameter names if possible (e.g. rgb = thisCD_Loop.rgb)
    if thisCD_Loop != None:
        for paramName in thisCD_Loop:
            exec('{} = thisCD_Loop[paramName]'.format(paramName))
    
    for thisCD_Loop in CD_Loop:
        currentLoop = CD_Loop
        # abbreviate parameter names if possible (e.g. rgb = thisCD_Loop.rgb)
        if thisCD_Loop != None:
            for paramName in thisCD_Loop:
                exec('{} = thisCD_Loop[paramName]'.format(paramName))
        
        # ------Prepare to start Routine "CaucasianD"-------
        continueRoutine = True
        # update component parameters for each repeat
        CD_image_1.setImage(Upper_Image)
        CD_image_2.setImage(Lower_Image)
        # setup some python lists for storing info about the CDMouse
        CDMouse.clicked_name = []
        CDMouse.clicked_pos = []
        gotValidClick = False  # until a click is received
        # keep track of which components have finished
        CaucasianDComponents = [Fixation4, CD_image_1, CD_image_2, CDMouse]
        for thisComponent in CaucasianDComponents:
            thisComponent.tStart = None
            thisComponent.tStop = None
            thisComponent.tStartRefresh = None
            thisComponent.tStopRefresh = None
            if hasattr(thisComponent, 'status'):
                thisComponent.status = NOT_STARTED
        # reset timers
        t = 0
        _timeToFirstFrame = win.getFutureFlipTime(clock="now")
        CaucasianDClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
        frameN = -1
        
        # -------Run Routine "CaucasianD"-------
        while continueRoutine:
            # get current time
            t = CaucasianDClock.getTime()
            tThisFlip = win.getFutureFlipTime(clock=CaucasianDClock)
            tThisFlipGlobal = win.getFutureFlipTime(clock=None)
            frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
            # update/draw components on each frame
            
            # *Fixation4* updates
            if Fixation4.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                Fixation4.frameNStart = frameN  # exact frame index
                Fixation4.tStart = t  # local t and not account for scr refresh
                Fixation4.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(Fixation4, 'tStartRefresh')  # time at next scr refresh
                Fixation4.setAutoDraw(True)
            if Fixation4.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > Fixation4.tStartRefresh + 0.5-frameTolerance:
                    # keep track of stop time/frame for later
                    Fixation4.tStop = t  # not accounting for scr refresh
                    Fixation4.frameNStop = frameN  # exact frame index
                    win.timeOnFlip(Fixation4, 'tStopRefresh')  # time at next scr refresh
                    Fixation4.setAutoDraw(False)
            
            # *CD_image_1* updates
            if CD_image_1.status == NOT_STARTED and tThisFlip >= 0.5-frameTolerance:
                # keep track of start time/frame for later
                CD_image_1.frameNStart = frameN  # exact frame index
                CD_image_1.tStart = t  # local t and not account for scr refresh
                CD_image_1.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(CD_image_1, 'tStartRefresh')  # time at next scr refresh
                CD_image_1.setAutoDraw(True)
            if CD_image_1.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > CD_image_1.tStartRefresh + 3-frameTolerance:
                    # keep track of stop time/frame for later
                    CD_image_1.tStop = t  # not accounting for scr refresh
                    CD_image_1.frameNStop = frameN  # exact frame index
                    win.timeOnFlip(CD_image_1, 'tStopRefresh')  # time at next scr refresh
                    CD_image_1.setAutoDraw(False)
            
            # *CD_image_2* updates
            if CD_image_2.status == NOT_STARTED and tThisFlip >= 0.5-frameTolerance:
                # keep track of start time/frame for later
                CD_image_2.frameNStart = frameN  # exact frame index
                CD_image_2.tStart = t  # local t and not account for scr refresh
                CD_image_2.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(CD_image_2, 'tStartRefresh')  # time at next scr refresh
                CD_image_2.setAutoDraw(True)
            if CD_image_2.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > CD_image_2.tStartRefresh + 3-frameTolerance:
                    # keep track of stop time/frame for later
                    CD_image_2.tStop = t  # not accounting for scr refresh
                    CD_image_2.frameNStop = frameN  # exact frame index
                    win.timeOnFlip(CD_image_2, 'tStopRefresh')  # time at next scr refresh
                    CD_image_2.setAutoDraw(False)
            # *CDMouse* updates
            if CDMouse.status == NOT_STARTED and t >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                CDMouse.frameNStart = frameN  # exact frame index
                CDMouse.tStart = t  # local t and not account for scr refresh
                CDMouse.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(CDMouse, 'tStartRefresh')  # time at next scr refresh
                CDMouse.status = STARTED
                CDMouse.mouseClock.reset()
                prevButtonState = CDMouse.getPressed()  # if button is down already this ISN'T a new click
            if CDMouse.status == STARTED:  # only update if started and not finished!
                buttons = CDMouse.getPressed()
                if buttons != prevButtonState:  # button state changed?
                    prevButtonState = buttons
                    if sum(buttons) > 0:  # state changed to a new click
                        # check if the mouse was inside our 'clickable' objects
                        gotValidClick = False
                        for obj in [CD_image_1,CD_image_2]:
                            if obj.contains(CDMouse):
                                gotValidClick = True
                                CDMouse.clicked_name.append(obj.name)
                                CDMouse.clicked_pos.append(obj.pos)
                        if gotValidClick:  # abort routine on response
                            continueRoutine = False
            
            # check for quit (typically the Esc key)
            if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
                core.quit()
            
            # check if all components have finished
            if not continueRoutine:  # a component has requested a forced-end of Routine
                break
            continueRoutine = False  # will revert to True if at least one component still running
            for thisComponent in CaucasianDComponents:
                if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                    continueRoutine = True
                    break  # at least one component has not yet finished
            
            # refresh the screen
            if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                win.flip()
        
        # -------Ending Routine "CaucasianD"-------
        for thisComponent in CaucasianDComponents:
            if hasattr(thisComponent, "setAutoDraw"):
                thisComponent.setAutoDraw(False)
        CD_Loop.addData('Fixation4.started', Fixation4.tStartRefresh)
        CD_Loop.addData('Fixation4.stopped', Fixation4.tStopRefresh)
        CD_Loop.addData('CD_image_1.started', CD_image_1.tStartRefresh)
        CD_Loop.addData('CD_image_1.stopped', CD_image_1.tStopRefresh)
        CD_Loop.addData('CD_image_2.started', CD_image_2.tStartRefresh)
        CD_Loop.addData('CD_image_2.stopped', CD_image_2.tStopRefresh)
        # store data for CD_Loop (TrialHandler)
        x, y = CDMouse.getPos()
        buttons = CDMouse.getPressed()
        if sum(buttons):
            # check if the mouse was inside our 'clickable' objects
            gotValidClick = False
            for obj in [CD_image_1,CD_image_2]:
                if obj.contains(CDMouse):
                    gotValidClick = True
                    CDMouse.clicked_name.append(obj.name)
                    CDMouse.clicked_pos.append(obj.pos)
        CD_Loop.addData('CDMouse.x', x)
        CD_Loop.addData('CDMouse.y', y)
        CD_Loop.addData('CDMouse.leftButton', buttons[0])
        CD_Loop.addData('CDMouse.midButton', buttons[1])
        CD_Loop.addData('CDMouse.rightButton', buttons[2])
        if len(CDMouse.clicked_name):
            CD_Loop.addData('CDMouse.clicked_name', CDMouse.clicked_name[0])
        if len(CDMouse.clicked_pos):
            CD_Loop.addData('CDMouse.clicked_pos', CDMouse.clicked_pos[0])
        CD_Loop.addData('CDMouse.started', CDMouse.tStart)
        CD_Loop.addData('CDMouse.stopped', CDMouse.tStop)
        # the Routine "CaucasianD" was not non-slip safe, so reset the non-slip timer
        routineTimer.reset()
        
        # ------Prepare to start Routine "Blank500"-------
        continueRoutine = True
        routineTimer.add(0.500000)
        # update component parameters for each repeat
        # keep track of which components have finished
        Blank500Components = [BlankTest]
        for thisComponent in Blank500Components:
            thisComponent.tStart = None
            thisComponent.tStop = None
            thisComponent.tStartRefresh = None
            thisComponent.tStopRefresh = None
            if hasattr(thisComponent, 'status'):
                thisComponent.status = NOT_STARTED
        # reset timers
        t = 0
        _timeToFirstFrame = win.getFutureFlipTime(clock="now")
        Blank500Clock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
        frameN = -1
        
        # -------Run Routine "Blank500"-------
        while continueRoutine and routineTimer.getTime() > 0:
            # get current time
            t = Blank500Clock.getTime()
            tThisFlip = win.getFutureFlipTime(clock=Blank500Clock)
            tThisFlipGlobal = win.getFutureFlipTime(clock=None)
            frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
            # update/draw components on each frame
            
            # *BlankTest* updates
            if BlankTest.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                BlankTest.frameNStart = frameN  # exact frame index
                BlankTest.tStart = t  # local t and not account for scr refresh
                BlankTest.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(BlankTest, 'tStartRefresh')  # time at next scr refresh
                BlankTest.setAutoDraw(True)
            if BlankTest.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > BlankTest.tStartRefresh + 0.5-frameTolerance:
                    # keep track of stop time/frame for later
                    BlankTest.tStop = t  # not accounting for scr refresh
                    BlankTest.frameNStop = frameN  # exact frame index
                    win.timeOnFlip(BlankTest, 'tStopRefresh')  # time at next scr refresh
                    BlankTest.setAutoDraw(False)
            
            # check for quit (typically the Esc key)
            if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
                core.quit()
            
            # check if all components have finished
            if not continueRoutine:  # a component has requested a forced-end of Routine
                break
            continueRoutine = False  # will revert to True if at least one component still running
            for thisComponent in Blank500Components:
                if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                    continueRoutine = True
                    break  # at least one component has not yet finished
            
            # refresh the screen
            if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                win.flip()
        
        # -------Ending Routine "Blank500"-------
        for thisComponent in Blank500Components:
            if hasattr(thisComponent, "setAutoDraw"):
                thisComponent.setAutoDraw(False)
        CD_Loop.addData('BlankTest.started', BlankTest.tStartRefresh)
        CD_Loop.addData('BlankTest.stopped', BlankTest.tStopRefresh)
        thisExp.nextEntry()
        
    # completed CD_rep repeats of 'CD_Loop'
    
    thisExp.nextEntry()
    
# completed 1 repeats of 'BlockTrail'


# ------Prepare to start Routine "End"-------
continueRoutine = True
routineTimer.add(3.000000)
# update component parameters for each repeat
# keep track of which components have finished
EndComponents = [text]
for thisComponent in EndComponents:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
EndClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
frameN = -1

# -------Run Routine "End"-------
while continueRoutine and routineTimer.getTime() > 0:
    # get current time
    t = EndClock.getTime()
    tThisFlip = win.getFutureFlipTime(clock=EndClock)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *text* updates
    if text.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        text.frameNStart = frameN  # exact frame index
        text.tStart = t  # local t and not account for scr refresh
        text.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(text, 'tStartRefresh')  # time at next scr refresh
        text.setAutoDraw(True)
    if text.status == STARTED:
        # is it time to stop? (based on global clock, using actual start)
        if tThisFlipGlobal > text.tStartRefresh + 3-frameTolerance:
            # keep track of stop time/frame for later
            text.tStop = t  # not accounting for scr refresh
            text.frameNStop = frameN  # exact frame index
            win.timeOnFlip(text, 'tStopRefresh')  # time at next scr refresh
            text.setAutoDraw(False)
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in EndComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "End"-------
for thisComponent in EndComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
thisExp.addData('text.started', text.tStartRefresh)
thisExp.addData('text.stopped', text.tStopRefresh)

# Flip one final time so any remaining win.callOnFlip() 
# and win.timeOnFlip() tasks get executed before quitting
win.flip()

# these shouldn't be strictly necessary (should auto-save)
thisExp.saveAsWideText(filename+'.csv')
thisExp.saveAsPickle(filename)
logging.flush()
# make sure everything is closed down
thisExp.abort()  # or data files will save again on exit
win.close()
core.quit()
