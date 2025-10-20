# Ndef

*node proxy definition*

**Categories:** JITLib>NodeProxy, Live Coding

**Related:** [ProxySpace](../Classes/ProxySpace.md), [Tdef](../Classes/Tdef.md)

## Description

Ndef registers synths by key. All accesses to the registered synths go through the Ndef class via that key. Registered synths can be replaced with other synths while playing. A synth and its replacement can automatically crossfade and the replacement time can be quantized.
Ndef is a reference to a proxy, forms an alternative to [ProxySpace](../Classes/ProxySpace.md). All methods are inherited from [NodeProxy](../Classes/NodeProxy.md).

```
Ndef(key)    // returns the instance
Ndef(key, obj)    // stores the object and returns the instance, like Tdef and Pdef.
```


Graphical editor overviewing all current Ndefs: [NdefMixer](../Classes/NdefMixer.md). A general overview: [JITLib](../Overviews/JITLib.md).

### First Example

```
s.boot;

Ndef(\a).play; // play to hardware output.
Ndef(\a).fadeTime = 2; // fadeTime specifies crossfade
// set the source
Ndef(\a, { SinOsc.ar([350, 351.3], 0, 0.2) });
Ndef(\a, { Pulse.ar([350, 351.3] / 4, 0.4, 0.2) });
Ndef(\a, Pbind(\dur, 0.03, \freq, Pbrown(0, 1, 0.1, inf).linexp(0, 1, 200, 350)));

Ndef(\a, { Ringz.ar(Ndef.ar(\b), [350, 351.3] * 2, 0.4) });
Ndef(\b, { Impulse.ar([5, 7]/2, [0, 0.5], 0.15) });

Ndef.clear(3); // clear all after 3 seconds
```





## Class Methods



### Creation

