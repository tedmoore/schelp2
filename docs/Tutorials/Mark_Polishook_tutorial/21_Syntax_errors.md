# 21_Syntax_errors

*Mark Polishook tutorial*

**Categories:** Tutorials>Mark_Polishook_tutorial

**Related:** [Mark_Polishook_tutorial/00_Introductory_tutorial](../../Tutorials/Mark_Polishook_tutorial/00_Introductory_tutorial.md)


## Syntax and grammar
Before it actually runs a program, SuperCollider examines the code to ensure that syntax and grammar are correct. For example, are all variable names and/or keywords spelled correctly in a program? Are statements terminated by semi-colons?

If syntax or grammar errors are found, SuperCollider writes a notification to the post window. Such messages are descriptive but terse.


```supercollider
* ERROR: Parse error
   in file 'selected text'
   line 1 char 2 :
  4,
-----------------------------------
* ERROR: Command line parse failed
nil
```




## Common errors
1. the name of a class or a variable is misspelled
2. a variable is used before being declared
3. a parenthesis or a square or curly brace is missing or used in the wrong context
4. a required comma or semicolon is missing or used improperly


////////////////////////////////////////////////////////////////////////////////////////////////////

Two helpful commands in the SuperCollider Edit menu:

1. "Go to Line ..." transports you to the line number of your choice. Use this when an error message identifies the line number on which a problem occurred.
2. "Find" searches for words or phrases. Use "Find" to locate code that has been identified in error messages or to replace all instances of an improperly spelled word.


////////////////////////////////////////////////////////////////////////////////////////////////////

go to [Mark_Polishook_tutorial/22_Runtime_errors](../../Tutorials/Mark_Polishook_tutorial/22_Runtime_errors.md)



