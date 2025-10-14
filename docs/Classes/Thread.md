# Thread

*The context of code evaluation*

**Categories:** Core>Kernel

**Related:** [Routine](../Classes/Routine.md)

## Description


> **Note:** A SuperCollider Thread is **not an operating system thread**. Although they have some conceptual similarities, they do not correspond.


A Thread represents the **context** within which code runs. It is also said that code runs "*on* a Thread". A Thread records the **state** of code execution, and thus provides support for code to be suspended at any time, and then resumed where it left off. It is then said that the Thread itself is **suspended and resumed**.
There is always one [main Thread](../Classes/Process.md#-mainthread) belonging to the [Process](../Classes/Process.md) - it is the Thread on which the top-level code runs. Another Thread may be started using an instance of the Thread's subclass [Routine](../Classes/Routine.md) which will run a [Function](../Classes/Function.md) in the context of its own (there is no use in instantiating the Thread class itself).
When code on a Thread starts or resumes another Thread (Routine), the former Thread becomes the latter's **parent**, and the latter its **child**. The parent Thread's execution is **blocked** until the child Thread finishes or is suspended, at which point the parent Thread continues execution. The **current** Thread may be accessed using [#thisThread](#thisthread), while a Thread's parent may be accessed using [#-parent](#-parent).
A Thread has
- associated [logical time](#-beats)
- an associated [Clock](#-clock)
- own [random number seed](#-randseed)
- own [exception handler](#-exceptionhandler)

### `thisThread`
The global pseudo-variable `thisThread` always represents the current Thread, i.e. the context in which the current code is running. It can be either the [main Thread](../Classes/Process.md#-mainthread) or the [Routine](../Classes/Routine.md) running the current code.See also: [Clock#Scheduling and Threads](../Classes/Clock.md#scheduling-and-threads).
```supercollider
// example
thisThread.beats;
thisThread.seconds;
thisThread.clock;
```




## Class Methods

### `new`
Creates an instance of Thread, passing it the Function with code to run.
> **Note:** There is no good use in instantiating a Thread, because this class offers no method of starting the given Function. Instead, use the Thread's subclass [Routine](../Classes/Routine.md). The only purpose of this constructor is for Routine to call it within its own constructor.

**Arguments:**

| Argument | Description |
|----------|-------------|
| `func` | A Function with code for the Thread to run. |  
| `stackSize` | Call stack size (an Integer). |  


## Instance Methods

### `parent`
The parent Thread that started or resumed this Thread.The parent Thread's execution is blocked until the child Thread finishes or is suspended.When a child Thread is started or resumed, it inherits certain aspects from its parent:- associated [Clock](#-clock)
- associated [logical time](#-beats)
### `beats`
Get or set the current logical time of the Thread in beats. This will be the same as the time in seconds, unless this Thread's [clock](#-clock) is [TempoClock](../Classes/TempoClock.md), and the clock's [tempo](../Classes/TempoClock.md#-tempo) is other than `1`.Setting `beats` also sets [#-seconds](#-seconds) to `thisThread.clock.beats2secs(beats)`.There are several sources of logical time:- When code is run from the code editor, the command line, or in response to OSC and MIDI messages, the [main Thread](../Classes/Process.md#-mainthread)'s logical time is set to the current **physical time** (see [Process#*elapsedTime](../Classes/Process.md#*elapsedtime)).
- When code **scheduled** on a [Clock](../Classes/Clock.md) is run, the [main Thread](../Classes/Process.md#-mainthread)'s logical time is set to the time the code was scheduled for.
- Child Threads **inherit** logical time from their [parents](#-parent) - whenever a Thread (Routine) is started or resumed, its logical time is set to that of the parent Thread.
However, a Thread's logical time may also be set **manually** (using this method or [#-seconds](#-seconds)). It may be useful to change the **current** Thread's time in order to manipulate behavior of streams that use the current logical time for their operation (e.g. streams created by [Pstep](../Classes/Pstep.md) and [Pseg](../Classes/Pseg.md) patterns). This will affect all code running within the current Thread, as well as any child Threads, due to logical time inheritance. Note however that changing **another** Thread's time will have no effect, because the time will be overridden by inheritance as soon as the Thread is run; likewise, any changes to the current Thread's time only have effect until the Thread is suspended (it [yields](../Classes/Object.md#-yield)) and resumed again.See also: [Clock#Scheduling and Threads](../Classes/Clock.md#scheduling-and-threads).### `seconds`
Get or set the current logical time of the Thread in seconds.Setting `seconds` also sets [#-beats](#-beats) to `thisThread.clock.secs2beats(seconds)`.See [#-beats](#-beats) for general discussion on Threads and logical time.### `clock`
Get or set the Thread's associated [Clock](../Classes/Clock.md).There are several ways a Clock becomes associated with a Thread:- When code is run from the code editor, the command line, or in response to OSC and MIDI messages, the [main Thread](../Classes/Process.md#-mainthread)'s clock is set to [SystemClock](../Classes/SystemClock.md).
- When code **scheduled** on a Clock is run, that clock becomes the [main Thread](../Classes/Process.md#-mainthread)'s clock.
- Child Threads **inherit** the associated clock from their [parents](#-parent).
A Thread's associated clock may also be set **manually** using this method. Setting the **current** Thread's clock is useful to manipulate further behavior of the Thread or its child Threads, but the clock will be reset the next time the Thread is resumed, due to clock inheritance. For the same reason, setting **another** Thread's clock will have no effect on code running on it.See also: [Clock#Scheduling and Threads](../Classes/Clock.md#scheduling-and-threads).### `deferAwayFrom`
Executes a given function, guaranteeing that it will not execute on the same thread as `this`. That is:- If `delta > 0` (the function should evaluate later), defer to [AppClock](../Classes/AppClock.md).
- If `delta <= 0` (execute right now), defer to [AppClock](../Classes/AppClock.md) if `thisThread` matches the thread receiving this method call. Otherwise, directly [Function#-value](../Classes/Function.md#-value) the function.
This method interface is designed to be used with function-call syntax, e.g. `deferAwayFrom(aThread) { ... function body ... }`.**Arguments:**

| Argument | Description |
|----------|-------------|
| `func` | The function to evaluate. It will not be passed any argument values. |  
| `delta` | A time delta in seconds. Normally, the default 0 will be used. |  
### `isPlaying`
**Returns:** true if it is playing.### `state`
The internal state values for a Thread instance can be polled:| 0 | not started | 
| --- | --- || 7 | running | | 8 | stopped | 
### Seeding the random number generator
see also: [randomSeed](../Reference/randomSeed.md)

### `randSeed`
Set the random number generator seed using a single integer.Example:
```supercollider
g = thisThread.randSeed = 4;
10.do{ 1.0.rand2.postln };
```


### `randData`
Get or set the three integer array which defines the internal basis for the random number generator. You can use this to get back the exact same random number sequence, and it provides a mechanism for automatic replay for generative music.Example:
```supercollider
g = thisThread.randData;
10.do{ 1.0.rand2.postln };
```


```supercollider
// each time the seed is reset, the random number generation should give the same sequence
thisThread.randData_(Int32Array[-662787342, 1546785953, 1661466823]);
10.do{ 1.0.rand2.postln };
```




