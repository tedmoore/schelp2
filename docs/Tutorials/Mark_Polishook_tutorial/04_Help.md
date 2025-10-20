# 04_Help

*Mark Polishook tutorial*

**Categories:** Tutorials>Mark_Polishook_tutorial

**Related:** [Mark_Polishook_tutorial/00_Introductory_tutorial](../../Tutorials/Mark_Polishook_tutorial/00_Introductory_tutorial.md)


## Help
SuperCollider has a built-in help system. To see the main help page, press cmd-d (without first selecting anything). From that page, click on underlined topics. Another useful document is [More-On-Getting-Help](../../Guides/More-On-Getting-Help.md).

In general, there are help files for classes (capitalized words, such as SinOsc, Array, Nil, etc.). Select the name of a class and press Cmd-d. A help file, if one exists, will open.



## Class definitions, message implementations, and the Find command
To see source code for class definitions, select the name of a class and type cmd-j

To see how a class or classes implement a particular message, select the message name and press cmd-y.

Use the Find and Find Next commands, available through the Edit menu, to search for text in the frontmost document



## grep
Use grep in the Terminal (in the Applications->Utilities folder) to search for all occurrences of a given word or phrase. For example, to see all documents that use the LFSaw class, evaluate (in the Terminal application)


```
grep -r LFSaw /Applications/SuperCollider
```


Because lines in the terminal application break according to the size of the window and not through schemes that enhance readability, it may be easier to write grep results to a file, as in


```
// change the name of the path (the argument after the '>' sign, as appropriate
grep -r LFSaw /Applications/SuperCollider/ > /Users/yourHomeDirectory/Desktop/grep_results
```




## Additional sources
The SuperCollider wiki:

- [http://swiki.hfbk-hamburg.de](http://swiki.hfbk-hamburg.de):8888/MusicTechnology/6


The SuperCollider users mailing list archive:

- [http://www.listarc.bham.ac.uk/marchives/sc-users/](http://www.listarc.bham.ac.uk/marchives/sc-users/)


The SuperCollider user or developer lists (or both).

- [http://www.beast.bham.ac.uk/research/sc_mailing_lists.shtml](http://www.beast.bham.ac.uk/research/sc_mailing_lists.shtml)


David Cottle has a large course on sound synthesis based around SC3.

A course by Nick Collins:

- [http://www.informatics.sussex.ac.uk/users/nc81/courses/cm1/workshop.html](http://www.informatics.sussex.ac.uk/users/nc81/courses/cm1/workshop.html)


The pseudonym tutorial:

- [http://www.psi-o.net/pseudonym/](http://www.psi-o.net/pseudonym/)


The MAT tutorial (UC-Santa Barbara) tutorial:

- [http://www.mat.ucsb.edu/~sc/](http://www.mat.ucsb.edu/~sc/)


////////////////////////////////////////////////////////////////////////////////////////////////////

go to [Mark_Polishook_tutorial/05_The_network](../../Tutorials/Mark_Polishook_tutorial/05_The_network.md)



