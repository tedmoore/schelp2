# SCDocNode

*An SCDoc parsed document node*

**Related:** [SCDoc](../Classes/SCDoc.md)

**Categories:** HelpSystem

## Description

This class is used internally by [SCDoc](../Classes/SCDoc.md) to represent a node in the parsed document tree returned by the parser. It has an id symbol, optional text and optional children.


## Class Methods

### `new`
Create a new node

## Instance Methods

### `id`
The node ID. A [Symbol](../Classes/Symbol.md)### `text`
Text associated with this node. A [String](../Classes/String.md) or nil.### `children`
Children of this node. A [Array](../Classes/Array.md) or nil.### `merge`
Merge another document node tree with this one. Used by document additions (*.ext.schelp)**Arguments:**

| Argument | Description |
|----------|-------------|
| `root2` | Another SCDocNode instance. |  
### `findChild`
Find the first child of this node with specified id.**Arguments:**

| Argument | Description |
|----------|-------------|
| `id` | A [Symbol](../Classes/Symbol.md) |  


