# Peak

*Track peak signal amplitude.*

**Related:** [PeakFollower](../Classes/PeakFollower.md)

**Categories:** UGens>Analysis>Amplitude

## Description

Outputs the peak amplitude of the signal received at the input. When a trigger occurs at the `reset` input, the maximum output value is reset to the current value.
The reported peak will always be positive, i.e. the absolute value  of the signal at its peak amplitude, even when that peak is negative. To obtain the minimum and maximum values of the signal as is, use the [RunningMin](../Classes/RunningMin.md) and [RunningMax](../Classes/RunningMax.md) UGens.


## Class Methods


### `ar`, `kr`
**Arguments:**

| Argument | Description |
|----------|-------------|
| `in` | The input signal. |  
| `trig` | Trigger. Resets the output value to the current input value. A trigger happens when the signal changes from non-positive to positive. |  

## Examples


```
(
{
    SinOsc.ar(
            Peak.ar(Dust.ar(20), Impulse.ar(0.4)) * 500 + 200,
            0, 0.2
    )

}.play;
)

// follow a sine lfo, reset rate controlled by mouse x
(
{
    SinOsc.ar(
            Peak.kr(SinOsc.kr(0.2), Impulse.kr(MouseX.kr(0.01, 2, 1))) * 500 + 200,
            0, 0.2
    )

}.play;
)
```




