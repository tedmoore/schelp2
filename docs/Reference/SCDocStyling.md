# SCDoc Styling

*Help system CSS styles customization and themes*

**Categories:** HelpSystem

**Related:** [WritingHelp](../Guides/WritingHelp.md), [SCDoc](../Classes/SCDoc.md), [SCDocHTMLRenderer](../Classes/SCDocHTMLRenderer.md)

Documentation rendered HTML reads the global style from `scdoc.css`, but also reads `frontend.css` and `custom.css` (in that order) if available. This is to enable specific frontends and allow users to override the CSS.
So to customise the CSS, the user can create a `custom.css` in their [SCDoc#*helpTargetDir](../Classes/SCDoc.md#*helptargetdir) or at the root of any HelpSource directory (for example in `YourExtension/HelpSource/custom.css`).

```
// open HelpTargetDir to see these css files
SCDoc.helpTargetDir.openOS
```


## Colors
Colors are defined as CSS variables, so that to change any color, it's sufficient for a user to override the relevant variable in their `custom.css`. These variables are then used to set any color in all other css files of the documentation.

Specific variables are not reported here, please refer to the default CSS theme for all their names and default values.


```
// open default theme
(SCDoc.helpTargetDir +/+ "themes" +/+ "default.css").openDocument

// copy default theme to 'custom.css' as a starting point
File.copy(
    SCDoc.helpTargetDir +/+ "themes" +/+ "default.css",
    SCDoc.helpTargetDir +/+ "custom.css"
)

// open directory with all themes
(SCDoc.helpTargetDir +/+ "themes").openOS;
```


The `themes` directory also contains a `README.md` which goes more into detail about how a theme gets applied and stored for a client and how a theme can be developed.


### Themes
CSS themes distributed in `HelpTargetDir/themes` are provided only to match ScIDE's UI themes. There is currently no implementation for modifying CSS themes dynamically or to add custom ones, so for any customization it's recommended to write a `custom.css` file as explained above





