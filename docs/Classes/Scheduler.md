# Scheduler

**Categories:** Scheduling

*schedules functions to be evaluated in the future*

## Description

A Scheduler can be used to schedule and reschedule functions to be evaluated at a specific time-point. The Scheduler's time needs to be advanced manually. In most cases you will probably want to use a Clock (e.g. [TempoClock](../Classes/TempoClock.md), [SystemClock](../Classes/SystemClock.md), [AppClock](../Classes/AppClock.md)) instead, in which the march of time is handled for you.


## Class Methods

### `new`
**Arguments:**

| Argument | Description |
|----------|-------------|
| `clock` | A clock, like SystemClock. |  
| `drift` | If `true`, [sched](#sched) will schedule tasks relative to the current absolute time ([Main.elapsedTime](../Classes/Process.md#*elapsedtime)), otherwise to the current logical time of the scheduler ([seconds](#seconds)). |  
| `recursive` | Sets [recursive](#recursive). |  


## Instance Methods

### `play`
Schedules the task immediately. Equivalent to `sched(0, task)`.### `sched`
Schedule the task at `delta` seconds relative to the current time, as defined by the `drift` argument of the [constructor](#*new).Regardless of what time a task is scheduled, it will only be awaken the next time [seconds](#seconds) is set.### `schedAbs`
Schedule the task at absolute `time` in seconds.### `advance`
Advance the current logical time by `delta` seconds. Has same effect as setting [seconds](#seconds).### `seconds`
The current logical time of the scheduler.Setting a new time will wake up (evaluate) any tasks scheduled within that time; a task that returns a new time will be rescheduled accordingly.### `isEmpty`
Returns whether the scheduling queue is empty.### `clear`
Clears the scheduling queue### `queue`
**Returns:** The instance of [PriorityQueue](../Classes/PriorityQueue.md) used internally as scheduling queue.### `recursive`
If waking up items results in new items being scheduled, but some of them are already expired (scheduled at current time or earlier), this variable determines whether those items will be awaken as well in the same call to -seconds.
## Examples


```supercollider
a = Scheduler(SystemClock);

a.sched(3, { "now it is 3 seconds.".postln; nil });
a.sched(5, { "now it is 5 seconds.".postln; nil });
a.sched(1, { "now it is 1 second.".postln; nil });

a.advance(0.5);
a.advance(0.5);
a.advance(2);
a.advance(2);

// the beats, seconds and clock are passed into the task function:
a.sched(1, { |beats, secs, clock| [beats, secs, clock].postln });
a.advance(1);

// the scheduling is relative to "now":
a.sched(3, { "now it was 3 seconds.".postln });
a.sched(5, { "now it was 5 seconds.".postln });
a.sched(1, { "now it was 1 second.".postln });

a.advance(0.5);
a.advance(0.5);
a.advance(2);
a.advance(2);

// play a Routine or a task:
a.play(Routine { 5.do { |i| i.postln; 1.yield } });
a.advance(0.9);
```



```supercollider
// scheduling tasks
(
x = Scheduler(TempoClock.default);

Task {
    inf.do { |i|
        ("next " ++ i ++ " in task." + Main.elapsedTime).postln;
        0.5.wait;
    }
}.play(x);
)

x.advance(0.1);
x.seconds;
x.advance(5);
x.seconds;

(
Routine {
    loop { x.advance(0.1); 0.1.wait };
}.play;
)

(
Task { 5.do {
    x.advance(1);
    2.0.rand.wait;
    }
}.play;
)

x.advance(8.1);

Pbind(\degree, Pseries(0, 2, 8), \dur, 0.25).play(x);

(
Task { 5.do {
    x.advance(0.20);
    1.0.wait;
    }
}.play;
)
```




