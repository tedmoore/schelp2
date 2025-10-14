# UnitTestScript

*run test scripts*

**Categories:** Testing

**Related:** [UnitTest](../Classes/UnitTest.md), [UnitTestResult](../Classes/UnitTestResult.md)

## Description

In order to make sure a method works correctly, a test can be implemented that assures the correct behavior.
It is a common practice to write tests to clarify how an object should respond, and it may avoid inconsistencies on the long run.
Test scripts are simply plain text files ending with `_unittest.scd`, which are interpreted. Scripts may be located next to a class in the classpath or one folder below. If they return a function, the `UnitTestScript` is passed in, allowing to call methods like assert etc. (see [UnitTest](../Classes/UnitTest.md))
`UnitTestScript` mimics some of the behavior of [Method](../Classes/Method.md), to be compatible with [UnitTest](../Classes/UnitTest.md).


## Class Methods



## Instance Methods


## Examples

An example script

> **Note:** This should be in a file `myUnitTest_unittest.scd`



```supercollider
{ |test|
    "Kant test".postln;
    "5 + 7 = ".post;
    (5 + 7).postln;
    test.assertEquals(5 + 7, 12, "five plus seven should always be twelve");
}
```


To run only the test scripts:

```supercollider
UnitTestScript.run;
```


The scripts are to be found under the class UnitTestScript in the GUI:

```supercollider
UnitTest.gui
```




