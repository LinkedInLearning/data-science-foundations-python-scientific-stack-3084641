# %%
from sklearn.datasets import fetch_california_housing
from sklearn.decomposition import PCA
from sklearn.model_selection import train_test_split
from sklearn.pipeline import Pipeline
from sklearn.preprocessing import StandardScaler
from sklearn.svm import SVR

cal_housing = fetch_california_housing()

X, y = cal_housing['data'], cal_housing['target']
X_train, X_test, y_train, y_test = train_test_split(
    X, y,
    test_size=0.3,
)

pipe = Pipeline([
    ('scale', StandardScaler()),
    ('pca', PCA(n_components=4)),
    ('svr', SVR()),
])

pipe.fit(X_train, y_train)
pipe.score(X_test, y_test)

# %%
import pickle

out_file = 'model.pkl'

with open(out_file, 'wb') as out:
    pickle.dump(pipe, out)

# %%
with open(out_file, 'rb') as fp:
    pipe1 = pickle.load(fp)
pipe1.score(X_test, y_test)