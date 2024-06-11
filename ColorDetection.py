from sklearn.cluster import KMeans
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.image as mpimg

image = mpimg.imread('/Users/skosovan/Documents/dress2_wb.jpeg')
w, h, d = tuple(image.shape)
pixel = np.reshape(image, (w * h, d))
n_colors = 5
model = KMeans(n_clusters=n_colors, random_state=42).fit(pixel)
colour_palette = np.uint8(model.cluster_centers_)
plt.imshow([colour_palette])
plt.show()
