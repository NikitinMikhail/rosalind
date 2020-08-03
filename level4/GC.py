import common

fdict = common.fasta_parser('GC.txt')
gc_count = dict()
max_gc = 0
max_key = ''

for key in fdict.keys():
	gc_count[key] = round((fdict[key].count('G') + fdict[key].count('C'))*100 / len(fdict[key]), 6)
	if gc_count[key] > max_gc:
		max_gc = gc_count[key]
		max_key = key

print(max_key)
print(max_gc)
