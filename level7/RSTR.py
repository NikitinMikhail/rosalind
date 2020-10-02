import common
import numpy

input_lines = common.multi_line_reader('RSTR.txt')
number, gc_cont = int(input_lines[0].split()[0]), float(input_lines[0].split()[1])
sequence = input_lines[1]
prob_single_letter = [gc_cont / 2 if letter in ['G', 'C'] else (1 - gc_cont) / 2 for letter in sequence]
prob_single_sequence = numpy.prod(prob_single_letter)
prob_multiple_sequence = 1 - (1 - prob_single_sequence)**number
print(round(prob_multiple_sequence, 3))