#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
This experiment was created using PsychoPy3 Experiment Builder (v2020.1.2),
    on Sat Jun 13 13:39:46 2020
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
expName = 'FatFace'  # from the Builder filename that created this script
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
    originPath='/Users/josephine/Documents/research/FatFaceIllusion/FatFaceprogram/Exp1/FatFace_exp1_lastrun.py',
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
    monitor='testMonitor', color='white', colorSpace='rgb',
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
    color='black', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=0.0);
InstrKey = keyboard.Keyboard()

# Initialize components for Routine "Practise"
PractiseClock = core.Clock()
Fixation0 = visual.ShapeStim(
    win=win, name='Fixation0', vertices='cross',
    size=(0.1, 0.1),
    ori=0, pos=(0, 0),
    lineWidth=1, lineColor='black', lineColorSpace='rgb',
    fillColor='black', fillColorSpace='rgb',
    opacity=1, depth=-1.0, interpolate=True)
Upper_image = visual.ImageStim(
    win=win,
    name='Upper_image', 
    image='sin', mask=None,
    ori=0, pos=(0, 0.16), size=None,
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=False, depth=-2.0)
Lower_image = visual.ImageStim(
    win=win,
    name='Lower_image', 
    image='sin', mask=None,
    ori=0, pos=(0, -0.16), size=None,
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=False, depth=-3.0)
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
    color='black', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=0.0);
Prac_Key = keyboard.Keyboard()

# Initialize components for Routine "AsianF"
AsianFClock = core.Clock()
import random
AFcondition = random.choice(('conditionList/AF_list1.xlsx','conditionList/AF_list2.xlsx','conditionList/AF_list3.xlsx','conditionList/AF_list4.xlsx','conditionList/AF_list5.xlsx'))

thisExp.addData('AFcondition_file', AFcondition)
Fixation = visual.ShapeStim(
    win=win, name='Fixation', vertices='cross',
    size=(0.1, 0.1),
    ori=0, pos=(0, 0),
    lineWidth=1, lineColor='black', lineColorSpace='rgb',
    fillColor='black', fillColorSpace='rgb',
    opacity=1, depth=-1.0, interpolate=True)
AF_image_1 = visual.ImageStim(
    win=win,
    name='AF_image_1', 
    image='sin', mask=None,
    ori=0, pos=(0, 0.16), size=None,
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=False, depth=-2.0)
AF_image_2 = visual.ImageStim(
    win=win,
    name='AF_image_2', 
    image='sin', mask=None,
    ori=0, pos=(0, -0.16), size=None,
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=False, depth=-3.0)
AFMouse = event.Mouse(win=win)
x, y = [None, None]
AFMouse.mouseClock = core.Clock()

# Initialize components for Routine "Blank500"
Blank500Clock = core.Clock()
BlankTest = visual.TextStim(win=win, name='BlankTest',
    text=None,
    font='Arial',
    pos=(0, 0), height=0.1, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=0.0);

# Initialize components for Routine "AsianM"
AsianMClock = core.Clock()
import random
AMcondition = random.choice(('conditionList/AM_list1.xlsx','conditionList/AM_list2.xlsx','conditionList/AM_list3.xlsx','conditionList/AM_list4.xlsx','conditionList/AM_list5.xlsx'))

thisExp.addData('AMcondition_file', AMcondition)
Fixation2 = visual.ShapeStim(
    win=win, name='Fixation2', vertices='cross',
    size=(0.1, 0.1),
    ori=0, pos=(0, 0),
    lineWidth=1, lineColor='black', lineColorSpace='rgb',
    fillColor='black', fillColorSpace='rgb',
    opacity=1, depth=-1.0, interpolate=True)
AM_image_1 = visual.ImageStim(
    win=win,
    name='AM_image_1', 
    image='sin', mask=None,
    ori=0, pos=(0, 0.16), size=None,
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=False, depth=-2.0)
AM_imgae_2 = visual.ImageStim(
    win=win,
    name='AM_imgae_2', 
    image='sin', mask=None,
    ori=0, pos=(0, -0.16), size=None,
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=False, depth=-3.0)
AMMouse = event.Mouse(win=win)
x, y = [None, None]
AMMouse.mouseClock = core.Clock()

# Initialize components for Routine "Blank500"
Blank500Clock = core.Clock()
BlankTest = visual.TextStim(win=win, name='BlankTest',
    text=None,
    font='Arial',
    pos=(0, 0), height=0.1, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=0.0);

# Initialize components for Routine "CaucasianF"
CaucasianFClock = core.Clock()
import random
CFcondition = random.choice(('conditionList/CF_list1.xlsx','conditionList/CF_list2.xlsx','conditionList/CF_list3.xlsx','conditionList/CF_list4.xlsx','conditionList/CF_list5.xlsx'))

thisExp.addData('CFcondition_file', CFcondition)
Fixation3 = visual.ShapeStim(
    win=win, name='Fixation3', vertices='cross',
    size=(0.1, 0.1),
    ori=0, pos=(0, 0),
    lineWidth=1, lineColor='black', lineColorSpace='rgb',
    fillColor='black', fillColorSpace='rgb',
    opacity=1, depth=-1.0, interpolate=True)
