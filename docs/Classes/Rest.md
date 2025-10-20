# Rest

*Represents a rest in event patterns*

**Categories:** Streams-Patterns-Events

**Related:** [Pbind](../Classes/Pbind.md), [Event](../Classes/Event.md), [AbstractFunction](../Classes/AbstractFunction.md)

## Description

A Rest may be used in event patterns to indicate that the resulting event should be a rest (i.e., silent). It should be used in one of the child patterns belonging to a Pbind, for instance.

```
// do nothing for 2 seconds
(note: Rest(), dur: 2).play;

// intersperse pauses in pattern
Pbind(\note, Pseq([0, 4, 7, 11], inf), \dur, Pseq([2, 1, Rest(1)], inf) / 5).play;
```



### Expressing rests in event patterns
The Rest class allows rests to be indicated in any stream, not only frequency or event type. Also, using the duration argument (see the [#*new](#*new) method below), rests may be embedded into a duration stream. That is, rests may be treated as part of the rhythmic specification, rather than the pitch specification.


> **Note:** As of SuperCollider 3.9, `Rest`'s behavior has changed to be more intuitive. Note that you have to now use `Rest()` - the shortcut of `Rest` as class directly is **not supported** anymore.




### Usage
- [Event#-isRest](../Classes/Event.md#-isrest) checks every item in the event to see if it meets the condition to be a rest: it may be a `Rest` instance, the `Rest` class, or either of the symbols `\` or `\r`. If any item meets the condition, the event will be considered a rest and it will not take action when played.
- If a Pbind child pattern yields a Rest object, the Rest is placed directly into the event. This is a change of behavior from 3.8.
- If a Rest object has a value, it will respond to math operations: `Rest(1) * 2 == Rest(2)`.





## Class Methods

All methods of Rest except *new are private, and should not be used directly.




### `new`
Create an instance of Rest, with a value to be used in the resulting rest event.**Arguments:**

| Argument | Description |
|----------|-------------|
| `value` | The Rest instance's numeric value, to be used in math operations. Note that a Rest's value is ignored for most Event keys (assuming the Event does nothing in response to `.play`). If a Rest appears in a rhythm key (`dur` or `delta`), then the number is the time until the next event. Consequently, numeric Rests are often used for duration -- but there is no requirement that a Rest's value must be a duration. |  

```
a = Rest(6);
b = a * 2; // returns Rest(12)
b = 2 * a; // the same
b.value; // returns 12
```

The rest of a rest is always a rest. This idempotence is implemented by Rest's superclass [Operand](../Classes/Operand.md).
```
Rest(Rest(1)) // returns Rest(1)
```



## Instance Methods


### `isRest`
returns true
### `unwrapBoolean`
returns the value.This method implements the following behavior.
```
Rest(6) + 1 // Rest(7)
Rest(true) // true
```

This makes comparisons work:
```
Rest(6) < 7 // true, and not Rest(true)
a = Pseq([1, 2, 1, 3, Rest(1), 2, Rest(3)], inf); // e.g. as a duration pattern
b = a.collect { |x| if(x > 2) { x / 2 } { x } };
b.asStream.nextN(8)
```


## Examples

Using Rest instances in a pitch stream

```
(
Pbind(
    \degree, Pif(
        0.1.loop.coin,
        Pseq([Rest(), 7], inf), // every second is a Rest
        Pseries(0, 1, inf).fold(-7, 7)
    ),
    \dur, 0.125
).play
)
```


Using a Rest instance in a duration stream

```
(
Pbind(
    \degree, Pseries(0, 1, inf).fold(-7, 7),
    \dur, Pseq([Pn(0.125, { rrand(3, 6) }), Rest(0.25)], inf)
).play
)
```



### Alternatives to Rest
In addition to Rest, in events, rests can be specified in two other ways (legacy usages).

- A [Symbol](../Classes/Symbol.md) may be specified in any frequency stream (under the keys degree, note, midinote or freq). The exception to this rule is control bus mapping symbols, beginning with 'c' followed by a number. Typical symbols that have been used include **\rest**, **\r** and the empty symbol **\**.
```
(
p = Pbind(
    \degree, Pseq([
        0, 1, 2, 0, 0, 1, 2, 0,
        2, 3, 4, \rest, 2, 3, 4, \rest
    ]),
    \dur, 0.25
).play;
)
```


- The event's **\type** may be set to **\rest**.
```
(
p = Pbind(
    \degree, Pseries(0, 1, inf).fold(-7, 7),
    \dur, 0.125,
    \type, Pwrand([\note, \rest], [0.9, 0.1], inf)
).play;
)

p.stop;
```








