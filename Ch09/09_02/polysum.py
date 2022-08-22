# %%
def polyn(n):
    total = 0
    for _ in range(n):
        total += (7*n*n) + (-3*n) + 42
    return total

%timeit -n 10_000 polyn(1000)

# %%
import numba

@numba.jit
def polyn_jit(n):
    total = 0
    for _ in range(n):
        total += (7*n*n) + (-3*n) + 42
    return total

%timeit -n 10_000 polyn_jit(1000)
