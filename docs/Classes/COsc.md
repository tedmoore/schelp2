# COsc

*Chorusing wavetable oscillator.*

**Related:** [Osc](../Classes/Osc.md), [OscN](../Classes/OscN.md), [VOsc](../Classes/VOsc.md), [VOsc3](../Classes/VOsc3.md)

**Categories:** UGens>Generators>Deterministic

## Description

Chorusing wavetable lookup oscillator. Produces sum of two signals at

```
(freq ± (beats / 2)).
```


Due to summing, the peak amplitude is not the same as the wavetable and can be twice of that.


## Class Methods


### `ar`, `kr`
**Arguments:**

| Argument | Description |
|----------|-------------|
| `bufnum` | The number of a buffer filled in wavetable format. |  
| `freq` | Frequency in Hertz. |  
| `beats` | Beat frequency in Hertz. |  
| `mul` | Output will be multiplied by this value. |  
| `add` | This value will be added to the output. |  

## Examples


```
(
b = Buffer.alloc(s, 512, 1, { |buf| buf.sine1Msg(1.0/[1, 2, 3, 4, 5, 6, 7, 8, 9, 10]) });
{ COsc.ar(b.bufnum, 200, 0.7, 0.25) }.play;
)
```




