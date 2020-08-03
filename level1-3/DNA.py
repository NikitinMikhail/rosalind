strand = open('DNA.txt', 'r').readlines()[0].strip()

print('{} {} {} {}'.format(strand.count('A'), strand.count('C'), strand.count('G'), strand.count('T')))
