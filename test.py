from parser import parse

def solve(d, l):
    print(d, l)

if __name__ == '__main__':
    parse_string = \
"""
<int t>
$t{
<int n>
$n{
<int d> <int i>
>>> ($d, $i)
}
<int D>
>>> solve($D, list(%n))
}
>>> list(%t)
"""
    parse(parse_string, globals())



