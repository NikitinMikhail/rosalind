import re

strand_lines = open('SUBS.txt', 'r').readlines()

strand1 = strand_lines[0].strip()
strand2 = strand_lines[1].strip()

positions = [str(m.start() + 1) for m in re.finditer('(?={})'.format(strand2), strand1)]

print(' '.join(positions))

