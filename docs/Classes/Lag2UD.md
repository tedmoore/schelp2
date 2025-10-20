# Lag2UD

*Exponential lag*

**Categories:** UGens>Filters

**Related:** [Lag](../Classes/Lag.md), [Lag2](../Classes/Lag2.md), [Lag3](../Classes/Lag3.md), [LagUD](../Classes/LagUD.md), [Lag3UD](../Classes/Lag3UD.md)

## Description

Lag2 is equivalent to Lag.kr(Lag.kr(in, time), time), thus resulting in a smoother transition. This saves on CPU as you only have to calculate the decay factor once instead of twice. See [Lag](../Classes/Lag.md) for more details.


## Class Methods


### `ar`, `kr`
**Arguments:**

| Argument | Description |
|----------|-------------|
| `in` | input signal. |  
| `lagTimeU` | 60 dB lag time in seconds for the upgoing signal. |  
| `lagTimeD` | 60 dB lag time in seconds for the downgoing signal. |  

## Examples


```
// used to lag pitch
(
SynthDef(\lag2ud_help, { |out, freq = 300, lagup = 1, lagdown = 5|
    Out.ar(out,
        SinOsc.ar( // sine wave
            Lag2UD.kr( // lag the frequency
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

x = Synth(\lag2ud_help); // create the synth

x.set(\freq, 500); // set the frequency to a higher value (takes 1 second)
x.set(\freq, 100); // set the frequency to a lower value (takes 5 seconds)
x.free;
```




