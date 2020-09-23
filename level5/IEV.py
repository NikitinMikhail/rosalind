import numpy
read_list = open('IEV.TXT', 'r').readline().strip().split()

parents_number = [int(item) for item in read_list]
dom_ratio = [1, 1, 1, 0.75, 0.5, 0]
expected_dom = 2 * numpy.dot(parents_number, dom_ratio)
print(expected_dom)
