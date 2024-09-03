

- children (a list of or a singular dash component, string or number; optional):
    Component type, embedded element within the button group.

- id (string; optional):
    Unique identifier for the component.

- className (string | dict; optional):
    CSS class name for the current component, supports [dynamic CSS](/advanced-classname).

- description (a list of or a singular dash component, string or number; optional):
    Component type, nested element within the button, available only when `shape='square'`.

- icon (a list of or a singular dash component, string or number; optional):
    Component type, prefix icon element nested within the button.

- key (string; optional):
    Updating the `key` value of the current component can force a redraw of the component.

- loading_state (dict; optional)

    `loading_state` is a dictionary with keys:
    - component_name (string; optional):
        Holds the name of the component that is loading.
    - is_loading (boolean; optional):
        Determines if the component is loading or not.
    - prop_name (string; optional):
        Holds which property is loading.

- open (boolean; optional):
    Set or monitor the current floating button group expansion state.

- shape (a value equal to: 'circle', 'square'; default 'circle'):
    The shape of each internal floating button. Options: `'circle'`, `'square'`. Default value: `'circle'`

- style (dict; optional):
    CSS styles for the current component.

- tooltip (a list of or a singular dash component, string or number; optional):
    Component type, additional tooltip content for the button.

- trigger (a value equal to: 'click', 'hover'; optional):
    The triggering method for the floating button group, options include `'click'`, `'hover'`.

- type (a value equal to: 'default', 'primary'; default 'default'):
    Type of the button group. Options are: `'default'`, `'primary'`. Default value: `'default'`.