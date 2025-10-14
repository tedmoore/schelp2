# NodeEvent

**Categories:** Streams-Patterns-Events

**Related:** [Event](../Classes/Event.md)

*synth- and group- like interface of Event*

## Description

The methods [Event#-synth](../Classes/Event.md#-synth) and [Event#-group](../Classes/Event.md#-group) set the parent event of the receiver to specialized events that duplicate the functionality of [Synth](../Classes/Synth.md) and [Group](../Classes/Group.md) objects. These objects follow the naming conventions of patterns (i.e., groups and addActions are integer ID's) and have the same stop/play/pause/resume interface as the EventStreamPlayers created by Pattern-play. So, they can be used interchangeably with patterns in control schemes and GUI's.
The following example creates a group with nodeID = 2 and plays a synth within it.

```supercollider
g = (id: 2).group;
g.play;
a = (group: 2).synth;
a.play;
g.release;
g.stop;
```



### Interface
### `play`
starts synth or group, returns this.delta
### `stop`
if ev[\hasGate] == true set gate to 0, otherwise frees the node
### `pause`
disables the node
### `resume`
reenables the node
### `set`
sets control identified by key to value
### `split`
returns an array of events, one for each synth or group specified by the receiver
### `map`
maps control to control bus
### `before`
moves to immediately before nodeID
### `after`
moves to immediately after nodeID
### `headOf`
moves to immediately to head of nodeID
### `tailOf`
moves to immediately to tail of nodeID


### Multi-channel expansion
With the exception of ~server, ~latency, and ~instrument any key in the event can have an array as a value and the standard rules of multi-channel expansion will be followed.



## Examples


```supercollider
// Here is a simple example of its use:

// define a multiple Group event
g = (id: [2,3,4,5,6], group: 0, addAction: 1).group;
g.play; // play it

// make a Synth event
b = ( freq: [500,510], group: [2,3]).synth;
b.play;

b.set(\freq,[1000,1006]);

g.release;

b.play;
h = g.split;    // split into individual group events
c = b.split;    // and synth events
c[0].set(\freq,700);
c[1].set(\freq,400);

h[0].stop;
h[1].stop;

g.stop;
```




