# LagUD

*Exponential lag*

**Categories:** UGens>Filters

**Related:** [Lag](../Classes/Lag.md), [Lag2](../Classes/Lag2.md), [Lag3](../Classes/Lag3.md), [Lag2UD](../Classes/Lag2UD.md), [Lag3UD](../Classes/Lag3UD.md)

## Description

This is essentially the same as [Lag](../Classes/Lag.md) except that you can supply a different 60 dB time for when the signal goes up, from when the signal goes down. This is useful for smoothing out control signals, where "fade in" should be different from "fade out".


## Class Methods

### `ar`, `kr`
**Arguments:**

| Argument | Description |
|----------|-------------|
| `in` | input signal. |  
| `lagTimeU` | 60 dB lag time in seconds for the upgoing signal. |  
| `lagTimeD` | 60 dB lag time in seconds for the downgoing signal. |  
| `mul` |  |  
| `add` |  |  

## Examples


```supercollider
// used to lag pitch
(
SynthDef(\lagud_help, { |out, freq = 300, lagup = 1, lagdown = 5|
    Out.ar(out,
        SinOsc.ar( // sine wave
            LagUD.kr( // lag the frequency
                freq,
                lagup,
                lagdown
            ),
            0, // phase
            0.2 // sine amplitude
        )
    );
}).add;
)

x = Synth(\lagud_help); // create the synth
x.set(\freq, 500); // set the frequency to a higher value (takes 1 second)
x.set(\freq, 100); // set the frequency to a lower value (takes 5 seconds)
x.free;
```




