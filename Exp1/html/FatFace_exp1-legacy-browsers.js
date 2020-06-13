/********************* 
 * Fatface_Exp1 Test *
 *********************/

// init psychoJS:
const psychoJS = new PsychoJS({
  debug: true
});

// open window:
psychoJS.openWindow({
  fullscr: true,
  color: new util.Color('white'),
  units: 'height',
  waitBlanking: true
});

// store info about the experiment session:
let expName = 'FatFace_exp1';  // from the Builder filename that created this script
let expInfo = {'participant': '', 'gender': '', 'age': '', 'session': '001'};

// schedule the experiment:
psychoJS.schedule(psychoJS.gui.DlgFromDict({
  dictionary: expInfo,
  title: expName
}));

const flowScheduler = new Scheduler(psychoJS);
const dialogCancelScheduler = new Scheduler(psychoJS);
psychoJS.scheduleCondition(function() { return (psychoJS.gui.dialogComponent.button === 'OK'); }, flowScheduler, dialogCancelScheduler);

// flowScheduler gets run if the participants presses OK
flowScheduler.add(updateInfo); // add timeStamp
flowScheduler.add(experimentInit);
flowScheduler.add(InstructionRoutineBegin());
flowScheduler.add(InstructionRoutineEachFrame());
flowScheduler.add(InstructionRoutineEnd());
const Prac_LoopLoopScheduler = new Scheduler(psychoJS);
flowScheduler.add(Prac_LoopLoopBegin, Prac_LoopLoopScheduler);
flowScheduler.add(Prac_LoopLoopScheduler);
flowScheduler.add(Prac_LoopLoopEnd);
flowScheduler.add(BreakRoutineBegin());
flowScheduler.add(BreakRoutineEachFrame());
flowScheduler.add(BreakRoutineEnd());
const BlockTrailLoopScheduler = new Scheduler(psychoJS);
flowScheduler.add(BlockTrailLoopBegin, BlockTrailLoopScheduler);
flowScheduler.add(BlockTrailLoopScheduler);
flowScheduler.add(BlockTrailLoopEnd);
flowScheduler.add(EndRoutineBegin());
flowScheduler.add(EndRoutineEachFrame());
flowScheduler.add(EndRoutineEnd());
flowScheduler.add(quitPsychoJS, '', true);

// quit if user presses Cancel in dialog box:
dialogCancelScheduler.add(quitPsychoJS, '', false);

psychoJS.start({
  expName: expName,
  expInfo: expInfo,
  });

function updateInfo() {
  expInfo['date'] = util.MonotonicClock.getDateStr();  // add a simple timestamp
  expInfo['expName'] = expName;
  expInfo['psychopyVersion'] = '2020.1.2';
  expInfo['OS'] = window.navigator.platform;

  // store frame rate of monitor if we can measure it successfully
  expInfo['frameRate'] = psychoJS.window.getActualFrameRate();
  if (typeof expInfo['frameRate'] !== 'undefined')
    frameDur = 1.0 / Math.round(expInfo['frameRate']);
  else
    frameDur = 1.0 / 60.0; // couldn't get a reliable measure so guess

  // add info from the URL:
  util.addInfoFromUrl(expInfo);
  
  return Scheduler.Event.NEXT;
}

