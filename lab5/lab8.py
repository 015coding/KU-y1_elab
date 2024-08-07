def modulo(n, m):
    num_mod = []
    for i in range(n):
        num = int(input(f"Input number {i+1}: "))
        mods = num % m
        a = num_mod.append(mods)
    set_a = set(num_mod)
    return len(set_a)

n = int(input("N: "))
m = int(input("M: "))
print(modulo(n, m))
