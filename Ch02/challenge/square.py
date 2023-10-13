# %%
import matplotlib.pyplot as plt

img = plt.imread('flower.png')
new_img = img.copy()  # make img writable
plt.imshow(new_img)

# %%
type(new_img)

# %%
new_img.shape

# %%
# Draw a blue square around the flower
# Top-left: 190x350
# Bottom-right: 680x850
# Line width: 5

# %%
# Creating a test image
test_img = img.copy()
plt.imshow(test_img)

# %%
# Experimenting with setting the entire array equal to various colors
test_img[:] = (0,0,255)
plt.imshow(test_img)

# %%
attempt_one = img.copy()
plt.imshow(attempt_one)

# %%
width = 1
axis = 349
while width < 5:
    attempt_one[axis, 189:679] = (0,0,255)
    axis += 1
    width += 1
  
plt.imshow(attempt_one)

# %%
width = 1
axis = 849
while width < 5:
    attempt_one[axis, 189:679] = (0,0,255)
    axis -= 1
    width += 1

plt.imshow(attempt_one)

# %%
width = 1
axis = 189
while width < 5:
    attempt_one[349:849, axis] = (0,0,255)
    axis += 1
    width += 1

plt.imshow(attempt_one)
# %%
width = 1
axis = 679
while width < 5:
    attempt_one[349:849, axis] = (0,0,255)
    axis -= 1
    width += 1

plt.imshow(attempt_one)
# %%
