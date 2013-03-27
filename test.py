from parser import parse, maplist

def solve(*args):
    print(*args)

parse_string = \
"""
<int t>
$t{
<int s> <int m>
$m{
<int x> <int y>
>>> ($x, $y)
}
>>> solve($s, list(%m))
}
>>> None
"""
parse(parse_string, globals())



