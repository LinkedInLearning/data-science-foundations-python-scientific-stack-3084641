# %%
nums = [1, 2, 3, 4, 5]
nums[2:4]

# %%
import numpy as np

v = np.arange(1, 6)
v[2:4]

# %%
arr = np.arange(12).reshape(3, 4)
arr

# %%
arr[0]

# %%
arr[1][1]

# %%
arr[1, 1]
# %%
arr[:, 1]

# %%
arr[:, 1].reshape((3, 1))

# %%
arr[1:, 2:]

# %%
arr[1:, 2:] = 7
arr

# %%
