# Association

*relate two objects*

**Categories:** Collections

## Description

Associates a key with a value. Associations can be created via the -> operator which is defined in class [Object](../Classes/Object.md).
Associations are used internally in [Dictionary](../Classes/Dictionary.md).


## Class Methods

### `new`
Create an Association between two objects.
```supercollider
(
x = 'name' -> 100;
x.postln;
)
```

**Arguments:**

| Argument | Description |
|----------|-------------|
| `key` | any object |  
| `value` | any object |  


## Instance Methods


### Accessing
### `key`
the key object.
### `value`
the value object.

### Testing
### `==`
Compare the keys of two Associations.
### `<`
Compare the keys of two Associations.
### `hash`
Compute the hash value of the Association.

### Writing to streams
### `printOn`
Write a string representation to the stream.
### `storeOn`
Write a compilable string representation to the stream.

## Examples


```supercollider
// associations can be a good way to store named data in order:
(
a = [\x -> 700, \y -> 200, \z -> 900];

fork {
    a.do { |assoc|
        assoc.key.postln;
        assoc.value.postln;
        (freq: assoc.value).play;
        2.wait;
    }
};
)
```




