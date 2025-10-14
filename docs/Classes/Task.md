# Task

**Categories:** Scheduling

*a pauseable process*

**Related:** [Routine](../Classes/Routine.md)

## Description

Task is a pauseable process. It is implemented by wrapping a [PauseStream](../Classes/PauseStream.md) around a [Routine](../Classes/Routine.md). Most of its methods (start, stop, reset) are inherited from PauseStream.
The purpose of a Task is to separate a Routine's state of execution from its running state (that is, its state of being scheduled on a clock or not, or paused in a [CondVar](../Classes/CondVar.md) or not). Use Task if you expect the process to need to start, stop or resume multiple times while maintaining the execution flow. (This means that Tasks are not 100% interchangeable with Routines -- for many uses, Tasks should be preferred over Routines.)
Note that stopping a task and restarting it quickly may yield surprising results (see example below), but this is necessary to prevent tasks from becoming unstable if they are started and/or stopped in rapid succession. (Routines do allow a quick stop-reset-play cycle, but they have no mechanism to prevent timing from being broken in this case, i.e. Routine is more brittle here.) If you need to start and stop quickly while maintaining timing, a better approach would be to swap the child Routine over to a new instance of PauseStream.


## Class Methods

### `new`
**Arguments:**

| Argument | Description |
|----------|-------------|
| `func` | A Function to be evaluated. |  
| `clock` | A Clock in which to play the [Routine](../Classes/Routine.md). If you do not provide a Clock the default is an instance of [TempoClock](../Classes/TempoClock.md). Remember that methods which call Cocoa primitives (i.e. GUI functions) must be played in [AppClock](../Classes/AppClock.md). |  


## Instance Methods

### `play`
**Arguments:**

| Argument | Description |
|----------|-------------|
| `argClock` | (optional) Override the clock assigned in Task.new. |  
| `doReset` | If true, the task will start over from the beginning. Default is false (task will resume where it was when it was last stopped). |  
| `quant` | See the [Quant](../Classes/Quant.md) helpfile. |  

### Other control methods
### `start`
Restart the task from the beginning.
### `resume`
Resume the task where it left off.
### `pause`
Stop playing now.
### `stop`
Stop playing now. (Pause and stop have the same implementation.)
### `reset`
Set the stream to restart from the beginning the next time it's played.
### `reschedule`
Switch the Task to a different clock, or a different time, without stopping. See [Routine#-reschedule](../Classes/Routine.md#-reschedule) for complete documentation.
> **Note:** If you want to reschedule a Task from within the Task itself, `thisThread.reschedule(...)` will not work, because `thisThread` refers to the Routine under control of the Task, not to the Task itself (whereas a Routine is playing on the clock directly). You must write `thisThread.threadPlayer.reschedule(...)` instead.



### Notifications
Other objects might need to be aware of changes in the state of a task. The following notifications are broadcast to dependents registered with the Task object.

- **\userPlayed** - Sent at the time the user calls play, start or resume.
- **\playing** - Sent at the time the task begins playing on the clock (corresponding to quant).
- **\userStopped** - Sent at the time the user calls pause or stop.
- **\stopped** - Sent at the time the task is finally removed from the clock (this is the time when the next event would have occurred if the task had not been stopped). If the task function completes on its own, this notification is sent without 'userStopped' being sent previously.



## Examples


### What happens if you stop and start the task too quickly?

```supercollider
(
t = Task({
    50.do({ |i|
        i.squared.postln;
        0.5.wait;
    });
});
)

t.start;
t.pause;
t.resume;
t.reset;
t.stop;

// unexpected behavior here
(
t = Task({
    ["go", thisThread.clock.beats].postln;
    inf.do({ |i|
        2.wait;
        ["wake up", i].postln;
    });
});

fork {
    t.start;
    0.1.wait;
    t.stop;
    0.1.wait;
    t.start;
    6.wait;
    t.stop;
};
)

[go, 1702.114411906]
[go, 1704.114411906]
```


Based on the forked thread, you would expect the second "go" line of output to occur 0.2 seconds after the first, but in fact it happens two seconds later (the same amount of time the task waits between iterations). This is because the task must not schedule itself on the clock more than once. When the task is stopped, it remains scheduled until it wakes up again (based on its wait time). If, during this interval, the task were restarted, there would be two references to the task in the scheduler queue -- a situation that is irrecoverable short of stopping everything with command-period.

For the above case, you can get completely stable timing by manually wrapping the Routine in a PauseStream. Note that `start` implicitly resets the routine to the beginning; using `play` instead only alters the timing, without interrupting the routine's flow.


```supercollider
(
r = Routine({
    ["go", thisThread.clock.beats].postln;
    inf.do({ |i|
        2.wait;
        ["wake up", i].postln;
    });
});

fork {
    t = PauseStream(r);
    t.start;  // prints "go..."
    0.1.wait;
    t.stop;   // but stop before the loop prints
    0.1.wait;
    t = PauseStream(r);
    t.start;  // prints "go..."
    6.wait;   // loop is allowed to run 2 cycles
    t.stop;
};
)
```






