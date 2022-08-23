# %%
import matplotlib.pyplot as plt
import numpy as np

xs = np.linspace(-6, 6, 100)
ys = np.sinc(xs)
plt.plot(xs, ys)

# %%
plt.style.available

# %%
plt.style.use('seaborn-whitegrid')
plt.plot(xs, ys)

# %%
plt.style.use('fivethirtyeight')
plt.plot(xs, ys)