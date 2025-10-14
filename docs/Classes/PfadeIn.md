# PfadeIn

*Fade an event pattern in*

**Categories:** Streams-Patterns-Events>Patterns>Filter

**Related:** [PfadeOut](../Classes/PfadeOut.md)

## Description

Fade an event pattern in by scaling its amplitude over a period of time.

> **Note:** This only works on event patterns that are playing synths that have a `\amp` argument in them.




## Class Methods

### `new`
**Arguments:**

| Argument | Description |
|----------|-------------|
| `pattern` | The pattern to fade in. Must be an event pattern that plays a synth with the `\amp` parameter. |  
| `fadeTime` | The time it will take to fade. |  
| `holdTime` |  |  
| `tolerance` | The tolerance for the rounding of elapsed time used when setting the amplitude of the input pattern. |  


## Instance Methods

### `fadeTime`
Get or set the fadetime### `holdTime`
Get or set the hold time### `tolerance`
Get or set the tolerance used when rounding the internal time.### `embedInStream`
**Arguments:**

| Argument | Description |
|----------|-------------|
| `inval` |  |  
### `storeArgs`

## Examples


```supercollider
(
// Create a pattern that you want to fade
var pat = Pbind(\dur, 0.125, \degree, Pwhite(1, 10));

// Fade it in over 30 beats
pat = PfadeIn.new(pattern: pat, fadeTime: 30.0, holdTime: 1.0, tolerance: 0.0001);

// Play it
pat.play;
)
```




