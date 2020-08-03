strand = open('REVC.txt', 'r').readlines()[0].strip()
comp_dict = {'A':'T', 'T':'A', 'G':'C', 'C':'G'}

rev_strand = strand[::-1]
rev_comp_strand = ''
for item in rev_strand:
	rev_comp_strand += comp_dict[item]

print(rev_comp_strand)
