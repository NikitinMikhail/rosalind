import itertools
import common
import numpy as np

input_number = int(common.one_line_reader('SIGN.txt'))
num_list = list(range(1, input_number + 1))
iter_list = list(itertools.permutations(num_list))
sign_list = list(itertools.product((-1, 1), repeat=input_number))
signed_perm_list = list()

for num in iter_list:
    for sign in sign_list:
        signed_perm_list.append(tuple(np.multiply(num, sign)))

with open('SIGN_result.txt', 'w') as f:
    print(len(signed_perm_list), file=f)
    for perm in signed_perm_list:
        print(' '.join(map(str, [item for item in perm])), file=f)