function experimentInit() {
  // Initialize components for Routine "Instruction"
  InstructionClock = new util.Clock();
  InstrText = new visual.TextStim({
    win: psychoJS.window,
    name: 'InstrText',
    text: 'Welcome to our experiment!\n\nIn our experiment, two faces will presented on the Screen, one is on top and another one is at the bottome. \nPlace indicate which face looks fatter by clicking on it as quick as you can.\n\nPress "Space" to go to the practical session.',
    font: 'Arial',
    units: undefined, 
    pos: [0, 0], height: 0.05,  wrapWidth: undefined, ori: 0,
    color: new util.Color('black'),  opacity: 1,
    depth: 0.0 
  });
  
  InstrKey = new core.Keyboard({psychoJS: psychoJS, clock: new util.Clock(), waitForStart: true});
  
  // Initialize components for Routine "Practise"
  PractiseClock = new util.Clock();
  Fixation0 = new visual.ShapeStim ({
    win: psychoJS.window, name: 'Fixation0', 
    vertices: 'cross', size:[0.1, 0.1],
    ori: 0, pos: [0, 0],
    lineWidth: 1, lineColor: new util.Color('black'),
    fillColor: new util.Color('black'),
    opacity: 1, depth: -1, interpolate: true,
  });
  
  Upper_image = new visual.ImageStim({
    win : psychoJS.window,
    name : 'Upper_image', units : undefined, 
    image : undefined, mask : undefined,
    ori : 0, pos : [0, 0.16], size : undefined,
    color : new util.Color([1, 1, 1]), opacity : 1,
    flipHoriz : false, flipVert : false,
    texRes : 128, interpolate : false, depth : -2.0 
  });
  Lower_image = new visual.ImageStim({
    win : psychoJS.window,
    name : 'Lower_image', units : undefined, 
    image : undefined, mask : undefined,
    ori : 0, pos : [0, (- 0.16)], size : undefined,
    color : new util.Color([1, 1, 1]), opacity : 1,
    flipHoriz : false, flipVert : false,
    texRes : 128, interpolate : false, depth : -3.0 
  });
  PracMouse = new core.Mouse({
    win: psychoJS.window,
  });
  PracMouse.mouseClock = new util.Clock();
  // Initialize components for Routine "Blank500"
  Blank500Clock = new util.Clock();
  BlankTest = new visual.TextStim({
    win: psychoJS.window,
    name: 'BlankTest',
    text: '',
    font: 'Arial',
    units: undefined, 
    pos: [0, 0], height: 0.1,  wrapWidth: undefined, ori: 0,
    color: new util.Color('white'),  opacity: 1,
    depth: 0.0 
  });
  
  // Initialize components for Routine "Break"
  BreakClock = new util.Clock();
  BreakText = new visual.TextStim({
    win: psychoJS.window,
    name: 'BreakText',
    text: 'The practise part is over.\n\nPress "Space" to go to the next part.',
    font: 'Arial',
    units: undefined, 
    pos: [0, 0], height: 0.05,  wrapWidth: undefined, ori: 0,
    color: new util.Color('black'),  opacity: 1,
    depth: 0.0 
  });
  
  Prac_Key = new core.Keyboard({psychoJS: psychoJS, clock: new util.Clock(), waitForStart: true});
  
  // Initialize components for Routine "AsianF"
  AsianFClock = new util.Clock();
  import * as random from 'random';
  var AFcondition;
  AFcondition = random.choice(["AF_list1.xlsx", "AF_list2.xlsx", "AF_list3.xlsx", "AF_list4.xlsx", "AF_list5.xlsx"]);
  thisExp.addData("AFcondition_file", AFcondition);
  
  Fixation = new visual.ShapeStim ({
    win: psychoJS.window, name: 'Fixation', 
    vertices: 'cross', size:[0.1, 0.1],
    ori: 0, pos: [0, 0],
    lineWidth: 1, lineColor: new util.Color('black'),
    fillColor: new util.Color('black'),
    opacity: 1, depth: -1, interpolate: true,
  });
  
  AF_image_1 = new visual.ImageStim({
    win : psychoJS.window,
    name : 'AF_image_1', units : undefined, 
    image : undefined, mask : undefined,
    ori : 0, pos : [0, 0.16], size : undefined,
    color : new util.Color([1, 1, 1]), opacity : 1,
    flipHoriz : false, flipVert : false,
    texRes : 128, interpolate : false, depth : -2.0 
  });
  AF_image_2 = new visual.ImageStim({
    win : psychoJS.window,
    name : 'AF_image_2', units : undefined, 
    image : undefined, mask : undefined,
    ori : 0, pos : [0, (- 0.16)], size : undefined,
    color : new util.Color([1, 1, 1]), opacity : 1,
    flipHoriz : false, flipVert : false,
    texRes : 128, interpolate : false, depth : -3.0 
  });
  AFMouse = new core.Mouse({
    win: psychoJS.window,
  });
  AFMouse.mouseClock = new util.Clock();
  // Initialize components for Routine "Blank500"
  Blank500Clock = new util.Clock();
  BlankTest = new visual.TextStim({
    win: psychoJS.window,
    name: 'BlankTest',
    text: '',
    font: 'Arial',
    units: undefined, 
    pos: [0, 0], height: 0.1,  wrapWidth: undefined, ori: 0,
    color: new util.Color('white'),  opacity: 1,
    depth: 0.0 
  });
  
  // Initialize components for Routine "AsianM"
  AsianMClock = new util.Clock();
  import * as random from 'random';
  var AMcondition;
  AMcondition = random.choice(["AM_list1.xlsx", "AM_list2.xlsx", "AM_list3.xlsx", "AM_list4.xlsx", "AM_list5.xlsx"]);
  thisExp.addData("AMcondition_file", AMcondition);
  
  Fixation2 = new visual.ShapeStim ({
    win: psychoJS.window, name: 'Fixation2', 
    vertices: 'cross', size:[0.1, 0.1],
    ori: 0, pos: [0, 0],
    lineWidth: 1, lineColor: new util.Color('black'),
    fillColor: new util.Color('black'),
    opacity: 1, depth: -1, interpolate: true,
  });
  
  AM_image_1 = new visual.ImageStim({
    win : psychoJS.window,
    name : 'AM_image_1', units : undefined, 
    image : undefined, mask : undefined,
    ori : 0, pos : [0, 0.16], size : undefined,
    color : new util.Color([1, 1, 1]), opacity : 1,
    flipHoriz : false, flipVert : false,
    texRes : 128, interpolate : false, depth : -2.0 
  });
  AM_imgae_2 = new visual.ImageStim({
    win : psychoJS.window,
    name : 'AM_imgae_2', units : undefined, 
    image : undefined, mask : undefined,
    ori : 0, pos : [0, (- 0.16)], size : undefined,
    color : new util.Color([1, 1, 1]), opacity : 1,
    flipHoriz : false, flipVert : false,
    texRes : 128, interpolate : false, depth : -3.0 
  });
  AMMouse = new core.Mouse({
    win: psychoJS.window,
  });
  AMMouse.mouseClock = new util.Clock();
  // Initialize components for Routine "Blank500"
  Blank500Clock = new util.Clock();
  BlankTest = new visual.TextStim({
    win: psychoJS.window,
    name: 'BlankTest',
    text: '',
    font: 'Arial',
    units: undefined, 
    pos: [0, 0], height: 0.1,  wrapWidth: undefined, ori: 0,
    color: new util.Color('white'),  opacity: 1,
    depth: 0.0 
  });
  
  // Initialize components for Routine "CaucasianF"
  CaucasianFClock = new util.Clock();
  import * as random from 'random';
  var CFcondition;
  CFcondition = random.choice(["conditionList/CF_list1.xlsx", "conditionList/CF_list2.xlsx", "conditionList/CF_list3.xlsx", "conditionList/CF_list4.xlsx", "conditionList/CF_list5.xlsx"]);
  thisExp.addData("CFcondition_file", CFcondition);
  
  Fixation3 = new visual.ShapeStim ({
    win: psychoJS.window, name: 'Fixation3', 
    vertices: 'cross', size:[0.1, 0.1],
    ori: 0, pos: [0, 0],
    lineWidth: 1, lineColor: new util.Color('black'),
    fillColor: new util.Color('black'),
    opacity: 1, depth: -1, interpolate: true,
  });
  
  CF_image_1 = new visual.ImageStim({
    win : psychoJS.window,
    name : 'CF_image_1', units : undefined, 
    image : undefined, mask : undefined,
    ori : 0, pos : [0, 0.16], size : undefined,
    color : new util.Color([1, 1, 1]), opacity : 1,
    flipHoriz : false, flipVert : false,
    texRes : 128, interpolate : false, depth : -2.0 
  });
  CF_image_2 = new visual.ImageStim({
    win : psychoJS.window,
    name : 'CF_image_2', units : undefined, 
    image : undefined, mask : undefined,
    ori : 0, pos : [0, (- 0.16)], size : undefined,
    color : new util.Color([1, 1, 1]), opacity : 1,
    flipHoriz : false, flipVert : false,
    texRes : 128, interpolate : false, depth : -3.0 
  });
  CFMouse = new core.Mouse({
    win: psychoJS.window,
  });
  CFMouse.mouseClock = new util.Clock();
  // Initialize components for Routine "Blank500"
  Blank500Clock = new util.Clock();
  BlankTest = new visual.TextStim({
    win: psychoJS.window,
    name: 'BlankTest',
    text: '',
    font: 'Arial',
    units: undefined, 
    pos: [0, 0], height: 0.1,  wrapWidth: undefined, ori: 0,
    color: new util.Color('white'),  opacity: 1,
    depth: 0.0 
  });
  
  // Initialize components for Routine "CaucasianM"
  CaucasianMClock = new util.Clock();
  Fixation4 = new visual.ShapeStim ({
    win: psychoJS.window, name: 'Fixation4', 
    vertices: 'cross', size:[0.1, 0.1],
    ori: 0, pos: [0, 0],
    lineWidth: 1, lineColor: new util.Color('black'),
    fillColor: new util.Color('black'),
    opacity: 1, depth: -1, interpolate: true,
  });
  
  CM_image_1 = new visual.ImageStim({
    win : psychoJS.window,
    name : 'CM_image_1', units : undefined, 
    image : undefined, mask : undefined,
    ori : 0, pos : [0, 0.16], size : undefined,
    color : new util.Color([1, 1, 1]), opacity : 1,
    flipHoriz : false, flipVert : false,
    texRes : 128, interpolate : false, depth : -2.0 
  });
  CM_image_2 = new visual.ImageStim({
    win : psychoJS.window,
    name : 'CM_image_2', units : undefined, 
    image : undefined, mask : undefined,
    ori : 0, pos : [0, (- 0.16)], size : undefined,
    color : new util.Color([1, 1, 1]), opacity : 1,
    flipHoriz : false, flipVert : false,
    texRes : 128, interpolate : false, depth : -3.0 
  });
  CMMouse = new core.Mouse({
    win: psychoJS.window,
  });
  CMMouse.mouseClock = new util.Clock();
  // Initialize components for Routine "Blank500"
  Blank500Clock = new util.Clock();
  BlankTest = new visual.TextStim({
    win: psychoJS.window,
    name: 'BlankTest',
    text: '',
    font: 'Arial',
    units: undefined, 
    pos: [0, 0], height: 0.1,  wrapWidth: undefined, ori: 0,
    color: new util.Color('white'),  opacity: 1,
    depth: 0.0 
  });
  
  // Initialize components for Routine "End"
  EndClock = new util.Clock();
  text = new visual.TextStim({
    win: psychoJS.window,
    name: 'text',
    text: 'Thank you!',
    font: 'Arial',
    units: undefined, 
    pos: [0, 0], height: 0.1,  wrapWidth: undefined, ori: 0,
    color: new util.Color('black'),  opacity: 1,
    depth: 0.0 
  });
  
  // Create some handy timers
  globalClock = new util.Clock();  // to track the time since experiment started
  routineTimer = new util.CountdownTimer();  // to track time remaining of each (non-slip) routine
  
  return Scheduler.Event.NEXT;
}

function InstructionRoutineBegin(trials) {
  return function () {
    //------Prepare to start Routine 'Instruction'-------
    t = 0;
    InstructionClock.reset(); // clock
    frameN = -1;
    // update component parameters for each repeat
    InstrKey.keys = undefined;
    InstrKey.rt = undefined;
    _InstrKey_allKeys = [];
    // keep track of which components have finished
    InstructionComponents = [];
    InstructionComponents.push(InstrText);
    InstructionComponents.push(InstrKey);
    
    InstructionComponents.forEach( function(thisComponent) {
      if ('status' in thisComponent)
        thisComponent.status = PsychoJS.Status.NOT_STARTED;
       });
    
    return Scheduler.Event.NEXT;
  };
}

function InstructionRoutineEachFrame(trials) {
  return function () {
    //------Loop for each frame of Routine 'Instruction'-------
    let continueRoutine = true; // until we're told otherwise
    // get current time
    t = InstructionClock.getTime();
    frameN = frameN + 1;// number of completed frames (so 0 is the first frame)
    // update/draw components on each frame
    
    // *InstrText* updates
    if (t >= 0.0 && InstrText.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      InstrText.tStart = t;  // (not accounting for frame time here)
      InstrText.frameNStart = frameN;  // exact frame index
      
      InstrText.setAutoDraw(true);
    }

    
    // *InstrKey* updates
    if (t >= 0.0 && InstrKey.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      InstrKey.tStart = t;  // (not accounting for frame time here)
      InstrKey.frameNStart = frameN;  // exact frame index
      
      // keyboard checking is just starting
      psychoJS.window.callOnFlip(function() { InstrKey.clock.reset(); });  // t=0 on next screen flip
      psychoJS.window.callOnFlip(function() { InstrKey.start(); }); // start on screen flip
      psychoJS.window.callOnFlip(function() { InstrKey.clearEvents(); });
    }

    if (InstrKey.status === PsychoJS.Status.STARTED) {
      let theseKeys = InstrKey.getKeys({keyList: ['space'], waitRelease: false});
      _InstrKey_allKeys = _InstrKey_allKeys.concat(theseKeys);
      if (_InstrKey_allKeys.length > 0) {
        InstrKey.keys = _InstrKey_allKeys[_InstrKey_allKeys.length - 1].name;  // just the last key pressed
        InstrKey.rt = _InstrKey_allKeys[_InstrKey_allKeys.length - 1].rt;
        // a response ends the routine
        continueRoutine = false;
      }
    }
    
    // check for quit (typically the Esc key)
    if (psychoJS.experiment.experimentEnded || psychoJS.eventManager.getKeys({keyList:['escape']}).length > 0) {
      return quitPsychoJS('The [Escape] key was pressed. Goodbye!', false);
    }
    
    // check if the Routine should terminate
    if (!continueRoutine) {  // a component has requested a forced-end of Routine
      return Scheduler.Event.NEXT;
    }
    
    continueRoutine = false;  // reverts to True if at least one component still running
    InstructionComponents.forEach( function(thisComponent) {
      if ('status' in thisComponent && thisComponent.status !== PsychoJS.Status.FINISHED) {
        continueRoutine = true;
      }
    });
    
    // refresh the screen if continuing
    if (continueRoutine) {
      return Scheduler.Event.FLIP_REPEAT;
    } else {
      return Scheduler.Event.NEXT;
    }
  };
}

