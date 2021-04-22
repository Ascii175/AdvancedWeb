def make_rug(m, n, *s):
    if s:
        return [''.join(s * n) for _ in range(m)]
    else:
        return ['#' * n for _ in range(m)]

# m = int(input("m : "))
# n = int(input("n : "))
# s = input("s : ")
m = 3
n = 2
s = 'A'
print(make_rug(m, n, *s))
