# BinaryOpStream

*two streams combined by a binary operator*

**Related:** [UnaryOpStream](../Classes/UnaryOpStream.md), [NAryOpStream](../Classes/NAryOpStream.md)

**Categories:** Streams-Patterns-Events

## Description

A BinaryOpStream is created as a result of a binary math operation on a pair of Streams. It is defined to respond to **next** by returning the result of the math operation on the **next** value from both streams. It responds to **reset** by resetting both Streams.

## Examples


```
x = Routine { 6.do { |i| i.yield } } + 64;
x.dump
```



```
(
x = Routine { 6.do { |i| i.yield } } + 64;
x.next.postln;
x.next.postln;
x.next.postln;
x.next.postln;
x.next.postln;
x.next.postln;
x.next.postln;
)
```



```
(
x = Routine { 6.do { |i| i.yield } } + Routine { (1..7).do { |i| (1 / i).yield } };
x.next.postln;
x.next.postln;
x.next.postln;
x.next.postln;
x.next.postln;
x.next.postln;
x.next.postln;
)
```




