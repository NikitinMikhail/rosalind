import common
'''
exterbal_nodes = n(leaves) (it's unrooted)
all_edges = (external + 3*internal) / 2
all_nodes = external + internal
all_edges = all_nodes - 1
'''
leaves_num = int(common.one_line_reader('INOD.txt'))
external_nodes = leaves_num
internal_nodes = external_nodes - 2
print(internal_nodes)