# Harmonics

*Convenient factory for filling buffers with harmonics on the server*

**Categories:** Collections, Server, UGens>Buffer

## Description

Harmonics objects are convenient factories for creating Arrays that are used to fill buffers using the b_gen sine fill commands on the server.


## Class Methods

### `new`
Create a new Harmonics array of size. Nothing is filled in for you, until instance methods are applied.
```supercollider
a = Harmonics.new(16);    // just returns an instance of Harmonics with size
```



## Instance Methods

### `ramp`

```supercollider
a.ramp(1.0, 1.0);    // returns a harmonic series

b = Buffer.alloc(s, 512, 1);
// harmonic series for freqs, ramp down for amps
b.sine2(a.ramp(1.0, 1.0).postln, a.ramp(0.5, -0.025).postln, true, true, true);
(
z = SynthDef("help-Osc", { |out = 0, bufnum = 0|
    Out.ar(out,
        Osc.ar(bufnum, 200, 0, 0.5)
    )
});
)
y = z.play(s, [\out, 0, \bufnum, b]);
y.free;
```

### `decay`
Implements the formula: 1 / ((i+1) ** k)
```supercollider
a.decay(1.0);

b.sine2(a.ramp(1.0, 1.0).postln, a.decay(1.0).postln, true, true, true);
y = z.play(s, [\out, 0, \bufnum, b]);
y.free;
```

### `geom`
Implements the formula: 1 / (i ** k)
```supercollider
a.geom(1.2);

b.sine2(a.ramp(1.0, 1.0).postln, a.geom(1.2).postln, true, true, true);
y = z.play(s, [\out, 0, \bufnum, b]);
y.free;
```

### `formant`
Create a formant like structure.
```supercollider
a.formant(6, 3);

b.sine2(a.formant(12, 3).postln, a.geom(1.2), true, true, true);
y = z.play(s, [\out, 0, \bufnum, b]);
y.free;
```

### `teeth`

```supercollider
a.teeth(6, 3);

b.sine2(a.teeth(2, 3).postln, a.geom(1.2), true, true, true);
y = z.play(s, [\out, 0, \bufnum, b]);
b.sine2(a.teeth(4, 1).postln, a.geom(1.2), true, true, true);
b.sine2(a.teeth(1, 3).postln, a.geom(1.2), true, true, true);
b.sine2(a.teeth(2, 3).postln, a.geom(1.2), true, true, true);
y.free;
```

### `cutoff`
Returns 1.0 to the nth place, fills the rest with 0.0
```supercollider
a.cutoff(3);

b.sine2(a.ramp(1.0, 1.0), a.cutoff(3), true, true, true);
y = z.play(s, [\out, 0, \bufnum, b]);
b.sine2(a.ramp(1.0, 1.0), a.cutoff(3), true, true, true);
b.sine2(a.ramp(1.0, 1.0), a.cutoff(5), true, true, true);
b.sine2(a.ramp(1.0, 1.0), a.cutoff(1), true, true, true);
y.free;
```

### `shelf`

```supercollider
a.shelf(0, 6, 1, 0);

b.sine2(a.ramp(1.0, 1.0), a.shelf(0, 6, 1, 0).postln, true, true, true);
y = z.play(s, [\out, 0, \bufnum, b]);
b.sine2(a.ramp(1.0, 1.0), a.shelf(0, 11, 1, 0).postln, true, true, true);
b.sine2(a.ramp(1.0, 1.0), a.shelf(2, 6, 1, 0).postln, true, true, true);
b.sine2(a.ramp(1.0, 1.0), a.shelf(6, 8, 1, 0).postln, true, true, true);
y.free;
```

### `sine`

```supercollider
a.sine(8, 0, 1, 0);

b.sine2(a.ramp(1.0, 1.0), a.sine(8, 0, 1, 0).postln, true, true, true);
y = z.play(s, [\out, 0, \bufnum, b]);
b.sine2(a.ramp(1.0, 1.0), a.sine(4, 0, 1, 0).postln, true, true, true);
b.sine2(a.ramp(1.0, 1.0), a.sine(2.2, 0.5pi, 0.4, 0.2).postln, true, true, true);
b.sine2(a.ramp(1.0, 1.0), a.sine(pi, 0.25pi, 0.5, 0).postln, true, true, true);
y.free;
```

### `pulse`

```supercollider
a.pulse(8, 0, 2, 1, 0);

b.sine2(a.ramp(1.0, 1.0), a.pulse(8, 0, 2, 1, 0).postln, true, true, true);
y = z.play(s, [\out, 0, \bufnum, b]);
b.sine2(a.ramp(1.0, 1.0), a.pulse(8, 0, 2, 1, 0).postln, true, true, true);
b.sine2(a.ramp(1.0, 1.0), a.pulse(4, 0, 2, 0.4, 0.2).postln, true, true, true);
b.sine2(a.ramp(1.0, 1.0), a.pulse(7, 0.5pi, 3, 0.5, 0.1).postln, true, true, true);
y.free;
```

### `rand`, `exprand`, `linrand`
### `rand2`
### `coin`