function InstructionRoutineEnd(trials) {
  return function () {
    //------Ending Routine 'Instruction'-------
    InstructionComponents.forEach( function(thisComponent) {
      if (typeof thisComponent.setAutoDraw === 'function') {
        thisComponent.setAutoDraw(false);
      }
    });
    psychoJS.experiment.addData('InstrKey.keys', InstrKey.keys);
    if (typeof InstrKey.keys !== 'undefined') {  // we had a response
        psychoJS.experiment.addData('InstrKey.rt', InstrKey.rt);
        routineTimer.reset();
        }
    
    InstrKey.stop();
    // the Routine "Instruction" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset();
    
    return Scheduler.Event.NEXT;
  };
}

function Prac_LoopLoopBegin(thisScheduler) {
  // set up handler to look after randomisation of conditions etc
  Prac_Loop = new TrialHandler({
    psychoJS: psychoJS,
    nReps: 1, method: TrialHandler.Method.RANDOM,
    extraInfo: expInfo, originPath: undefined,
    trialList: 'Prac_Order.xlsx',
    seed: undefined, name: 'Prac_Loop'
  });
  psychoJS.experiment.addLoop(Prac_Loop); // add the loop to the experiment
  currentLoop = Prac_Loop;  // we're now the current loop

  // Schedule all the trials in the trialList:
  Prac_Loop.forEach(function() {
    const snapshot = Prac_Loop.getSnapshot();

    thisScheduler.add(importConditions(snapshot));
    thisScheduler.add(PractiseRoutineBegin(snapshot));
    thisScheduler.add(PractiseRoutineEachFrame(snapshot));
    thisScheduler.add(PractiseRoutineEnd(snapshot));
    thisScheduler.add(Blank500RoutineBegin(snapshot));
    thisScheduler.add(Blank500RoutineEachFrame(snapshot));
    thisScheduler.add(Blank500RoutineEnd(snapshot));
    thisScheduler.add(endLoopIteration(thisScheduler, snapshot));
  });

  return Scheduler.Event.NEXT;
}

function Prac_LoopLoopEnd() {
  psychoJS.experiment.removeLoop(Prac_Loop);

  return Scheduler.Event.NEXT;
}

function BlockTrailLoopBegin(thisScheduler) {
  // set up handler to look after randomisation of conditions etc
  BlockTrail = new TrialHandler({
    psychoJS: psychoJS,
    nReps: 1, method: TrialHandler.Method.RANDOM,
    extraInfo: expInfo, originPath: undefined,
    trialList: 'BlockOrder.xlsx',
    seed: undefined, name: 'BlockTrail'
  });
  psychoJS.experiment.addLoop(BlockTrail); // add the loop to the experiment
  currentLoop = BlockTrail;  // we're now the current loop

  // Schedule all the trials in the trialList:
  BlockTrail.forEach(function() {
    const snapshot = BlockTrail.getSnapshot();

    thisScheduler.add(importConditions(snapshot));
    const AF_LoopLoopScheduler = new Scheduler(psychoJS);
    thisScheduler.add(AF_LoopLoopBegin, AF_LoopLoopScheduler);
    thisScheduler.add(AF_LoopLoopScheduler);
    thisScheduler.add(AF_LoopLoopEnd);
    const AM_LoopLoopScheduler = new Scheduler(psychoJS);
    thisScheduler.add(AM_LoopLoopBegin, AM_LoopLoopScheduler);
    thisScheduler.add(AM_LoopLoopScheduler);
    thisScheduler.add(AM_LoopLoopEnd);
    const CF_LoopLoopScheduler = new Scheduler(psychoJS);
    thisScheduler.add(CF_LoopLoopBegin, CF_LoopLoopScheduler);
    thisScheduler.add(CF_LoopLoopScheduler);
    thisScheduler.add(CF_LoopLoopEnd);
    const CM_LoopLoopScheduler = new Scheduler(psychoJS);
    thisScheduler.add(CM_LoopLoopBegin, CM_LoopLoopScheduler);
    thisScheduler.add(CM_LoopLoopScheduler);
    thisScheduler.add(CM_LoopLoopEnd);
    thisScheduler.add(endLoopIteration(thisScheduler, snapshot));
  });

  return Scheduler.Event.NEXT;
}

function AF_LoopLoopBegin(thisScheduler) {
  // set up handler to look after randomisation of conditions etc
  AF_Loop = new TrialHandler({
    psychoJS: psychoJS,
    nReps: AF_rep, method: TrialHandler.Method.RANDOM,
    extraInfo: expInfo, originPath: undefined,
    trialList: AFcondition,
    seed: undefined, name: 'AF_Loop'
  });
  psychoJS.experiment.addLoop(AF_Loop); // add the loop to the experiment
  currentLoop = AF_Loop;  // we're now the current loop

  // Schedule all the trials in the trialList:
  AF_Loop.forEach(function() {
    const snapshot = AF_Loop.getSnapshot();

    thisScheduler.add(importConditions(snapshot));
    thisScheduler.add(AsianFRoutineBegin(snapshot));
    thisScheduler.add(AsianFRoutineEachFrame(snapshot));
    thisScheduler.add(AsianFRoutineEnd(snapshot));
    thisScheduler.add(Blank500RoutineBegin(snapshot));
    thisScheduler.add(Blank500RoutineEachFrame(snapshot));
    thisScheduler.add(Blank500RoutineEnd(snapshot));
    thisScheduler.add(endLoopIteration(thisScheduler, snapshot));
  });

  return Scheduler.Event.NEXT;
}

function AF_LoopLoopEnd() {
  psychoJS.experiment.removeLoop(AF_Loop);

  return Scheduler.Event.NEXT;
}

function AM_LoopLoopBegin(thisScheduler) {
  // set up handler to look after randomisation of conditions etc
  AM_Loop = new TrialHandler({
    psychoJS: psychoJS,
    nReps: AM_rep, method: TrialHandler.Method.RANDOM,
    extraInfo: expInfo, originPath: undefined,
    trialList: AMcondition,
    seed: undefined, name: 'AM_Loop'
  });
  psychoJS.experiment.addLoop(AM_Loop); // add the loop to the experiment
  currentLoop = AM_Loop;  // we're now the current loop

  // Schedule all the trials in the trialList:
  AM_Loop.forEach(function() {
    const snapshot = AM_Loop.getSnapshot();

    thisScheduler.add(importConditions(snapshot));
    thisScheduler.add(AsianMRoutineBegin(snapshot));
    thisScheduler.add(AsianMRoutineEachFrame(snapshot));
    thisScheduler.add(AsianMRoutineEnd(snapshot));
    thisScheduler.add(Blank500RoutineBegin(snapshot));
    thisScheduler.add(Blank500RoutineEachFrame(snapshot));
    thisScheduler.add(Blank500RoutineEnd(snapshot));
    thisScheduler.add(endLoopIteration(thisScheduler, snapshot));
  });

  return Scheduler.Event.NEXT;
}

function AM_LoopLoopEnd() {
  psychoJS.experiment.removeLoop(AM_Loop);

  return Scheduler.Event.NEXT;
}

function CF_LoopLoopBegin(thisScheduler) {
  // set up handler to look after randomisation of conditions etc
  CF_Loop = new TrialHandler({
    psychoJS: psychoJS,
    nReps: CF_rep, method: TrialHandler.Method.RANDOM,
    extraInfo: expInfo, originPath: undefined,
    trialList: CFcondition,
    seed: undefined, name: 'CF_Loop'
  });
  psychoJS.experiment.addLoop(CF_Loop); // add the loop to the experiment
  currentLoop = CF_Loop;  // we're now the current loop

  // Schedule all the trials in the trialList:
  CF_Loop.forEach(function() {
    const snapshot = CF_Loop.getSnapshot();

    thisScheduler.add(importConditions(snapshot));
    thisScheduler.add(CaucasianFRoutineBegin(snapshot));
    thisScheduler.add(CaucasianFRoutineEachFrame(snapshot));
    thisScheduler.add(CaucasianFRoutineEnd(snapshot));
    thisScheduler.add(Blank500RoutineBegin(snapshot));
    thisScheduler.add(Blank500RoutineEachFrame(snapshot));
    thisScheduler.add(Blank500RoutineEnd(snapshot));
    thisScheduler.add(endLoopIteration(thisScheduler, snapshot));
  });

  return Scheduler.Event.NEXT;
}

function CF_LoopLoopEnd() {
  psychoJS.experiment.removeLoop(CF_Loop);

  return Scheduler.Event.NEXT;
}

