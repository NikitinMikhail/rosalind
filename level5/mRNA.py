import common
read_line = open('mRNA.txt', 'r').readline().strip()
cod_dict = common.codon_dict()

amino_list = [cod_dict[key] for key in cod_dict.keys()]
variances = 1
for letter in read_line:
    variances = variances % 1e6
    variances *= amino_list.count(letter)

variances *= amino_list.count('Stop')
print(int(variances % 1e6))
