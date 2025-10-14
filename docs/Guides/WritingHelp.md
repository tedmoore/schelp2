# Writing Help

*Get started with writing help*

**Categories:** HelpSystem

**Related:** [SCDocSyntax](../Reference/SCDocSyntax.md), [SCDoc](../Classes/SCDoc.md)


## Writing new help
The simplest way is to look at an existing help file or class document, and read this document and [SCDocSyntax](../Reference/SCDocSyntax.md)


> **Note:** The help files should use UTF-8 encoding!


All tags that are used for document metadata should be entered at the top of the document source file, before any section or other text. See [SCDocSyntax / Header tags ](../Reference/SCDocSyntax.md#header-tags)

In the header, you must specify the title, summary and categories parts of the header.

Example header:


Use regular text in sections and subsections, and possible other tags for lists, tables, trees, images, links, etc.. See [SCDocSyntax](../Reference/SCDocSyntax.md) for tag reference.



### Documenting new classes
When you navigate to an undocumented class, it will contain an schelp template that can be filled in and saved to HelpSource/Classes/ClassName.schelp.

A list of all undocumented classes can be seen here: [Browse / Undocumented classes ](../Browse.md#undocumented-classes) (auto-generated).





## Directory layout
The help system uses different folders under HelpSource depending on document kind:


**HelpSource**
: **Classes**
: class reference, file must be named as the class.

**Reference**
: other reference documentation.

**Tutorials**
: yes, tutorials.

**Guides**
: guides that explain stuff but without being a real tutorial.

**Overviews**
: overviews of other documents, these are mostly auto-generated.

**Other**
: stuff that don't fit in any other directory.




> **Note:** It's important that the document is put in the right folder. For Classes, it's a must!


All .schelp files will be parsed and rendered to an equal directory layout in the help target directory. Any other files, like images or ready-made HTML files, will just be copied.



## Class reference
Class reference has some special tags and a more strict structure. Normal text should be written inside the special top-level sections DESCRIPTION, CLASSMETHODS, INSTANCEMETHODS and EXAMPLES.

Named subsections can be used under each of the above mentioned top-level sections.

Also named sections can be used, but they will be put after all above top-level sections.


### Methods and arguments
Methods are documented like this:

`method::` name(s)short description of method.`argument::` name1description of argument`argument::` name2description of another argument.`returns::`description of return value`discussion::`optional discussion and example code

> **Note:** Don't list arguments in the method tag, only the method names


After the method description comes the arguments, written with `argument:: name` where **name** is optional, and will be auto-filled in if not given. If given, it must match the real argument name of the method. After each argument line comes the description of that argument.

There is an optional `returns::` tag that could be used to describe the methods return value.

If a longer discussion is needed, use the `discussion::` tag. This is a good place to insert example code, etc.

Setters are handled automagically, when documenting a setter/getter, use only the getter name (no underscore) and describe both setter and getter as a single property, example:


Methods get an anchor name automatically, prefixed with `*` for class methods and `-` for instance methods. For example, to link to the `foo` class method, use `link::#*foo::`.

The `method::` tag can be used also in normal documents, and *should* then have argumentnames. This can be useful for documenting common interfaces outside of a specific class document, for example [plot](../Reference/plot.md). Anchors for these methods get prefixed with a dot (.) instead of * or -.

When multiple methods have the same signature (like ar and kr in ugens), they should all be listed in one single method tag.

SCDoc generates docs for all undocumented methods. To ignore private methods, add them to a `private::` tag, which works just like the method tag but without a section body.

Extensions can add methods to existing class docs, see the [#Extensions](#extensions) section below.




### Copy methods from other class
You can use `copymethod:: ClassName, methodName` to copy the documentation of a method from another helpfile to this one.

`methodName` must be prefixed with `*` (asterix) for class methods and `-` (dash) for instance methods.




### Redirect classes
Some classes uses the `*doesNotUnderstand` trick to redirect to another implementing class. To document such classes, you need to add this tag in the header:


Where `implClass` is the name of the class variable holding the implementing class.




### Example
An example of documentation for LFPulse UGen, saved to HelpSource/Classes/LFPulse.schelp






## Categories
Try to find good categories for the doc you are writing/converting. If a suitable category already exists, you should use that. See the [Document Browser](../Browse.md) (auto-generated) for existing categories.

For UGens, you should use the existing categories like UGens>Filter>Nonlinear. View the current categories like this:


```supercollider
Ball.categories
```


Documents can exist in multiple categories, and also have hierarchical categories, like Sequencing>Patterns.



## Cross-document linking
To link another document, use `link::Path/To/Document::` where the path is relative to [SCDoc#*helpTargetDir](../Classes/SCDoc.md#*helptargetdir) and the document filename is with no extension. Example:



### Methods
To link to a specific class method, append `#*methodName` or to an instance method, append `#-methodName`:


This will render as [Function#-play](../Classes/Function.md#-play)

For generic methods documented outside of instancemethods or classmethods (like the generic [play](../Reference/play.md) document), use a dot (.) as prefix instead of * or -.

The special [Methods](../Overviews/Methods.md) overview is dynamic and allows a specific method to be shown by appending `#name` where name is the name of the method:






## Making the document findable by Search
The [Search](../Search.md) page can match on document title/filename, summary, non-private methods, and categories. If you mention something that should match in search but is not one of the above, you can explicitly add it with the keyword tag:




## Extensions

### Quarks and extensions
Each extension should have their own HelpSource folder with files that should be included in the help system.

Example file layout:


```supercollider
MyQuark/HelpSource/Classes/MyClass1.schelp
MyQuark/HelpSource/Classes/MyClass2.schelp
MyQuark/HelpSource/Guides/MyGuide.schelp
MyQuark/HelpSource/Guides/MyPicture.png
MyQuark/MyClass1.sc
MyQuark/MyClass2.sc
```



> **Note:** All helpfiles contained in a quark will automatically get a category "Quarks>NameOfQuark" added, so you should not add this yourself. This makes it easy to navigate all documentation of a specific quark.


If you want to set a main help file for the quark, set `\schelp` in the Quark directory file to the path for the help file relative to `HelpSource` and without the `.schelp` extension. Example: `\schelp: "Guides/MyGuide"`




### Method extensions
An extension that adds methods to existing classes should document these in `Classes/TheClass.ext.schelp`, only including the relevant bits (no title, summary, categories, etc..)

Example: Classes/String.ext.schelp


The contents are inserted into the right spot (section, subsection, etc). It works for all kind of sections, for example one can add a subsection to `DESCRIPTION::` with additional information, or add another top-level section, etc.





## Links
URL's are automagically converted to links.

The `link::` tag is used for cross-reference between docs. It uses a simple namespace, example:


```supercollider
See also link::Classes/SinOsc:: for a nice oscillator.
Or take a look at link::Browse#UGens:: for a full list.
The link::Overviews/Methods#play#play method:: is often very useful.
```


Anchors can be inserted manually with `anchor::name::` and referenced like this:


```supercollider
link::Foo/Bar#hello::
```


or to jump to an anchor in this document:


```supercollider
link::#hello::
```


All sections get anchor names automagically.

All methods get anchor names prefixed with `*` for class methods and `-` for instance methods.

One can change the rendered text of the link by using another `#` character:


```supercollider
Also see link::Classes/SinOsc##a nice oscillator::
```


A link to specific methods:


```supercollider
Take a look at link::Classes/SinOsc#*ar:: and link::Classes/Function#-play::
```


Renders as: [SinOsc#*ar](../Classes/SinOsc.md#*ar) and [Function#-play](../Classes/Function.md#-play)

The [Methods](../Overviews/Methods.md) overview is dynamic and allows a specific method to be shown, by using the methodname as anchor, for example to get a list of all classes implementing `play` :


```supercollider
All classes implementing code::play:: can be seen link::Overviews/Methods#play#here::.
```


Renders as: All classes implementing `play` can be seen [here](../Overviews/Methods.md#play).

The [Browse](../Browse.md) page is also dynamic, and can take a category tree as anchor name:


```supercollider
For more filters, see link::Browse#UGens>Filters::
```


Renders as: For more filters, see [Browse#UGens>Filters](../Browse.md#ugens>filters)



## Contributing with documentation
The easiest way to contribute to the documentation is:

 1. Fork the SuperCollider repository [https://github.com/supercollider/supercollider](https://github.com/supercollider/supercollider)

 2. Clone your repository


```supercollider
    git clone --recursive https://github.com/{your_username}/supercollider.git
```


 3. Create a branch for doc updates


```supercollider
    git checkout -b doc_updates
```


 4. Do your update, commit your changes and push to github


```supercollider
    git push origin -u doc_updates
```


 5. Submit your pull request through github, from your branch doc_updates to SuperCollider develop



## Working with legacy documentation
Here is some information for working with documentation that is written in legacy format or syntax.


### News in SC 3.5.2
SCDoc was rewritten and the parser implemented in C++ for speed and stability in 3.5.2. The syntax got more strict, and the parser now throws errors or warnings if there are faults in the documentation.

Some important changes to keep in mind:

- Linking to sections does no longer use lower_case_and_underscored anchors, but the exact section title as it is. Example: `link::#Language-side news::` renders: [#Language-side news](#language-side-news)
- Run `SCDoc.indexAllDocuments` if you add a new document or other file and want to see the change reflected in the help. If you just changed a document and want to see the changes, just press Reload in the browser and SCDoc will detect and re-index automatically.
- The `CLASS::` tag is deprecated, just use `TITLE::` instead also for class reference docs.
- The argument name given to the `ARGUMENT::` tag is now optional. If not given, SCDoc will auto-fill the real argument name.





### Converting old helpfiles
There is no automated process for this, but for most help files it's really simple to do it manually:

1. open the old helpfile in your web browser
2. copy the text and insert it in a new textfile: FileName.schelp
3. add the appropriate tags, like title, sections, etc.. (see below)
4. save the file to the right subdirectory under HelpSource, depending on the document kind (see [#Directory layout](#directory-layout) below)
5. **check that it rendered OK**. You can run `SCDoc.indexAllDocuments` (link to method documentation: [SCDoc#*indexAllDocuments](../Classes/SCDoc.md#*indexalldocuments)) to make SCDoc detect the new file and add it to the document index.If the file already existed and you want to see the changes, just press Reload in the help browser and SCDoc will re-render it.








