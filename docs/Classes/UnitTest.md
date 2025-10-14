# UnitTest

*a class for programmatic testing of classes*

**Categories:** Testing

**Related:** [UnitTestResult](../Classes/UnitTestResult.md), [UnitTestScript](../Classes/UnitTestScript.md)

## Description

In order to make sure a method works correctly, a test can be implemented that assures the correct behavior.
It is a common practice to write tests to clarify how an object should respond, and it may avoid inconsistencies on the long run. A test is always a subclass of `UnitTest`, implementing at least one method starting with `test_`.
When running all tests of one class (see [#*run](#*run)), each test method is called in a separate instance of this class. Test methods, therefore, do not interfere with each other.

> **Note:** UnitTests for the Common library classes are kept in the `testsuite/classlibrary` directory of the SuperCollider sources.To install, [download the sources](https://github.com/supercollider/supercollider) and add the directory to your `sclang_conf.yaml`, either by editing it or via the ScIDE preferences.




## Class Methods


### `gui`
A graphical interface to run and browse all tests
```supercollider
UnitTest.gui
```


### `reportPasses`
Accessor controlling whether passing tests should be reported. Defaults to `true`. See also [#*passVerbosity](#*passverbosity) which controls how much detail is reported from passing tests when this is set to true.**Arguments:**

| Argument | Description |
|----------|-------------|
| `value` | Should be `true` or `false`. |  

### `passVerbosity`
Accessor controlling whether extra details should be reported for passing tests.Defaults to `UnitTest.full` so that all details are reported; however this behaviour may be too verbose for some, for whom it is sufficient to see that a test is passing without needing to see the detail. If set to `UnitTest.brief`, and [#*reportPasses](#*reportpasses)  is true, passes will be reported, but without any extra details which may be provided by assertions.**Arguments:**

| Argument | Description |
|----------|-------------|
| `value` | Should be `UnitTest.full` or `UnitTest.brief`. |  

### `run`
Run all methods whose names begin with `test_`.
```supercollider
TestUnitTest.new.run;
```

**Arguments:**

| Argument | Description |
|----------|-------------|
| `reset` | If `true`, first runs [#*reset](#*reset) on the class. |  
| `report` | If `true`, outputs the test results. |  

### `runTest`
Run a single test method.
```supercollider
UnitTest.reset;
UnitTest.runTest("TestUnitTest:test_assert");
```

**Arguments:**

| Argument | Description |
|----------|-------------|
| `methodName` | A [String](../Classes/String.md) referring to the class and test method within it, e.g. `"TestPolyPlayerPool:test_prepareChildrenToBundle"`. |  

### `runAll`
Run the entire test suite. As this method addresses the entire test suite, it should be called only on `UnitTest`. Calling it on any of its subclasses will result in throwing an `Error`.
```supercollider
UnitTest.reset;
UnitTest.runAll;
```



## Instance Methods

### `runTestMethod`
Run a single test method of this class
```supercollider
TestUnitTest.new.runTestMethod(TestUnitTest.findMethod(\test_assert));
```

**Arguments:**

| Argument | Description |
|----------|-------------|
| `method` | the method to run |  
| `report` | Reports the result of the test if `true` (default is `true`) |  
**Returns:** (describe returnvalue here)### `assert`
Asserts that an expression must be true.
```supercollider
this.assert(2 == 2, "passes");
this.assert(2 == 2.00001, "fails");
```

**Arguments:**

| Argument | Description |
|----------|-------------|
| `boolean` | A boolean, where `true` means that the test is passed. |  
| `message` | A message describing the purpose of the assertion, e.g. `"foo should be less than bar"`. Posted if `report` is true. |  
| `report` | Reports the result of the test if `true`. |  
| `onFailure` | If not `nil`, a failure stops the tests and evaluates this function. |  
| `details` | Some optional extra details which will be passed to the reporting framework for display unless brief reporting is requested (see [#*passVerbosity](#*passverbosity)). |  
### `assertEquals`
Asserts that an expression `a` is equal to the value `b`, where equality is determined according to `a`'s implementation of `==`.Automatically passes details of the equality check to the reporting framework, which will be displayed if the assertion fails, and also if it passes and [#*reportPasses](#*reportpasses) is `true` and [#*passVerbosity](#*passverbosity) is not set to `UnitTest.brief`.
```supercollider
this.assertEquals(2 + 2, 4, "passes");
this.assertEquals(2 + 2, 5, "fails");
```

**Arguments:**

| Argument | Description |
|----------|-------------|
| `a` | the experimentally produced value |  
| `b` | the expected value |  
| `message` | A message describing the purpose of the assertion, e.g. `"Adding two numbers should return their sum."`. Posted if `report` is true. |  
| `report` | Reports the result of the test if `true` (default is `true`) |  
| `onFailure` | If not `nil`, a failure stops the tests and evaluates this function. |  
### `assertFloatEquals`
Asserts that an expression `a` returning a float is within a given range (`within`) of being equal to `b`.Automatically passes details of the equality check to the reporting framework, which will be displayed if the assertion fails, and also if it passes and [#*reportPasses](#*reportpasses) is `true` and [#*passVerbosity](#*passverbosity) is not set to `UnitTest.brief`.
```supercollider
this.assertFloatEquals(2, 2.0001, "Pass since 2 is close enough to 2.0001.", 0.001);
this.assertFloatEquals(2, 2.0001, "Fail since 2 isn't close enough to 2.0001.", 0.0001);
```

**Arguments:**

| Argument | Description |
|----------|-------------|
| `a` | the experimentally produced float value |  
| `b` | the expected float value |  
| `message` | A message describing the purpose of the assertion, e.g. `"Adding two numbers should return their sum."`. Posted if `report` is true. |  
| `within` | The range within which `a` must be of `b` in order for the test to pass. |  
| `report` | Reports the result of the test if `true` (default is `true`) |  
| `onFailure` | If not `nil`, a failure stops the tests and evaluates this function. |  
### `assertArrayFloatEquals`
Make sure that the two arrays of floats `a` and `b` equal within a given range (`within`).
```supercollider
this.assertArrayFloatEquals([2, 3] + 0.0001, [2, 3], "Pass since pairs of floats are close enough", 0.001);
this.assertArrayFloatEquals([2, 3.0001], [2, 3], "Fail since pairs of floats aren't both close enough", 0.0001);
```

**Arguments:**

| Argument | Description |
|----------|-------------|
| `a` | the experimentally produced value, which is an `Array` of floats |  
| `b` | the `Array` of float values expected |  
| `message` | A message describing the purpose of the assertion, e.g. `"Arrays foo and bar should be equal."`. Posted if `report` is true. |  
| `within` | The range within which each item of `a` must be of the corresponding item in `b` in order for the test to pass. |  
| `report` | Reports the result of the test if `true` (default is `true`) |  
| `onFailure` | If not `nil`, a failure stops the tests and evaluates this function. |  
### `ifAsserts`
Make a further assertion only if it passed, or only if it failed.
```supercollider
(
a = UnitTest.new;
a.ifAsserts(2 == 3, "yes", { a.assert(2 == 4) }, { a.assert(1 == 1, "but this is correct") });
)
```

### `assertException`
Make sure that a specific [Exception](../Classes/Exception.md) or [Error](../Classes/Error.md) is thrown.**Arguments:**

| Argument | Description |
|----------|-------------|
| `func` | Pass the code that is expected to throw an error in this function. |  
| `errorClass` | The class or class name which the error should be kind of. |  
| `message` | A message describing the purpose of the assertion. |  
| `report` | Reports the result of the test if `true` (default is `true`) |  
| `onFailure` | If not `nil`, a failure stops the tests and evaluates this function. |  
| `details` | Some optional extra details which will be passed to the reporting framework for display unless brief reporting is requested (see [#*passVerbosity](#*passverbosity)). |  
### `assertNoException`
Make sure that a specific [Exception](../Classes/Exception.md) or [Error](../Classes/Error.md) is **not** thrown. For arguments, see [#-assertException](#-assertexception).### `wait`
Wait for a predicate function to return `true`. Considers the test failed after `maxTime`. Only valid within a test (or a routine).
> **Note:** It's best to avoid using this method in tests. See [CondVar#-waitFor](../Classes/CondVar.md#-waitfor) for a better option.


```supercollider
(
{
    s.reboot;
    UnitTest.new.wait({ s.serverRunning }, "server failed to boot in time", 2);
}.fork
)
```

### `bootServer`
Wait for server boot until continued. Only valid within a test (or a routine).If already booted, then freeAll and create new allocators.
```supercollider
(
{
    UnitTest.new.bootServer(s);
}.fork
)
```

### `debug`
Supply some debugging information relevant to the currently running test case. This will be displayed immediately preceding any details which may be displayed through use of the `details` argument of [#-passed](#-passed) and [#-failed](#-failed).**Arguments:**

| Argument | Description |
|----------|-------------|
| `text` | The debugging text. |  

```supercollider
test_myMethod {
    var obj = MyClass.new;
    this.debug("obj has color" + obj.color);
    this.assert(2 + 2, 5);
}
```

will result in:
```supercollider
FAIL: a TestMyClass: test_myMethod
obj has color red
Is:
         4
Should be:
         5
```

### `passed`
Register a passed test.**Arguments:**

| Argument | Description |
|----------|-------------|
| `method` | Name of the method in which the test is passing. |  
| `message` | A message describing the purpose of the assertion, e.g. `"foo should be less than bar"`. Posted if neither `report` nor [#*reportPasses](#*reportpasses) are false. |  
| `report` | Reports the result of the test if true and [#*reportPasses](#*reportpasses) is true. |  
| `details` | Some optional extra details which will be displayed if [#*reportPasses](#*reportpasses) is true and [#*passVerbosity](#*passverbosity) is not set to `UnitTest.brief`. |  

```supercollider
this.passed(message: "this passed");
```

### `failed`
Register a test failure.**Arguments:**

| Argument | Description |
|----------|-------------|
| `method` | Name of the method in which the test is failing. |  
| `message` | A message describing the purpose of the assertion, e.g. `"foo should be less than bar"`. Posted if `report` is true. |  
| `report` | Reports the result of the test if true. |  
| `details` | Some optional extra details which will be displayed if `report`is true. |  

```supercollider
this.failed(message: "this failed");
```


## Examples

Write tests by subclassing UnitTest, and defining methods whose names begins `test_`. Each test method will be called from a fresh instance of the subclass.
If you implement the methods `setUp` and `tearDown` in your test class, they will be called before and after every test. This can help to eliminate repetitive code, and makes it easier to maintain your tests by ensuring that they all run under the same set of conditions.

```supercollider
TestYourClass : UnitTest {
    setUp {
        // this will be called before each test
    }
    tearDown {
        // this will be called after each test
    }

    test_yourMethod {
        // every method whose name begins with "test_" will be run
        var synth;

        this.assert(6 == 6, "6 should equal 6");

        this.assertEquals(9, 9, "9 should equal 9");

        this.assertFloatEquals(4.0, 1.0 * 4.0 / 4.0 * 4.0,
            "floating point math should be close to equal");

        // we are inside a Routine, you may wait
        1.0.wait;

        // this will wait until the server is booted
        // if the server is already booted it will free all nodes
        // and create new allocators, giving you a clean slate
        this.bootServer;

        synth = { SinOsc.ar / 10 }.play;
        synth.register; 

        // will wait until the condition is true
        // will be considered a failure after 10 seconds
        this.wait({ synth.isPlaying }, "waiting for synth to play", 10);
    }
}
```