function CM_LoopLoopBegin(thisScheduler) {
  // set up handler to look after randomisation of conditions etc
  CM_Loop = new TrialHandler({
    psychoJS: psychoJS,
    nReps: CM_rep, method: TrialHandler.Method.RANDOM,
    extraInfo: expInfo, originPath: undefined,
    trialList: CMcondition,
    seed: undefined, name: 'CM_Loop'
  });
  psychoJS.experiment.addLoop(CM_Loop); // add the loop to the experiment
  currentLoop = CM_Loop;  // we're now the current loop

  // Schedule all the trials in the trialList:
  CM_Loop.forEach(function() {
    const snapshot = CM_Loop.getSnapshot();

    thisScheduler.add(importConditions(snapshot));
    thisScheduler.add(CaucasianMRoutineBegin(snapshot));
    thisScheduler.add(CaucasianMRoutineEachFrame(snapshot));
    thisScheduler.add(CaucasianMRoutineEnd(snapshot));
    thisScheduler.add(Blank500RoutineBegin(snapshot));
    thisScheduler.add(Blank500RoutineEachFrame(snapshot));
    thisScheduler.add(Blank500RoutineEnd(snapshot));
    thisScheduler.add(endLoopIteration(thisScheduler, snapshot));
  });

  return Scheduler.Event.NEXT;
}

function CM_LoopLoopEnd() {
  psychoJS.experiment.removeLoop(CM_Loop);

  return Scheduler.Event.NEXT;
}

function BlockTrailLoopEnd() {
  psychoJS.experiment.removeLoop(BlockTrail);

  return Scheduler.Event.NEXT;
}

function PractiseRoutineBegin(trials) {
  return function () {
    //------Prepare to start Routine 'Practise'-------
    t = 0;
    PractiseClock.reset(); // clock
    frameN = -1;
    routineTimer.add(3.500000);
    // update component parameters for each repeat
    PracMouse.setPos({"newPos": [0, 0]});
    
    Upper_image.setImage(UImage);
    Lower_image.setImage(LImage);
    // setup some python lists for storing info about the PracMouse
    PracMouse.clicked_name = [];
    PracMouse.clicked_pos = [];
    gotValidClick = false; // until a click is received
    // keep track of which components have finished
    PractiseComponents = [];
    PractiseComponents.push(Fixation0);
    PractiseComponents.push(Upper_image);
    PractiseComponents.push(Lower_image);
    PractiseComponents.push(PracMouse);
    
    PractiseComponents.forEach( function(thisComponent) {
      if ('status' in thisComponent)
        thisComponent.status = PsychoJS.Status.NOT_STARTED;
       });
    
    return Scheduler.Event.NEXT;
  };
}

function PractiseRoutineEachFrame(trials) {
  return function () {
    //------Loop for each frame of Routine 'Practise'-------
    let continueRoutine = true; // until we're told otherwise
    // get current time
    t = PractiseClock.getTime();
    frameN = frameN + 1;// number of completed frames (so 0 is the first frame)
    // update/draw components on each frame
    
    // *Fixation0* updates
    if (t >= 0.0 && Fixation0.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      Fixation0.tStart = t;  // (not accounting for frame time here)
      Fixation0.frameNStart = frameN;  // exact frame index
      
      Fixation0.setAutoDraw(true);
    }

    frameRemains = 0.0 + 0.5 - psychoJS.window.monitorFramePeriod * 0.75;  // most of one frame period left
    if (Fixation0.status === PsychoJS.Status.STARTED && t >= frameRemains) {
      Fixation0.setAutoDraw(false);
    }
    
    // *Upper_image* updates
    if (t >= 0.5 && Upper_image.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      Upper_image.tStart = t;  // (not accounting for frame time here)
      Upper_image.frameNStart = frameN;  // exact frame index
      
      Upper_image.setAutoDraw(true);
    }

    frameRemains = 0.5 + 3 - psychoJS.window.monitorFramePeriod * 0.75;  // most of one frame period left
    if (Upper_image.status === PsychoJS.Status.STARTED && t >= frameRemains) {
      Upper_image.setAutoDraw(false);
    }
    
    // *Lower_image* updates
    if (t >= 0.5 && Lower_image.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      Lower_image.tStart = t;  // (not accounting for frame time here)
      Lower_image.frameNStart = frameN;  // exact frame index
      
      Lower_image.setAutoDraw(true);
    }

    frameRemains = 0.5 + 3 - psychoJS.window.monitorFramePeriod * 0.75;  // most of one frame period left
    if (Lower_image.status === PsychoJS.Status.STARTED && t >= frameRemains) {
      Lower_image.setAutoDraw(false);
    }
    // *PracMouse* updates
    if (t >= 0.5 && PracMouse.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      PracMouse.tStart = t;  // (not accounting for frame time here)
      PracMouse.frameNStart = frameN;  // exact frame index
      
      PracMouse.status = PsychoJS.Status.STARTED;
      PracMouse.mouseClock.reset();
      prevButtonState = PracMouse.getPressed();  // if button is down already this ISN'T a new click
      }
    frameRemains = 0.5 + 3 - psychoJS.window.monitorFramePeriod * 0.75;  // most of one frame period left
    if (PracMouse.status === PsychoJS.Status.STARTED && t >= frameRemains) {
      PracMouse.status = PsychoJS.Status.FINISHED;
  }
    if (PracMouse.status === PsychoJS.Status.STARTED) {  // only update if started and not finished!
      let buttons = PracMouse.getPressed();
      if (!buttons.every( (e,i,) => (e == prevButtonState[i]) )) { // button state changed?
        prevButtonState = buttons;
        if (buttons.reduce( (e, acc) => (e+acc) ) > 0) { // state changed to a new click
          // check if the mouse was inside our 'clickable' objects
          gotValidClick = false;
          for (const obj of [Upper_image,Lower_image]) {
            if (obj.contains(PracMouse)) {
              gotValidClick = true;
              PracMouse.clicked_name.push(obj.name)
              PracMouse.clicked_pos.push(obj.pos)
            }
          }
          if (gotValidClick === true) { // abort routine on response
            continueRoutine = false;
          }
        }
      }
    }
    // check for quit (typically the Esc key)
    if (psychoJS.experiment.experimentEnded || psychoJS.eventManager.getKeys({keyList:['escape']}).length > 0) {
      return quitPsychoJS('The [Escape] key was pressed. Goodbye!', false);
    }
    
    // check if the Routine should terminate
    if (!continueRoutine) {  // a component has requested a forced-end of Routine
      return Scheduler.Event.NEXT;
    }
    
    continueRoutine = false;  // reverts to True if at least one component still running
    PractiseComponents.forEach( function(thisComponent) {
      if ('status' in thisComponent && thisComponent.status !== PsychoJS.Status.FINISHED) {
        continueRoutine = true;
      }
    });
    
    // refresh the screen if continuing
    if (continueRoutine && routineTimer.getTime() > 0) {
      return Scheduler.Event.FLIP_REPEAT;
    } else {
      return Scheduler.Event.NEXT;
    }
  };
}

function PractiseRoutineEnd(trials) {
  return function () {
    //------Ending Routine 'Practise'-------
    PractiseComponents.forEach( function(thisComponent) {
      if (typeof thisComponent.setAutoDraw === 'function') {
        thisComponent.setAutoDraw(false);
      }
    });
    // store data for thisExp (ExperimentHandler)
    const xys = PracMouse.getPos();
    const buttons = PracMouse.getPressed();
    psychoJS.experiment.addData('PracMouse.x', xys[0]);
    psychoJS.experiment.addData('PracMouse.y', xys[1]);
    psychoJS.experiment.addData('PracMouse.leftButton', buttons[0]);
    psychoJS.experiment.addData('PracMouse.midButton', buttons[1]);
    psychoJS.experiment.addData('PracMouse.rightButton', buttons[2]);
    if (PracMouse.clicked_name.length > 0) {
      psychoJS.experiment.addData('PracMouse.clicked_name', PracMouse.clicked_name[0]);}
    if (PracMouse.clicked_pos.length > 0) {
      psychoJS.experiment.addData('PracMouse.clicked_pos', PracMouse.clicked_pos[0]);}
    return Scheduler.Event.NEXT;
  };
}

function Blank500RoutineBegin(trials) {
  return function () {
    //------Prepare to start Routine 'Blank500'-------
    t = 0;
    Blank500Clock.reset(); // clock
    frameN = -1;
    routineTimer.add(0.500000);
    // update component parameters for each repeat
    // keep track of which components have finished
    Blank500Components = [];
    Blank500Components.push(BlankTest);
    
    Blank500Components.forEach( function(thisComponent) {
      if ('status' in thisComponent)
        thisComponent.status = PsychoJS.Status.NOT_STARTED;
       });
    
    return Scheduler.Event.NEXT;
  };
}

