# Writing tests

*Get started with writing unit tests*

**Categories:** Testing

**Related:** [SCDocSyntax](../Reference/SCDocSyntax.md), [SCDoc](../Classes/SCDoc.md)

To write, use and develop UnitTests, you need to 
- install a sourcecode version of SuperCollider
- change your environment to include only core library functionality
- run UnitTests


## install a sourcecode version of SuperCollider
Download or clone SuperCollider from github: [https://github.com/supercollider/supercollider.](https://github.com/supercollider/supercollider.)It is not needed to compile SuperCollider from its sources, you can instead use a pre-compiled binary and include the relevant folders (`SCClassLibrary, HelpSource, testsuite/classlibrary` in your environment. See below for an example.



## Change your environment to include only core library functionality
In order to mimick the standard SuperCollider installation, make sure that you have only the class library installed. 

Best practise is to create a separate `.yaml` configuration file that resides parallel to the default one. You can do this either interactively from within the preferences of your IDE (`Preferences>Interpreter`), or programatically


```supercollider
~sclangConf = "SCLANG_CONF".getenv;
LanguageConfig.addIncludePath(~scSourceDir +/+ "testsuite/classlibrary");
+   LanguageConfig.addExcludePath(~scSourceDir +/+ "testsuite/classlibrary/server");
+   LanguageConfig.addExcludePath(Quarks.folder +/+ "UnitTesting/tests");
+   postf("Writing configuration to %\n", ~sclangConf);
+   LanguageConfig.store(~sclangConf);
```


 



## Organisation
Core class [UnitTest](../Classes/UnitTest.md)s are located in the directory:

1. [UnitTest](../Classes/UnitTest.md)s go into parrallel directory.
2. server-related tests go into `server` subdirectory.
3. [UnitTest](../Classes/UnitTest.md)s should use [UnitTest#-assert](../Classes/UnitTest.md#-assert) and [UnitTest#-assertFloat](../Classes/UnitTest.md#-assertfloat).
4. look at existing [UnitTest](../Classes/UnitTest.md)s to understand what are good [UnitTest](../Classes/UnitTest.md)s
5. [UnitTest](../Classes/UnitTest.md) setup
6. run [UnitTest](../Classes/UnitTest.md)s either automatically (`UnitTest.runAll`), interactively (`UnitTEst.gui`), or individually by class (`MyClass.test` or `TestMyClass.run`. They are synonyms)




## Writing new tests
The simplest way is to look at an existing help file or class document, and read this document and [SCDocSyntax](../Reference/SCDocSyntax.md)



