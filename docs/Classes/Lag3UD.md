# Lag3UD

*Exponential lag*

**Categories:** UGens>Filters

**Related:** [Lag](../Classes/Lag.md), [Lag2](../Classes/Lag2.md), [Lag3](../Classes/Lag3.md), [LagUD](../Classes/LagUD.md), [Lag2UD](../Classes/Lag2UD.md)

## Description

Lag3UD is equivalent to LagUD.kr(LagUD.kr(LagUD.kr(in, timeU, timeD), timeU, timeD), timeU, timeD), thus resulting in a smoother transition. This saves on CPU as you only have to calculate the decay factor once instead of three times. See [LagUD](../Classes/LagUD.md) for more details.


## Class Methods

### `ar`, `kr`
**Arguments:**

| Argument | Description |
|----------|-------------|
| `in` | input signal. |  
| `lagTimeU` | 60 dB lag time in seconds for the upgoing signal. |  
| `lagTimeD` | 60 dB lag time in seconds for the downgoing signal. |  

## Examples


```supercollider
// used to lag pitch
(
SynthDef(\lag3ud_help, { |out, freq = 300, lagup = 1, lagdown = 5|
    Out.ar(out,
        SinOsc.ar( // sine wave
            Lag3UD.kr( // lag the frequency
                freq,
                lagup,
                lagdown
            ),
            0, // phase
            0.2 // sine amplitude
        )
    )
}).add;
)

x = Synth(\lag3ud_help); // create the synth

x.set(\freq, 500); // set the frequency to a higher value (takes 1 second)
x.set(\freq, 100); // set the frequency to a lower value (takes 5 seconds)
x.free;
```