function Blank500RoutineEachFrame(trials) {
  return function () {
    //------Loop for each frame of Routine 'Blank500'-------
    let continueRoutine = true; // until we're told otherwise
    // get current time
    t = Blank500Clock.getTime();
    frameN = frameN + 1;// number of completed frames (so 0 is the first frame)
    // update/draw components on each frame
    
    // *BlankTest* updates
    if (t >= 0.0 && BlankTest.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      BlankTest.tStart = t;  // (not accounting for frame time here)
      BlankTest.frameNStart = frameN;  // exact frame index
      
      BlankTest.setAutoDraw(true);
    }

    frameRemains = 0.0 + 0.5 - psychoJS.window.monitorFramePeriod * 0.75;  // most of one frame period left
    if (BlankTest.status === PsychoJS.Status.STARTED && t >= frameRemains) {
      BlankTest.setAutoDraw(false);
    }
    // check for quit (typically the Esc key)
    if (psychoJS.experiment.experimentEnded || psychoJS.eventManager.getKeys({keyList:['escape']}).length > 0) {
      return quitPsychoJS('The [Escape] key was pressed. Goodbye!', false);
    }
    
    // check if the Routine should terminate
    if (!continueRoutine) {  // a component has requested a forced-end of Routine
      return Scheduler.Event.NEXT;
    }
    
    continueRoutine = false;  // reverts to True if at least one component still running
    Blank500Components.forEach( function(thisComponent) {
      if ('status' in thisComponent && thisComponent.status !== PsychoJS.Status.FINISHED) {
        continueRoutine = true;
      }
    });
    
    // refresh the screen if continuing
    if (continueRoutine && routineTimer.getTime() > 0) {
      return Scheduler.Event.FLIP_REPEAT;
    } else {
      return Scheduler.Event.NEXT;
    }
  };
}

function Blank500RoutineEnd(trials) {
  return function () {
    //------Ending Routine 'Blank500'-------
    Blank500Components.forEach( function(thisComponent) {
      if (typeof thisComponent.setAutoDraw === 'function') {
        thisComponent.setAutoDraw(false);
      }
    });
    return Scheduler.Event.NEXT;
  };
}

function BreakRoutineBegin(trials) {
  return function () {
    //------Prepare to start Routine 'Break'-------
    t = 0;
    BreakClock.reset(); // clock
    frameN = -1;
    // update component parameters for each repeat
    Prac_Key.keys = undefined;
    Prac_Key.rt = undefined;
    _Prac_Key_allKeys = [];
    // keep track of which components have finished
    BreakComponents = [];
    BreakComponents.push(BreakText);
    BreakComponents.push(Prac_Key);
    
    BreakComponents.forEach( function(thisComponent) {
      if ('status' in thisComponent)
        thisComponent.status = PsychoJS.Status.NOT_STARTED;
       });
    
    return Scheduler.Event.NEXT;
  };
}

function BreakRoutineEachFrame(trials) {
  return function () {
    //------Loop for each frame of Routine 'Break'-------
    let continueRoutine = true; // until we're told otherwise
    // get current time
    t = BreakClock.getTime();
    frameN = frameN + 1;// number of completed frames (so 0 is the first frame)
    // update/draw components on each frame
    
    // *BreakText* updates
    if (t >= 0.0 && BreakText.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      BreakText.tStart = t;  // (not accounting for frame time here)
      BreakText.frameNStart = frameN;  // exact frame index
      
      BreakText.setAutoDraw(true);
    }

    
    // *Prac_Key* updates
    if (t >= 0.0 && Prac_Key.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      Prac_Key.tStart = t;  // (not accounting for frame time here)
      Prac_Key.frameNStart = frameN;  // exact frame index
      
      // keyboard checking is just starting
      psychoJS.window.callOnFlip(function() { Prac_Key.clock.reset(); });  // t=0 on next screen flip
      psychoJS.window.callOnFlip(function() { Prac_Key.start(); }); // start on screen flip
      psychoJS.window.callOnFlip(function() { Prac_Key.clearEvents(); });
    }

    if (Prac_Key.status === PsychoJS.Status.STARTED) {
      let theseKeys = Prac_Key.getKeys({keyList: ['space'], waitRelease: false});
      _Prac_Key_allKeys = _Prac_Key_allKeys.concat(theseKeys);
      if (_Prac_Key_allKeys.length > 0) {
        Prac_Key.keys = _Prac_Key_allKeys[_Prac_Key_allKeys.length - 1].name;  // just the last key pressed
        Prac_Key.rt = _Prac_Key_allKeys[_Prac_Key_allKeys.length - 1].rt;
        // a response ends the routine
        continueRoutine = false;
      }
    }
    
    // check for quit (typically the Esc key)
    if (psychoJS.experiment.experimentEnded || psychoJS.eventManager.getKeys({keyList:['escape']}).length > 0) {
      return quitPsychoJS('The [Escape] key was pressed. Goodbye!', false);
    }
    
    // check if the Routine should terminate
    if (!continueRoutine) {  // a component has requested a forced-end of Routine
      return Scheduler.Event.NEXT;
    }
    
    continueRoutine = false;  // reverts to True if at least one component still running
    BreakComponents.forEach( function(thisComponent) {
      if ('status' in thisComponent && thisComponent.status !== PsychoJS.Status.FINISHED) {
        continueRoutine = true;
      }
    });
    
    // refresh the screen if continuing
    if (continueRoutine) {
      return Scheduler.Event.FLIP_REPEAT;
    } else {
      return Scheduler.Event.NEXT;
    }
  };
}

function BreakRoutineEnd(trials) {
  return function () {
    //------Ending Routine 'Break'-------
    BreakComponents.forEach( function(thisComponent) {
      if (typeof thisComponent.setAutoDraw === 'function') {
        thisComponent.setAutoDraw(false);
      }
    });
    psychoJS.experiment.addData('Prac_Key.keys', Prac_Key.keys);
    if (typeof Prac_Key.keys !== 'undefined') {  // we had a response
        psychoJS.experiment.addData('Prac_Key.rt', Prac_Key.rt);
        routineTimer.reset();
        }
    
    Prac_Key.stop();
    // the Routine "Break" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset();
    
    return Scheduler.Event.NEXT;
  };
}

function AsianFRoutineBegin(trials) {
  return function () {
    //------Prepare to start Routine 'AsianF'-------
    t = 0;
    AsianFClock.reset(); // clock
    frameN = -1;
    routineTimer.add(3.500000);
    // update component parameters for each repeat
    AFMouse.setPos({"newPos": [0, 0]});
    
    AF_image_1.setImage(Upper_Image);
    AF_image_2.setImage(Lower_Image);
    // setup some python lists for storing info about the AFMouse
    AFMouse.clicked_name = [];
    AFMouse.clicked_pos = [];
    gotValidClick = false; // until a click is received
    // keep track of which components have finished
    AsianFComponents = [];
    AsianFComponents.push(Fixation);
    AsianFComponents.push(AF_image_1);
    AsianFComponents.push(AF_image_2);
    AsianFComponents.push(AFMouse);
    
    AsianFComponents.forEach( function(thisComponent) {
      if ('status' in thisComponent)
        thisComponent.status = PsychoJS.Status.NOT_STARTED;
       });
    
    return Scheduler.Event.NEXT;
  };
}

function AsianFRoutineEachFrame(trials) {
  return function () {
    //------Loop for each frame of Routine 'AsianF'-------
    let continueRoutine = true; // until we're told otherwise
    // get current time
    t = AsianFClock.getTime();
    frameN = frameN + 1;// number of completed frames (so 0 is the first frame)
    // update/draw components on each frame
    
    // *Fixation* updates
    if (t >= 0.0 && Fixation.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      Fixation.tStart = t;  // (not accounting for frame time here)
      Fixation.frameNStart = frameN;  // exact frame index
      
      Fixation.setAutoDraw(true);
    }

    frameRemains = 0.0 + 0.5 - psychoJS.window.monitorFramePeriod * 0.75;  // most of one frame period left
    if (Fixation.status === PsychoJS.Status.STARTED && t >= frameRemains) {
      Fixation.setAutoDraw(false);
    }
    
    // *AF_image_1* updates
    if (t >= 0.5 && AF_image_1.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      AF_image_1.tStart = t;  // (not accounting for frame time here)
      AF_image_1.frameNStart = frameN;  // exact frame index
      
      AF_image_1.setAutoDraw(true);
    }

    frameRemains = 0.5 + 3 - psychoJS.window.monitorFramePeriod * 0.75;  // most of one frame period left
    if (AF_image_1.status === PsychoJS.Status.STARTED && t >= frameRemains) {
      AF_image_1.setAutoDraw(false);
    }
    
    // *AF_image_2* updates
    if (t >= 0.5 && AF_image_2.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      AF_image_2.tStart = t;  // (not accounting for frame time here)
      AF_image_2.frameNStart = frameN;  // exact frame index
      
      AF_image_2.setAutoDraw(true);
    }

    frameRemains = 0.5 + 3 - psychoJS.window.monitorFramePeriod * 0.75;  // most of one frame period left
    if (AF_image_2.status === PsychoJS.Status.STARTED && t >= frameRemains) {
      AF_image_2.setAutoDraw(false);
    }
    // *AFMouse* updates
    if (t >= 0.5 && AFMouse.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      AFMouse.tStart = t;  // (not accounting for frame time here)
      AFMouse.frameNStart = frameN;  // exact frame index
      
      AFMouse.status = PsychoJS.Status.STARTED;
      AFMouse.mouseClock.reset();
      prevButtonState = AFMouse.getPressed();  // if button is down already this ISN'T a new click
      }
    frameRemains = 0.5 + 3 - psychoJS.window.monitorFramePeriod * 0.75;  // most of one frame period left
    if (AFMouse.status === PsychoJS.Status.STARTED && t >= frameRemains) {
      AFMouse.status = PsychoJS.Status.FINISHED;
  }
    if (AFMouse.status === PsychoJS.Status.STARTED) {  // only update if started and not finished!
      let buttons = AFMouse.getPressed();
      if (!buttons.every( (e,i,) => (e == prevButtonState[i]) )) { // button state changed?
        prevButtonState = buttons;
        if (buttons.reduce( (e, acc) => (e+acc) ) > 0) { // state changed to a new click
          // check if the mouse was inside our 'clickable' objects
          gotValidClick = false;
          for (const obj of [AF_image_1,AF_image_2]) {
            if (obj.contains(AFMouse)) {
              gotValidClick = true;
              AFMouse.clicked_name.push(obj.name)
              AFMouse.clicked_pos.push(obj.pos)
            }
          }
          if (gotValidClick === true) { // abort routine on response
            continueRoutine = false;
          }
        }
      }
    }
    // check for quit (typically the Esc key)
    if (psychoJS.experiment.experimentEnded || psychoJS.eventManager.getKeys({keyList:['escape']}).length > 0) {
      return quitPsychoJS('The [Escape] key was pressed. Goodbye!', false);
    }
    
    // check if the Routine should terminate
    if (!continueRoutine) {  // a component has requested a forced-end of Routine
      return Scheduler.Event.NEXT;
    }
    
    continueRoutine = false;  // reverts to True if at least one component still running
    AsianFComponents.forEach( function(thisComponent) {
      if ('status' in thisComponent && thisComponent.status !== PsychoJS.Status.FINISHED) {
        continueRoutine = true;
      }
    });
    
    // refresh the screen if continuing
    if (continueRoutine && routineTimer.getTime() > 0) {
      return Scheduler.Event.FLIP_REPEAT;
    } else {
      return Scheduler.Event.NEXT;
    }
  };
}

