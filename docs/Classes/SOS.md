# SOS

*Second order filter section (biquad).*

**Related:** [FOS](../Classes/FOS.md)

**Categories:** UGens>Filters>Linear

## Description

A standard second order filter section. Filter coefficients are given directly rather than calculated for you. Formula is equivalent to:

```
out(i) = (a0 * in(i)) + (a1 * in(i-1)) + (a2 * in(i-2)) + (b1 * out(i-1)) + (b2 * out(i-2))
```




## Class Methods


### `ar`, `kr`
**Arguments:**

| Argument | Description |
|----------|-------------|
| `in` | signal input |  
| `a0` | See formula above. |  
| `a1` | See formula above. |  
| `a2` | See formula above. |  
| `b1` | See formula above. |  
| `b2` | See formula above. |  
| `mul` |  |  
| `add` |  |  

## Examples


```
// example: same as TwoPole
(
{
    var rho, theta, b1, b2;
    theta = MouseX.kr(0.2pi, pi);
    rho = MouseY.kr(0.6, 0.99);
    b1 = 2.0 * rho * cos(theta);
    b2 = rho.squared.neg;
    SOS.ar(LFSaw.ar(200, 0, 0.1), 1.0, 0.0, 0.0, b1, b2)
}.play
)


(
{
    var rho, theta, b1, b2;
    theta = MouseX.kr(0.2pi, pi);
    rho = MouseY.kr(0.6, 0.99);
    b1 = 2.0 * rho * cos(theta);
    b2 = rho.squared.neg;
    SOS.ar(WhiteNoise.ar(0.1 ! 2), 1.0, 0.0, 0.0, b1, b2)
}.play
)

// example with SOS.kr kr as modulator
(
{
    var rho, theta, b1, b2, vib;
    theta = MouseX.kr(0.2pi, pi);
    rho = MouseY.kr(0.6, 0.99);
    b1 = 2.0 * rho * cos(theta);
    b2 = rho.squared.neg;

    vib = SOS.kr(LFSaw.kr(3.16), 1.0, 0.0, 0.0, b1, b2);
    SinOsc.ar(vib * 200 + 600) * 0.2
}.play
)
```




