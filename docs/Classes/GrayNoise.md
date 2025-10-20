# GrayNoise

*Bit-flipping Noise*

**Related:** [BrownNoise](../Classes/BrownNoise.md), [ClipNoise](../Classes/ClipNoise.md), [PinkNoise](../Classes/PinkNoise.md), [WhiteNoise](../Classes/WhiteNoise.md)

**Categories:** UGens>Generators>Stochastic

## Description

Generates noise which results from flipping random bits in a word.> *Generated through $X_{0} = 1;\;X_{n+1} = X_{n} \oplus z$, where $\oplus$ is bitwise exclusive or, and $z$ is a 32-bit binary number with exactly one nonzero digit; the position of the nonzero digit is a uniform random variable.*
This type of noise has a high RMS level relative to its peak to peak level. The spectrum is emphasized towards lower frequencies.
Grey/gray noise does not have a standard definition as pink and white noise do. While [GrayNoise](../Classes/GrayNoise.md) generates bit-flipping noise, the term "grey/gray noise" may also refer to noise shaped to perceptual equal loudness contours.> *See [Joseph Wisniewski's 1996 usenet message](https://web.archive.org/web/20090427190825/http://www.ptpart.co.uk:80/show.php?contentid=71) that seems to have informed the wikipedia articles on [Grey noise](https://en.wikipedia.org/wiki/Grey_noise) and on [Colors of noise](https://en.wikipedia.org/wiki/Colors_of_noise). Notice that the bit-flipping version of gray noise is mentioned in a reply to said usenet message.*


## Class Methods


### `ar`, `kr`
**Arguments:**

| Argument | Description |
|----------|-------------|
| `mul` | Output will be multiplied by this value. |  
| `add` | This value will be added to the output. |  

## Examples


```
(
SynthDef("help-GrayNoise", { |out = 0|
    Out.ar(out,
        GrayNoise.ar(-20.dbamp)
    )
}).play;
)
```




