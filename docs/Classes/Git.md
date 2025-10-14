# Git

*git interface*

**Categories:** Frontends

**Related:** [Quarks](../Classes/Quarks.md), [Quark](../Classes/Quark.md)

## Description

An interface to the git toolchain. For more information on git, see [http://git.io](http://git.io).


## Class Methods

### `new`
creates a new instance of `Git`, pointing to an existing local git repository.**Arguments:**

| Argument | Description |
|----------|-------------|
| `localPath` | path to the git repository. |  

### `isGit`
returns `true`, if a local directory is a git repository.**Arguments:**

| Argument | Description |
|----------|-------------|
| `localPath` |  |  

### `checkForGit`
returns `true`, if the git toolchain is found on the system.

## Instance Methods


### info
### `branch`
**Returns:** current branch name.
### `remote`, `url`
**Returns:** url of the first remote that it finds.
### `remoteAsHttpUrl`
Detects if the remote URI starts with `"git@"` or `"git:"` and remodels it to a valid `"https"` URI. Otherwise, it returns the unaltered remote.
```supercollider
// git-style remote URI's are transformed to https
Git().url_("git@github.com:foo/bar.git").remoteAsHttpUrl;
Git().url_("https://github.com/foo/bar").remoteAsHttpUrl;
Git().url_("git@foo.net:foo/bar.git").remoteAsHttpUrl;

// http and https are left untouched
Git().url_("https://foo.org/bar").remoteAsHttpUrl;
Git().url_("http://foo.org/bar").remoteAsHttpUrl;

// unknown URI styles are left untouched
Git().url_("fooBar").remoteAsHttpUrl;
```

**Returns:** remote URI formatted for `http` respectively `https` requests.
### `remoteLatest`
**Returns:** hash of latest commit on the remote
### `localPath`
**Returns:** path to local repository
### `tag`
**Returns:** currently checked out tag
### `tags`
**Returns:** avaliable tags
### `sha`
**Returns:** hash of the currently checked out version
### `shaForTag`
**Arguments:**

| Argument | Description |
|----------|-------------|
| `tag` | one of the tags returned by [tags](#tags) |  
**Returns:** hash of the given tag
### `isDirty`
**Returns:** `true` if there are local changes

### perform actions on remote
### `fetch`
perform a fetch from remote
### `checkout`
perform a checkout from remote with argument `refspec`**Arguments:**

| Argument | Description |
|----------|-------------|
| `refspec` |  |  

### `pull`
perform a pull from remote
### `clone`
perform a clone from url into [localPath](#localpath)**Arguments:**

| Argument | Description |
|----------|-------------|
| `url` | the url of the remotes |  



## Examples


```supercollider
// create a Git that points to a Quark directory
g = Git(Quarks.all.choose.localPath);

// alternatively, provide a pathname to a local git repository:
g = Git("/path/to/local/repo");

// get all available tags
g.tags;

// return local path
g.localPath;

// return url
g.url;
```




