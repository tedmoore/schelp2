# NAryOpStream

*several streams combined by an n-ary operator*

**Related:** [UnaryOpStream](../Classes/UnaryOpStream.md), [BinaryOpStream](../Classes/BinaryOpStream.md)

**Categories:** Streams-Patterns-Events

## Description

A NAryOpStream is created as a result of a n-ary math operation on a Stream. It is defined to respond to **next** by returning the result of the math operation on the **next** value from the stream. It responds to **reset** by resetting the Stream.

## Examples


```supercollider
x = Routine { 6.do { |i| i.yield } }.wrap(0, 3);
x.dump;
```



```supercollider
(
x = Routine { 6.do { |i| i.yield } }.wrap(0, 3);
x.next.postln;
x.next.postln;
x.next.postln;
x.next.postln;
x.next.postln;
x.next.postln;
x.next.postln;
)
```




