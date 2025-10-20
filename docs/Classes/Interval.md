# Interval

*range of integers*

**Categories:** Math

## Description

An Interval is a range of integers from a starting value to an ending value by some step value.


## Class Methods


### `new`
Create a new Interval.
```
Interval(10, 30, 4);
10 to: 30; // the message to creates an interval with step 1
```



## Instance Methods


### `start`
The starting value of the interval.
### `end`
The ending value of the interval.
### `step`
The step value of the interval.
### `size`
Return the number of items in the interval.
```
Interval(10, 30, 4).size.postln;
```


### `at`
Return the indexed item in the interval.
```
Interval(10, 30, 4).at(3).postln;
```


### `do`
Evaluates function for each item in the interval. The function is passed two arguments, the item and an integer index.
```
Interval(10, 30, 4).do({ |item, i| item.postln });
```



