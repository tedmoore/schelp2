# Impulse

*Impulse oscillator.*

**Related:** [Blip](../Classes/Blip.md)

**Categories:** UGens>Generators>Deterministic

## Description

Outputs non-bandlimited single sample impulses.


## Class Methods


### `ar`, `kr`
**Arguments:**

| Argument | Description |
|----------|-------------|
| `freq` | Frequency in Hertz. **freq** may be negative. |  
| `phase` | Phase offset in cycles (0..1). Staying in this range offers a slight efficiency advantage, though phase offsets outside this range are supported and wrapped internally. |  
| `mul` | The output will be multiplied by this value. |  
| `add` | This value will be added to the output. |  
`Impulse` will output a `1.0` on the first sample (assuming no phase offset).If the initial `freq = 0`, a single impulse is output on first sample, followed by silence until the frequency changes.Supported rate combinations for `(freq, phase)` are `(a,a)`, `(a,k)`, `(a,i)`, `(k,k)`, `(k,i)`, `(i,k)`, `(i,i)`.`Impulse` is based on a wrapping phasor: phase advances on each frame and if the phase goes out of range and is wrapped in that frame, an impulse is output.Internally, the **phase** offset value is applied and wrapped into range *before* applying the phase increment (which is determined by the **freq**). After this phase increment, the trigger condition is checked. Therefore, it is the phase increment (freq) that triggers an impulse, *not* the phase offset.For example, if you wanted to create an impulse train by setting `freq: 0` and modulating the **phase** offset directly, `Impulse` would not support that. However, a you could generate an impulse train by phase modulation using the **rate** parameter of a [Phasor](../Classes/Phasor.md), like this:
```
(
{
    var f = 1000;
    HPZ1.ar(HPZ1.ar(
        Phasor.ar(rate: f * SampleDur.ir)
    )) > 1e-5
}.plot(0.005).plotMode_(\dstems)
)
```


## Examples


```
{ Impulse.ar(800, 0.0, 0.5, 0) }.play

{ Impulse.ar(XLine.kr(800, 100, 5), 0.0, 0.5, 0) }.play
```


modulate phase:

```
{ Impulse.ar(4, [0, MouseX.kr(0, 1)], 0.2) }.play;
```


an Impulse with frequency 0 returns a single impulse:

```
SynthDef(\imp, { OffsetOut.ar(0, Impulse.ar(0)); FreeSelf.kr(Impulse.kr(0)) }).add;
fork { (1 / (1..60).scramble).do { |dt| Synth.grain(\imp);  dt.wait } };
```




