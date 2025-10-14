# Dwrand

*Demand rate weighted random sequence generator*

**Categories:** UGens>Demand, UGens>Random

**Related:** [Demand](../Classes/Demand.md)


## Class Methods

### `new`
**Arguments:**

| Argument | Description |
|----------|-------------|
| `list` | array of values or other ugens |  
| `weights` | array of values (should sum up to 1.0) |  
| `repeats` | number of values to return |  
structurally related: [Pwrand](../Classes/Pwrand.md), [TWindex](../Classes/TWindex.md), [TWChoose](../Classes/TWChoose.md)
## Examples


```supercollider
(
{
    var a, freq, trig;
    a = Dwrand([0, 1, 2, 7], [0.4, 0.4, 0.1, 0.1], inf).dpoll;
    trig = Impulse.kr(MouseX.kr(1, 400, 1));
    freq = Demand.kr(trig, 0, a) * 30 + 340;
    SinOsc.ar(freq) * 0.1

}.play;
)
```




