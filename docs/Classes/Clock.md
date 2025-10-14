# Clock

**Categories:** Scheduling>Clocks

*abstract superclass for clocks*

**Related:** [AppClock](../Classes/AppClock.md), [SystemClock](../Classes/SystemClock.md), [TempoClock](../Classes/TempoClock.md)

## Description

Clock is an abstract class: it only defines an abstract set of methods that all clocks should implement. See its subclasses: [SystemClock](../Classes/SystemClock.md), [TempoClock](../Classes/TempoClock.md), [AppClock](../Classes/AppClock.md) for specific implementations.

### Scheduling
A Clock keeps track of time and allows **tasks** to be **scheduled** for some time in the future (e.g. using [sched](../Classes/TempoClock.md#-sched), [schedAbs](../Classes/TempoClock.md#-schedabs) or [play](../Classes/TempoClock.md#-play) methods). A task can be any [Object](../Classes/Object.md). When the time at which a task was scheduled is up, the task is *awoken*, i.e. its [awake](../Classes/Object.md#-awake) method is evaluated. If the value returned by this method is a number, the task is automatically **rescheduled** for the time equal to its last scheduled time plus the return value (in [beats](../Classes/TempoClock.md#-beats)).



### Useful Tasks
Objects of different classes may do different things in response to being scheduled on a clock by having own implementation of the `awake` method. The [Object#-awake](../Classes/Object.md#-awake) method that all classes inherit simply calls the same object's [next](../Classes/Object.md#-next) method, forwarding the `beats` argument as well as the return value, so subclasses may implement either one to equivalent effect, as far as clock scheduling is concerned. > *However, note that the `next` method is also involved in the concept of [streams](../Tutorials/Streams-Patterns-Events1.html.md#streams).*

Examples of useful objects to be scheduled on clocks:

- [Function#-awake](../Classes/Function.md#-awake) method is implemented so as to call the function's own [Function#-value](../Classes/Function.md#-value) method, effectively running the code within the function.
- [Routine#-awake](../Classes/Routine.md#-awake) calls own [Routine#-next](../Classes/Routine.md#-next), in turn starting or resuming the Routine's Function.
- Some subclasses of [Stream](../Classes/Stream.md) will have its `next` method do something useful aside from returning a new value in a stream.




### Scheduling and Threads
Whenever a task is awaken, its `awake` method is called in the context of the [main thread](../Classes/Process.md#-mainthread). Just before that, the main thread's [logical time](../Classes/Thread.md#-beats) is set to the scheduling time of the awaken task, and its [clock](../Classes/Thread.md#-clock) is set to the scheduling clock. Note however that if the task is a [Routine](../Classes/Routine.md) it will then immediately start or resume its Function, setting itself as the [current thread](../Classes/Thread.md#.thisthread).




