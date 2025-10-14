# DebugFrame

*A representation of the call frame*

**Categories:** Core

## Description

A representation of the call frame. Can be used to reconstruct a backtrace by using [caller](#caller).
An instance can be acquired by calling [Object#-getBackTrace](../Classes/Object.md#-getbacktrace). While this is often not useful due to function inlining, it is useful when called on an [Exception](../Classes/Exception.md), see the implementation of [Exception#-reportError](../Classes/Exception.md#-reporterror) where a call to [Object#-dumpBackTrace](../Classes/Object.md#-dumpbacktrace) can be replaced by a call to [Object#-getBackTrace](../Classes/Object.md#-getbacktrace) and a call stack constructed manually.


## Instance Methods

### `functionDef`
Returns a [FunctionDef](../Classes/FunctionDef.md) or a [Method](../Classes/Method.md) of the current function or method.### `caller`
Returns another [DebugFrame](../Classes/DebugFrame.md) for the function that called this function.Can be used to make a back trace, but watch out for function inlining.
```supercollider
(
var debugFrame = { 1.0.getBackTrace }.();

while{ debugFrame.isNil.not }{
    var def = debugFrame.functionDef;
    def.postln;
    if(def.isKindOf(Method)){
        File.readAllString(def.filenameSymbol.asString)[def.charPos..def.charPos + 200].post;
        "...".postln;
    } {
        def.sourceCode.postln
    };
    "\n".post;
    debugFrame = debugFrame.caller
}
)
```

### `args`
Returns an [Array](../Classes/Array.md) of the argument's values, if there are no arguments, returns a [Nil](../Classes/Nil.md). This does not contain the argument names, which must be accessed through the [functionDef](#functiondef).
```supercollider
{ thisFunction.getBackTrace }.().args == nil;
{ |a, b, c| thisFunction.getBackTrace }.().args == [nil, nil, nil];
{ |a, b, c = 1| thisFunction.getBackTrace }.().args == [nil, nil, 1];
{ |a, b, c = 1| thisFunction.getBackTrace }.(2, 3, c: 4).args == [2, 3, 4];
```

### `vars`
Same as [args](#args) but for the variables.
```supercollider
{ thisFunction.getBackTrace }.().vars == nil
{ var a; thisFunction.getBackTrace }.().vars == [nil]
{ var a, b = 1; thisFunction.getBackTrace }.().vars == [nil, 1]
```

### `address`
Returns a [RawPointer](../Classes/RawPointer.md), rarely useful.### `context`
Returns another [DebugFrame](../Classes/DebugFrame.md) of the compiling context, rarely useful.

