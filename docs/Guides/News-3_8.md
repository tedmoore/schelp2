# News in 3.8

*A summary of news in SC 3.8*

**Categories:** News

**Related:** [News-3_7](../Guides/News-3_7.md), [News-3_6](../Guides/News-3_6.md), [News-3_5](../Guides/News-3_5.md), [Debugging-tips](../Guides/Debugging-tips.md)

3.8 is light on new features and heavy on small bugfixes. See CHANGELOG.md for more details.

## SuperCollider IDE
- The middle mouse button now closes tabs.
- A new menu entry, Language > Quarks, launches Quarks.gui.




## SuperCollider Language
- New methods: [Function#-plotAudio](../Classes/Function.md#-plotaudio), [Bus#-plotAudio](../Classes/Bus.md#-plotaudio).
- It is now easier to insert custom views, in particular subclasses of [SCViewHolder](../Classes/SCViewHolder.md), into layouts.
- New methods: [TreeView#-addChild](../Classes/TreeView.md#-addchild), [TreeView#-insertChild](../Classes/TreeView.md#-insertchild), and [TreeView#-childAt](../Classes/TreeView.md#-childat), alias methods provided for symmetry with TreeViewItem.




## SuperCollider Server
- A new command-line option for scsynth, -B, allows binding to a specific address.
- [VOsc](../Classes/VOsc.md) supports an audio-rate phasein argument.
- [TGrains](../Classes/TGrains.md) supports numChannels set to 1.




## API changes
- The number of default audio buses has been increased from 128 to 1024.
- [TGrains](../Classes/TGrains.md), [GrainBuf](../Classes/GrainBuf.md), [GrainSin](../Classes/GrainSin.md), [GrainFM](../Classes/GrainFM.md), and [GrainIn](../Classes/GrainIn.md) now have unified panning behavior when numChannels is 2 and the pan exceeds the range [-1, 1].
- Several old methods have been deprecated from [PathName](../Classes/PathName.md): *fromOS9, foldersWithoutCVS, isCVS, foldersWithoutSVN, isSVN, filesDoNoCVS, filesDoNoSVN, streamTreeNoCVS.
- The argument "startframe" has been renamed to "startFrame" and "aSoundFile" to "soundFile" in the following methods of [SoundFileView](../Classes/SoundFileView.md): loadFile, setData, readFile, read, readFileWithTask, readWithTask.




## Known Issues
While much has improved and many bugs from 3.7 have been fixed, there are still many known issues. For a complete list see: [https://github.com/supercollider/supercollider/issues/](https://github.com/supercollider/supercollider/issues/)

Please do not hesitate to add new issues you find to the [issue tracker](https://github.com/supercollider/supercollider/issues) or mention them on the [mailing list](http://www.birmingham.ac.uk/facilities/ea-studios/research/supercollider/mailinglist.aspx)



