# FreqScopeView

*Frequency analysis view*

**Categories:** GUI>Views

**Related:** [FreqScope](../Classes/FreqScope.md)

## Description

FreqScopeView shows the frequency spectrum of a specified audio bus.

> **Note:** The scope will remain active after a command-period. To turn it off you must use the 'active' method. Very important: You must run `kill()` when the parent window is closed to avoid problems. It also frees the buffers that the scope allocated and stops the FFT analysis synth. So:
```supercollider
(
w = Window("My Analyzer", Rect(0, 0, 511, 300));
f = FreqScopeView(w, w.view.bounds);
w.onClose_({ f.kill }); // YOU MUST HAVE THIS
w.front;
)
```




## Class Methods


### `new`
**Arguments:**

| Argument | Description |
|----------|-------------|
| `parent` | The parent view. |  
| `bounds` | An instance of [Rect](../Classes/Rect.md), or a [Point](../Classes/Point.md) indicating `width@height`. |  
| `server` | The server to be shown in scope. |  
Example:
```supercollider
// Start server
s.boot;

// Create analyzer in a window
(
w = Window("My Analyzer", Rect(0, 0, 511, 300)); // width should be 511
f = FreqScopeView(w, w.view.bounds);
f.active_(true); // turn it on the first time;

w.onClose_({ f.kill }); // you must have this
w.front;
{ SinOsc.ar([500, 1000], 0, 0.25).mean.dup }.play(s); // start two sine waves
)
```


### `response`
Create a scope in a special frequency-response mode. This uses FFT-based spectral division to estimate the frequency response of some effect, on the assumption that the signal to bus1 is transformed to the signal at bus2 by some linear time-invariant process.**Arguments:**

| Argument | Description |
|----------|-------------|
| `parent` | The parent view. |  
| `bounds` | An instance of [Rect](../Classes/Rect.md), or a [Point](../Classes/Point.md) indicating `width@height`. |  
| `bus1` | The bus on which the "pre" signal is found. |  
| `bus2` | The bus on which the "post" signal is found. |  
| `freqMode` | Linear (0) or log(1) frequency mode. Defaults to 1. |  
Example:
```supercollider
s.boot

// basic usage. try these. Each one will open a new window
// move the mouse left and right to test response in different ranges
LPF.scopeResponse
HPF.scopeResponse
MoogFF.scopeResponse
BBandPass.scopeResponse
BLowShelf.scopeResponse // by default BLowShelf doesn't mangle much
Resonz.scopeResponse
BRF.scopeResponse
Integrator.scopeResponse
Median.scopeResponse // nonlinear, and therefore interesting

// customize the parameters for more informative scoping
{ |in| MoogFF.ar(in, freq: MouseX.kr(10, 10000, 1),
gain: MouseY.kr(4, 0)) }.scopeResponse
```



### Subclassing and Internal Methods
The following methods are usually not used directly or are called by a primitive. Programmers can still call or override these as needed.



## Instance Methods

### `kill`
Very important. This must be run when the parent window is closed to avoid problems. It also frees the buffers that the scope allocated and stops the FFT analysis synth.### `active`
Turn the scope on or off.**Arguments:**

| Argument | Description |
|----------|-------------|
| `bool` | An instance of [Boolean](../Classes/Boolean.md). |  
### `freqMode`
**Arguments:**

| Argument | Description |
|----------|-------------|
| `mode` | 0 = linear, 1 = logarithmic. |  
### `inBus`
The bus to listen on.**Arguments:**

| Argument | Description |
|----------|-------------|
| `num` | An audio [Bus](../Classes/Bus.md) number. |  
### `dbRange`
Get/set the amplitude range.**Arguments:**

| Argument | Description |
|----------|-------------|
| `db` | A [Number](../Classes/Number.md). |  
### `special`
Put the scope into a special mode using a user-specified [SynthDef](../Classes/SynthDef.md). Note that only very particular SynthDefs should be used, namely ones that are derived from the `\freqScope0` or `\freqScope1` SynthDefs. Most users will not need to use this method directly, but it can be used to provide a customised analysis shown in the scope.**Arguments:**

| Argument | Description |
|----------|-------------|
| `defname` | Name of the [SynthDef](../Classes/SynthDef.md) you wish to use. |  
| `extraArgs` | Extra arguments that you may wish to pass to the synth. |  

### instance variables
### `server`
the server that is freqscoped
### `synth`
the synth running the freqscope analysis
### `scope`
the scopeview that shows the running analysis
### `scopebuf`
the buffer used by the scope

### Internal Methods
The following methods are usually not used directly or are called by a primitive. Programmers can still call or override these in subclasses as needed.

### `initFreqScope`
initialize and show on parent view
### `doesNotUnderstand`
redirects methods to scope view variable
### `start`

### `allocBuffers`

### `freeBuffers`

### `bufSize`

### `doOnServerQuit`

### `doOnServerTree`

### `shmScopeAvailable`

### `specialSynthArgs`

### `specialSynthDef`


## Examples


```supercollider
// Start server
s.boot;

// Create analyzer in a window
(
w = Window("My Analyzer", Rect(0, 0, 511, 300)); // width should be 511
f = FreqScopeView(w, w.view.bounds);
f.active_(true); // turn it on the first time;

w.onClose_({ f.kill }); // you must have this
w.front;
{ SinOsc.ar([500, 1000], 0, 0.25).mean.dup }.play(s); // start two sine waves
)

f.freqMode_(1); // change to log scale so we can see them
f.inBus_(1); // look at bus 1
f.dbRange_(200); // expand amplitude range
f.active_(false); // turn scope off (watch CPU)
f.active_(true); // turn it back on

// Now press command-period. The scope is still running.

{ Mix.ar(SinOsc.ar([500, 1200, 3000, 9000, 12000], 0, [0.2, 0.1, 0.05, 0.03, 0.01])) }.play(s); // restart some sines

// Close window and scope is killed.
```




