# CustardPython

CustardPython is a library of custom Python utility functions and classes that extend the standard library.  
It provides a collection of helpful functions for everyday programming tasks, including dictionary and list manipulation, terminal output, ASCII shape drawing, date formatting, math, and chemistry utilities.

## Getting Started

Import the desired utility class into your project:

```python
from CustardPython import DictionaryUtils, ListUtils, TerminalUtils, ShapeDrawer, DateUtils, MathUtils, ChemistryUtils
```

## Utility Classes

| Category                | Class Name         | Description                                      |
|-------------------------|-------------------|--------------------------------------------------|
| Dictionary utilities    | `DictionaryUtils` | Enhanced dictionary manipulation                 |
| List utilities          | `ListUtils`       | Common list operations                           |
| Terminal output         | `TerminalUtils`   | Screen clearing and typewriter effects           |
| ASCII shape drawing     | `ShapeDrawer`     | Draw shapes with symbols in the terminal         |
| Date formatting         | `DateUtils`       | Format and manipulate dates                      |
| Math utilities          | `MathUtils`       | Number theory and sequence functions             |
| Chemistry utilities     | `ChemistryUtils`  | Chemistry calculations and formula manipulation  |

## Example Usage

```python
# Rename a key in a dictionary
d = {'a': 1, 'b': 2}
new_d = DictionaryUtils.rename_key(d, 'a', 'alpha')

# Reverse a list
reversed_list = ListUtils.reversed_list([1, 2, 3])

# Flatten a nested list
flat = ListUtils.flatten([1, [2, [3, 4]], 5])

# Remove duplicates from a list
deduped = ListUtils.deduplicate([1, 2, 2, 3, 1])

# Chunk a list
chunks = ListUtils.chunk([1, 2, 3, 4, 5], 2)

# Rotate a list
rotated = ListUtils.rotate([1, 2, 3, 4], 2)

# Merge two dictionaries
merged = DictionaryUtils.merge({'a': 1}, {'b': 2})

# Filter dictionary by key
filtered_keys = DictionaryUtils.filter_by_key({'a': 1, 'b': 2}, lambda k: k == 'a')

# Filter dictionary by value
filtered_values = DictionaryUtils.filter_by_value({'a': 1, 'b': 2}, lambda v: v > 1)

# Invert a dictionary
inverted = DictionaryUtils.invert({'a': 1, 'b': 2})

# Clear the terminal screen
TerminalUtils.clear_screen()

# Print text with a typewriter effect
TerminalUtils.typewriter("Hello, world!", 0.1)

# Draw a square
ShapeDrawer.draw_square(4, '*')

# Format today's date
print(DateUtils.formatted_date("Month Day(31), Year"))

# Collatz sequence steps
steps = MathUtils.collatz_steps(7, print_steps=True)

# Get empirical formula
emp = ChemistryUtils.empirical_formula("H2O2")
```

## Features

- Dictionary key renaming and insertion
- Dictionary merging, filtering, and key/value inversion
- List reversal, flattening, deduplication, chunking, and rotation
- Terminal screen clearing and typewriter effect
- Drawing triangles, squares, and hexagons in ASCII
- Flexible date formatting
- Collatz sequence and other math utilities
- Empirical formula calculation for chemical compounds

---
