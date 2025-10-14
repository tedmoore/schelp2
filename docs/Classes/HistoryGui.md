# HistoryGui

*A gui for History objects*

**Categories:** GUI>Interfaces

**Related:** [History](../Classes/History.md)

## Description

HistoryGui allows easy access to History as it happens: one can read recent lines, when they were written and by whom; one can search for text strings and by author names; and one can quickly grab lines of code for rewriting. Apart from documenting just in time programming sessions, all of this can be useful in live coding performances. See e.g. the system developed by powerbooks_unplugged, in the Quark called Republic.
The gui elements in detail:

**button start/end**
: starts and ends History *if* `gui.history` is current.

**button all/filt**
: turns filtering on/off.

**popup all/...**
: selects which name key to search for (useful if networked)

**TextView**
: allows for typing in a search string.

**button top/keep**
: sets mode whether ListView stays on top line, or keeps sticking to the selected line.

**ListView**
: shows either all `lineShorts`, or the filtered `lineShorts`; selecting them in ListView makes them come appear in post-doc window.


first example:

```supercollider
(
// create a short history
h = History([
    [0, \me, "1+2"],
    [1, \me, "3+5"], [1.234, \you, "q = q ? ();"],
    [3, \they, "\"The story\".speak"]
]);
// make a gui for it
g = h.makeWin(0@20);
// find or make a text window for code line display
// (called 'doc' because that was a Document in pre-Qt times)
g.findDoc;
// post line at index 2 in h.lines in doc window
g.postDoc(2);
)
```




## Class Methods

### `docHeight`
get and set the height of the text window opened by HistoryGui
### `docTitle`
get and set the title of the text window opened by HistoryGui
### `new`
create a new HistoryGui**Arguments:**

| Argument | Description |
|----------|-------------|
| `object` | the history |  
| `numItems` | the number of lines in the TextView above |  
| `parent` | a parent window or view in which to place new HistoryGui |  
| `bounds` | bounds for new HistoryGui, constrained by its minSize. |  
| `makeSkip` | flag whether to create a skipjack for the HistoryGui. |  
| `options` | options to set for the HistoryGui (inherited from JITGui). |  


## Instance Methods


### views
### `textV`
top: the TextView for the selected line
### `startBut`, `filtBut`, `keyPop`, `filTextV`, `topBut`
the line of buttons, popup and TextView
### `listV`
the ListView for the history lines
### `resetViews`
reset all views
### `showLineAt`
show the line at that index in History.lines in the TextView.

### 'doc'-related
### `doc`
the external text window made by HistoryGui to show codelines on. This is still called doc because it used to be a Document in pre-Qt times.
### `findDoc`
find an open a re-usable text window, or make a new one
### `docFlag`
get or set the symbol for the doc strategy to use: `\sameDoc` tries to re-use a single text window, `\newDoc` always makes a new one (and keep track of old docs)
### `oldDocs`
list of previous text windows (docs) opened
### `postDoc`
find the codeline at index in History, and post it on the textwindow
### `setDocStr`
set the string of the current textwindow
### `rip`
create a new textwindow with currently selected line

### filtering
### `filtering`
flag whether filtering is on
### `filterOn`, `filterOff`
convenience on/off methods
### `filters`
keys and string fragments to filter for. e.g. ['all', "+"] gets lines from all sources that contain the string "+".
### `filterLines`
apply filtering to history lines
### `filteredIndices`
the indices of the current filtered lines
### `filteredShorts`
the current filtered short lines for gui displaymethod:.setKeyFilter set the key(s) to filter for, and perform filtering
### `setStrFilter`
set the string to filter for, and perform filtering
### `stickMode`
stickMode 0 means top, i.e. select top when new lines come in; stickMode 1 means keep, i.e. keep current line selected after new lines come in.

## Examples


```supercollider
(
// create a short history
h = History([
    [0, \me, "1+2"],
    [1, \me, "3+5"], [1.234, \you, "q = q ? ();"],
    [3, \they, "\"The story\".speak"]
]);
// make a gui for it
g = h.makeWin(0@20);
// find or make a text window for code line display
// (called 'doc' because that was a Document in pre-Qt times)
g.findDoc;
// post line at index 2 in h.lines in doc window
g.postDoc(2);
)

h.document;

// show how filtering works:

g.filtering; // is filter on?
g.filterOff; // shorthand for off
g.filterOn;  // and on

// filtering looks for lines by author key(s)
// and strings in the code lines:
g.filters.postcs;

g.setKeyFilter(\all);
g.setKeyFilter(\me);
g.setStrFilter("");
g.setStrFilter("3");

g.filters.postcs;

// internal state cached in the HistoryGui:
g.filteredIndices;
g.filteredShorts;
```




