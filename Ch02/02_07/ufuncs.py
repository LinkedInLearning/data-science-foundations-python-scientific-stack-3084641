# %%
import numpy as np
len(dir(np))

# %%
np.sin(90)
# %%
v = np.arange(-3, 3)
np.sin(v)

# %%
def relu(n):
    if n < 0:
        return 0.0
    return n

relu(-2)

# %%
relu(v)
# %%

@np.vectorize
def relu(n):
    if n < 0:
        return 0.0
    return n

relu(v)
# %%
relu(-2)

# %%
relu(-2) - 7

# %%
nv = np.array([-1.0, np.nan, 1.0])
np.sin(nv)