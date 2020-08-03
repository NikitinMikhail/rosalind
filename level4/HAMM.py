import re

strand_lines = open('HAMM.txt', 'r').readlines()

strand1 = strand_lines[0].strip()
strand2 = strand_lines[1].strip()
mismatches = 0
counter = 0

for letter in strand1:
	if letter != strand2[counter]:
		mismatches += 1
	counter += 1

#print(strand1)
#print(strand2)
print(mismatches)
