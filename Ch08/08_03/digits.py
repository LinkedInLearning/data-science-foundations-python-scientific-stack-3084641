# %%
from sklearn.datasets import load_digits

digits = load_digits()

# %%
import matplotlib.pyplot as plt

idx = 37
plt.imshow(digits['images'][idx], cmap=plt.cm.gray)

# %%
digits['target'][idx]

# %%
digits['images'].shape, digits['data'].shape

# %%
from tensorflow.keras.utils import to_categorical

to_categorical([0, 1, 2, 0, 1])

# %%
X = digits['data']
y = to_categorical(digits['target'])

# %%
from sklearn.model_selection import train_test_split

X_train, X_test, y_train, y_test = \
    train_test_split(X, y, test_size=0.3)

# %%
from tensorflow.keras import Sequential
from tensorflow.keras.layers import Dense, Activation

in_dim = X.shape[1]
out_dim = y.shape[1]

model = Sequential()
model.add(Dense(128, input_shape=(in_dim,)))
model.add(Activation('relu'))
model.add(Dense(out_dim))
model.add(Activation('sigmoid'))
model.compile(
    loss='categorical_crossentropy',
    optimizer='adam',
    metrics=['accuracy'],
)

# %%
model.fit(X_train, y_train, epochs=10)

# %%
_, accuracy = model.evaluate(X_test, y_test)
accuracy

# %%
model.predict(X_test[:3])

# %%
model.predict(X_test[:3]).argmax(axis=1)

# %%
y_test[:3].argmax(axis=1)

# %%
model.save('digits.h5')
# %%
from tensorflow.keras.models import load_model

model1 = load_model('digits.h5')
model1.predict(X_test[:3]).argmax(axis=1)
