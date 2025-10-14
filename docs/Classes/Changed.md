# Changed

**Categories:** UGens>Triggers, UGens>Filters>Linear

*Triggers when a value changes*

## Description

Triggers when a value changes.


## Class Methods

### `ar`, `kr`
A special case fixed filter.**Arguments:**

| Argument | Description |
|----------|-------------|
| `input` | signal input |  
| `threshold` | threshold |  
Implements the formula:
```supercollider
out(i) = abs(in(i) - in(i-1)) > thresh
```


## Examples

detect changes in a signal:

```supercollider
(
{
    var changingSignal = LFNoise0.ar(1000);
    var changed = Changed.ar(changingSignal);
    [changingSignal, changed]
}.plot
);
```




