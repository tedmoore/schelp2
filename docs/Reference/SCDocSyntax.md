# SCDoc Syntax

*SCDoc markup language syntax*

**Categories:** HelpSystem

**Related:** [WritingHelp](../Guides/WritingHelp.md), [SCDoc](../Classes/SCDoc.md), [SCDocHTMLRenderer](../Classes/SCDocHTMLRenderer.md)


## Introduction
This document specifies the syntax and [#Grammar](#grammar) of the [SCDoc](../Classes/SCDoc.md) markup language. `SCDoc Markup` is used in SuperCollider mainly for helpfiles. It is a syntax that features semantic a semantic level specific to the requirements of SuperCollider.


> **Note:** A guide to writing help can be found at [WritingHelp](../Guides/WritingHelp.md).




## Specification
A document is split into a header section and a body. The header contains only header tags, which are not allowed in the document body.

SCDoc documents consist of *tags* and *text*.

- Tags consists of single words ending with `::` (double-colon).
- Untagged text becomes plain prose.
- Paragraphs are separated by one or more empty lines.
- Tags are case-insensitive: `TITLE::`, `Title::` and `title::` are interepreted equally.
- Some tags take the remaining text on the same line as their argument
- Some tags enclose the following text until a single end-tag (double-colon `::`).
- Some enclosing tags can be nested, while others are modal and ignore any tag until an end-tag.



### Header tags
Header tags take the remaining text in their definition line as their argument. They expect no end-tag.


**title::`TITLE::` name**
: Title of the document. For class reference documents, this must be the same as the classname.

**categories::`CATEGORIES::` list**
: A comma-separated list of document categories. Mainly used by the [Browse](../Browse.md) page.Categories can be hierarchical, where levels are denoted with `>`.

**related::`RELATED::` link(s)**
: A comma-separated list of related docs.

**summary::`SUMMARY::` text**
: A short summary of this document.

**redirect::`REDIRECT::` name**
: For class redirect systems, specify the name of the instance variable holding the implementing class. Example:

**class::`CLASS::` name**
: Deprecated, use TITLE instead.






### Section tags
A document can be divided into sections and subsections. Section bodies consist of everything that follows its section tag until another section tag of same or higher level.

Sections have a link anchor with the same name as the section.


> **Note:** Method tags also create such anchors. The methodname then is prefixed with `*` (class methods) or `-` (instance methods).


Structural tags at the same level in the hierarchy may be functionally equivalent but treated differently for rendering or querying purposes. For example `examples::` is equivalent to `section::` but imply particular formatting or specially identify the examples section for customised uses like concatenating all examples for classes with a given parent class.

Structural tags can have child elements, for example the items in a list or the subsections and prose in a section.

Level 1 (highest):


**section::`SECTION::` name**
: A named section. The name should be plain text and can not contain any tags.

**description::`DESCRIPTION::`**
**classmethods::`CLASSMETHODS::`**
**instancemethods::`INSTANCEMETHODS::`**
**examples::`EXAMPLES::`**
: These tags starts standard sections of a class reference. CLASSMETHODS and INSTANCEMETHODS have special meaning, in that they specify if a documented method is a classmethod or instancemethod.



Level 2:


**subsection::`SUBSECTION::` name**
: A named subsection. The name should be plain text and can not contain any tags. Example:



Level 3:


**subsubsection::`SUBSUBSECTION::` name**
: A named subsubsection. The name should be plain text and can not contain any tags. Example:






### Method tags
These are level 3 subsections:


**method::`METHOD::` methodname(s) [argstring]**
: Document one or more methods, given as a comma-separated list of methodnames.
> **Note:** If multiple methods are documented as a group, the methods must have the same argument name signature for existing arguments. For example, grouping the following methods would be ok:But not:

Following the method tag should come a short description of the method, and optional description of the arguments and return value. See the [#tags allowed inside a method](#tags-allowed-inside-a-method) section below.SCDoc regards getter and setter methods as read/write interfaces for a single *property*. This means that you should not write the trailing underscore for setters. Instead, document it as a single property without the underscore, as if there was only a getter, and describe the property that can be set/gotten.The METHOD tag is normally used inside CLASSMETHODS and INSTANCEMETHODS, but can also be used outside of these sections. In those cases, it documents a generic interface not bound to a specific class, and the arguments and default values should then be given in the optional **argstring**For real methods, the argstring is not allowed, instead the argument names and default values will be auto-filled in.

**private::`PRIVATE::` methodname(s)**
: This tag behaves like a section but does not have a section body. It marks one or more methods as private, so that it does not show up under the auto-generated *Undocumented Methods* sections. Expects a comma-separated list of methodnames.

**copymethod::`COPYMETHOD::` classname methodname**
: This tag behaves like a section but does not have a section body. Copy a method documentation from a class reference and insert it here as if the method was documented in this document. The methodname must be prefixed with `*` for classmethods and `-` for instancemethods.



<a id="tags allowed inside a method"></a>Inside a method section, the following optional tags are allowed, in the order given below. These tags are level 4 subsections.


**argument::`ARGUMENT::` [argname]**
: One for each argument. The argument section body should contain a description of the given argument. The **argname** is optional, and will be auto-filled in if not given. If given, it must match the real name of the argument at this position.If the method has varargs, the argname for the varargs (if given) should be prefixed with three dots and a space (`"... "`)

**returns::`RETURNS::`**
: This section should contain a description of the return value, especially the type.

**discussion::`DISCUSSION::`**
: This optional section can contain a more detailed discussion and code examples related to this method.







### Modal tags
These tags enclose a text and ends with a single `::` (double-colon) end-tag. The enclosed text can not contain any other tags.


**strong::`STRONG::`**
: Render text in bold font.

**emphasis::`EMPHASIS::`**
: Render text in emphasized font, typically italics.

**soft::`SOFT::`**
: Render text in a soft shade.

**link::`LINK::`**
: Create a link to another document. The text should be the document key, which is the path relative the Help folder and without extension, like `Classes/SinOsc` or `Reference/SCDocSyntax`Optionally, the path can be followed by `#anchor` to jump to a specific place in the document, and `#label` to specify another label for the link.All kinds of sections automatically creates an anchor with the same name as the section. Methods also creates an anchor, with the methodname prefixed with `*` for class methods and `-` for instance methods.The path can be empty for linking to an anchor inside the current document, and the anchor can be empty to only specify the link label.URL's are automagically turned into links, but can be explicitly created with this tag, if one wants to use another link label.

**anchor::`ANCHOR::`**
: Manually create an anchor at this position in the document.

**image::`IMAGE::`**
: Insert image, the text should be the relative path to the image.Optionally an image caption can be given:And, the image can be clickable and link to another page:Just leave the caption empty if you want a link but no caption.

**math::`MATH::`**
: Converts LaTeX code into an inline formula. E.g.becomes $\frac{\pi}{2}$ embedded within a line of text.



The following tags (CODE, TELETYPE and MATH) can be written in two forms, either inline or block. **Inline** form has the end-tag on the same line, and need any enclosed double-colons that should be part of the text to be escaped with backslash (`\`). **Block** form has the tag and end-tag on lines by themselves, and can take multi-line text. In block form, only a single end-tag on its own line counts and any end-tags inside the text should not be escaped (except if it's on a single line).



**code::`CODE::`**
: Render syntax-colored SuperCollider code.

**teletype::`TELETYPE::`**
: Render monospace text.

**math::`MATH::`**
: Renders LaTeX code in display style. E.g.becomeswhich is separated from the text through a block. For specifics check out the used rendering engine kaTeX at [https://katex.org](https://katex.org)






### Lists and tables
List items, table rows and definition terms are denoted with `##` (double-hash). Table cells and definition descriptions are denoted with `||` (double-bar). Lists and tables can be nested, and ends with the end-tag.


**table::`TABLE::`**
: Create a table. Example:Renders:| a 1 | a 2 | a 3 | 
| --- | --- | --- || b 1 | b 2 | b 3 | | c 1 | c 2 | c 3 |

**definitionlist::`DEFINITIONLIST::`**
: A definition list item consists of one or more terms prefixed with `##` followed by a description prefixed with `||`. Example:

**list::`LIST::`**
: Create a simple bulleted list. Items are prefixed with `##`

**numberedlist::`NUMBEREDLIST::`**
: Create a numbered list. Items are prefixed with `##`

**tree::`TREE::`**
: Create a tree structure. Typically nested with more TREE tags. Items are prefixed with `##`






### Notes and warnings
These can have other tags in them, and ends with the end-tag.


**note::`NOTE::`**
: Create a NOTE box with important content.
> **Note:** like this

**warning::`WARNING::`**
: Create a WARNING box with very important content.> **⚠️ Warning:** like this

**footnote::`FOOTNOTE::`**
: Create a footnote which will be rendered at the end of the document. At the position of the FOOTNOTE tag, the footnote number will be rendered with a link to the footnote. Example:The result looks like this: Hello I'm a geek> *According to [http://en.wikipedia.org/wiki/Geek](http://en.wikipedia.org/wiki/Geek) the word geek is a slang term, with different meanings ranging from "a computer expert or enthusiast" to "a carnival performer who performs sensationally morbid or disgusting acts"*






### Other tags

**keyword::`KEYWORD::` keyword(s)**
: Specify one or more searchable keywords for this document. An anchor named the keyword prefixed with `kw_` will be created at the position of this tag.

**classtree::`CLASSTREE::` classname**
: Render a class tree of subclasses starting from the given class.







## Grammar
The following is an exact specification of the grammar:






