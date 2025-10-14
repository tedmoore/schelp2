# AppClock

**Categories:** Scheduling>Clocks

*Clock running on main application thread*

**Related:** [SystemClock](../Classes/SystemClock.md), [TempoClock](../Classes/TempoClock.md)

## Description

SystemClock is more accurate, but cannot call GUI primitives.
You will need to use the [SystemClock](../Classes/SystemClock.md) to get accurate/musical scheduling.
See [Clock](../Classes/Clock.md) for general explanation of how clocks operate.


## Class Methods


### `sched`
The float you return specifies the delta to resched the function for. Returning nil will stop the task from being rescheduled.
```supercollider
(
AppClock.sched(0.0, { |time|
    ["AppClock has been playing for ", time].postln;
    rrand(0.1, 0.9);
});
)
```


```supercollider
(
t = Main.elapsedTime;
"It is now % seconds after the computer booted.".format(t).postln;
AppClock.sched(2.0, { "It is now % sec later".format(Main.elapsedTime - t).postln; nil })
)
```


### `schedAbs`
Schedules a task to be performed at a particular time. Because `AppClock` is not intended to schedule with high precision, this time is approximate.When the scheduling time is up, the task's `awake` method is called. If the method returns a number, the task will be rescheduled for the time equal to the last scheduling time plus the returned value.See also: [Clock / Scheduling ](../Classes/Clock.md#scheduling), [Object#-awake](../Classes/Object.md#-awake).
```supercollider
(
t = Main.elapsedTime;
"It is now % seconds after the computer booted.".format(t).postln;
AppClock.schedAbs(t + 1.0, { "It is now % sec later".format(Main.elapsedTime - t).postln; nil })
)
```


### `clear`
Clear the AppClock's scheduler to stop it.
```supercollider
AppClock.clear;
```


### `play`
The [Routine](../Classes/Routine.md) (or [Task](../Classes/Task.md)) yields a float value indicating the delta (secs) for the AppClock to wait until resuming the Routine.
```supercollider
(
var w, r;
w = Window.new("trem", Rect(512, 256, 360, 130));
w.front;
r = Routine({ |appClockTime|
    ["AppClock has been playing for secs:", appClockTime].postln;
    60.do({ |i|
        0.05.yield;
        w.bounds = w.bounds.moveBy(10.rand2, 10.rand2);
        w.alpha = cos(i*0.1pi)*0.5+0.5;
    });
    1.yield;
    w.close;
});
AppClock.play(r);
)
```


### `tick`
AppClock.tick is called periodically by the SuperCollider language interpreter. This updates the [Scheduler](../Classes/Scheduler.md) and causes any scheduled tasks to be executed. You should never call this method yourself.

