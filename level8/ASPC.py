import common
from common import combinations as C

n, m = map(int, common.one_line_reader('ASPC.txt').split())
print(common.modulo(sum([common.modulo(C(n,i), int(1e6)) for i in range(m, n + 1)]), int(1e6)))
