# ProxySpace

*an environment of references on a server*

**Categories:** JITLib>Environments, Live Coding, Collections>Unordered

**Related:** [NodeProxy](../Classes/NodeProxy.md), [ProxyMixer](../Classes/ProxyMixer.md), [Overviews/JITLib](../Overviews/JITLib.md)

## Description

Generally a **proxy** is a placeholder for something. A node proxy is a placeholder for something **playing on a server** that writes to a limited number of busses (e.g. a synth or an event stream). NodeProxy objects can be replaced and recombined while they play. Also they can be used to build a larger structure which is used and modified later on. Overview: [JITLib](../Overviews/JITLib.md)
When accessed, ProxySpace returns a [NodeProxy](../Classes/NodeProxy.md). A similar class without environment: [Ndef](../Classes/Ndef.md)
For more examples see: [JITLib/proxyspace_examples](../Tutorials/JITLib/proxyspace_examples.md), [JITLib/jitlib_basic_concepts_01](../Tutorials/JITLib/jitlib_basic_concepts_01.md)
For GUI overview, see [ProxyMixer](../Classes/ProxyMixer.md). See [NodeProxy](../Classes/NodeProxy.md) for many relevant methods.

### First Example

```supercollider
s.boot;

p = ProxySpace.new;
p.fadeTime = 2; // fadeTime specifies crossfade
p[\out].play; // monitor an empty placeholder through hardware output
// set its source
p[\out] = { SinOsc.ar([350, 351.3], 0, 0.2) };
p[\out] = { Pulse.ar([350, 351.3] / 4, 0.4) * 0.2 };
p[\out] = Pbind(\dur, 0.03, \freq, Pbrown(0, 1, 0.1, inf).linexp(0, 1, 200, 350));

// route one proxy through another:
p[\out] = { Ringz.ar(p[\in].ar, [350, 351.3] * 8, 0.2) * 4 };
p[\in] = { Impulse.ar([5, 7]/2, [0, 0.5]) };

p.clear(3); // clear after 3 seconds
```





## Class Methods



### Creation
### `new`
**Arguments:**

| Argument | Description |
|----------|-------------|
| `server` | a [Server](../Classes/Server.md) object. Note that on remote computers the clock must be in sync. |  
| `name` | a [Symbol](../Classes/Symbol.md). If a name is given, the proxy space is **stored** in `ProxySpace.all` under this name. |  
| `clock` | for event-based or beat-sync playing use a [TempoClock](../Classes/TempoClock.md). |  

### `push`
replace the currentEnvironment with a new ProxySpace and **clear** the current one, if it is a ProxySpace (this is to avoid piling up proxy spaces).In order to move to another ProxySpace while keeping the current, use **pop** and then **push** a new one. To have multiple levels of proxy spaces, use **.new.push;**
### `pop`
restore the previous currentEnvironment
### `clearAll`
clear all registered spaces


## Instance Methods


### Play back and access
### `play`
returns a group that plays the [NodeProxy](../Classes/NodeProxy.md) at that **key**.**Arguments:**

| Argument | Description |
|----------|-------------|
| `key` | a [Symbol](../Classes/Symbol.md) |  
| `out` | output channel offset |  
| `numChannels` | play this number of channels. |  

