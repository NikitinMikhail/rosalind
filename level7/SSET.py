import common


def f(n):
    fact = 1
    for i in range(1, n + 1):
        fact *= i
    return fact


def c(n, k):
    return (f(n) // f(n - k) // f(k))


if __name__ == '__main__':
    n_max = int(common.one_line_reader('SSET.txt'))
    subset_list = [c(n_max, k) for k in range(n_max)]
    subset_num = 1  # empty set is a subset too
    for item in subset_list:
        subset_num += item

    print(int(subset_num % 1e6))