function AsianFRoutineEnd(trials) {
  return function () {
    //------Ending Routine 'AsianF'-------
    AsianFComponents.forEach( function(thisComponent) {
      if (typeof thisComponent.setAutoDraw === 'function') {
        thisComponent.setAutoDraw(false);
      }
    });
    // store data for thisExp (ExperimentHandler)
    const xys = AFMouse.getPos();
    const buttons = AFMouse.getPressed();
    psychoJS.experiment.addData('AFMouse.x', xys[0]);
    psychoJS.experiment.addData('AFMouse.y', xys[1]);
    psychoJS.experiment.addData('AFMouse.leftButton', buttons[0]);
    psychoJS.experiment.addData('AFMouse.midButton', buttons[1]);
    psychoJS.experiment.addData('AFMouse.rightButton', buttons[2]);
    if (AFMouse.clicked_name.length > 0) {
      psychoJS.experiment.addData('AFMouse.clicked_name', AFMouse.clicked_name[0]);}
    if (AFMouse.clicked_pos.length > 0) {
      psychoJS.experiment.addData('AFMouse.clicked_pos', AFMouse.clicked_pos[0]);}
    return Scheduler.Event.NEXT;
  };
}

function AsianMRoutineBegin(trials) {
  return function () {
    //------Prepare to start Routine 'AsianM'-------
    t = 0;
    AsianMClock.reset(); // clock
    frameN = -1;
    routineTimer.add(3.500000);
    // update component parameters for each repeat
    AMMouse.setPos({"newPos": [0, 0]});
    
    AM_image_1.setImage(Upper_Image);
    AM_imgae_2.setImage(Lower_Image);
    // setup some python lists for storing info about the AMMouse
    AMMouse.clicked_name = [];
    AMMouse.clicked_pos = [];
    gotValidClick = false; // until a click is received
    // keep track of which components have finished
    AsianMComponents = [];
    AsianMComponents.push(Fixation2);
    AsianMComponents.push(AM_image_1);
    AsianMComponents.push(AM_imgae_2);
    AsianMComponents.push(AMMouse);
    
    AsianMComponents.forEach( function(thisComponent) {
      if ('status' in thisComponent)
        thisComponent.status = PsychoJS.Status.NOT_STARTED;
       });
    
    return Scheduler.Event.NEXT;
  };
}

function AsianMRoutineEachFrame(trials) {
  return function () {
    //------Loop for each frame of Routine 'AsianM'-------
    let continueRoutine = true; // until we're told otherwise
    // get current time
    t = AsianMClock.getTime();
    frameN = frameN + 1;// number of completed frames (so 0 is the first frame)
    // update/draw components on each frame
    
    // *Fixation2* updates
    if (t >= 0.0 && Fixation2.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      Fixation2.tStart = t;  // (not accounting for frame time here)
      Fixation2.frameNStart = frameN;  // exact frame index
      
      Fixation2.setAutoDraw(true);
    }

    frameRemains = 0.0 + 0.5 - psychoJS.window.monitorFramePeriod * 0.75;  // most of one frame period left
    if (Fixation2.status === PsychoJS.Status.STARTED && t >= frameRemains) {
      Fixation2.setAutoDraw(false);
    }
    
    // *AM_image_1* updates
    if (t >= 0.5 && AM_image_1.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      AM_image_1.tStart = t;  // (not accounting for frame time here)
      AM_image_1.frameNStart = frameN;  // exact frame index
      
      AM_image_1.setAutoDraw(true);
    }

    frameRemains = 0.5 + 3 - psychoJS.window.monitorFramePeriod * 0.75;  // most of one frame period left
    if (AM_image_1.status === PsychoJS.Status.STARTED && t >= frameRemains) {
      AM_image_1.setAutoDraw(false);
    }
    
    // *AM_imgae_2* updates
    if (t >= 0.5 && AM_imgae_2.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      AM_imgae_2.tStart = t;  // (not accounting for frame time here)
      AM_imgae_2.frameNStart = frameN;  // exact frame index
      
      AM_imgae_2.setAutoDraw(true);
    }

    frameRemains = 0.5 + 3 - psychoJS.window.monitorFramePeriod * 0.75;  // most of one frame period left
    if (AM_imgae_2.status === PsychoJS.Status.STARTED && t >= frameRemains) {
      AM_imgae_2.setAutoDraw(false);
    }
    // *AMMouse* updates
    if (t >= 0.5 && AMMouse.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      AMMouse.tStart = t;  // (not accounting for frame time here)
      AMMouse.frameNStart = frameN;  // exact frame index
      
      AMMouse.status = PsychoJS.Status.STARTED;
      AMMouse.mouseClock.reset();
      prevButtonState = AMMouse.getPressed();  // if button is down already this ISN'T a new click
      }
    if (AMMouse.status === PsychoJS.Status.STARTED && Boolean(3)) {
      AMMouse.status = PsychoJS.Status.FINISHED;
  }
    if (AMMouse.status === PsychoJS.Status.STARTED) {  // only update if started and not finished!
      let buttons = AMMouse.getPressed();
      if (!buttons.every( (e,i,) => (e == prevButtonState[i]) )) { // button state changed?
        prevButtonState = buttons;
        if (buttons.reduce( (e, acc) => (e+acc) ) > 0) { // state changed to a new click
          // check if the mouse was inside our 'clickable' objects
          gotValidClick = false;
          for (const obj of [AM_image_1,AM_imgae_2]) {
            if (obj.contains(AMMouse)) {
              gotValidClick = true;
              AMMouse.clicked_name.push(obj.name)
              AMMouse.clicked_pos.push(obj.pos)
            }
          }
          if (gotValidClick === true) { // abort routine on response
            continueRoutine = false;
          }
        }
      }
    }
    // check for quit (typically the Esc key)
    if (psychoJS.experiment.experimentEnded || psychoJS.eventManager.getKeys({keyList:['escape']}).length > 0) {
      return quitPsychoJS('The [Escape] key was pressed. Goodbye!', false);
    }
    
    // check if the Routine should terminate
    if (!continueRoutine) {  // a component has requested a forced-end of Routine
      return Scheduler.Event.NEXT;
    }
    
    continueRoutine = false;  // reverts to True if at least one component still running
    AsianMComponents.forEach( function(thisComponent) {
      if ('status' in thisComponent && thisComponent.status !== PsychoJS.Status.FINISHED) {
        continueRoutine = true;
      }
    });
    
    // refresh the screen if continuing
    if (continueRoutine && routineTimer.getTime() > 0) {
      return Scheduler.Event.FLIP_REPEAT;
    } else {
      return Scheduler.Event.NEXT;
    }
  };
}

