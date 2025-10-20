# Operand

*Idempotent wrapper around math operations*

**Categories:** Core

**Related:** [AbstractFunction](../Classes/AbstractFunction.md), [Maybe](../Classes/Maybe.md), [Ref](../Classes/Ref.md), [Rest](../Classes/Rest.md)

## Description

If you need to ensure that math operations always return the result wrapped in a specific object, you can use Operand or subclass from it. For some practical examples, see its subclass [Rest](../Classes/Rest.md). If you need to keep nested operations, use [Maybe](../Classes/Maybe.md).
Its creation is idempotent, that is `Operand(Operand(x)) == Operand(x)`.

```
// An Operand is an Operand is an Operand
Operand(Operand(Operand(1))) - 1 == 0
```



```
// math operations
a = Operand(2);
b = Operand([1, 2, 3]);
c = a + b * a; // Operand([6, 8, 10])
c.value; // [6, 8, 10]
```




## Class Methods


### `new`
**Arguments:**

| Argument | Description |
|----------|-------------|
| `value` | Return a new instance of Operand, using an arbitrary object as value.
```
a = Operand(1) + 7; // returns Operand(8)

// the *new method is idempotent:
Operand(Operand(Operand(1))) == Operator(1)
``` |  


## Instance Methods


### `value`
Set or return the current value.
```
a = Operand(2) ** 8;
a.value; // 256
a.value = 78;
a.value; // 78
```


### `==`
**Arguments:**

| Argument | Description |
|----------|-------------|
| `obj` | An Operand is equal to another one if their value are equal.
```
Operand(1) == Operand(1);
Operand(1) + 2 == Operand(3);
``` |  

### `hash`
Two instances with the same value return the same hash value.
```
Set[Operand(1), Operand(1)] == Set[Operand(1)] // true
```


### `dereferenceOperand`
This method is called to avoid nesting. You may override it in subclasses to perform actions on resulting values. `Operand(Operand(1)) // Operand(1)`.
## Examples


```
// you could make a class that always converts values to integers:

IntegerOperand : Operand {
    dereferenceOperand {
        ^value.asInteger
    }
}

// then you would get:
IntegerOperand(1) + pi == IntegerOperand(4)
```




