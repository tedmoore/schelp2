# LorenzL

*Lorenz chaotic generator*

**Categories:** UGens>Generators>Chaotic

## Description

A strange attractor discovered by Edward N. Lorenz while studying mathematical models of the atmosphere. The system is composed of three ordinary differential equations:

The time step amount `h` determines the rate at which the ODE is evaluated. Higher values will increase the rate, but cause more instability. A safe choice is the default amount of 0.05.


## Class Methods


### `ar`
**Arguments:**

| Argument | Description |
|----------|-------------|
| `freq` | Iteration frequency in Hertz |  
| `s` | Equation variable |  
| `r` | Equation variable |  
| `b` | Equation variable |  
| `h` | Integration time step |  
| `xi` | Initial value of x |  
| `yi` | Initial value of y |  
| `zi` | Initial value of z |  
| `mul` |  |  
| `add` |  |  

## Examples


```
// vary frequency
{ LorenzL.ar(MouseX.kr(20, SampleRate.ir)) * 0.3 }.play(s);
```



```
// randomly modulate params
(
{ LorenzL.ar(
    SampleRate.ir,
    LFNoise0.kr(1, 2, 10),
    LFNoise0.kr(1, 20, 38),
    LFNoise0.kr(1, 1.5, 2)
) * 0.2 }.play(s);
)
```



```
// as a frequency control
{ SinOsc.ar(Lag.ar(LorenzL.ar(MouseX.kr(1, 200)), 3e-3)*800+900)*0.4 }.play(s);
```




