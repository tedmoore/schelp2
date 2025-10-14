# Symbol

*a unique name for something*

**Categories:** Core

## Description

A symbol, like a [String](../Classes/String.md), is a sequence of characters. Unlike strings, two symbols with exactly the same characters will be the exact same object. Symbols are optimized for recreating the same symbol over and over again. In practice, this means that symbols are best used for identifiers or tags that are only meaningful within your program, whereas you should use a string when your characters are really processed as text data. Use symbols to name things, use strings for input and output.
Good uses of symbols include symbolic constant values and [Dictionary](../Classes/Dictionary.md) keys.
Symbols are represented syntactically as literals which are described in [Literals / Symbols ](../Reference/Literals.md#symbols).

### Creating a Symbol
A symbol can be written by surrounding characters by single quotes (may include whitespace):

`'foo bar'`

Or by a preceding backslash (then it may not include whitespace):

`\foo`

A String can be converted into a symbol:

`"arbeit".scramble.asSymbol;`




## Class Methods



## Instance Methods


### Testing
### `isClassName`
Answer whether the symbol can be a class name. This does not say if the class exists.
```supercollider
\Array.isClassName;
\Bauxite.isClassName;
```


### `isMetaClassName`
Answer whether the symbol can be meta class name. This does not say if the class exists.
```supercollider
\Meta_Array.isMetaClassName;
```


### `isSetter`
Answer whether the symbol has a trailing underscore.
```supercollider
'action_'.isSetter;
```


### `isPrimitiveName`
Answer whether the symbol is a valid primitive name
```supercollider
'_SymbolIsClassName'.isPrimitiveName;
```


### `isPrefix`
Answer whether the symbol is a prefix of another one
```supercollider
'a'.isPrefix('all'); // true
'z'.isPrefix('all');  // false
```


### `isIdentifier`
Return true if the symbol is a valid variable name, or equivalently a valid method name in the two most common method call syntaxes (`foo.bar()` and `bar(foo)`). A valid identifier contains only alphanumeric characters and underscores, and the first character must be a lowercase letter.
### `isBinaryOp`
Return true if the symbol is a valid binary operator. A valid binary operator contains only the symbols `!@%&*-+=|<>?/`, does not start with '`//`' or '`/*`', and is not the string '`=`'.

### Conversion
### `asString`
Convert to a String
### `asInteger`
Convert to an Integer
### `asClass`
Answer the Class named by the receiver.
### `asSetter`
Return a symbol with a trailing underscore added.
### `asGetter`
Return a symbol with a trailing underscore removed.
### `ascii`
return the ascii codes as an array
### `asSpec`
Convert to a ControlSpec
### `asTuning`
Convert to a Tuning
### `asScale`
Convert to a Scale

### Environments
Symbols are used as keys to look up objects in dictionaries and environments, but also in arrays. See [IdentityDictionary](../Classes/IdentityDictionary.md), [Environment](../Classes/Environment.md), [Event](../Classes/Event.md)


```supercollider
a = ();
a.put(\commune, 1871);
a.at(\commune);
```


### `envirPut`
put a value to the current environment using receiver as key
### `envirGet`
return a value from the current environment using receiver as key
```supercollider
\foo.envirPut(100);
\foo.envirGet;
\foo.envirPut(nil);
```



### Math
Symbols respond to all unary and binary math operations by returning themselves. The result of any math operation between a Number or other math object and a Symbol is to return the Symbol. This allows for example operations on lists of notes which contain 'rest's to preserve the rests.

`Pseq([1, 3, \rest, 2, 4] + 8);`

### `applyTo`
Use the symbol as a method selector and perform the message on firstArg, with args as arguments. This is used for mixing functions with method selectors (see also: Function).
```supercollider
'%'.applyTo(2553, 345);
['+', '-', '*', { |a, b| a.rand + b.rand }].choose.applyTo(2, 3);
```



### Synthesis
Inside SynthDefs and UGen functions, symbols can be used to conveniently specify control inputs of different rates and with lags (see: NamedControl, ControlName, and Control).

### `kr`
Return a control rate NamedControl input with a default value (val), and if supplied, with a lag. If val is an array, the control will be multichannel. A [ControlSpec](../Classes/ControlSpec.md) provided to the `spec` parameter will be written into the spec metadata for the current synth.
```supercollider
a = { SinOsc.ar(\freq.kr(440, 1.2)) }.play;
a.set(\freq, 330);
a.release;
a = { SinOsc.ar(\freq.kr([440, 460], 1.2)) }.play;
a.setn(\freq, [330, 367]);
a.release;
```


### `ar`
Return an audio rate NamedControl input with a default value (val), and if supplied, with a lag. If val is an array, the control will be multichannel.
### `ir`
Return an initialization rate NamedControl input with a default value (val). If val is an array, the control will be multichannel.
### `tr`
Return a TrigControl input with a default value (val). If val is an array, the control will be multichannel.
```supercollider
a = { Ringz.ar(T2A.ar(\trig.tr), \freq.kr(500, 1), 0.8) }.play;
a.set(\freq, 330, \trig, 1);
a.set(\freq, 830, \trig, 1);
a.release;
```




