Python Input Parser
-------------------
-------------------

This implements a general parsing language to parse input from `stdin`, to be used
in programming contests. This is intended to be compatible with Python 2.7. 

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

parse_string = """
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

A line parser will read in one line and try to bind normal variables to the data
read from the input. If we are trying to bind more than one variable on each
line, the data must be separated by spaces. Any line that is neither a block
parser nor a return statement is a line parser.

All variables are all bound to one single global frame.

A normal variable starts with a "$", followed by its name, which must be all
letters. All normal variables are referentially transparent, but they are
mutable by executing line parsers.

A block parser starts with a number or a variable. If it starts with a variable,
the value of the variable is looked up and substituted. The number is the number
of times the block can be executed. 