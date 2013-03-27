"""Parser code
"""

import re

CASTING = {'int': int,
           'float': float,
           'str': str}

LINEPARSER = "<([a-zA-Z]*) ([a-zA-Z]*)>"
BLOCKSTART = "\\$([a-zA-Z]*)\\{"
ITERVAR = "%([a-zA-Z]*)"

def parser(parse_string):
    bindings = {"NORMAL__MAIN": 1}
    lines = filter(lambda x: x != "", parse_string.split("\n"))
    lines =  read_blocks(lines, 0)
    parse_block(lines, "NORMAL__MAIN", bindings)
    return list(bindings["ITER__MAIN"]())[0]
    
def read_blocks(lines, start_index):
    nested = []
    index = start_index
    while index < len(lines):
        match = re.match(BLOCKSTART, lines[index])
        if match:
            block, index = read_blocks(lines, index + 1)
            initvar = "NORMAL_" + match.group(1)
            nested.append((initvar, block))
        elif lines[index] == "}":
            return nested, index
        else:
            nested.append(lines[index])
        index += 1
    return nested
    
def parse_block(lines, init_var, bindings) :
    times = bindings[init_var]
    return_statement = lines[-1]
    lines = lines[:-1]
    assert type(times) == int, "Block parser must start with integer variable!"
    assert return_statement[:4] == ">>> ", \
        "Block parser must have return statement!"
    return_statement = return_statement.replace(">>> ", "")
    return_statement = return_statement.replace("$", "NORMAL_")
    itervars = re.findall(ITERVAR, return_statement)
    for var in itervars:
        return_statement = return_statement.replace("%" + var,
                                                    "ITER_" + var + "()")
        
    def block_iter():
        for _ in range(times):
            for line in lines:
                if type(line) == tuple: # Parse Block
                    parse_block(line[1], line[0], bindings)
                else:                   # Parse Line
                    parse_line(line, bindings)            
            yield eval(return_statement, bindings)

    iter_var = init_var.replace("NORMAL_", "ITER_")
    bindings[iter_var] = block_iter

def parse_line(format_string, bindings):
    variables = re.findall(LINEPARSER, format_string)
    line = raw_input().split()
    if len(line) != len(variables):
        raise ValueError("Incorrect line parser: " + format_string)
    for i in range(len(line)):
        vartype = variables[i][0]
        varname = variables[i][1]
        try:
            bindings["NORMAL_" + varname] = CASTING[vartype](line[i])
        except ValueError, e:
            raise ValueError("Cannot turn {0} into {1} for variable {2}".format(
                type(line[i]), vartype, varname))

def main():
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
    print parser(parse_string)

if __name__ == '__main__':
    main()
