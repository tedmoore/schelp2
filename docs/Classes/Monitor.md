# Monitor

*link between busses*

**Categories:** JITLib>NodeProxy, Live Coding

**Related:** [playN](../Reference/playN.md), [NodeProxy](../Classes/NodeProxy.md), [Bus](../Classes/Bus.md)

## Description

A general purpose class for monitoring or crosslinking between busses. It supports multichannel expansion and crossfading between settings. It provides optimizations for playing contiguous channels to other contiguous busses ([#-play](#-play)) and for more complex routings, such as splitting, spreading etc to multiple channels ([#-playN](#-playn)). Monitor uses the existing set of [SystemSynthDefs](../Classes/SystemSynthDefs.md) to do this.

```supercollider
{ Out.ar(87, SinOsc.ar(MouseX.kr(240, 1000, 1) * [1, 2, 3], 0, 0.2)) }.play; // play three sine tone on channels 87, 88, and 89
x = Monitor.new; // create a new monitor
x.play(fromIndex: 87, fromNumChannels: 3, toIndex: 0, toNumChannels: 2); // play them back to the stereo hardware channels
```




## Class Methods



## Instance Methods

### `play`
Plays from a bus index with a number of channels to another index with a number of channels, within a target group, or a server.**Arguments:**

| Argument | Description |
|----------|-------------|
| `fromIndex` | bus index from which to read |  
| `fromNumChannels` | number of channels to read from. |  
| `toIndex` | bus index to which to write. |  
| `toNumChannels` | number of channels to write. If this number is larger or smaller than fromNumChannels, wrap around. If nothing is given, uses fromNumChannels. |  
| `target` | where to send the synths to (default: server default group) |  
| `multi` | keep old links and add new one: this allows you to add layer after layer, otherwise free the previous mapping (false by default). |  
| `volume` | volume at which to monitor |  
| `fadeTime` | specifies the fade in and fade out time |  
| `addAction` | where, relative to the target to place the monitor group.
```supercollider
s.boot;
s.scope(16);

{ Out.ar(87, SinOsc.ar(MouseX.kr(40, 10000, 1) * [1, 2, 3], 0, 0.2)) }.play;
x = Monitor.new;
x.play(87, 3, 1, 2);
x.out = 0;
x.stop(3.0);
x.play(87, 1, 0, 1); // in > out : now mixes down (wrapping)
x.play(89, 1, 0, 2); // in < out : now distributes to 2 channels
x.stop;

// multiple play
x.play(87, 1, 0, 2, multi: true);
x.play(88, 1, 0, 2, multi: true);
x.play(89, 1, 0, 2, multi: true);
x.stop;
``` |  
### `playN`
Plays from an array of bus indices to another array of bus indices with an array of amplitudes, within a target group, or a server.
> **Note:** The arguments **out**, **amp** and **in** can be nested arrays. see also [playN](../Reference/playN.md)The three arguments out, amp, and in will wrap if they do not have the same size, like this: `[[0, 1], [0.1], [3, 4, 5]].flop`

**Arguments:**

| Argument | Description |
|----------|-------------|
| `out` | array of destination channels. |  
| `amp` | array of amplitudes for each channel |  
| `in` | array of source channels |  
| `vol` | global scaling value for amplitudes |  
| `fadeTime` | specifies the fade in and fade out time |  
| `target` | where to play (default: server default group) |  
| `addAction` | where, relative to the target to place the monitor group. |  
| `multi` | keep old links and add new one: this allows you to add layer after layer, otherwise free ther previous mapping (false by default).
```supercollider
// examples: args are // outs, amps, ins, vol, fadeTime

{ Out.ar(87, SinOsc.ar(MouseX.kr(40, 10000, 1) * [1, 2, 3], 0, 0.2)) }.play;
x = Monitor.new;

(
x.playN(
    [0, 1, 4],             // to these outs
    [0.1, 0.4, 0.3],     // with these volumes
    [87, 88, 89]        // from these ins
);
)
(
x.playN(
    [0, [1, 3, 2], 4],         // outs can be nested: 87 -> 0, 88 -> [1, 3, 2], 89 -> 4
    [0.1, [0.4, 0.2, 0.1], 0.3],    // with nested volumes 0.1, [0.4, 0.2, 0.1], and 0.3
    [87, 88, 89]);             // reading from these ins
)
// can also set global volume and fadetime
x.playN(vol: 0.0, fadeTime: 4);
``` |  
### `stop`
Stops within the fadeTime.
> **Note:** this keeps all the settings, so when using `play` next time, it will play in the same configuration, overriding only values provided.


```supercollider
{ Out.ar(87, SinOsc.ar(MouseX.kr(340, 1000, 1) * [1, 2, 3], 0, 0.2)) }.play;
x = Monitor.new.play(87, 3, 0, fadeTime: 3);
x.stop;
x.play;
```

**Arguments:**

| Argument | Description |
|----------|-------------|
| `argFadeTime` | The time for fading out all routing synths. |  
### `clear`
Stops within the fadeTime.
> **Note:** unlike `stop`, this removes all the settings.

### `vol`
Set the volume.
```supercollider
{ Out.ar(87, SinOsc.ar(MouseX.kr(340, 1000, 1) * [1, 2, 3], 0, 0.2)) }.play;
x = Monitor.new.play(87, 3, 0, fadeTime: 3);
x.vol = 0.3;
x.stop;
```

### `out`
Set or get the first output index.### `outs`
Set or get the array of output bus indices.### `ins`
Set or get the array of input bus indices.### `amps`
Set the array of amplitudes.### `fadeTimes`
Set or get the array of fadeTimes.### `fadeTime`
Set one single fadeTime for the next transition (may be a stop or a new play).### `isPlaying`
Returns true if the group is still playing.### `group`
Return the group in which all mapping synths are running.### `numChannels`
Return the number of input channels.### `copy`
Return a copy of the receiver, with the same channel setting, but not running. You can run it with the settings by sending it the [#-play](#-play) message, and pass in any modifications you want to make.### `playToBundle`
Adds all playing osc messages to a bundle, passed as an argument. The bundle object should implement the method **.add**

