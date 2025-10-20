# BusPlug

*a listener on a bus*

**Categories:** JITLib>NodeProxy, Live Coding

**Related:** [Bus](../Classes/Bus.md), [Monitor](../Classes/Monitor.md), [InBus](../Classes/InBus.md), [NodeProxy](../Classes/NodeProxy.md), [Ndef](../Classes/Ndef.md)

## Description

A BusPlug represents a listener on a private [Bus](../Classes/Bus.md) that makes it easy to play back to multiple channels. It is mainly in use as a superclass of NodeProxy, but it can be used for general channel routings as well. Most methods are documented in the [NodeProxy](../Classes/NodeProxy.md) helpfile.

```
s.boot;
z = Bus.control(s, 16);
z.setn({ |i| (i * 5).nthPrime } ! 16 * 5 + 100);
a = BusPlug.for(z);
{ Splay.ar(SinOsc.ar(a.kr(3, MouseX.kr(0, 25)))) * 0.1 }.play; // selectively play 3 channel of the 16, modulate offset
```




## Class Methods


### `new`
Create a new (neutral) instance on the given server.

### `for`
Create an instance with a given [Bus](../Classes/Bus.md).

### `audio`
Create a new audio rate instance on the given server.

### `control`
Create a new control rate instance on the given server.

### `defaultNumAudio`
Default number of channels when initializing in audio rate and no specific number is given (default: 2).

### `defaultNumControl`
Default number of channels when initializing in control rate and no specific number is given (default: 1).

