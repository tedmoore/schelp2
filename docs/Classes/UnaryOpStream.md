# UnaryOpStream

*stream modified by a unary operator*

**Related:** [BinaryOpStream](../Classes/BinaryOpStream.md), [NAryOpStream](../Classes/NAryOpStream.md)

**Categories:** Streams-Patterns-Events

## Description

A UnaryOpStream is created as a result of a unary math operation on a Stream. It is defined to respond to **next** by returning the result of the math operation on the **next** value from the stream. It responds to **reset** by resetting the Stream.

## Examples


```
x = Routine { 6.do { |i| i.yield } }.squared;
x.dump;
```



```
(
x = Routine { 6.do { |i| i.yield } }.squared;
x.next.postln;
x.next.postln;
x.next.postln;
x.next.postln;
x.next.postln;
x.next.postln;
x.next.postln;
)
```




