# %%
from sklearn.datasets import load_iris

iris = load_iris(as_frame=True)
df = iris['data'].head(5)
df

# %%
df.style.highlight_max()

# %%
df.style.background_gradient()

# %%
df.style.bar()

# %%
def color_round(val):
    if round(val) == val:
        return 'color: blue'
    return None

df.style.applymap(color_round)


# %%
def color_odd(val):
    if int(val) % 2 == 1:
        return 'background-color: orange'
    return ''

df.style.applymap(color_round).applymap(color_odd)

# %%
df.style.applymap(
    color_odd,
    subset=df.columns[:2],
)

# %%
def top50(col):
    is_top50 = col >= col.median()
    return [
        'font-weight: bold' if v else ''
        for v in is_top50
    ]

df.style.apply(top50) 
