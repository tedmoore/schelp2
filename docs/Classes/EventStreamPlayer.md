# EventStreamPlayer

*two streams combined by a binary operator*

**Related:** [Event](../Classes/Event.md), [Pbind](../Classes/Pbind.md)

**Categories:** Streams-Patterns-Events

## Description

An EventStreamPlayer is used by [Event](../Classes/Event.md) based Patterns.
The EventStreamPlayer holds a stream which returns a series of Events, and a protoEvent. At each call to next, it copies the protoEvent, passes that to the stream, and calls **play** on the [Event](../Classes/Event.md) returned.
For more on EventStreamPlayer see [Streams-Patterns-Events4](../Tutorials/Streams-Patterns-Events4.md)
EventStreamPlayer uses the same control methods and status notifications as [Task](../Classes/Task.md).


## Class Methods


### `new`

> **Note:** You do not explicitly create an EventStreamPlayers, they are created for you when you call [Pattern#-play](../Classes/Pattern.md#-play).



## Instance Methods


### `play`
**Arguments:**

| Argument | Description |
|----------|-------------|
| `argClock` | (optional) Override the clock assigned in Task.new. |  
| `doReset` | If true, the task will start over from the beginning. Default is false (task will resume where it was when it was last stopped). |  
| `quant` | See the [Quant](../Classes/Quant.md) helpfile. |  

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
> **Note:** Rescheduling an EventStreamPlayer from within the pattern itself is currently not supported.



