from math import factorial as f

line = open('LIA.txt', 'r').readline().strip()

generation, organisms_amount  = [int(i) for i in line.split()]
print(organisms_amount, generation)

def c(n, k):
    return f(n) // f(n - k) // f(k)

def belong_to_generation(k, n):
    total = 2 ** k
    return 1 - sum([c(total, i) * (1 / 4) ** i * (3 / 4) ** (total - i) for i in range(0, n)])

print(belong_to_generation(generation, organisms_amount))
