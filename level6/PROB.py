import common
import numpy as np

strand, gc_cont = common.multi_line_reader('PROB.txt')
gc_cont_list = list(map(float, gc_cont.split()))
prob_list = []
for gc_cont in gc_cont_list:
    prob = [gc_cont / 2 if letter in ['G', 'C'] else (1 - gc_cont) / 2 for letter in strand]
    prob_list.append(str(round(np.log10(np.prod(prob)), 3)))

print(' '.join(prob_list))
