# FreqScope

*Frequency spectrum visualizer*

**Categories:** GUI>Interfaces

**Related:** [FreqScopeView](../Classes/FreqScopeView.md)

## Description

FreqScope shows the frequency spectrum of the specified audio bus. The scope will remain active after a command-period. To turn it off you must either click off the 'Power' button or close the window.
Panel commands:
| Power | Turns the scope on and off. This is useful for freezing the signal on the display or for saving CPU. | 
| --- | --- || BusIn | The audio bus to be analyzed. | | FrqScl | Determines the mapping of frequencies on the x-axis. Can be linear (lin) or logarithmic (log). Logarithmic is equal spacing per musical octave. | | dbCut | Determines the lowest decibel shown on the y-axis. | 


## Class Methods


### `new`
**Arguments:**

| Argument | Description |
|----------|-------------|
| `width` | Default value is 512. |  
| `height` | Default value is 300. |  
| `busNum` | The number of the audio [Bus](../Classes/Bus.md) to be monitored. |  
| `scopeColor` | An instance of [Color](../Classes/Color.md). The drawing color of the scope. |  
| `bgColor` | An instance of [Color](../Classes/Color.md). The background color of the scope. |  
| `server` | the server whose buses to show on scope. |  
Example:
```
s.boot;

// create a new analyzer
FreqScope.new(400, 200, 0, server: s);

// basic sine
{ SinOsc.ar(2000, 0, 0.25) }.play(s);

// random saw
{ RLPF.ar(Saw.ar(110, 0.2), LFNoise2.kr(1, 1e4, 1e4), LFNoise2.kr(1, 0.2, 0.22)) }.play(s);

// modulate phase
{ SinOsc.ar(800, SinOsc.ar(XLine.kr(20, 8000, 10), 0, 2pi), 0.25) }.play(s);

// all harmonics
{ Blip.ar(200, Line.kr(1, 100, 10), 0.2) }.play(s);
```



### Subclassing and Internal Methods
The following methods are usually not used directly or are called by a primitive. Programmers can still call or override these as needed.


### `scopeOpen`
Returns a [Boolean](../Classes/Boolean.md), whether the scope is open.


## Instance Methods


### Subclassing and Internal Methods
The following methods are usually not used directly or are called by a primitive. Programmers can still call or override these as needed.


### `window`
Returns the window in which the [FreqScopeView](../Classes/FreqScopeView.md) is placed.

### `scope`
Returns the [FreqScopeView](../Classes/FreqScopeView.md).


