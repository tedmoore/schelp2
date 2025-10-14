# MouseButton

*Mouse button UGen.*

**Related:** [KeyState](../Classes/KeyState.md), [MouseX](../Classes/MouseX.md), [MouseY](../Classes/MouseY.md)

**Categories:** UGens>User interaction

## Description

Mouse button UGen.
> **⚠️ Warning:** This UGen will not work for Linux users using Wayland, as the Wayland protocol does not allow a global keyboard or mouse state to be captured. The UGen will return $0.0$ as constant value. For more information see [https://github.com/supercollider/supercollider/issues/4544](https://github.com/supercollider/supercollider/issues/4544)


## Class Methods

### `kr`
**Arguments:**

| Argument | Description |
|----------|-------------|
| `minval` | Value when the button is not pressed. |  
| `maxval` | Value when the button is pressed. |  
| `lag` | Lag factor. |  

## Examples


```supercollider
{ SinOsc.ar(MouseButton.kr(400, 440, 0.1), 0, 0.1) }.play;
{ SinOsc.ar(MouseButton.kr(400, 740, 2), 0, 0.1) }.play;

(
SynthDef(\mousexyb, { |out = 0|
    var mousex, mousey, mousebutton;
    mousex = MouseX.kr(500, 1000); // this will determine the frequency of the sound (minimum value, maximum value, warp, lag)
    mousey = MouseY.kr(0, 0.3); // this will determine the amplitude of the sound
    mousebutton = MouseButton.kr(0, 1, 2); // this will turn the sound on or off (minimum value, maximum value, lag)
    Out.ar(out, SinOsc.ar(mousex, 0, mousey) * mousebutton);
}).add
)

x = Synth.new(\mousexyb);
x.free;
```




