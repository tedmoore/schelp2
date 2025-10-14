# StaticText

*A view displaying non-editable text*

**Categories:** GUI>Views

## Description

A view displaying non-editable text


## Class Methods



## Instance Methods


### Data
### `string`
 The text displayed by the view.**Arguments:**

| Argument | Description |
|----------|-------------|
| `` | A String. |  

### `object`
 If [#-setBoth](#-setboth) is true, setting this variable also sets [#-string](#-string) to the value interpreted [as String](../Classes/Object.md#-asstring).**Arguments:**

| Argument | Description |
|----------|-------------|
| `` | Any object, typically one which makes sense to display as a string, such as a Float. |  

### `setBoth`
 A variable stating whether setting [#-object](#-object) will also set [#-string](#-string).**Arguments:**

| Argument | Description |
|----------|-------------|
| `` | A Boolean. |  


### Appearance
### `align`
 The alignment of the displayed text. See [gui_alignments](../Reference/gui_alignments.md) for possible values.
### `font`
 The font used to display the text.**Arguments:**

| Argument | Description |
|----------|-------------|
| `` | A Font. |  

### `stringColor`
 The color used to display the text.**Arguments:**

| Argument | Description |
|----------|-------------|
| `` | A Color. |  

### `background`
 Setting this variable colors the whole area occupied by the view under the text with the given color.**Arguments:**

| Argument | Description |
|----------|-------------|
| `` | A Color. |  


## Examples


### Basic Example

```supercollider
(
w = Window.new.front;
a = StaticText(w, Rect(10, 10, 200, 20));
a.string = "Rolof's Rolex";
)

// adjust look, alignment and content
a.background = Color.grey;
a.align = \center;
a.font = Font("Monaco", 11);
a.string = "Your Rolex";
```




### Monitoring Values in a Synth

```supercollider
(
var w, a, r, b, q;
w = Window("Frequency Monitor", Rect(200, Window.screenBounds.height - 200, 300, 150)).front;

a = StaticText(w, Rect(45, 10, 200, 20)).background_(Color.rand);
a.string = " Current Frequency ";

Button.new(w, Rect(45, 70, 200, 20)).states_([["close", Color.black, Color.rand]]).action_({ w.close });

s.waitForBoot({

    b = Bus.new(\control, 0, 1);

    q = SynthDef(\Docs_FreqMonitor, {
        var freq, snd;
        freq = LFNoise0.ar(2, 400, 650);
        snd = SinOsc.ar(freq, 0, 0.2);
        Out.ar(0, snd);
        Out.kr(b.index, freq); // output the frequency to a control bus
    }).play;

    r = Routine {
        {
            // Set the value of the StaticText to the value in the control bus.
            // Setting GUI values is asynchronous, so you must use .defer in the system clock.
            // Also you must check if the window is still open, since Routine will continue for at least
            // one step after you close the window.
            b.get({ |v|
                {
                    if(w.isClosed.not) {
                        a.string = " Current Frequency: " ++ v.round(0.01)
                    }
                }.defer
            });

            0.01.wait;
        }.loop

    }.play
});

CmdPeriod.doOnce({ w.close });
w.onClose = { r.stop; q.free; b.free }; // clean up if the window closes
)
```




### Dynamic Text

```supercollider
(
w = Window.new.front;
w.view.background = Color.white;
a = Array.fill(20, { StaticText(w, Rect(w.bounds.extent.x.rand, w.bounds.extent.y.rand, 160, 16))
    .string_("Rolof's Rolex".scramble)
    .align_(\center)
    .stringColor_(Color.rand)
    .font_(Font([
        "Helvetica-Bold",
        "Helvetica",
        "Monaco",
        "Arial",
        "Gadget",
        "MarkerFelt-Thin"
    ].choose, 11))
});

r = {
    inf.do { |i|
        thisThread.randSeed_(1284);
        a.do { |item|
            // setting GUI values is asynchronous, so you must use .defer
            {
                item.bounds = Rect(
                    5 + w.bounds.extent.x.rand * abs(cos(i * 0.01)),
                    w.bounds.extent.y.rand * sin(i * 0.01),
                    160,
                    20
                )
            }.defer;
        };
        0.15.wait;
    }
}.fork;
CmdPeriod.doOnce({ w.close });
w.onClose_({ r.stop });
)
```