### `record`
returns a [RecNodeProxy](../Classes/RecNodeProxy.md) that records the NodeProxy at that key.
### `ar`, `kr`
returns a NodeProxy output that plays the NodeProxy at that key, to be used within a function used as input to a node proxy
### `wakeUp`
when the proxyspace is created without a running server this method can be used. To run it (internally this is done by [play](#play) as well).
### `fadeTime`
set the fadetime of all proxies as well as the default fade time
### `clock`
set the clock of all proxies as well as the default clock.
### `quant`
set the quant of all proxies as well as the default quant.
### `free`
free all proxies (i.e. free also the groups, do not stop the monitors)
### `release`
release all proxies (i.e. keep the groups running)
### `stop`
stop all proxies (stop only monitors, do not stop synths)
### `end`
end all proxies (free and stop the monitors)
### `clear`
clear all proxies and remove them from the environment. This frees all buses. If a fadeTime is given, first fade out, then clear.
### `add`
add the ProxySpace to the repository (name required)
### `remove`
remove the ProxySpace from the repository

### Setting the sources
The **rate** and **numChannels** of the [NodeProxy](../Classes/NodeProxy.md) determined in a lazy way from the first object put into this environment (see helpfile). Once it is created it can only be set to a function that returns the same rate and a number of channels equal to the intial one or smaller. For details, see [JITLib/the_lazy_proxy](../Tutorials/JITLib/the_lazy_proxy.md).

### `put`
Gets the NodeProxy at **key** (if none exists, returns a new one) and sets its source to **obj**. For how this works, see also [LazyEnvir](../Classes/LazyEnvir.md) and [NodeProxy](../Classes/NodeProxy.md).
### `at`
Return the proxy source object at that key.

### garbage collecting
### `clean`
free and remove all proxies that are not needed in order to play the ones passed in with 'exclude'. if none are passed in, all proxies that are monitoring (with the .play message) are kept as well as their parents etc.
### `reduce`
free all proxies that are not needed in order to play the ones passed in with 'to'. if none are passed in, all proxies that are monitored (with the play message) are kept as well as their parents etc.

### making copies
### `copy`
Copies the environment into a new one, with each proxy being copied as well (See: [NodeProxy#-copy](../Classes/NodeProxy.md#-copy)). Also the instance variables that determine the ProxySpace behaviour are included, such as server, fadeTime, quant, reshaping (this happens in the `copyState` method).
```supercollider
p = ProxySpace.push(s.boot);
p.reshaping = \elastic;
~out.play;
~out = { Blip.ar(~freq, ~numharm) };
~freq = 70;
~numharm = { MouseX.kr(2, 100, 1) };

q = p.copy; p.pop; q.push;

q.reshaping.postln; // also elastic
~out.play;
~freq = { MouseY.kr(2, 1000, 1) * [1, 1.2] };

p.end; q.end;
```



### Writing code
### `document`
creates a new document with the current proxyspace state. This does not allow open functions as proxy sources. see: [JITLib/jitlib_asCompileString](../Tutorials/JITLib/jitlib_asCompileString.md).**Arguments:**

| Argument | Description |
|----------|-------------|
| `keys` | list of keys to document a subset of proxies |  
| `onlyAudibleOutput` | a boolean. |  
| `includeSettings` | a boolean. |  

### `asCode`
If proxyspace is globally accessible, this posts a code string that can access it.
```supercollider
p = ProxySpace.push(s.boot);
p.reshaping = \elastic;
p.asCode;
p.pop;

Ndef(\x); // initializes an Ndef proxyspace for default server
Ndef.all[\localhost]; // access that proxyspace
Ndef.all[\localhost].asCode; // posts as valid code
```



## Examples


```supercollider
// ProxySpace returns instances of NodeProxy:
a = NodeProxy(s)     is equivalent to ~a;
a.source = ...        is equivalent to ~a = ...
a[3] = ...        is equivalent to ~a[3] = ...

// the two expressions are equivalent:
~out = something;
currentEnvironment.put(\out, something);
```



```supercollider
// examples

p = ProxySpace.push(s.boot); // use ProxySpace as current environment.

~out.play;

~out = { SinOsc.ar([400, 407] * 0.9, 0, 0.2) };

~out = { SinOsc.ar([400, 437] * 0.9, 0, 0.2) * LFPulse.kr([1, 1.3]) };

~out = { SinOsc.ar([400, 437] * 0.9, 0, 0.2) * ~x.kr(2) };

~x = { LFPulse.kr([1, 1.3] * MouseX.kr(1, 30, 1)) };

~out = { SinOsc.ar([400, 437] * Lag.kr(0.1 + ~x, 0.3), 0, 0.2) * ~x };

p.fadeTime = 5;

~out = { SinOsc.ar([400, 437] * 1.1, 0, 0.2) * ~x.kr(2) };

p.clear(8); // end and clear all in 8 sec.


p.pop; // move out.
```




