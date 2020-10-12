import common

input_lines = common.multi_line_reader('SETO.txt')
A, B, complete_set = eval(input_lines[1]), eval(input_lines[2]), set(range(1, int(input_lines[0]) + 1))
print('\n'.join(map(str, [A | B, A & B, A - B, B - A, complete_set - A, complete_set - B])))
