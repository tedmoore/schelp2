# Decay

*Exponential decay*

**Related:** [Decay2](../Classes/Decay2.md), [Integrator](../Classes/Integrator.md)

**Categories:** UGens>Filters>Linear, UGens>Envelopes

## Description

An integrating filter which, if given an impulse, will produce an exponentially decaying envelope. `Decay` is essentially the same as [Integrator](../Classes/Integrator.md), but instead of specifying the integration coefficient directly, it is calculated from the **decayTime**—the time required for input signal to attentuate 60 dB, or decay to 99.9% of its value.


## Class Methods


### `ar`, `kr`
**Arguments:**

| Argument | Description |
|----------|-------------|
| `in` | The input signal. |  
| `decayTime` | The time it takes for the input signal to decay 60 dB. |  
| `mul` | The output will be multiplied by this value. |  
| `add` | This value will be added to the output. |  

## Examples


```
// Plot the exponentially decaying envelope
(
var t60 = 0.1; // decayTime
plot({ Decay.ar(Impulse.ar(0), t60) }, t60);
)
```



```
// Used as an evelope generator
(
play({
    Decay.ar(
        in: Impulse.ar(XLine.kr(5,50,10), 0.25),
        decayTime: 0.2,
        mul: FSinOsc.ar(300)
    )
})
)
```


As can be heard in the previous example, when `Decay` is used as a modulator, its immediate onset can lead to discontinuities and audible clicks. This can be seen in the waveform:

```
(
plot({
    Decay.ar(
        in: Impulse.ar(50),
        decayTime: 0.015,
        mul: FSinOsc.ar(370)
    )
}, 0.1, bounds: Rect(50,50,1200,400))
)
```


[Decay2](../Classes/Decay2.md) allows for onset control, as shown below:

```
(
var t60, riseScale, riseFac, normFac;

t60 = 0.3; // decay time

// Onset control and normalization factor for Decay2
// (See Decay2 Help doc for more info)
riseScale = 0.3;
riseFac = riseScale / (2 - riseScale);
normFac = riseFac.pow(riseFac / (riseFac - 1)) / (1 - riseFac);

// Compare Decay (blue) and Decay2 (red)
plot({
    var imp = Impulse.ar(0);
    [
        Decay.ar(imp, t60),
        Decay2.ar(imp,
            attackTime: t60 * riseFac,
            decayTime: t60,
            mul: normFac
        )
    ]
}, duration: t60/2)
.plotColor_([Color.blue, Color.red])
.superpose_(true)
)
```




