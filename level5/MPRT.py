import requests
import re

path = "http://www.uniprot.org/uniprot/"
with open("MPRT.txt", 'r') as inf:
	for line in inf:
		line = line.strip()
		r = requests.get(path+line+".fasta")
		a = ''.join((r.text.strip().split("\n"))[1:])
		pattern = r"(?=N[^P][ST][^P])"
		positions = [str(m.start() + 1) for m in re.finditer(pattern, a)]
		if len(positions) > 0:
			print(line)
			print(' '.join(positions))
