import common
import math
import itertools

input_number = int(common.one_line_reader('PERM.txt'))
total_perm = math.factorial(input_number)
num_list = list(range(1, input_number + 1))
iter_list = list(itertools.permutations(num_list))

with open('PERM_result.txt', 'w') as f:
    print(total_perm, file=f)
    for perm in iter_list:
        print(' '.join(map(str, [item for item in perm])), file=f)
