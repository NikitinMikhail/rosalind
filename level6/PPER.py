import common

def part_perm_number(all, choose):
    perm_num = 1
    for i in range(all - choose + 1, all + 1):
        perm_num = perm_num * i
    return perm_num

all_items, choose_items = map(int, common.one_line_reader('PPER.txt').split())
print(int(part_perm_number(all_items, choose_items) % 1e6))