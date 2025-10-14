# Dstutter

*Demand rate input replicator*

**Categories:** UGens>Demand

**Related:** [Ddup](../Classes/Ddup.md)


> **Note:** It is recommended to use [Ddup](../Classes/Ddup.md) instead. This class is retained for backwards compatibility.



> **⚠️ Warning:** Dstutter will return [Ddup](../Classes/Ddup.md)

## Class Methods

### `new`
**Arguments:**

| Argument | Description |
|----------|-------------|
| `n` | number of repeats (can be a demand ugen) |  
| `in` | input ugen |  
**Returns:** [Ddup](../Classes/Ddup.md)structurally related: [Pdup](../Classes/Pdup.md)
## Examples


```supercollider
(
{
    var freq, trig;
    var in = Dseq([1, 2, 3], inf);
    var rep = Dstutter(Diwhite(2, 8, inf), in);
    trig = Impulse.kr(MouseX.kr(1, 40, 1));
    freq = Demand.kr(trig, 0, rep).poll(trig) * 30 + 340;
    SinOsc.ar(freq) * 0.1

}.play;
)
```