CF_image_1 = visual.ImageStim(
    win=win,
    name='CF_image_1', 
    image='sin', mask=None,
    ori=0, pos=(0, 0.16), size=None,
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=False, depth=-2.0)
CF_image_2 = visual.ImageStim(
    win=win,
    name='CF_image_2', 
    image='sin', mask=None,
    ori=0, pos=(0, -0.16), size=None,
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=False, depth=-3.0)
CFMouse = event.Mouse(win=win)
x, y = [None, None]
CFMouse.mouseClock = core.Clock()

# Initialize components for Routine "Blank500"
Blank500Clock = core.Clock()
BlankTest = visual.TextStim(win=win, name='BlankTest',
    text=None,
    font='Arial',
    pos=(0, 0), height=0.1, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=0.0);

# Initialize components for Routine "CaucasianM"
CaucasianMClock = core.Clock()
import random
CMcondition = random.choice(('conditionList/CM_list1.xlsx','conditionList/CM_list2.xlsx','conditionList/CM_list3.xlsx','conditionList/CM_list4.xlsx','conditionList/CM_list5.xlsx'))

thisExp.addData('CMcondition_file', CMcondition)
Fixation4 = visual.ShapeStim(
    win=win, name='Fixation4', vertices='cross',
    size=(0.1, 0.1),
    ori=0, pos=(0, 0),
    lineWidth=1, lineColor='black', lineColorSpace='rgb',
    fillColor='black', fillColorSpace='rgb',
    opacity=1, depth=-1.0, interpolate=True)