### `defaultReshaping`
default reshaping behaviour for BusPlug and its sublass NodeProxy. See: [#-reshaping](#-reshaping)

## Instance Methods


### `server`
Return the server that the BusPlug runs on.
### `clear`
Free the bus, end the monitor.
### Making copies

### `copy`
copies the hidden internal state to make the new BusPlug independent of the old, running on a new [Bus](../Classes/Bus.md). By design, the [Monitor](../Classes/Monitor.md) is copied, but is not running (use play to start it in the same configuration). If needed, you can also copy the [Monitor](../Classes/Monitor.md) only (see: [NodeProxy#-copy](../Classes/NodeProxy.md#-copy)).

### `copyState`
Copy the internal settings of one proxy into another. Old state is cleared, the bus is freed.**Arguments:**

| Argument | Description |
|----------|-------------|
| `proxy` | The object whose internal state is being copied. |  


### `reshaping`
Determines how to behave when [#-initBus](#-initbus) is called. Current options:- `nil` Once initialized, keep the same bus - this is the default
- `\static` Same as nil, but allows you to override the default in instances
- `\elastic` On a change, shrink and grow according to need, replace bus. Monitoring is adjusted.
- `\expanding` On a change, only grow according to need, replace bus. Monitoring is adjusted.


### In UGen graphs and Patterns

### `ar`, `kr`
Return a link to numChannels of my output. If uninitialized, creates a matching bus. Normally, **ar defaults to stereo, kr to mono**. This can be set in the classvars: [#*defaultNumAudio](#*defaultnumaudio), [#*defaultNumControl](#*defaultnumcontrol)For consistency, it always returns an array of signals when no numChannels are given. To make it a single ugen output, use `numChannels = 1` . See also: [InBus](../Classes/InBus.md).**Arguments:**

| Argument | Description |
|----------|-------------|
| `numChannels` | Number of channels returned. If the receiver is neutral or reshaping is elastic, initialize it to this number. If this is more than the available channels, use the clip behaviour (below). If set to `1`, it will return an instance of [InBus](../Classes/InBus.md), otherwise an Array of one or more instances of InBus. |  
| `offset` | Channel offset when reading a bus that has more channels than numChannels, cross fading between adjacent channels. |  
| `clip` | If set to 'wrap', exceeding channels will wrap around, if set to 'clip', repeat the last one. |  


### `asUGenInput`
Returns the appropriate output to read from the BusPlug bus (an [InBus](../Classes/InBus.md) UGen)
```
b = BusPlug.new;
{ Blip.ar(b + 5) }.play;
b.bus.set(12);
```



### `embedInStream`
Returns the map argument for the bus, if the bus has multiple channels, it will return an array of map args.
```
b = BusPlug.new;
x = Pbind(\z, b).asStream;
x.next(()); // returns the map argument for the bus
b.defineBus(\audio, 3);
x.next(()); // returns map arguments for the audio rate bus
```



### `asControlInput`
Returns the map argument for the bus, just like [#-embedInStream](#-embedinstream)

### Monitoring and Routing

### `isPlaying`
Returns true if server is running and bus not nil. [NodeProxy](../Classes/NodeProxy.md) this returns true if the group is playing.

### `isMonitoring`
Returns true if monitor is playing

### `play`
Play from a bus index with a number of channels to another index with a number of channels, within a [Group](../Classes/Group.md) (i.e. a target group or server).**Arguments:**

| Argument | Description |
|----------|-------------|
| `out` | bus index |  
| `numChannels` | number of channels to output. If BusPlug is neutral or reshaping is elastic, initialize it to this number. If this is more than the available channels, wrap around. If this is not given, and reshaping is elastic, it will automatically expand. |  
| `group` | target [Group](../Classes/Group.md) or [Server](../Classes/Server.md) in which to play the monitor synths. |  
| `multi` | keep old playback links and add new one |  
| `vol` | overall volume at which to monitor |  
| `fadeTime` | fade in / fade out time |  
| `addAction` | Where in the node tree to play the monitor synths |  


### `playN`
Play back on non-contiguous channels. See: [Monitor](../Classes/Monitor.md) and [playN](../Reference/playN.md)**Arguments:**

| Argument | Description |
|----------|-------------|
| `outs` | array of destination channels (or single value) |  
| `amps` | array of amplitudes for each channel (or single value) |  
| `ins` | array of source channel offsets within the bus (or single value) |  
| `vol` | Overall volume (multiplied by amps) |  
| `fadeTime` | array of fadeTimes (or single value) for fade in / fade out |  
| `group` | target [Group](../Classes/Group.md) or [Server](../Classes/Server.md) in which to play the monitor synths. |  
| `addAction` | Where in the node tree to play the monitor synths |  


### `stop`
stop to play out public channels.**Arguments:**

| Argument | Description |
|----------|-------------|
| `fadeTime` | decay time for this action |  
| `reset` | if set to true, reset all monitor state. Otherwise, the previous play arguments are kept. |  


### `monitor`
returns the current monitor (see [Monitor](../Classes/Monitor.md))

### Bus changes
These methods are a little numerous, because they are important for implementing [NodeProxy](../Classes/NodeProxy.md) behavior. Mostly the methods [#-bus](#-bus) and [#-initBus](#-initbus) will be sufficient in normal use.


> **Note:** The old bus is freed when a new bus is made.



### `isNeutral`
Returns true if no bus has been initialized so far.

### `bus`
Set or get the bus. If BusPlug monitor is playing, restart the monitor to adequately play back the new bus.

### `setBus`
set the bus object by passing a [Bus](../Classes/Bus.md).
> **Note:** you have to stop and play explicitly



### `defineBus`
make a new bus for the BusPlug with a given rate and number of channels.

### `initBus`
Make a new bus only if necessary. This depends on the current bus and the [#-reshaping](#-reshaping) mode.**Returns:** Boolean (true if successful).

## Examples


```
// using as a control bus listener

s.boot;
z = Bus.control(s, 16);
a = BusPlug.for(z);

m = { Mix(SinOsc.ar(a.kr(16), 0, 0.1)) }.play;

z.setn(Array.rand(16, 300, 320).put(16.rand, rrand(500, 1000)));
z.setn(Array.rand(16, 300, 320).put(16.rand, rrand(500, 1000)));
z.setn(Array.rand(16, 300, 320).put(16.rand, rrand(500, 1000)));

m.free;


m = { SinOsc.ar(a.kr(2, MouseX.kr(0, 19)), 0, 0.1) }.play; // modulate channel offset

z.setn(Array.rand(16, 300, 1320).put(16.rand, rrand(500, 1000)));


m.free; z.free;

// using as a audio monitor

p = BusPlug.audio(s, 2);
d = { Out.ar(p.index, PinkNoise.ar([0.1, 0.1])) }.play;


p.play; // monitor whatever plays in p (the execution order does not matter)



d.free;
d = { Out.ar(p.index, PinkNoise.ar([0.1, 0.1])) }.play;

p.stop;
p.play;

// also p can play to another bus:

p.stop;
p.play(12);

// listen to that bus for a test:
x = { InFeedback.ar(12, 2) }.play;
x.free;
```




