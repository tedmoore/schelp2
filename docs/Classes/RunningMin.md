# RunningMin

*Track minimum level.*

**Related:** [RunningMax](../Classes/RunningMax.md), [RunningSum](../Classes/RunningSum.md)

**Categories:** UGens>Maths

## Description

Outputs the minimum value received at the input. When a trigger occurs at the reset input, the minimum output value is reset to the current value.


## Class Methods


### `ar`, `kr`
**Arguments:**

| Argument | Description |
|----------|-------------|
| `in` | The input signal. |  
| `trig` | Resets the output value to the current input value. A trigger happens when the signal changes from non-positive to positive. |  

## Examples


```
(
{
    SinOsc.ar(
            RunningMin.ar(Dust.ar(20), Impulse.ar(0.4)) * 500 + 200,
            0, 0.2
    )

}.play;
)

// follow a sine lfo, reset rate controlled by mouse x
(
{
    SinOsc.ar(
            RunningMin.kr(SinOsc.kr(0.2), Impulse.kr(MouseX.kr(0.01, 2, 1))) * 500 + 200,
            0, 0.2
    )

}.play;
)
```