CM_image_1 = visual.ImageStim(
    win=win,
    name='CM_image_1', 
    image='sin', mask=None,
    ori=0, pos=(0, 0.16), size=None,
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=False, depth=-2.0)
CM_image_2 = visual.ImageStim(
    win=win,
    name='CM_image_2', 
    image='sin', mask=None,
    ori=0, pos=(0, -0.16), size=None,
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=False, depth=-3.0)
CMMouse = event.Mouse(win=win)
x, y = [None, None]
CMMouse.mouseClock = core.Clock()

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
    color='black', colorSpace='rgb', opacity=1, 
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
    routineTimer.add(3.500000)
    # update component parameters for each repeat
    PracMouse.setPos(newPos=(0,0))
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
    while continueRoutine and routineTimer.getTime() > 0:
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
        if PracMouse.status == NOT_STARTED and t >= 0.5-frameTolerance:
            # keep track of start time/frame for later
            PracMouse.frameNStart = frameN  # exact frame index
            PracMouse.tStart = t  # local t and not account for scr refresh
            PracMouse.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(PracMouse, 'tStartRefresh')  # time at next scr refresh
            PracMouse.status = STARTED
            PracMouse.mouseClock.reset()
            prevButtonState = PracMouse.getPressed()  # if button is down already this ISN'T a new click
        if PracMouse.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > PracMouse.tStartRefresh + 3-frameTolerance:
                # keep track of stop time/frame for later
                PracMouse.tStop = t  # not accounting for scr refresh
                PracMouse.frameNStop = frameN  # exact frame index
                win.timeOnFlip(PracMouse, 'tStopRefresh')  # time at next scr refresh
                PracMouse.status = FINISHED
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
    AF_Loop = data.TrialHandler(nReps=AF_rep, method='random', 
        extraInfo=expInfo, originPath=-1,
        trialList=data.importConditions(AFcondition),
        seed=None, name='AF_Loop')
    thisExp.addLoop(AF_Loop)  # add the loop to the experiment
    thisAF_Loop = AF_Loop.trialList[0]  # so we can initialise stimuli with some values
    # abbreviate parameter names if possible (e.g. rgb = thisAF_Loop.rgb)
    if thisAF_Loop != None:
        for paramName in thisAF_Loop:
            exec('{} = thisAF_Loop[paramName]'.format(paramName))
    
    for thisAF_Loop in AF_Loop:
        currentLoop = AF_Loop
        # abbreviate parameter names if possible (e.g. rgb = thisAF_Loop.rgb)
        if thisAF_Loop != None:
            for paramName in thisAF_Loop:
                exec('{} = thisAF_Loop[paramName]'.format(paramName))
        
        # ------Prepare to start Routine "AsianF"-------
        continueRoutine = True
        routineTimer.add(3.500000)
        # update component parameters for each repeat
        AFMouse.setPos(newPos=(0,0))
        AF_image_1.setImage(Upper_Image)
        AF_image_2.setImage(Lower_Image)
        # setup some python lists for storing info about the AFMouse
        AFMouse.clicked_name = []
        AFMouse.clicked_pos = []
        gotValidClick = False  # until a click is received
        # keep track of which components have finished
        AsianFComponents = [Fixation, AF_image_1, AF_image_2, AFMouse]
        for thisComponent in AsianFComponents:
            thisComponent.tStart = None
            thisComponent.tStop = None
            thisComponent.tStartRefresh = None
            thisComponent.tStopRefresh = None
            if hasattr(thisComponent, 'status'):
                thisComponent.status = NOT_STARTED
        # reset timers
        t = 0
        _timeToFirstFrame = win.getFutureFlipTime(clock="now")
        AsianFClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
        frameN = -1
        
        # -------Run Routine "AsianF"-------
        while continueRoutine and routineTimer.getTime() > 0:
            # get current time
            t = AsianFClock.getTime()
            tThisFlip = win.getFutureFlipTime(clock=AsianFClock)
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
            
            # *AF_image_1* updates
            if AF_image_1.status == NOT_STARTED and tThisFlip >= 0.5-frameTolerance:
                # keep track of start time/frame for later
                AF_image_1.frameNStart = frameN  # exact frame index
                AF_image_1.tStart = t  # local t and not account for scr refresh
                AF_image_1.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(AF_image_1, 'tStartRefresh')  # time at next scr refresh
                AF_image_1.setAutoDraw(True)
            if AF_image_1.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > AF_image_1.tStartRefresh + 3-frameTolerance:
                    # keep track of stop time/frame for later
                    AF_image_1.tStop = t  # not accounting for scr refresh
                    AF_image_1.frameNStop = frameN  # exact frame index
                    win.timeOnFlip(AF_image_1, 'tStopRefresh')  # time at next scr refresh
                    AF_image_1.setAutoDraw(False)
            
            # *AF_image_2* updates
            if AF_image_2.status == NOT_STARTED and tThisFlip >= 0.5-frameTolerance:
                # keep track of start time/frame for later
                AF_image_2.frameNStart = frameN  # exact frame index
                AF_image_2.tStart = t  # local t and not account for scr refresh
                AF_image_2.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(AF_image_2, 'tStartRefresh')  # time at next scr refresh
                AF_image_2.setAutoDraw(True)
            if AF_image_2.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > AF_image_2.tStartRefresh + 3-frameTolerance:
                    # keep track of stop time/frame for later
                    AF_image_2.tStop = t  # not accounting for scr refresh
                    AF_image_2.frameNStop = frameN  # exact frame index
                    win.timeOnFlip(AF_image_2, 'tStopRefresh')  # time at next scr refresh
                    AF_image_2.setAutoDraw(False)
            # *AFMouse* updates
            if AFMouse.status == NOT_STARTED and t >= 0.5-frameTolerance:
                # keep track of start time/frame for later
                AFMouse.frameNStart = frameN  # exact frame index
                AFMouse.tStart = t  # local t and not account for scr refresh
                AFMouse.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(AFMouse, 'tStartRefresh')  # time at next scr refresh
                AFMouse.status = STARTED
                AFMouse.mouseClock.reset()
                prevButtonState = AFMouse.getPressed()  # if button is down already this ISN'T a new click
            if AFMouse.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > AFMouse.tStartRefresh + 3-frameTolerance:
                    # keep track of stop time/frame for later
                    AFMouse.tStop = t  # not accounting for scr refresh
                    AFMouse.frameNStop = frameN  # exact frame index
                    win.timeOnFlip(AFMouse, 'tStopRefresh')  # time at next scr refresh
                    AFMouse.status = FINISHED
            if AFMouse.status == STARTED:  # only update if started and not finished!
                buttons = AFMouse.getPressed()
                if buttons != prevButtonState:  # button state changed?
                    prevButtonState = buttons
                    if sum(buttons) > 0:  # state changed to a new click
                        # check if the mouse was inside our 'clickable' objects
                        gotValidClick = False
                        for obj in [AF_image_1,AF_image_2]:
                            if obj.contains(AFMouse):
                                gotValidClick = True
                                AFMouse.clicked_name.append(obj.name)
                                AFMouse.clicked_pos.append(obj.pos)
                        if gotValidClick:  # abort routine on response
                            continueRoutine = False
            
            # check for quit (typically the Esc key)
            if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
                core.quit()
            
            # check if all components have finished
            if not continueRoutine:  # a component has requested a forced-end of Routine
                break
            continueRoutine = False  # will revert to True if at least one component still running
            for thisComponent in AsianFComponents:
                if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                    continueRoutine = True
                    break  # at least one component has not yet finished
            
            # refresh the screen
            if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                win.flip()
        
        # -------Ending Routine "AsianF"-------
        for thisComponent in AsianFComponents:
            if hasattr(thisComponent, "setAutoDraw"):
                thisComponent.setAutoDraw(False)
        AF_Loop.addData('Fixation.started', Fixation.tStartRefresh)
        AF_Loop.addData('Fixation.stopped', Fixation.tStopRefresh)
        AF_Loop.addData('AF_image_1.started', AF_image_1.tStartRefresh)
        AF_Loop.addData('AF_image_1.stopped', AF_image_1.tStopRefresh)
        AF_Loop.addData('AF_image_2.started', AF_image_2.tStartRefresh)
        AF_Loop.addData('AF_image_2.stopped', AF_image_2.tStopRefresh)
        # store data for AF_Loop (TrialHandler)
        x, y = AFMouse.getPos()
        buttons = AFMouse.getPressed()
        if sum(buttons):
            # check if the mouse was inside our 'clickable' objects
            gotValidClick = False
            for obj in [AF_image_1,AF_image_2]:
                if obj.contains(AFMouse):
                    gotValidClick = True
                    AFMouse.clicked_name.append(obj.name)
                    AFMouse.clicked_pos.append(obj.pos)
        AF_Loop.addData('AFMouse.x', x)
        AF_Loop.addData('AFMouse.y', y)
        AF_Loop.addData('AFMouse.leftButton', buttons[0])
        AF_Loop.addData('AFMouse.midButton', buttons[1])
        AF_Loop.addData('AFMouse.rightButton', buttons[2])
        if len(AFMouse.clicked_name):
            AF_Loop.addData('AFMouse.clicked_name', AFMouse.clicked_name[0])
        if len(AFMouse.clicked_pos):
            AF_Loop.addData('AFMouse.clicked_pos', AFMouse.clicked_pos[0])
        AF_Loop.addData('AFMouse.started', AFMouse.tStart)
        AF_Loop.addData('AFMouse.stopped', AFMouse.tStop)
        
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
        AF_Loop.addData('BlankTest.started', BlankTest.tStartRefresh)
        AF_Loop.addData('BlankTest.stopped', BlankTest.tStopRefresh)
        thisExp.nextEntry()
        
    # completed AF_rep repeats of 'AF_Loop'
    
    
    # set up handler to look after randomisation of conditions etc
    AM_Loop = data.TrialHandler(nReps=AM_rep, method='random', 
        extraInfo=expInfo, originPath=-1,
        trialList=data.importConditions(AMcondition),
        seed=None, name='AM_Loop')
    thisExp.addLoop(AM_Loop)  # add the loop to the experiment
    thisAM_Loop = AM_Loop.trialList[0]  # so we can initialise stimuli with some values
    # abbreviate parameter names if possible (e.g. rgb = thisAM_Loop.rgb)
    if thisAM_Loop != None:
        for paramName in thisAM_Loop:
            exec('{} = thisAM_Loop[paramName]'.format(paramName))
    
    for thisAM_Loop in AM_Loop:
        currentLoop = AM_Loop
        # abbreviate parameter names if possible (e.g. rgb = thisAM_Loop.rgb)
        if thisAM_Loop != None:
            for paramName in thisAM_Loop:
                exec('{} = thisAM_Loop[paramName]'.format(paramName))
        
        # ------Prepare to start Routine "AsianM"-------
        continueRoutine = True
        routineTimer.add(3.500000)
        # update component parameters for each repeat
        AMMouse.setPos(newPos=(0,0))
        AM_image_1.setImage(Upper_Image)
        AM_imgae_2.setImage(Lower_Image)
        # setup some python lists for storing info about the AMMouse
        AMMouse.clicked_name = []
        AMMouse.clicked_pos = []
        gotValidClick = False  # until a click is received
        # keep track of which components have finished
        AsianMComponents = [Fixation2, AM_image_1, AM_imgae_2, AMMouse]
        for thisComponent in AsianMComponents:
            thisComponent.tStart = None
            thisComponent.tStop = None
            thisComponent.tStartRefresh = None
            thisComponent.tStopRefresh = None
            if hasattr(thisComponent, 'status'):
                thisComponent.status = NOT_STARTED
        # reset timers
        t = 0
        _timeToFirstFrame = win.getFutureFlipTime(clock="now")
        AsianMClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
        frameN = -1
        
        # -------Run Routine "AsianM"-------
        while continueRoutine and routineTimer.getTime() > 0:
            # get current time
            t = AsianMClock.getTime()
            tThisFlip = win.getFutureFlipTime(clock=AsianMClock)
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
            
            # *AM_image_1* updates
            if AM_image_1.status == NOT_STARTED and tThisFlip >= 0.5-frameTolerance:
                # keep track of start time/frame for later
                AM_image_1.frameNStart = frameN  # exact frame index
                AM_image_1.tStart = t  # local t and not account for scr refresh
                AM_image_1.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(AM_image_1, 'tStartRefresh')  # time at next scr refresh
                AM_image_1.setAutoDraw(True)
            if AM_image_1.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > AM_image_1.tStartRefresh + 3-frameTolerance:
                    # keep track of stop time/frame for later
                    AM_image_1.tStop = t  # not accounting for scr refresh
                    AM_image_1.frameNStop = frameN  # exact frame index
                    win.timeOnFlip(AM_image_1, 'tStopRefresh')  # time at next scr refresh
                    AM_image_1.setAutoDraw(False)
            
            # *AM_imgae_2* updates
            if AM_imgae_2.status == NOT_STARTED and tThisFlip >= 0.5-frameTolerance:
                # keep track of start time/frame for later
                AM_imgae_2.frameNStart = frameN  # exact frame index
                AM_imgae_2.tStart = t  # local t and not account for scr refresh
                AM_imgae_2.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(AM_imgae_2, 'tStartRefresh')  # time at next scr refresh
                AM_imgae_2.setAutoDraw(True)
            if AM_imgae_2.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > AM_imgae_2.tStartRefresh + 3-frameTolerance:
                    # keep track of stop time/frame for later
                    AM_imgae_2.tStop = t  # not accounting for scr refresh
                    AM_imgae_2.frameNStop = frameN  # exact frame index
                    win.timeOnFlip(AM_imgae_2, 'tStopRefresh')  # time at next scr refresh
                    AM_imgae_2.setAutoDraw(False)
            # *AMMouse* updates
            if AMMouse.status == NOT_STARTED and t >= 0.5-frameTolerance:
                # keep track of start time/frame for later
                AMMouse.frameNStart = frameN  # exact frame index
                AMMouse.tStart = t  # local t and not account for scr refresh
                AMMouse.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(AMMouse, 'tStartRefresh')  # time at next scr refresh
                AMMouse.status = STARTED
                AMMouse.mouseClock.reset()
                prevButtonState = AMMouse.getPressed()  # if button is down already this ISN'T a new click
            if AMMouse.status == STARTED:
                if bool(3):
                    # keep track of stop time/frame for later
                    AMMouse.tStop = t  # not accounting for scr refresh
                    AMMouse.frameNStop = frameN  # exact frame index
                    win.timeOnFlip(AMMouse, 'tStopRefresh')  # time at next scr refresh
                    AMMouse.status = FINISHED
            if AMMouse.status == STARTED:  # only update if started and not finished!
                buttons = AMMouse.getPressed()
                if buttons != prevButtonState:  # button state changed?
                    prevButtonState = buttons
                    if sum(buttons) > 0:  # state changed to a new click
                        # check if the mouse was inside our 'clickable' objects
                        gotValidClick = False
                        for obj in [AM_image_1,AM_imgae_2]:
                            if obj.contains(AMMouse):
                                gotValidClick = True
                                AMMouse.clicked_name.append(obj.name)
                                AMMouse.clicked_pos.append(obj.pos)
                        if gotValidClick:  # abort routine on response
                            continueRoutine = False
            
            # check for quit (typically the Esc key)
            if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
                core.quit()
            
            # check if all components have finished
            if not continueRoutine:  # a component has requested a forced-end of Routine
                break
            continueRoutine = False  # will revert to True if at least one component still running
            for thisComponent in AsianMComponents:
                if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                    continueRoutine = True
                    break  # at least one component has not yet finished
            
            # refresh the screen
            if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                win.flip()
        
        # -------Ending Routine "AsianM"-------
        for thisComponent in AsianMComponents:
            if hasattr(thisComponent, "setAutoDraw"):
                thisComponent.setAutoDraw(False)
        AM_Loop.addData('Fixation2.started', Fixation2.tStartRefresh)
        AM_Loop.addData('Fixation2.stopped', Fixation2.tStopRefresh)
        AM_Loop.addData('AM_image_1.started', AM_image_1.tStartRefresh)
        AM_Loop.addData('AM_image_1.stopped', AM_image_1.tStopRefresh)
        AM_Loop.addData('AM_imgae_2.started', AM_imgae_2.tStartRefresh)
        AM_Loop.addData('AM_imgae_2.stopped', AM_imgae_2.tStopRefresh)
        # store data for AM_Loop (TrialHandler)
        x, y = AMMouse.getPos()
        buttons = AMMouse.getPressed()
        if sum(buttons):
            # check if the mouse was inside our 'clickable' objects
            gotValidClick = False
            for obj in [AM_image_1,AM_imgae_2]:
                if obj.contains(AMMouse):
                    gotValidClick = True
                    AMMouse.clicked_name.append(obj.name)
                    AMMouse.clicked_pos.append(obj.pos)
        AM_Loop.addData('AMMouse.x', x)
        AM_Loop.addData('AMMouse.y', y)
        AM_Loop.addData('AMMouse.leftButton', buttons[0])
        AM_Loop.addData('AMMouse.midButton', buttons[1])
        AM_Loop.addData('AMMouse.rightButton', buttons[2])
        if len(AMMouse.clicked_name):
            AM_Loop.addData('AMMouse.clicked_name', AMMouse.clicked_name[0])
        if len(AMMouse.clicked_pos):
            AM_Loop.addData('AMMouse.clicked_pos', AMMouse.clicked_pos[0])
        AM_Loop.addData('AMMouse.started', AMMouse.tStart)
        AM_Loop.addData('AMMouse.stopped', AMMouse.tStop)
        
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
        AM_Loop.addData('BlankTest.started', BlankTest.tStartRefresh)
        AM_Loop.addData('BlankTest.stopped', BlankTest.tStopRefresh)
        thisExp.nextEntry()
        
    # completed AM_rep repeats of 'AM_Loop'
    
    
    # set up handler to look after randomisation of conditions etc
    CF_Loop = data.TrialHandler(nReps=CF_rep, method='random', 
        extraInfo=expInfo, originPath=-1,
        trialList=data.importConditions(CFcondition),
        seed=None, name='CF_Loop')
    thisExp.addLoop(CF_Loop)  # add the loop to the experiment
    thisCF_Loop = CF_Loop.trialList[0]  # so we can initialise stimuli with some values
    # abbreviate parameter names if possible (e.g. rgb = thisCF_Loop.rgb)
    if thisCF_Loop != None:
        for paramName in thisCF_Loop:
            exec('{} = thisCF_Loop[paramName]'.format(paramName))
    
    for thisCF_Loop in CF_Loop:
        currentLoop = CF_Loop
        # abbreviate parameter names if possible (e.g. rgb = thisCF_Loop.rgb)
        if thisCF_Loop != None:
            for paramName in thisCF_Loop:
                exec('{} = thisCF_Loop[paramName]'.format(paramName))
        
        # ------Prepare to start Routine "CaucasianF"-------
        continueRoutine = True
        routineTimer.add(3.500000)
        # update component parameters for each repeat
        CFMouse.setPos(newPos=(0,0))
        CF_image_1.setImage(Upper_Image)
        CF_image_2.setImage(Lower_Image)
        # setup some python lists for storing info about the CFMouse
        CFMouse.clicked_name = []
        CFMouse.clicked_pos = []
        gotValidClick = False  # until a click is received
        # keep track of which components have finished
        CaucasianFComponents = [Fixation3, CF_image_1, CF_image_2, CFMouse]
        for thisComponent in CaucasianFComponents:
            thisComponent.tStart = None
            thisComponent.tStop = None
            thisComponent.tStartRefresh = None
            thisComponent.tStopRefresh = None
            if hasattr(thisComponent, 'status'):
                thisComponent.status = NOT_STARTED
        # reset timers
        t = 0
        _timeToFirstFrame = win.getFutureFlipTime(clock="now")
        CaucasianFClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
        frameN = -1
        
        # -------Run Routine "CaucasianF"-------
        while continueRoutine and routineTimer.getTime() > 0:
            # get current time
            t = CaucasianFClock.getTime()
            tThisFlip = win.getFutureFlipTime(clock=CaucasianFClock)
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
            
            # *CF_image_1* updates
            if CF_image_1.status == NOT_STARTED and tThisFlip >= 0.5-frameTolerance:
                # keep track of start time/frame for later
                CF_image_1.frameNStart = frameN  # exact frame index
                CF_image_1.tStart = t  # local t and not account for scr refresh
                CF_image_1.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(CF_image_1, 'tStartRefresh')  # time at next scr refresh
                CF_image_1.setAutoDraw(True)
            if CF_image_1.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > CF_image_1.tStartRefresh + 3-frameTolerance:
                    # keep track of stop time/frame for later
                    CF_image_1.tStop = t  # not accounting for scr refresh
                    CF_image_1.frameNStop = frameN  # exact frame index
                    win.timeOnFlip(CF_image_1, 'tStopRefresh')  # time at next scr refresh
                    CF_image_1.setAutoDraw(False)
            
            # *CF_image_2* updates
            if CF_image_2.status == NOT_STARTED and tThisFlip >= 0.5-frameTolerance:
                # keep track of start time/frame for later
                CF_image_2.frameNStart = frameN  # exact frame index
                CF_image_2.tStart = t  # local t and not account for scr refresh
                CF_image_2.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(CF_image_2, 'tStartRefresh')  # time at next scr refresh
                CF_image_2.setAutoDraw(True)
            if CF_image_2.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > CF_image_2.tStartRefresh + 3-frameTolerance:
                    # keep track of stop time/frame for later
                    CF_image_2.tStop = t  # not accounting for scr refresh
                    CF_image_2.frameNStop = frameN  # exact frame index
                    win.timeOnFlip(CF_image_2, 'tStopRefresh')  # time at next scr refresh
                    CF_image_2.setAutoDraw(False)
            # *CFMouse* updates
            if CFMouse.status == NOT_STARTED and t >= 0.5-frameTolerance:
                # keep track of start time/frame for later
                CFMouse.frameNStart = frameN  # exact frame index
                CFMouse.tStart = t  # local t and not account for scr refresh
                CFMouse.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(CFMouse, 'tStartRefresh')  # time at next scr refresh
                CFMouse.status = STARTED
                CFMouse.mouseClock.reset()
                prevButtonState = CFMouse.getPressed()  # if button is down already this ISN'T a new click
            if CFMouse.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > CFMouse.tStartRefresh + 3-frameTolerance:
                    # keep track of stop time/frame for later
                    CFMouse.tStop = t  # not accounting for scr refresh
                    CFMouse.frameNStop = frameN  # exact frame index
                    win.timeOnFlip(CFMouse, 'tStopRefresh')  # time at next scr refresh
                    CFMouse.status = FINISHED
            if CFMouse.status == STARTED:  # only update if started and not finished!
                buttons = CFMouse.getPressed()
                if buttons != prevButtonState:  # button state changed?
                    prevButtonState = buttons
                    if sum(buttons) > 0:  # state changed to a new click
                        # check if the mouse was inside our 'clickable' objects
                        gotValidClick = False
                        for obj in [CF_image_1,CF_image_2]:
                            if obj.contains(CFMouse):
                                gotValidClick = True
                                CFMouse.clicked_name.append(obj.name)
                                CFMouse.clicked_pos.append(obj.pos)
                        if gotValidClick:  # abort routine on response
                            continueRoutine = False
            
            # check for quit (typically the Esc key)
            if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
                core.quit()
            
            # check if all components have finished
            if not continueRoutine:  # a component has requested a forced-end of Routine
                break
            continueRoutine = False  # will revert to True if at least one component still running
            for thisComponent in CaucasianFComponents:
                if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                    continueRoutine = True
                    break  # at least one component has not yet finished
            
            # refresh the screen
            if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                win.flip()
        
        # -------Ending Routine "CaucasianF"-------
        for thisComponent in CaucasianFComponents:
            if hasattr(thisComponent, "setAutoDraw"):
                thisComponent.setAutoDraw(False)
        CF_Loop.addData('Fixation3.started', Fixation3.tStartRefresh)
        CF_Loop.addData('Fixation3.stopped', Fixation3.tStopRefresh)
        CF_Loop.addData('CF_image_1.started', CF_image_1.tStartRefresh)
        CF_Loop.addData('CF_image_1.stopped', CF_image_1.tStopRefresh)
        CF_Loop.addData('CF_image_2.started', CF_image_2.tStartRefresh)
        CF_Loop.addData('CF_image_2.stopped', CF_image_2.tStopRefresh)
        # store data for CF_Loop (TrialHandler)
        x, y = CFMouse.getPos()
        buttons = CFMouse.getPressed()
        if sum(buttons):
            # check if the mouse was inside our 'clickable' objects
            gotValidClick = False
            for obj in [CF_image_1,CF_image_2]:
                if obj.contains(CFMouse):
                    gotValidClick = True
                    CFMouse.clicked_name.append(obj.name)
                    CFMouse.clicked_pos.append(obj.pos)
        CF_Loop.addData('CFMouse.x', x)
        CF_Loop.addData('CFMouse.y', y)
        CF_Loop.addData('CFMouse.leftButton', buttons[0])
        CF_Loop.addData('CFMouse.midButton', buttons[1])
        CF_Loop.addData('CFMouse.rightButton', buttons[2])
        if len(CFMouse.clicked_name):
            CF_Loop.addData('CFMouse.clicked_name', CFMouse.clicked_name[0])
        if len(CFMouse.clicked_pos):
            CF_Loop.addData('CFMouse.clicked_pos', CFMouse.clicked_pos[0])
        CF_Loop.addData('CFMouse.started', CFMouse.tStart)
        CF_Loop.addData('CFMouse.stopped', CFMouse.tStop)
        
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
        CF_Loop.addData('BlankTest.started', BlankTest.tStartRefresh)
        CF_Loop.addData('BlankTest.stopped', BlankTest.tStopRefresh)
        thisExp.nextEntry()
        
    # completed CF_rep repeats of 'CF_Loop'
    
    
    # set up handler to look after randomisation of conditions etc
    CM_Loop = data.TrialHandler(nReps=CM_rep, method='random', 
        extraInfo=expInfo, originPath=-1,
        trialList=data.importConditions(CMcondition),
        seed=None, name='CM_Loop')
    thisExp.addLoop(CM_Loop)  # add the loop to the experiment
    thisCM_Loop = CM_Loop.trialList[0]  # so we can initialise stimuli with some values
    # abbreviate parameter names if possible (e.g. rgb = thisCM_Loop.rgb)
    if thisCM_Loop != None:
        for paramName in thisCM_Loop:
            exec('{} = thisCM_Loop[paramName]'.format(paramName))
    
    for thisCM_Loop in CM_Loop:
        currentLoop = CM_Loop
        # abbreviate parameter names if possible (e.g. rgb = thisCM_Loop.rgb)
        if thisCM_Loop != None:
            for paramName in thisCM_Loop:
                exec('{} = thisCM_Loop[paramName]'.format(paramName))
        
        # ------Prepare to start Routine "CaucasianM"-------
        continueRoutine = True
        routineTimer.add(3.500000)
        # update component parameters for each repeat
        CMMouse.setPos(newPos=(0,0))
        CM_image_1.setImage(Upper_Image)
        CM_image_2.setImage(Lower_Image)
        # setup some python lists for storing info about the CMMouse
        CMMouse.clicked_name = []
        CMMouse.clicked_pos = []
        gotValidClick = False  # until a click is received
        # keep track of which components have finished
        CaucasianMComponents = [Fixation4, CM_image_1, CM_image_2, CMMouse]
        for thisComponent in CaucasianMComponents:
            thisComponent.tStart = None
            thisComponent.tStop = None
            thisComponent.tStartRefresh = None
            thisComponent.tStopRefresh = None
            if hasattr(thisComponent, 'status'):
                thisComponent.status = NOT_STARTED
        # reset timers
        t = 0
        _timeToFirstFrame = win.getFutureFlipTime(clock="now")
        CaucasianMClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
        frameN = -1
        
        # -------Run Routine "CaucasianM"-------
        while continueRoutine and routineTimer.getTime() > 0:
            # get current time
            t = CaucasianMClock.getTime()
            tThisFlip = win.getFutureFlipTime(clock=CaucasianMClock)
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
            
            # *CM_image_1* updates
            if CM_image_1.status == NOT_STARTED and tThisFlip >= 0.5-frameTolerance:
                # keep track of start time/frame for later
                CM_image_1.frameNStart = frameN  # exact frame index
                CM_image_1.tStart = t  # local t and not account for scr refresh
                CM_image_1.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(CM_image_1, 'tStartRefresh')  # time at next scr refresh
                CM_image_1.setAutoDraw(True)
            if CM_image_1.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > CM_image_1.tStartRefresh + 3-frameTolerance:
                    # keep track of stop time/frame for later
                    CM_image_1.tStop = t  # not accounting for scr refresh
                    CM_image_1.frameNStop = frameN  # exact frame index
                    win.timeOnFlip(CM_image_1, 'tStopRefresh')  # time at next scr refresh
                    CM_image_1.setAutoDraw(False)
            
            # *CM_image_2* updates
            if CM_image_2.status == NOT_STARTED and tThisFlip >= 0.5-frameTolerance:
                # keep track of start time/frame for later
                CM_image_2.frameNStart = frameN  # exact frame index
                CM_image_2.tStart = t  # local t and not account for scr refresh
                CM_image_2.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(CM_image_2, 'tStartRefresh')  # time at next scr refresh
                CM_image_2.setAutoDraw(True)
            if CM_image_2.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > CM_image_2.tStartRefresh + 3-frameTolerance:
                    # keep track of stop time/frame for later
                    CM_image_2.tStop = t  # not accounting for scr refresh
                    CM_image_2.frameNStop = frameN  # exact frame index
                    win.timeOnFlip(CM_image_2, 'tStopRefresh')  # time at next scr refresh
                    CM_image_2.setAutoDraw(False)
            # *CMMouse* updates
            if CMMouse.status == NOT_STARTED and t >= 0.5-frameTolerance:
                # keep track of start time/frame for later
                CMMouse.frameNStart = frameN  # exact frame index
                CMMouse.tStart = t  # local t and not account for scr refresh
                CMMouse.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(CMMouse, 'tStartRefresh')  # time at next scr refresh
                CMMouse.status = STARTED
                CMMouse.mouseClock.reset()
                prevButtonState = CMMouse.getPressed()  # if button is down already this ISN'T a new click
            if CMMouse.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > CMMouse.tStartRefresh + 3-frameTolerance:
                    # keep track of stop time/frame for later
                    CMMouse.tStop = t  # not accounting for scr refresh
                    CMMouse.frameNStop = frameN  # exact frame index
                    win.timeOnFlip(CMMouse, 'tStopRefresh')  # time at next scr refresh
                    CMMouse.status = FINISHED
            if CMMouse.status == STARTED:  # only update if started and not finished!
                buttons = CMMouse.getPressed()
                if buttons != prevButtonState:  # button state changed?
                    prevButtonState = buttons
                    if sum(buttons) > 0:  # state changed to a new click
                        # check if the mouse was inside our 'clickable' objects
                        gotValidClick = False
                        for obj in [CM_image_1,CM_image_2]:
                            if obj.contains(CMMouse):
                                gotValidClick = True
                                CMMouse.clicked_name.append(obj.name)
                                CMMouse.clicked_pos.append(obj.pos)
                        if gotValidClick:  # abort routine on response
                            continueRoutine = False
            
            # check for quit (typically the Esc key)
            if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
                core.quit()
            
            # check if all components have finished
            if not continueRoutine:  # a component has requested a forced-end of Routine
                break
            continueRoutine = False  # will revert to True if at least one component still running
            for thisComponent in CaucasianMComponents:
                if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                    continueRoutine = True
                    break  # at least one component has not yet finished
            
            # refresh the screen
            if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                win.flip()
        
        # -------Ending Routine "CaucasianM"-------
        for thisComponent in CaucasianMComponents:
            if hasattr(thisComponent, "setAutoDraw"):
                thisComponent.setAutoDraw(False)
        CM_Loop.addData('Fixation4.started', Fixation4.tStartRefresh)
        CM_Loop.addData('Fixation4.stopped', Fixation4.tStopRefresh)
        CM_Loop.addData('CM_image_1.started', CM_image_1.tStartRefresh)
        CM_Loop.addData('CM_image_1.stopped', CM_image_1.tStopRefresh)
        CM_Loop.addData('CM_image_2.started', CM_image_2.tStartRefresh)
        CM_Loop.addData('CM_image_2.stopped', CM_image_2.tStopRefresh)
        # store data for CM_Loop (TrialHandler)
        x, y = CMMouse.getPos()
        buttons = CMMouse.getPressed()
        if sum(buttons):
            # check if the mouse was inside our 'clickable' objects
            gotValidClick = False
            for obj in [CM_image_1,CM_image_2]:
                if obj.contains(CMMouse):
                    gotValidClick = True
                    CMMouse.clicked_name.append(obj.name)
                    CMMouse.clicked_pos.append(obj.pos)
        CM_Loop.addData('CMMouse.x', x)
        CM_Loop.addData('CMMouse.y', y)
        CM_Loop.addData('CMMouse.leftButton', buttons[0])
        CM_Loop.addData('CMMouse.midButton', buttons[1])
        CM_Loop.addData('CMMouse.rightButton', buttons[2])
        if len(CMMouse.clicked_name):
            CM_Loop.addData('CMMouse.clicked_name', CMMouse.clicked_name[0])
        if len(CMMouse.clicked_pos):
            CM_Loop.addData('CMMouse.clicked_pos', CMMouse.clicked_pos[0])
        CM_Loop.addData('CMMouse.started', CMMouse.tStart)
        CM_Loop.addData('CMMouse.stopped', CMMouse.tStop)
        
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
        CM_Loop.addData('BlankTest.started', BlankTest.tStartRefresh)
        CM_Loop.addData('BlankTest.stopped', BlankTest.tStopRefresh)
        thisExp.nextEntry()
        
    # completed CM_rep repeats of 'CM_Loop'
    
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
