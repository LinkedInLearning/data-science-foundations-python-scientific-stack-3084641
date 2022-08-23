# %%
from sklearn.datasets import load_digits

digits = load_digits()
X, y = digits['data'], digits['target']

# %%
import matplotlib.pyplot as plt

i = 353
print(y[i])
img = digits['images'][i]
plt.imshow(img, cmap='gray')

# %%
img.shape

# %%
X.shape

# %%

"""
Write a pipeline that will learn to predict digits.
It should reduce the number of features to 10 and use a KNeighborsClassifier.

Split the data to train and test, and answer:
- What is the score of the pipeline on the test data?
- What is the size (in kb) of the serialized pipeline?
"""