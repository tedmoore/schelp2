# CustomViewAction

*A MenuAction that can contain a View.*

**Categories:** GUI

**Related:** [MenuAction](../Classes/MenuAction.md), [Menu](../Classes/Menu.md), [ToolBar](../Classes/ToolBar.md), [MainMenu](../Classes/MainMenu.md)

## Description

A CustomViewAction is a [MenuAction](../Classes/MenuAction.md) that contains a [View](../Classes/View.md) instead of an icon or text. This enables embedding of interactive components to a [Menu](../Classes/Menu.md) or [ToolBar](../Classes/ToolBar.md).

```supercollider
(
~view = View().layout_(HLayout(
    ToolBar(
        MenuAction("Min", { ~slider.value = 0 }),
        MenuAction("Max", { ~slider.value = 1 }),
        CustomViewAction(
            ~slider = Slider().orientation_(\horizontal)
        ),
        Menu(
            MenuAction("Randomize", { ~multi.value = 4.collect({ 1.0.rand }) }),
            CustomViewAction(
                ~multi = MultiSliderView().drawLines_(true).elasticMode_(true).value_([0, 1, 0, 1])
            )
        ).title_("Submenu")
    ).minWidth_(400)
)).front;
)
```




## Class Methods

### `new`
 Create a new CustomViewAction**Arguments:**

| Argument | Description |
|----------|-------------|
| `` | A View. |  
| `` | A Function to execute when this item is selected.
> **Note:** In some cases, the View that the CustomViewAction contains will absorb mouse clicks, making it difficult to select this menu item (and thus trigger the action). |  


## Instance Methods

### `defaultView`
 Set the View that is attached to this CustomViewAction.**Arguments:**

| Argument | Description |
|----------|-------------|
| `` | A View. |  