### `new`
Return a new node proxy and store it in a global ProxySpace under the key. If there is already an Ndef there, replace its object with the new one. The object can be any supported class, see [NodeProxy#Supported sources](../Classes/NodeProxy.md#supported-sources) help. Internally, all instances are kept in a [ProxySpace](../Classes/ProxySpace.md). The [EnvironmentRedirect#dispatch](../Classes/EnvironmentRedirect.md#dispatch) function is called when the source is set.**Arguments:**

| Argument | Description |
|----------|-------------|
| `key` | the name of the proxy (usually a symbol). If only the key is given and no object, it returns the proxy object:
```
Ndef(\x) // get the proxy
```

If key is an association, it is interpreted as **key -> server name**. (order changed in SC3.3 !). If no name is given, it uses the default server that was default when Ndef was first called. (to change it, see [#*defaultServer](#*defaultserver)). |  
| `object` | an object
```
Ndef(\x, { Dust.ar }); // returns the proxy and set the source object.
``` |  


### `ar`
equivalent to `*new(key).ar(numChannels, offset)` (see [BusPlug#-ar](../Classes/BusPlug.md#-ar))

### `kr`
equivalent to `*new(key).kr(numChannels, offset)` (see [BusPlug#-kr](../Classes/BusPlug.md#-kr))

### `clear`
clear all Ndefs in all proxyspaces of the Ndef class

### `clearDict`
clear all Ndefs and remove all proxyspaces of the Ndef class

### `defaultServer`
set the default server (default: `Server.default`)

### `all`
Return the dictionary of all servers, pointing to proxyspaces with Ndefs for each.
```
Ndef.all;
```



### `dictFor`
Return the proxyspace for a given server.
```
Ndef.dictFor(s);
```




## Instance Methods


### `proxyspace`
Return the proxyspace for this instance
```
Ndef(\x).proxyspace
```


### Setting default parameters
Behind every Ndef there is one single instance of [ProxySpace](../Classes/ProxySpace.md) per server used (usually just the one for the default server). This ProxySpace keeps default values for the proxies that can be set. This can be done by:


```
// set default quant
Ndef(\x).proxyspace.quant = 1.0;
```


The other values that can be set in such a way are: `clock, fadeTime, quant, reshaping, awake`.


## Examples


```
s.boot;

Ndef(\sound).play;
Ndef(\sound).fadeTime = 1;
Ndef(\sound, { SinOsc.ar([600, 635], 0, SinOsc.kr(2).max(0) * 0.2) });
Ndef(\sound, { SinOsc.ar([600, 635] * 3, 0, SinOsc.kr(2 * 3).max(0) * 0.2) });
Ndef(\sound, { SinOsc.ar([600, 635] * 2, 0, SinOsc.kr(2 * 3).max(0) * 0.2) });
Ndef(\sound, Pbind(\dur, 0.17, \freq, Pfunc({ rrand(300, 700) })));

Ndef(\lfo, { LFNoise1.kr(3, 400, 800) });
Ndef(\sound).map(\freq, Ndef(\lfo));
Ndef(\sound, { |freq| SinOsc.ar([600, 635] + freq, 0, SinOsc.kr(2 * 3).max(0) * 0.2) });
Ndef(\lfo, { LFNoise1.kr(300, 400, 800) });

Ndef.clear; // clear all Ndefs
```



### using Ndef inside other Ndefs

```
Ndef(\lfo2, { LFNoise1.kr(LFNoise1.kr(0.1).exprange(1, 300) ! 2, 400, 800) });
Ndef(\sound, { Blip.ar(Ndef.kr(\lfo2), 30) * 0.2 }).play;

Ndef(\lfo2, { [MouseX.kr(10, 300, 1), MouseY.kr(10, 300, 1)] });
```




### setting and mapping parameters

```
Ndef(\sound, { |freq = 56, numHarm = 10| Blip.ar(freq, numHarm, 30) * 0.2 }).play;
Ndef(\sound).set(\freq, 15);
Ndef(\sound).set(\freq, 15, \numHarm, 100);

Ndef(\lfo, { LFNoise2.kr(2).exprange(10, 200) });
Ndef(\sound).map(\numHarm, Ndef(\lfo));
Ndef(\sound).set(\numHarm, nil); // unmap.
Ndef(\sound).stop;
```




### Reserved parameters
Three parameters are automatically specified if they don't exist in a given UGen function. You can override their use: `[\out, \gate, \fadeTime]`



### Specifying your own envelope
If a UGen function that is passed to the proxy has its own envelope, and if this envelope can free the synth, the node proxy uses this envelope instead of making its own. If you provide a `fadeTime` argument, the proxy's fadeTime will be used.


```
Ndef(\sound).fadeTime = 3;
(
Ndef(\sound, { |fadeTime = 1, gate = 1|
    var e = Env.adsr(fadeTime, 0.01, 0.4, fadeTime).ar(2, gate);
    SinOsc.ar(100 + (e * 700), SinOsc.ar(208) * (1 - e) * 6) * e * 0.1
}).play
)
```




### Simple audio routing with the <<> operator

```
(
Ndef(\sound, {
    RHPF.ar(
        \in1.ar([0, 0]) * \in2.ar([0, 0]),
        \freq.kr(6000, 2),
        \rq.kr(0.2)
    ) * 7
}).play;
Ndef(\sound).fadeTime = 0.2;    // avoid harsh clicks
)

Ndef(\a, { SinOsc.ar(MouseX.kr(300, 1000, 1) * [1, 1.2], \phase.ar([0, 0]) * 0.2) });
Ndef(\b, { LFDNoise3.ar(MouseY.kr(3, 1000, 1) * [1, 1.2]) });
Ndef(\c, { LFTri.ar(MouseY.kr(3, 10, 1) * [1, 1.2]).max(0) });
Ndef(\a).fadeTime = 0.2;    // avoid harsh clicks again

Ndef(\sound) <<>.in1 Ndef(\a);
Ndef(\sound) <<>.in2 Ndef(\b);
Ndef(\sound) <<>.in2 Ndef(\c);
Ndef(\a) <<>.phase Ndef(\sound);
Ndef(\a) <<>.phase nil;    // unmap
Ndef.clear(3);        // fade out and clear all Ndefs
```




### Embedding multi-channel Patterns, playing Streams in parallel
Controlling multi-channeled sequenced streams and having independent control over filtering and node ordering is a difficult topic in SuperCollider. However, using Ndefs (or their superclass [NodeProxy](../Classes/NodeProxy.md) or a [ProxySpace](../Classes/ProxySpace.md)) may provide a convenient solution.


```
// a SynthDef, creating single-channel grain when instantiated
(
SynthDef(\grain, { |out = 0, freq = 300, amp = 0.3|
    OffsetOut.ar(out, Pulse.ar(freq) * EnvGen.kr(Env.perc, doneAction: Done.freeSelf) * amp)
}).add;
)

// number of channels
~numChans = 5;

// values in a Pattern may be set in various ways
// here we use control buses, except for \dur which
// doesn't accept a control bus in parallel playing streams
// therefore we use PatternProxies
~durs = ~numChans.collect({ |i| PatternProxy(0.5 + (i/10)) });

// other parameters could as well be controlled in PatternProxies,
// yet, control buses are convenient either
~freqs = Bus.control(s, ~numChans);
~freqs.setn(Array.geom(~numChans, 300, 1.1));
~amps = Bus.control(s, ~numChans);
~amps.setn(0.2 ! ~numChans);

// the Pattern: a Ppar holding one Pbind for each channel,
// all wrapped in a Pdef
(
Pdef(\ppar,
    Ppar({ |i|
        Pbind(
            \instrument, \grain,
            // we only set a single channel
            \dur, ~durs[i],
            \freq, ~freqs.subBus(i).asMap,
            \amp, ~amps.subBus(i).asMap,
            // the Pattern will play to a yet unknown private bus
            // we only want to make sure the offset is right
            \channelOffset, i,
        )
    } ! ~numChans)
)
)

// initialize an Ndef that will hold the Pdef as its source
// make sure the Ndef gets initialized to the right number of channels by calling 'mold'
Ndef(\ppar).mold(~numChans, \audio, \elastic);
Ndef(\ppar)[0] = Pdef(\ppar);

// mix the 5 channel audio coming from Ndef(\ppar) down to stereo
// Splay will spread the channels over the stereo panorama
// possibly use headphones to clearly identify the effect
Ndef(\stereo, { Splay.ar(\in.ar(0 ! ~numChans)) });

// concatenate the Ndefs, so Ndef(\ppar)'s out will feed into Ndef(\stereo)'s in
Ndef(\stereo) <<> Ndef(\ppar);
Ndef(\stereo).play;

// change durations
~durs.do({ |pp, i| pp.source = Pseq(Array.fib(5, i/10 + 0.1, i+1/5), inf) });
~durs.do({ |pp, i| pp.source = 0.5 + (i/10) });
~durs.do({ |pp| pp.source.postcs });

// frequencies
~freqs.setn(Array.geom(~numChans, 250, 1.6));
~freqs.setn(Array.geom(~numChans, 300, 1.1));

// add a filter Ndef
(
Ndef(\filter, {
    HPF.ar(
        \in.ar(0 ! ~numChans),
        SinOsc.ar({ |i| 2 + i }  ! ~numChans) + 1 * \multFreq.kr(Array.geom(~numChans, 400, 2))
    )
}).mold(~numChans, \audio, \elastic);
)

// set a fadeTime for smooth transitions and add the filter to the chain
#[ppar, stereo, filter].do({ |k| Ndef(k).fadeTime_(3) });
Ndef(\stereo) <<> Ndef(\filter) <<> Ndef(\ppar);

// set filter param, considering fadeTime
Ndef(\filter).xset(\multFreq, Array.rand(~numChans, 20, 10000));

Ndef.clear;
Pdef.clear;
```




### Making Copies

### `copy`
Because an Ndef is a unique instance for a given key, it can be copied only by supplying a new key. See also: [NodeProxy#-copy](../Classes/NodeProxy.md#-copy).
```
Ndef(\x, { SinOsc.ar(Rand(500, 900)) * 0.1 }).play;
Ndef(\x).copy(\y);
Ndef(\y).play;
```

**Arguments:**

| Argument | Description |
|----------|-------------|
| `newKey` | A valid new key, usually a [Symbol](../Classes/Symbol.md) |  



### Recursion
Ndefs can be used recursively. A structure like the following works:


```
Ndef(\sound, { SinOsc.ar([600, 635], Ndef.ar(\sound), LFNoise1.kr(2).max(0) * 0.2) });
Ndef(\sound).play;
Ndef.clear;
```


This is because there is a feedback delay (the server's **block size**), usually 64 samples, so that calculation can reiterate over its own outputs. For single sample feedback, see:


```
(Platform.resourceDir +/+ "examples/demonstrations/single_sample_feedback.scd").openDocument;
```




### Using different servers

```
// create a new server
a = Server(\foo, NetAddr("127.0.0.1", 57123)).boot.makeWindow;
Ndef(\sound, { SinOsc.ar([600, 635]) * SinOsc.kr(2).max(0) * 0.2 }).play; // play on default
Ndef(\sound -> \foo, { SinOsc.ar([700, 745]) * SinOsc.kr(2).max(0) * 0.2 }).play; // play on foo

// clear definitions
Ndef(\sound -> \foo).clear(3);
Ndef(\sound).clear(3);

a.dump;    // display settings of new server
a.quit;    // terminate new server
```






### GUI

```
// create a window for a given Ndef
Ndef(\sound).edit
(
Ndef(\sound, { |freq = 440, rate = 2|
    SinOsc.ar(freq * [1, 1.625]) * SinOsc.kr(rate).max(0) * 0.2
}).play;
)

// set lags for controls:
Ndef(\sound).lag(\freq, 0.2, \rate, 0.5);
Ndef(\sound).clear(1);

// create a mixer for all Ndefs:
NdefMixer(s);
```




### Using Associations
For a complete list, see [NodeProxy](../Classes/NodeProxy.md), and [NodeProxy_roles](../Reference/NodeProxy_roles.md)


```
// setsrc
(
Ndef(\x,
    \setsrc -> Pbind(\source,
        Pseq([
            { LFTri.ar(280 * Line.kr(1.1, 0.4, rrand(2, 3)) + [0, 1]) * 0.1 },
            { Pulse.ar(40 + [0, 1]) * 0.1 },
            { LFTri.ar(LFTri.kr(1).round(1.0.rand) + 1 * 180 + [0, 1], 0.04) * 0.3 },
        ], inf),
        \dur, Prand([3, 2, 4], inf)
    )
).play;
)
```






