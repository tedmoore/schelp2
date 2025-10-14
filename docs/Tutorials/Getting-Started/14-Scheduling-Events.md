# 14. Scheduling Events

*Getting Started With SuperCollider*

**Categories:** Tutorials>Getting-Started

**Related:** [Getting-Started/00-Getting-Started-With-SC](../../Tutorials/Getting-Started/00-Getting-Started-With-SC.md)

Music happens over time, and to make effective music, it's necessary to control when things happen. In SuperCollider, this is done by scheduling things on clocks.

## Clocks
A clock in SuperCollider has two major functions. It knows what time it is, and it knows what time things are supposed to happen, so that it can wake them up at just the right time.

Musical sequencing will usually use [TempoClock](../../Classes/TempoClock.md), because you can change its tempo and it is also aware of meter changes. Two other kinds of clock exist: [SystemClock](../../Classes/SystemClock.md), which always runs in seconds, and [AppClock](../../Classes/AppClock.md), which also runs in seconds but has a lower system priority (so it is better for graphic updates and other activities that are not time critical).



## Scheduling
Scheduling means to tell the clock to execute something at some time in the future. So, you need to have the thing to schedule, and a number indicating the time.

Let's have SuperCollider say hello, 5 seconds from now.


```supercollider
SystemClock.sched(5, { "hello".postln });
```


Notice that when you do this, 'SystemClock' prints immediately. Every time you run something in SuperCollider, it has to return a value right away; the method's return value is the clock. Before returning, however, the clock 'remembers' the function, and that you wanted it to run 5 seconds later. And indeed, 'hello' appears in the post window, right on cue. `{ "hello".postln }` is an *asynchronous* action: it runs *after* its code block has already returned.

**sched** does *relative* scheduling. The actual time when the function runs is x seconds (or beats, for TempoClock) later than the time the .sched call occurred. It is also possible to schedule for an exact time point, provided you know what time it is on the clock. **schedAbs** handles *absolute* scheduling.


```supercollider
(
var timeNow = TempoClock.default.beats;
"Time is now: ".post; timeNow.postln;
"Scheduling for: ".post; (timeNow + 5).postln;
TempoClock.default.schedAbs(timeNow + 5,
    { "Time is later: ".post; thisThread.clock.beats.postln; nil });
)
```


Note that we have moved to TempoClock, since this is the most commonly used. While there is only one SystemClock, there can be many TempoClocks all running at different speeds, if need be. One TempoClock is the default, accessed by `TempoClock.default` -- we will use this throughout. (To save typing, you may wish to assign a TempoClock to a variable, for instance, `t = TempoClock.default`.)

For fun, change the tempo and run the last example again:


```supercollider
(
var timeNow;
TempoClock.default.tempo = 2;    // 2 beats/sec, or 120 BPM
timeNow = TempoClock.default.beats;
"Time is now: ".post; timeNow.postln;
"Scheduling for: ".post; (timeNow + 5).postln;
TempoClock.default.schedAbs(timeNow + 5,
    { "Time is later: ".post; thisThread.clock.beats.postln; nil });
)
```


Notice that the 'Time is later' message shows up after a shorter delay, but the difference between the two times is still 5.



## What time is it?
Inside a scheduled function, you might want to know which clock is running the function. `thisThread.clock` tells you this -- don't worry for now about how it knows, just know that you can use this to find out.

Once you know the clock, you can find out what time it is using **beats** :


```supercollider
SystemClock.beats;
TempoClock.default.beats;
AppClock.beats;
thisThread.clock.beats;
```




## What can you schedule?
Suppose we schedule "hello" by itself.


```supercollider
TempoClock.default.sched(5, "hello");
```


Nothing happens. That's because "hello" is just a value -- it doesn't do anything. The lesson is that it makes sense to schedule objects that will *take some action*.


```supercollider
Function
Routine
Task
```


Routines and Tasks will be covered in the next section, and Functions we have already seen. There are some others, but these are the best starting point.



## Caution
If you schedule function that returns a number, the clock will treat that number as the amount of time before running the function again.


```supercollider
// fires many times (but looks like it should fire just once)
TempoClock.default.sched(1, { rrand(1, 3).postln; });
```


This will keep going forever, until you stop it with cmd-.

If you want the function to run only once, make sure to end the function with 'nil':


```supercollider
// fires once
TempoClock.default.sched(1, { rrand(1, 3).postln; nil });
```


It's easy to return a number by mistake, and get an ongoing activity when you wanted a one-shot action.

If that number happens to be 0, or negative, something worse happens. The function will run again immediately. And, if the number is always 0, it creates an infinite loop that can lock up SuperCollider.

That shouldn't scare you off of scheduling -- this is less likely to happen with Routines and Tasks, which you will use more often. But you should be aware of it.

For more: [SystemClock](../../Classes/SystemClock.md), [TempoClock](../../Classes/TempoClock.md), [AppClock](../../Classes/AppClock.md), [Function](../../Classes/Function.md)

____________________

This document is part of the tutorial **Getting Started With SuperCollider**.

Click here to go on to the next section: [Getting-Started/15-Sequencing-with-Routines-and-Tasks](../../Tutorials/Getting-Started/15-Sequencing-with-Routines-and-Tasks.md)

Click here to return to the table of Contents: [Getting-Started/00-Getting-Started-With-SC](../../Tutorials/Getting-Started/00-Getting-Started-With-SC.md)



