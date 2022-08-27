# %%
from sklearn.datasets import fetch_california_housing

cal_housing = fetch_california_housing()

# %%
type(cal_housing)

# %%
cal_housing.keys()

# %%
type(cal_housing['data'])

# %%
cal_housing['feature_names']

# %%
print(cal_housing['DESCR'])

# %%
cal_housing['target'][:10]

# %%
from sklearn.ensemble import RandomForestRegressor

X, y = cal_housing['data'], cal_housing['target']

clf = RandomForestRegressor()
clf.fit(X, y)  # train

# %%
clf.score(X, y)

# %%
clf.score?

# %%
dir(clf)

# %%
clf.n_features_in_

# %%
X.shape

# %%
from sklearn.tree import export_graphviz

export_graphviz(
    clf.estimators_[0], 
    'tree.dot',
    feature_names=cal_housing['feature_names'],
    max_depth=5,
)
# %%
!dot -Tsvg -o tree.svg tree.dot

# %%
from IPython import display

display.SVG('tree.svg')

# %%
i = 17
row = X[i]
clf.predict(row)

# %%
row.shape

#%%

row = X[i:i+1]
row.shape

# %%
clf.predict(row)

# %%
y[i]