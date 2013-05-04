from parser import parse

def solve(*args):
    print(*args)

parse_string = \
"""
<int t>
$t{
<int n>
$n{
<int a> <int b> <int c>
>>> {'a':$a, 'b': $b, 'c':$c}
}
>>> solve(list(%n))
}
>>> None
"""
parse(parse_string, globals())



