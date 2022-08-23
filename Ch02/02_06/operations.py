# %%
import numpy as np

v = np.array([
    [0, 1, 2],
    [3, 4, 5],
    [6, 7, 8],
])
v

# %%
v.T
# %%
v.any()

# %%
v.all()

# %%
if v:
    print('ok')
# %%
v.prod()

# %%
v.sum(axis=1)

# %%
v.sum(axis=0)

# %%
v1 = v.copy()
v1[0,0] = -1
v