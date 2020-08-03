strand = open('FIB.txt', 'r').readlines()[0].strip()

def fibb(months, newborn, start_mature, start_young):
	nyoung = start_young
	nmature = start_mature
	for i in range(months - 1):
		new_young = nmature * newborn
		new_mature = nyoung
		nyoung = new_young
		nmature += new_mature

	return(nyoung + nmature)

months, newborn = [int(i) for i in strand.split()]

print(months, newborn)
print(fibb(months, newborn, 0, 1))
