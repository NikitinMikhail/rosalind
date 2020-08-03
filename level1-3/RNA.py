strand = open('RNA.txt', 'r').readlines()[0].strip()

tr_strand = strand.replace('T', 'U')

print(tr_strand)
