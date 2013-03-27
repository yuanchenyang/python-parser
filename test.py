from parser import parse

mapint = lambda s: list(map(int, s.split()))

parse_string = \
"""
<int t>
$t{
<int n>
<str s>
<str p>
>>> print(mapint($s), mapint($p))
}
>>> None
"""
parse(parse_string, globals())



