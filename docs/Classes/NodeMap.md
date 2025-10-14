# NodeMap

*store control values and bus mappings*

**Categories:** JITLib>NodeProxy, Server>Nodes, Server>Abstractions

**Related:** [Bus](../Classes/Bus.md)

## Description

Object to store control values and bus mappings independently of a specific node.

```supercollider
a = NodeMap.new;
a.set(\freq, [446, 662], \amp, 0.2, \out, Bus.audio(s));
a.asOSCArgArray;
```




## Instance Methods

### `set`
set arguments of a node### `unset`
remove settings### `unmap`
remove mappings### `at`
return setting at that key.### `sendToNode`
apply a setting to a node by sending a bundle### `send`
apply a setting to a node by sending a bundle### `addToBundle`
add all my messages to the bundle### `addToEvent`
add all my values to the event### `asOSCArgArray`
returns the arguments for an OSC message.### `unmapArgsToBundle`
returns the arguments for an OSC message to unmap any mapped controls.### `setMsg`
returns the OSC message for setting a synth**Arguments:**

| Argument | Description |
|----------|-------------|
| `target` | a group, synth, or server to use as a nodeID to set. |  
### `get`
Kept for backward compatibility.### `clear`
Remove all settings and clear cache
## Examples


```supercollider
s.boot;

(
SynthDef("modsine",
    { |out, freq = 320, amp = 0.2|
        Out.ar(out, SinOsc.ar(freq, 0, amp));
    }).add;
SynthDef("lfo",
    { |out, rate = 2|
        Out.kr(out, LFPulse.kr(rate, 0, 0.1, 0.2))
    }).add;
)

// start nodes
(
b = Bus.control(s, 1);
x = Synth("modsine");
y = Synth.before(x, "lfo", [\out, b]);
)

// create some node maps
(
h = NodeMap.new;
h.set(\freq, 800);
h.map(\amp, b);

k = NodeMap.new;
k.set(\freq, 400);
k.unmap(\amp);
)

// apply the maps

h.sendToNode(x); // the first time a new bundle is made
k.sendToNode(x);

h.sendToNode(x); // the second time the cache is used
k.sendToNode(x);

h.set(\freq, 600);

h.sendToNode(x); // when a value was changed, a new bundle is made

// free all
x.free; b.free; y.free;
```




