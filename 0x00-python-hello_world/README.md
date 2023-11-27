# Python & string Formatting

### Key Takeaway

The web page provides practical examples and a comparison of old-style string formatting using `%` and new-style formatting using `.format()` in Python, covering basic formatting, value conversion, padding and aligning strings, truncating long strings, handling numbers, named placeholders, accessing nested data structures, datetime formatting, parametrized formats, and custom object formatting.

### Summary

- Python offers both old-style (`%`) and new-style (`.format()`) string formatting methods.
- Examples work across Python 2.7, 3.2, 3.3, 3.4, and 3.5 without additional libraries.
- Basic formatting:
    - Old: `'%s %s' % ('one', 'two')`
    - New: `'{} {}'.format('one', 'two')`
- Positional index in new style allows reordering without changing arguments.
- Value conversion:
    - `!s` and `!r` flags in new style for `str()` and `repr()` conversions.
- Padding and aligning strings:
    - New style offers more control over padding, alignment, and choice of padding character.
- Truncating long strings:
    - Old: `'%.5s' % ('xylophone',)`
    - New: `'{:.5}'.format('xylophone')`
- Combining truncating and padding:
    - Old: `'%-10.5s' % ('xylophone',)`
    - New: `'{:10.5}'.format('xylophone')`
- Handling numbers:
    - Integers: `%d` (old) vs. `'{:d}'.format(42)` (new)
    - Floats: `%f` (old) vs. `'{:f}'.format(3.141592653589793)` (new)
- Padding numbers:
    - Similar to strings, with precision for floating point numbers.
- Signed numbers:
    - New style allows control over sign position.
- Named placeholders:
    - Both styles support named placeholders, but new style is more flexible.
- Accessing nested data structures:
    - New style allows accessing containers and attributes more flexibly.
- Datetime formatting:
    - New style allows inline formatting of datetime objects.
- Parametrized formats:
    - New style allows dynamic specification of format components.
- Custom objects:
    - New style allows custom format handling by overriding `__format__()` method.
