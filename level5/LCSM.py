import common

def long_substr(data):
	substr = ''
	if len(data) > 1 and len(data[0]) > 0:
		for i in range(len(data[0])):
			for j in range(len(data[0])-i+1):
				if j > len(substr) and all(data[0][i:i+j] in x for x in data):
					substr = data[0][i:i+j]
	return substr

fasta_dict = common.fasta_parser('LCSM.txt')
data = [fasta_dict[key] for key in fasta_dict.keys()]

print(long_substr(data))
