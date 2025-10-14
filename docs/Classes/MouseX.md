# MouseX

*Cursor tracking UGen.*

**Related:** [KeyState](../Classes/KeyState.md), [MouseButton](../Classes/MouseButton.md), [MouseY](../Classes/MouseY.md)

**Categories:** UGens>User interaction

## Description

Cursor tracking UGen.
> **⚠️ Warning:** This UGen will not work for Linux users using Wayland, as the Wayland protocol does not allow a global keyboard or mouse state to be captured. The UGen will return a constant random value between $0.0$ and $1.0$. For more information see [https://github.com/supercollider/supercollider/issues/4544](https://github.com/supercollider/supercollider/issues/4544)


## Class Methods

### `kr`
**Arguments:**

| Argument | Description |
|----------|-------------|
| `minval` | Value corresponding to the left edge of the screen. |  
| `maxval` | Value corresponding to the right edge of the screen. |  
| `warp` | Mapping curve. 0 is linear, 1 is exponential (e. g. for freq or times). Alternatively you can specify: 'linear' or 'exponential'. |  
| `lag` | Lag factor to dezipper cursor movement. |  

## Examples


```supercollider
{ SinOsc.ar(MouseX.kr(40, 10000, 1), 0, 0.1) }.play;
{ SinOsc.ar(MouseX.kr(500, 10000, 1).poll, 0, 0.1) }.play;
```




