from parser import parse

parse_string = \
"""
<int t>
$t{
<int m> <int n>
$m{
<str s>
>>> bin(int($s, 16))[2:].zfill($n)
}
>>> list(%m)
}
>>> list(%t)
"""

data = parse(parse_string)

print(data)