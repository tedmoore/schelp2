# TempoClock

**Categories:** Scheduling>Clocks

*tempo based scheduler*

**Related:** [AppClock](../Classes/AppClock.md), [SystemClock](../Classes/SystemClock.md)

## Description

TempoClock is a scheduler like [SystemClock](../Classes/SystemClock.md), but it schedules relative to a **tempo** in beats per second.
See [Clock](../Classes/Clock.md) for general explanation of how clocks operate.


## Class Methods


### `new`
Creates a new instance of TempoClock.**Arguments:**

| Argument | Description |
|----------|-------------|
| `tempo` | The initial [tempo](#-tempo). Defaults to `1`. |  
| `beats` | The time in beats, corresponding to the reference time given with the `seconds` argument. Defaults to `0`. |  
| `seconds` | The reference time in seconds, to which the `beats` argument corresponds. Defaults to the current Thread's logical time (see [Thread#-seconds](../Classes/Thread.md#-seconds)). |  
| `queueSize` | The storage size of the scheduling queue. Each scheduled item takes 2 counts of space, so this size divided by 2 gives the amount of items that can be scheduled at a time. See also [#-queue](#-queue). |  
The TempoClock will be created **as if** it started counting beats at the time given in the `seconds` argument with the starting amount given in the `beats` argument. The current count of beats will thus be equal to that starting amount plus the amount of beats that would be counted since the given reference time in seconds, according to the given tempo.The default arguments create a TempoClock that starts counting beats with `0` at the current logical time.
```supercollider
// Create a TempoClock that starts counting beats with 5 now.
(
t = TempoClock.new(2, 5);
"current beats:" + t.beats;
)

// Create a TempoClock, as if it started counting beats 5 seconds ago with 0.
(
t = TempoClock.new(2, 0, thisThread.seconds - 5);
"current beats:" + t.beats;
)
```


### `default`
Sets or gets the permanent default TempoClock instantiated at startup.
```supercollider
TempoClock.default.beats // beats since default TempoClock was started
```



### Forwarding to the default instance
The following methods only forward to the [default instance](#*default), allowing you to use the TempoClock class itself in place of `TempoClock.default`.

### `stop`

### `play`

### `sched`

### `schedAbs`

### `clear`

### `tempo`

### `etempo`

### `beats`

### `beats2secs`

### `secs2beats`

### `nextTimeOnGrid`

### `timeToNextBeat`

### `setTempoAtBeat`

### `setTempoAtSec`

### `setMeterAtBeat`

### `beatsPerBar`

### `baseBarBeat`

### `baseBar`

### `playNextBar`

### `beatDur`

### `elapsedBeats`

### `beats2bars`

### `bars2beats`

### `bar`

### `nextBar`

### `beatInBar`

### `isRunning`



## Instance Methods

### `stop`
Destroys the scheduler and releases the OS thread running the scheduler.### `clear`
Removes all tasks from the scheduling queue.### `isRunning`
**Returns:** A Boolean, true if the clock is active or false if the clock has been stopped.### `tempo`
Sets or gets the current tempo in beats per second at the current **logical time**.
```supercollider
t = TempoClock.new;
t.tempo_(2.0); // equivalent to t.tempo = 2.0;
t.tempo;
t.tempo_(72/60) // 72 beats per minute
t.tempo;
```

### `etempo`
Sets or gets the current tempo at the current **elapsed time**.### `permanent`
Sets or gets a [Boolean](../Classes/Boolean.md) value indicating whether the clock will survive cmd-period. If false the clock is stopped (and thus removed) on cmd-period. If true the clock survives cmd-period. It is false by default.### `beats`
Gets or sets the current logical time in beats according to this clock.When **getting** `beats`, if this clock is the current Thread's [associated clock](../Classes/Thread.md#-clock), the Thread's own [time in beats](../Classes/Thread.md#-beats) is returned, otherwise the Thread's [time in seconds](../Classes/Thread.md#-seconds) converted to beats according to this clock is returned.After **changing** `beats` towards the **future**, the clock will immediately perform all tasks scheduled until the new time. Likewise, when changing `beats` towards the **past**, already scheduled tasks will be postponed, so they will still be performed at the scheduled time in beats.
> **Note:** When changing `beats`, you are only changing the clocks's notion of time, and not the current Thread's [logical time](../Classes/Thread.md#-beats), which will stay the same until the Thread is called again. Hence, if this clock is the current Thread's [associated clock](../Classes/Thread.md#-clock), and you ask the clock for time in beats just after changing it, you will see no effect. Nevertheless, the effect will be visible immediately on a different Thread.


```supercollider
(
t = TempoClock.new;

t.sched(3, {
    t.beats = 100;
    t.beats.postln; // still 3
    nil
});
)

(
c = TempoClock.new;
fork {
    loop {
        c.beats.postln; // updates, because ".wait" calls the thread
        1.wait;
    }
};
)

c.beats = 100;
```

### `schedAbs`
Schedules a task to be performed at a particular time in **beats**.When the scheduling time is up, the task's `awake` method is called. If the method returns a number, the task will be rescheduled for the time equal to the last scheduling time plus the returned value.See also: [Clock#Scheduling](../Classes/Clock.md#scheduling), [Object#-awake](../Classes/Object.md#-awake).### `sched`
Schedules a task to be performed `delta` amount of **beats** after the current Thread's logical time. If this clock is the current Thread's [associated clock](../Classes/Thread.md#-clock), the Thread's [time in beats](../Classes/Thread.md#-beats) is used, otherwise the Thread's [time in seconds](../Classes/Thread.md#-seconds) is converted to beats according to this clock's tempo and time of origin.When the scheduling time is up, the task's `awake` method is called. If the method returns a number, the task will be rescheduled for the time equal to the last scheduling time plus the returned value.See also: [Clock#Scheduling](../Classes/Clock.md#scheduling), [Object#-awake](../Classes/Object.md#-awake).### `play`
Plays task (a function) at the next beat, where **quant** is 1 by default. Shortcut for [#-schedAbs](#-schedabs); see [#-seconds](#-seconds) and [#-nextTimeOnGrid](#-nexttimeongrid) for further details on time and quant.
```supercollider
t = TempoClock.default;
t.play({ |beats, time, clock| [beats, time, clock].postln });
```

### `playNextBar`
Plays task (a function) at the next bar using [#-schedAbs](#-schedabs).### `queue`
Returns the scheduling queue Array in the form [beat, function]. The maximum number of items is determined by the clock's queueSize argument upon instantiation. The default queueSize of 256 allows 128 functions to be in the queue at any time.### `beatDur`
Returns the duration in seconds of a current whole beat.### `beatsPerBar`
Gets or sets the number of beats per bar. The default is 4. Setting the meter must be done from within the same clock's scheduling thread. Scheduled functions and playing Routines (or Tasks) are running on the clock's thread, so both of these are valid.Setting beatsPerBar also updates the barline reference (baseBarBeat). Be careful to call `beatsPerBar_` *only* on a barline ([#-nextBar](#-nextbar) below).`thisThread.clock` is always the current clock -- so, writing `thisThread.clock.beatsPerBar = /* number */` as a matter of habit will guarantee that the meter change only ever applies to the current clock.
```supercollider
t = TempoClock.new;

t.beatsPerBar = 3;  // error! wrong thread

t.schedAbs(t.nextBar, { t.beatsPerBar_(3) });  // OK

t.beatsPerBar;  // will be reflected after the barline

t.schedAbs(t.nextBar, { thisThread.clock.beatsPerBar_(4) });  // OK

(
r = Routine {
    // by addressing "this" clock,
    // we are always changing meter in the right place
    var clock = thisThread.clock;
    
    clock.beats.debug("start time");
    clock.timeToNextBeat(-1).wait;
    clock.beats.debug("barline");

    // no need to 'sched'
    // because the Routine is already on this clock
    // flip 3/4 -> 4/4 or 4/4 -> 3/4
    clock.beatsPerBar = 7 - clock.beatsPerBar;
    clock.beatsPerBar.debug("set meter to");

    0.01.wait;  // must be after barline for 'timeToNextBeat'
    clock.timeToNextBeat(-1).wait;
    clock.beats.debug("next barline");
}.play;
)
```

### `bar`
Returns the current bar. See [#-bars2beats](#-bars2beats) for returning beat of current bar.### `nextBar`
Returns the number of beats at the next bar line relative to the beat argument. If **beat** is not supplied, returns the beat at which the next bar begins.### `beatInBar`
Returns the current bar beat (as a [Float](../Classes/Float.md)) in relation to [#-beatsPerBar](#-beatsperbar). Values range from 0 to < beatsPerBar.### `baseBar`
Returns bar at which [#-beatsPerBar](#-beatsperbar) was last changed. If beatsPerBar has not been changed since the clock was created, returns 0.### `baseBarBeat`
Returns beat at which the [#-beatsPerBar](#-beatsperbar) was last changed. If beatsPerBar has not been changed since the clock was created, returns 0.### `beats2bars`
Returns a bar as a float relative to [#-baseBarBeat](#-basebarbeat).### `bars2beats`
Returns a beat relative to [#-baseBar](#-basebar).
```supercollider
t = TempoClock.default;
t.bars2beats(t.bar) // downbeat of the current bar
```

### `timeToNextBeat`
Returns the logical time to next beat. **quant** is 1 by default, relative to baseBarBeat, see [#-nextTimeOnGrid](#-nexttimeongrid).### `nextTimeOnGrid`
With default values, returns the next whole beat. **quant** is 1 by default, **phase** is 0. quant is relative to [#-baseBarBeat](#-basebarbeat), such that
```supercollider
t = TempoClock.default;
t.nextTimeOnGrid(t.beatsPerBar) == t.nextBar // => true
```

Together **quant** and **phase** are useful for finding the next n beat in a bar, e.g. `nextTimeOnGrid(4, 2)` will return the next 3rd beat of a bar (of 4 beats), whereas `nextBar-2` may return an elapsed beat.`referenceBeat` may be used to evaluate the quant and phase relative to an arbitrary beat. Normally, no reference beat will be specified (`nil`) and the clock's current beats will be used.### `elapsedBeats`
Returns the current elapsed time in beats. This is equivalent to `tempoClock.secs2beats(Main.elapsedTime)`. It is often preferable to use [#-beats](#-beats) instead of elapsedBeats because beats uses a thread's logical time.### `seconds`
Returns the current elapsed time. (This method is inherited from [Clock](../Classes/Clock.md).)### `beats2secs`
Converts absolute **beats** to absolute **seconds**, returning the elapsed time of the clock at the given **beats**. Only works for times in the current tempo. If the tempo changes any computed time in future will be wrong.
```supercollider
t = TempoClock.default;
t.beats2secs(t.beats) // equivalent to t.seconds
t.beats2secs(0) // how many seconds after startup did beat 0 occur?
```

### `secs2beats`
Converts absolute **seconds** to absolute beats. Only works for times in the current tempo. If the tempo changes any computed time in future will be wrong.
## Examples


```supercollider
t = TempoClock(1); // create a TempoClock

// schedule an event at next whole beat
t.schedAbs(t.beats.ceil, { |beat, sec| [beat, sec].postln; 1 });

t.tempo = 2;
t.tempo = 4;
t.tempo = 0.5;
t.tempo = 1;

t.clear;

t.schedAbs(t.beats.ceil, { |beat, sec| [beat, sec].postln; 1 });

t.stop;
```




```supercollider
(
// get elapsed time, round up to next second
v = Main.elapsedTime.ceil;

// create two clocks in a 5:2 relation, starting at time v.
t = TempoClock(1, 0, v);
u = TempoClock(0.4, 0, v);

// start two functions at beat zero in each clock.
t.schedAbs(0, { |beat, sec| [\t, beat, sec].postln; 1 });
u.schedAbs(0, { |beat, sec| [\u, beat, sec].postln; 1 });
)

(
u.tempo = u.tempo * 3;
t.tempo = t.tempo * 3;
)

(
u.tempo = u.tempo * 1/4;
t.tempo = t.tempo * 1/4;
)

(
t.stop;
u.stop;
)
```




```supercollider
(
// get elapsed time, round up to next second
v = Main.elapsedTime.ceil;

// create two clocks, starting at time v.
t = TempoClock(1, 0, v);
u = TempoClock(1, 0, v);

// start two functions at beat zero in each clock.
// t controls u's tempo. They should stay in sync.
t.schedAbs(0, { |beat, sec| u.tempo = t.tempo * [1, 2, 3, 4, 5].choose; [\t, beat, sec].postln; 1 });
u.schedAbs(0, { |beat, sec| [\u, beat, sec].postln; 1 });
)

(
u.tempo = u.tempo * 3;
t.tempo = t.tempo * 3;
)

(
u.tempo = u.tempo * 1/4;
t.tempo = t.tempo * 1/4;
)

(
t.stop;
u.stop;
)
```




