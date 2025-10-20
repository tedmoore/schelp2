# News in 3.6

*A summary of news in SC 3.6*

**Categories:** News


## SuperCollider IDE
A new cross-platform SuperCollider coding environment.

Read [the guide](../Guides/SCIde.md)!



## Language-side news

### More informative syntax errors
The parser now posts the details of syntax errors, example:


```
[1,2,%,4];
123;
```


Posts the following error message:





### Remove old syntax
`#(a:1)` was valid syntax, but yielded nonsense results. This will now result in a syntax error instead.




### YAML/JSON parser
[String#-parseYAML](../Classes/String.md#-parseyaml) and [String#-parseYAMLFile](../Classes/String.md#-parseyamlfile) can be used to parse YAML or JSON.




### SynthDef optimizations for additive terms
When the SynthDef is compiled, separate additive ugens are combined via the new [Sum3](../Classes/Sum3.md) and [Sum4](../Classes/Sum4.md) ugens.




### Basic dead code elimination for SynthDefs
The process of building synthdefs now performs a simple dead code elimination pass, which removes all [PureUGen](../Classes/PureUGen.md) instances without successor.




### Case sensitive String comparison
String comparison operators (`==, !=, <=, >=, >, <`) are now case sensitive.


```
"Foo" == "fOo"; // false
```





### SplayAz Bug Fix
Positioning of SplayAz was broken. The semantics of the `spread` and `center` arguments has been changed in order to fix the behavior.




### Array primitives respect mutability
The array primitives now respect object mutability: writing to an immutable object now fails and changing an immutable object with `add`, `addAll`, `insert`, `extend`, `growClear` and `overwrite` will return a newly allocated object.





## Server-side news

### SynthDef2 fileformat



### C++ base class for Unit Generators
A new C++ base class has been introduced, which extends the plain c-style Unit struct by a C++ interface.





