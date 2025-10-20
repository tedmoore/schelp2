# Post

*posts text to the post window*

**Categories:** Files

## Description

The class Post is a stream destination. Its main use is that it can sometimes make code more readable and execution slightly more efficient.

```
Post <<< a << " " <<< b << " " <<< c << " " <<< d << Char.nl;
```


vs

```
(a.asCompileString + b.asCompileString + c.asCompileString + d.asCompileString).postln;
```


> **⚠️ Warning:** << also means object left shift.


## Class Methods


### `<<`
Post as string
```
Post << "string";
```



### `<<<`
Post as compile string
```
Post <<< "string";
```



### `comma`
Prints a comma
```
Post.comma;
```



### `space`
Prints a space
```
Post.space;
```



### `nl`
Prints a newline
```
Post.nl;
```



### `ff`
Prints the char $\f
```
Post.ff;
```



### `tab`
Prints a tab
```
Post.tab;
```


## Examples


```
a = "a string";
b = 'a symbol';
c = 4;
d = [1, 2, 3, 4, a, b];

// post as string
Post << a << Char.nl;
// post as compile string
Post <<< a << Char.nl;

// post as string
Post << d << Char.nl;
// post as compile string
Post <<< d << Char.nl;

// This is the equivalent of :
d.postln;
// or
d.asCompileString.postln;
```




