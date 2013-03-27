Python Input Parser
===================

This implements a general parsing language to parse input from `stdin`, to be
used in programming contests. This is intended to be compatible with both Python
2 and Python 3.

How to use
----------

To parse input, call the function: `parse(parse_string)`. This returns a data
structure as defined in `parse_string`.

Example
-------
Lets say you are given the following description of the input:

> The first line of the input gives the number of test cases, **T**. **T** test
> cases follow. Each case begins with a line containing an integer **N**,
> denoting the number of lines in that case. The next N lines each describe one
> subcase containing integers **A** and string **B**.

This is an example of a possible input from `stdin`:

```
2
3
1 q
5 w
7 e
2
1 r
2 t
```

We wish to parse this into the following python data-structure:

```python
[[{'A': 1, 'B': 'q'}, {'A': 5, 'B': 'w'}, {'A': 7, 'B': 'e'}],
 [{'A': 1, 'B': 'r'}, {'A': 2, 'B': 't'}]]
```

This is how it is done:

```python
from parser import parse

parse_string = \
"""
<int t>
$t{
<int n>
$n{
<int a> <str b>
>>> {'A' : $a, 'B': $b}
}
>>> list(%n)
}
>>> list(%t)
"""

data = parse(parse_string)
```

Specification
-------------

There are two types of parsers, line parser and block parser. There are also two
types of variables, normal variables and iterable variables.

### Line Parser Syntax

A line parser will read in one line and try to bind normal variables to the data
read from the input. To bind more than one variable, the data and the line
parser entries must be separated by spaces.

Each entry in a line parser must have the following form:
```
<type varname>
```
Where `varname` must be a valid normal variable name.

Types supported by line parser:

|Type           | Name  |
|---------------|-------|
|String         | str   |
|Integer        | int   |
|Float          | float |

### Block Parser Syntax

Every block parser must start with `$varname{`, where `varname` is the name of
an integer-valued normal variable. It must end with one return statement,
followed by `}` on a new line.

A block parser starts with an initializing integer normal variable. The value of
the variable is looked up at the start of the execution of the block parser,
which is the number of times the block can be executed. The block parser then
binds an iterable variable with the same name as the initializing variable. The
iterable variable points to an iterator, which yields the result of each
iteration of the block, as defined by the return statement.

### Return Statement Syntax

A return statement starts with `>>> `, followed by a python expression. The
result from evaluating the python expression is what each iteration of the block
should yield. The python expression can use normal and iterable variables, as
well as any function or variable defined in the global frame of the program.

### Normal Variables

A normal variable starts with a `$`, followed by its name, which must be all
letters. All normal variables are referentially transparent, but they are
mutable by executing line parsers.

### Iterable Variables

An iterable variable starts with a `%` followed by its name, which must be all
letters. Iterable variables are not referentially transparent, and they should
only be used only once in a return statement. During execution, a iterable
variable is replaced with an iterator generated from executing its block.