function AsianMRoutineEnd(trials) {
  return function () {
    //------Ending Routine 'AsianM'-------
    AsianMComponents.forEach( function(thisComponent) {
      if (typeof thisComponent.setAutoDraw === 'function') {
        thisComponent.setAutoDraw(false);
      }
    });
    // store data for thisExp (ExperimentHandler)
    const xys = AMMouse.getPos();
    const buttons = AMMouse.getPressed();
    psychoJS.experiment.addData('AMMouse.x', xys[0]);
    psychoJS.experiment.addData('AMMouse.y', xys[1]);
    psychoJS.experiment.addData('AMMouse.leftButton', buttons[0]);
    psychoJS.experiment.addData('AMMouse.midButton', buttons[1]);
    psychoJS.experiment.addData('AMMouse.rightButton', buttons[2]);
    if (AMMouse.clicked_name.length > 0) {
      psychoJS.experiment.addData('AMMouse.clicked_name', AMMouse.clicked_name[0]);}
    if (AMMouse.clicked_pos.length > 0) {
      psychoJS.experiment.addData('AMMouse.clicked_pos', AMMouse.clicked_pos[0]);}
    return Scheduler.Event.NEXT;
  };
}

function CaucasianFRoutineBegin(trials) {
  return function () {
    //------Prepare to start Routine 'CaucasianF'-------
    t = 0;
    CaucasianFClock.reset(); // clock
    frameN = -1;
    routineTimer.add(3.500000);
    // update component parameters for each repeat
    CFMouse.setPos({"newPos": [0, 0]});
    
    CF_image_1.setImage(Upper_Image);
    CF_image_2.setImage(Lower_Image);
    // setup some python lists for storing info about the CFMouse
    CFMouse.clicked_name = [];
    CFMouse.clicked_pos = [];
    gotValidClick = false; // until a click is received
    // keep track of which components have finished
    CaucasianFComponents = [];
    CaucasianFComponents.push(Fixation3);
    CaucasianFComponents.push(CF_image_1);
    CaucasianFComponents.push(CF_image_2);
    CaucasianFComponents.push(CFMouse);
    
    CaucasianFComponents.forEach( function(thisComponent) {
      if ('status' in thisComponent)
        thisComponent.status = PsychoJS.Status.NOT_STARTED;
       });
    
    return Scheduler.Event.NEXT;
  };
}

function CaucasianFRoutineEachFrame(trials) {
  return function () {
    //------Loop for each frame of Routine 'CaucasianF'-------
    let continueRoutine = true; // until we're told otherwise
    // get current time
    t = CaucasianFClock.getTime();
    frameN = frameN + 1;// number of completed frames (so 0 is the first frame)
    // update/draw components on each frame
    
    // *Fixation3* updates
    if (t >= 0.0 && Fixation3.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      Fixation3.tStart = t;  // (not accounting for frame time here)
      Fixation3.frameNStart = frameN;  // exact frame index
      
      Fixation3.setAutoDraw(true);
    }

    frameRemains = 0.0 + 0.5 - psychoJS.window.monitorFramePeriod * 0.75;  // most of one frame period left
    if (Fixation3.status === PsychoJS.Status.STARTED && t >= frameRemains) {
      Fixation3.setAutoDraw(false);
    }
    
    // *CF_image_1* updates
    if (t >= 0.5 && CF_image_1.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      CF_image_1.tStart = t;  // (not accounting for frame time here)
      CF_image_1.frameNStart = frameN;  // exact frame index
      
      CF_image_1.setAutoDraw(true);
    }

    frameRemains = 0.5 + 3 - psychoJS.window.monitorFramePeriod * 0.75;  // most of one frame period left
    if (CF_image_1.status === PsychoJS.Status.STARTED && t >= frameRemains) {
      CF_image_1.setAutoDraw(false);
    }
    
    // *CF_image_2* updates
    if (t >= 0.5 && CF_image_2.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      CF_image_2.tStart = t;  // (not accounting for frame time here)
      CF_image_2.frameNStart = frameN;  // exact frame index
      
      CF_image_2.setAutoDraw(true);
    }

    frameRemains = 0.5 + 3 - psychoJS.window.monitorFramePeriod * 0.75;  // most of one frame period left
    if (CF_image_2.status === PsychoJS.Status.STARTED && t >= frameRemains) {
      CF_image_2.setAutoDraw(false);
    }
    // *CFMouse* updates
    if (t >= 0.5 && CFMouse.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      CFMouse.tStart = t;  // (not accounting for frame time here)
      CFMouse.frameNStart = frameN;  // exact frame index
      
      CFMouse.status = PsychoJS.Status.STARTED;
      CFMouse.mouseClock.reset();
      prevButtonState = CFMouse.getPressed();  // if button is down already this ISN'T a new click
      }
    frameRemains = 0.5 + 3 - psychoJS.window.monitorFramePeriod * 0.75;  // most of one frame period left
    if (CFMouse.status === PsychoJS.Status.STARTED && t >= frameRemains) {
      CFMouse.status = PsychoJS.Status.FINISHED;
  }
    if (CFMouse.status === PsychoJS.Status.STARTED) {  // only update if started and not finished!
      let buttons = CFMouse.getPressed();
      if (!buttons.every( (e,i,) => (e == prevButtonState[i]) )) { // button state changed?
        prevButtonState = buttons;
        if (buttons.reduce( (e, acc) => (e+acc) ) > 0) { // state changed to a new click
          // check if the mouse was inside our 'clickable' objects
          gotValidClick = false;
          for (const obj of [CF_image_1,CF_image_2]) {
            if (obj.contains(CFMouse)) {
              gotValidClick = true;
              CFMouse.clicked_name.push(obj.name)
              CFMouse.clicked_pos.push(obj.pos)
            }
          }
          if (gotValidClick === true) { // abort routine on response
            continueRoutine = false;
          }
        }
      }
    }
    // check for quit (typically the Esc key)
    if (psychoJS.experiment.experimentEnded || psychoJS.eventManager.getKeys({keyList:['escape']}).length > 0) {
      return quitPsychoJS('The [Escape] key was pressed. Goodbye!', false);
    }
    
    // check if the Routine should terminate
    if (!continueRoutine) {  // a component has requested a forced-end of Routine
      return Scheduler.Event.NEXT;
    }
    
    continueRoutine = false;  // reverts to True if at least one component still running
    CaucasianFComponents.forEach( function(thisComponent) {
      if ('status' in thisComponent && thisComponent.status !== PsychoJS.Status.FINISHED) {
        continueRoutine = true;
      }
    });
    
    // refresh the screen if continuing
    if (continueRoutine && routineTimer.getTime() > 0) {
      return Scheduler.Event.FLIP_REPEAT;
    } else {
      return Scheduler.Event.NEXT;
    }
  };
}

function CaucasianFRoutineEnd(trials) {
  return function () {
    //------Ending Routine 'CaucasianF'-------
    CaucasianFComponents.forEach( function(thisComponent) {
      if (typeof thisComponent.setAutoDraw === 'function') {
        thisComponent.setAutoDraw(false);
      }
    });
    // store data for thisExp (ExperimentHandler)
    const xys = CFMouse.getPos();
    const buttons = CFMouse.getPressed();
    psychoJS.experiment.addData('CFMouse.x', xys[0]);
    psychoJS.experiment.addData('CFMouse.y', xys[1]);
    psychoJS.experiment.addData('CFMouse.leftButton', buttons[0]);
    psychoJS.experiment.addData('CFMouse.midButton', buttons[1]);
    psychoJS.experiment.addData('CFMouse.rightButton', buttons[2]);
    if (CFMouse.clicked_name.length > 0) {
      psychoJS.experiment.addData('CFMouse.clicked_name', CFMouse.clicked_name[0]);}
    if (CFMouse.clicked_pos.length > 0) {
      psychoJS.experiment.addData('CFMouse.clicked_pos', CFMouse.clicked_pos[0]);}
    return Scheduler.Event.NEXT;
  };
}

function CaucasianMRoutineBegin(trials) {
  return function () {
    //------Prepare to start Routine 'CaucasianM'-------
    t = 0;
    CaucasianMClock.reset(); // clock
    frameN = -1;
    routineTimer.add(3.500000);
    // update component parameters for each repeat
    CMMouse.setPos({"newPos": [0, 0]});
    
    CM_image_1.setImage(Upper_Image);
    CM_image_2.setImage(Lower_Image);
    // setup some python lists for storing info about the CMMouse
    CMMouse.clicked_name = [];
    CMMouse.clicked_pos = [];
    gotValidClick = false; // until a click is received
    // keep track of which components have finished
    CaucasianMComponents = [];
    CaucasianMComponents.push(Fixation4);
    CaucasianMComponents.push(CM_image_1);
    CaucasianMComponents.push(CM_image_2);
    CaucasianMComponents.push(CMMouse);
    
    CaucasianMComponents.forEach( function(thisComponent) {
      if ('status' in thisComponent)
        thisComponent.status = PsychoJS.Status.NOT_STARTED;
       });
    
    return Scheduler.Event.NEXT;
  };
}

