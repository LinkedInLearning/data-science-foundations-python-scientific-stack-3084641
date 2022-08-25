# %%
from sklearn.datasets import fetch_california_housing

cal_housing = fetch_california_housing()
X, y = cal_housing['data'], cal_housing['target']
X.shape

# %%
from sklearn.model_selection import train_test_split

X_train, X_test, y_train, y_test = train_test_split(
    X, y,
    test_size=0.3,
)
X_train.shape

# %%
from sklearn.ensemble import RandomForestRegressor

clf = RandomForestRegressor()
clf.fit(X_train, y_train)
clf.score(X_test, y_test)