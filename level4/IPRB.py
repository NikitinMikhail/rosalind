line = open('IPRB.txt', 'r').readline().strip()

dom, het, rec = [int(i) for i in line.split()]

total_comb = (dom + het + rec)*(dom + het + rec - 1)
dom_comb = dom * (dom + het + rec - 1) + het * (dom + 0.75 * (het - 1) + 0.5 * rec) + rec * (dom + 0.5 * het)

prob = dom_comb / total_comb

print(prob)