function CaucasianMRoutineEachFrame(trials) {
  return function () {
    //------Loop for each frame of Routine 'CaucasianM'-------
    let continueRoutine = true; // until we're told otherwise
    // get current time
    t = CaucasianMClock.getTime();
    frameN = frameN + 1;// number of completed frames (so 0 is the first frame)
    // update/draw components on each frame
    
    // *Fixation4* updates
    if (t >= 0.0 && Fixation4.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      Fixation4.tStart = t;  // (not accounting for frame time here)
      Fixation4.frameNStart = frameN;  // exact frame index
      
      Fixation4.setAutoDraw(true);
    }

    frameRemains = 0.0 + 0.5 - psychoJS.window.monitorFramePeriod * 0.75;  // most of one frame period left
    if (Fixation4.status === PsychoJS.Status.STARTED && t >= frameRemains) {
      Fixation4.setAutoDraw(false);
    }
    
    // *CM_image_1* updates
    if (t >= 0.5 && CM_image_1.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      CM_image_1.tStart = t;  // (not accounting for frame time here)
      CM_image_1.frameNStart = frameN;  // exact frame index
      
      CM_image_1.setAutoDraw(true);
    }

    frameRemains = 0.5 + 3 - psychoJS.window.monitorFramePeriod * 0.75;  // most of one frame period left
    if (CM_image_1.status === PsychoJS.Status.STARTED && t >= frameRemains) {
      CM_image_1.setAutoDraw(false);
    }
    
    // *CM_image_2* updates
    if (t >= 0.5 && CM_image_2.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      CM_image_2.tStart = t;  // (not accounting for frame time here)
      CM_image_2.frameNStart = frameN;  // exact frame index
      
      CM_image_2.setAutoDraw(true);
    }

    frameRemains = 0.5 + 3 - psychoJS.window.monitorFramePeriod * 0.75;  // most of one frame period left
    if (CM_image_2.status === PsychoJS.Status.STARTED && t >= frameRemains) {
      CM_image_2.setAutoDraw(false);
    }
    // *CMMouse* updates
    if (t >= 0.5 && CMMouse.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      CMMouse.tStart = t;  // (not accounting for frame time here)
      CMMouse.frameNStart = frameN;  // exact frame index
      
      CMMouse.status = PsychoJS.Status.STARTED;
      CMMouse.mouseClock.reset();
      prevButtonState = CMMouse.getPressed();  // if button is down already this ISN'T a new click
      }
    frameRemains = 0.5 + 3 - psychoJS.window.monitorFramePeriod * 0.75;  // most of one frame period left
    if (CMMouse.status === PsychoJS.Status.STARTED && t >= frameRemains) {
      CMMouse.status = PsychoJS.Status.FINISHED;
  }
    if (CMMouse.status === PsychoJS.Status.STARTED) {  // only update if started and not finished!
      let buttons = CMMouse.getPressed();
      if (!buttons.every( (e,i,) => (e == prevButtonState[i]) )) { // button state changed?
        prevButtonState = buttons;
        if (buttons.reduce( (e, acc) => (e+acc) ) > 0) { // state changed to a new click
          // check if the mouse was inside our 'clickable' objects
          gotValidClick = false;
          for (const obj of [CM_image_1,CM_image_2]) {
            if (obj.contains(CMMouse)) {
              gotValidClick = true;
              CMMouse.clicked_name.push(obj.name)
              CMMouse.clicked_pos.push(obj.pos)
            }
          }
          if (gotValidClick === true) { // abort routine on response
            continueRoutine = false;
          }
        }
      }
    }
    // check for quit (typically the Esc key)
    if (psychoJS.experiment.experimentEnded || psychoJS.eventManager.getKeys({keyList:['escape']}).length > 0) {
      return quitPsychoJS('The [Escape] key was pressed. Goodbye!', false);
    }
    
    // check if the Routine should terminate
    if (!continueRoutine) {  // a component has requested a forced-end of Routine
      return Scheduler.Event.NEXT;
    }
    
    continueRoutine = false;  // reverts to True if at least one component still running
    CaucasianMComponents.forEach( function(thisComponent) {
      if ('status' in thisComponent && thisComponent.status !== PsychoJS.Status.FINISHED) {
        continueRoutine = true;
      }
    });
    
    // refresh the screen if continuing
    if (continueRoutine && routineTimer.getTime() > 0) {
      return Scheduler.Event.FLIP_REPEAT;
    } else {
      return Scheduler.Event.NEXT;
    }
  };
}

function CaucasianMRoutineEnd(trials) {
  return function () {
    //------Ending Routine 'CaucasianM'-------
    CaucasianMComponents.forEach( function(thisComponent) {
      if (typeof thisComponent.setAutoDraw === 'function') {
        thisComponent.setAutoDraw(false);
      }
    });
    // store data for thisExp (ExperimentHandler)
    const xys = CMMouse.getPos();
    const buttons = CMMouse.getPressed();
    psychoJS.experiment.addData('CMMouse.x', xys[0]);
    psychoJS.experiment.addData('CMMouse.y', xys[1]);
    psychoJS.experiment.addData('CMMouse.leftButton', buttons[0]);
    psychoJS.experiment.addData('CMMouse.midButton', buttons[1]);
    psychoJS.experiment.addData('CMMouse.rightButton', buttons[2]);
    if (CMMouse.clicked_name.length > 0) {
      psychoJS.experiment.addData('CMMouse.clicked_name', CMMouse.clicked_name[0]);}
    if (CMMouse.clicked_pos.length > 0) {
      psychoJS.experiment.addData('CMMouse.clicked_pos', CMMouse.clicked_pos[0]);}
    return Scheduler.Event.NEXT;
  };
}

function EndRoutineBegin(trials) {
  return function () {
    //------Prepare to start Routine 'End'-------
    t = 0;
    EndClock.reset(); // clock
    frameN = -1;
    routineTimer.add(3.000000);
    // update component parameters for each repeat
    // keep track of which components have finished
    EndComponents = [];
    EndComponents.push(text);
    
    EndComponents.forEach( function(thisComponent) {
      if ('status' in thisComponent)
        thisComponent.status = PsychoJS.Status.NOT_STARTED;
       });
    
    return Scheduler.Event.NEXT;
  };
}

function EndRoutineEachFrame(trials) {
  return function () {
    //------Loop for each frame of Routine 'End'-------
    let continueRoutine = true; // until we're told otherwise
    // get current time
    t = EndClock.getTime();
    frameN = frameN + 1;// number of completed frames (so 0 is the first frame)
    // update/draw components on each frame
    
    // *text* updates
    if (t >= 0.0 && text.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      text.tStart = t;  // (not accounting for frame time here)
      text.frameNStart = frameN;  // exact frame index
      
      text.setAutoDraw(true);
    }

    frameRemains = 0.0 + 3 - psychoJS.window.monitorFramePeriod * 0.75;  // most of one frame period left
    if (text.status === PsychoJS.Status.STARTED && t >= frameRemains) {
      text.setAutoDraw(false);
    }
    // check for quit (typically the Esc key)
    if (psychoJS.experiment.experimentEnded || psychoJS.eventManager.getKeys({keyList:['escape']}).length > 0) {
      return quitPsychoJS('The [Escape] key was pressed. Goodbye!', false);
    }
    
    // check if the Routine should terminate
    if (!continueRoutine) {  // a component has requested a forced-end of Routine
      return Scheduler.Event.NEXT;
    }
    
    continueRoutine = false;  // reverts to True if at least one component still running
    EndComponents.forEach( function(thisComponent) {
      if ('status' in thisComponent && thisComponent.status !== PsychoJS.Status.FINISHED) {
        continueRoutine = true;
      }
    });
    
    // refresh the screen if continuing
    if (continueRoutine && routineTimer.getTime() > 0) {
      return Scheduler.Event.FLIP_REPEAT;
    } else {
      return Scheduler.Event.NEXT;
    }
  };
}

function EndRoutineEnd(trials) {
  return function () {
    //------Ending Routine 'End'-------
    EndComponents.forEach( function(thisComponent) {
      if (typeof thisComponent.setAutoDraw === 'function') {
        thisComponent.setAutoDraw(false);
      }
    });
    return Scheduler.Event.NEXT;
  };
}

function endLoopIteration(thisScheduler, loop) {
  // ------Prepare for next entry------
  return function () {
    if (typeof loop !== 'undefined') {
      // ------Check if user ended loop early------
      if (loop.finished) {
        // Check for and save orphaned data
        if (psychoJS.experiment.isEntryEmpty()) {
          psychoJS.experiment.nextEntry(loop);
        }
      thisScheduler.stop();
      } else {
        const thisTrial = loop.getCurrentTrial();
        if (typeof thisTrial === 'undefined' || !('isTrials' in thisTrial) || thisTrial.isTrials) {
          psychoJS.experiment.nextEntry(loop);
        }
      }
    return Scheduler.Event.NEXT;
    }
  };
}

function importConditions(trials) {
  return function () {
    psychoJS.importAttributes(trials.getCurrentTrial());
    return Scheduler.Event.NEXT;
    };
}

function quitPsychoJS(message, isCompleted) {
  // Check for and save orphaned data
  if (psychoJS.experiment.isEntryEmpty()) {
    psychoJS.experiment.nextEntry();
  }
  
  
  
  
  
  
  
  
  
  
  psychoJS.window.close();
  psychoJS.quit({message: message, isCompleted: isCompleted});
  
  return Scheduler.Event.QUIT;
}
