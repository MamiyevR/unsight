# import cv2
# import numpy as np

# img = cv2.imread("image.png")
# blurred_img = cv2.GaussianBlur(img, (21, 21), 0)

# mask = np.zeros((4000,2666,3), dtype=np.uint8)
# mask = cv2.(mask, (255, 255), 100, (255, 255, 255), -1)

# out = np.where(mask == (255, 255, 255), img, blurred_img)

# cv2.imwrite("./out.png", out)

import cv2

# Read in image
image = cv2.imread('image.png')

# Create ROI coordinates
topLeft = (600, 1340)
bottomRight = (2000, 3500)
x, y = topLeft[0], topLeft[1]
w, h = bottomRight[0] - topLeft[0], bottomRight[1] - topLeft[1]

# Grab ROI with Numpy slicing and blur
ROI = image[y:y+h, x:x+w]
blur = cv2.blur(ROI, (100, 100), 0)

# Insert ROI back into image
image[y:y+h, x:x+w] = blur

cv2.imshow('blur', blur)
cv2.imshow('image', image)
cv2.waitKey()
