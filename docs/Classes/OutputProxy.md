# OutputProxy

*Place holder for multiple outputs*

**Categories:** UGens>Base

## Description

OutputProxy is used by some UGens as a place holder for multiple outputs. There is no reason for a user to create an OutputProxy directly.

```supercollider
var out;
// Pan2 uses an OutputProxy for each of its two outputs.
out = Pan2.ar(WhiteNoise.ar, 0.0);
out.postln;
```




## Class Methods



## Instance Methods

### `source`
The UGen that is the source for this OutputProxy.
```supercollider
var left, right;
// Pan2 uses an OutputProxy for each of its two outputs.
# left, right = Pan2.ar(WhiteNoise.ar, 0.0);
left.source.postln;
```

The `source` method is also defined in Array, so that the source can be obtained this way as well:
```supercollider
var out;
// Pan2 uses an OutputProxy for each of its two outputs.
out = Pan2.ar(WhiteNoise.ar, 0.0);
out.postln;
out.source.postln;
```



