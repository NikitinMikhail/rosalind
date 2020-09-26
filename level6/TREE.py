import common

#Just using the fact that N(edges) = N(nodes) - 1

lines = common.multi_line_reader('TREE.txt')
nodes_num = int(lines[0])
print(nodes_num - len(lines))