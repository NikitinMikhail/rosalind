import common

protein = common.one_line_reader('PRTM.txt')
sum_mass = sum(common.get_protein_mass(letter) for letter in protein)
print(round(sum_mass, 3))