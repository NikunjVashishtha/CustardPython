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
- List reversal
- Terminal screen clearing and typewriter effect
- Drawing triangles, squares, and hexagons in ASCII
- Flexible date formatting
- Collatz sequence and other math utilities
- Empirical formula calculation for chemical compounds

---
Contributions and suggestions are welcome!

