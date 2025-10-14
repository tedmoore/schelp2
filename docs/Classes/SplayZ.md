# SplayZ

*Spreads an array of channels across a ring of channels*

**Categories:** UGens>Multichannel>Panners

**Related:** [PanAz](../Classes/PanAz.md), [SplayAz](../Classes/SplayAz.md)

## Description

SplayZ spreads an array of channels across a ring of channels. Optional spread and center controls, and levelComp(ensation) (equal power). numChans and orientation are as in PanAz.
> **⚠️ Warning:** ATTENTION - SplayZ is deprecated because its geometry is wrong. It is only kept for backwards compatibility - please adapt your patches to [SplayAz](../Classes/SplayAz.md)! See [SplayAz](../Classes/SplayAz.md) help file for the comparison in behavior.


## Class Methods

### `ar`
**Arguments:**

| Argument | Description |
|----------|-------------|
| `numChans` |  |  
| `inArray` |  |  
| `spread` |  |  
| `level` |  |  
| `width` |  |  
| `center` |  |  
| `orientation` |  |  
| `levelComp` |  |  

### `arFill`
**Arguments:**

| Argument | Description |
|----------|-------------|
| `numChans` |  |  
| `n` |  |  
| `function` |  |  
| `spread` |  |  
| `level` |  |  
| `width` |  |  
| `center` |  |  
| `orientation` |  |  
| `levelComp` |  |  

## Examples


```supercollider
(
x = { |spread = 1, level = 0.2, width = 2, center = 0.0|
 SplayZ.ar(
  4,
  SinOsc.ar({ |i| LFNoise2.kr(rrand(10, 20), 200, i + 3 * 100) } ! 10),
  spread,
  level,
  width,
  center
 );
}.scope;
)

x.set(\spread, 1,   \center, 0);  // full n chans
x.set(\spread, 0.5, \center, -0.25); // less wide
x.set(\spread, 0, \center, 0);  // mono center (depends on orientation, see PanAz)
x.set(\spread, 0, \center, -0.25); //
x.set(\spread, 0.0, \center, 0.5); // mono, but rotate 1 toward the higher channels
x.set(\spread, 0.5, \center, 0.5); // spread over the higher channels
x.set(\spread, 0,   \center, -0.25); // all first
x.set(\spread, 1,   \center, 0);  // full n chans

x.free;

 // the same example written with arFill:
(
x = { |spread = 1, level = 0.5, width = 2, center = 0.0|
 SplayZ.arFill(
  4,
  10,
  { |i| SinOsc.ar(LFNoise2.kr(rrand(10, 20), 200, i + 3 * 100)) },
  spread,
  level,
  width,
  center
 );
}.scope;
)

 // or with mouse control
(
x = { var src;
 src = SinOsc.ar({ |i| LFNoise2.kr(rrand(10, 20), 200, i * 100 + 400) } ! 10);
 SplayZ.ar(4, src, MouseY.kr(1, 0), 0.2, center: MouseX.kr(-1, 1));
}.scope;
)
```




