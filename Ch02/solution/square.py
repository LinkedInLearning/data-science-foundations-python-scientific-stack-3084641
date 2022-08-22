# %%
import matplotlib.pyplot as plt

img = plt.imread('flower.png')
img = img.copy()  # make img writable
plt.imshow(img)
#%%
type(img)
# %%
img.shape

# %%
# Draw a blue square around the flower
# Top-left: 190x350
# Bottom-right: 680x850
# Line width: 5

# first dimension is rows (y)
tl_x, tl_y = 350, 190
br_x, br_y = 850, 680
width = 5

color = [0, 0, 0xFF] # blue

# Top line
img[tl_x:tl_x+width, tl_y:br_y] = color
# Bottom line
img[br_x:br_x+width, tl_y:br_y] = color
# Left line
img[tl_x:br_x, tl_y:tl_y+width] = color
# Right line
img[tl_x:br_x, br_y-width:br_y] = color

plt.imshow(img)