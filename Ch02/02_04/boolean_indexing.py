# %%
import numpy as np

arr = np.arange(3)
arr

# %%
arr[[True, False, True]]

# %%
arr >= 1

# %%
arr[arr >= 1]

# %%
arr = np.arange(10)

arr[(arr>2) & (arr<7)]

# %%
arr[(arr>7) | (arr<2)]

# %%
arr[~(arr>7)]

# %%
values = np.random.normal(0, 10, 1_000)
values[33] = 1038
values[832] = -3423

# %%
mask = np.abs(values - values.mean()) > (2 * values.std())
values[mask]

# %%
values[mask] = values.mean()