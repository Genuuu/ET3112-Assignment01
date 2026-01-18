import cv2 as cv
import numpy as np
import matplotlib.pyplot as plt

f = cv.imread('Images/runway.png', cv.IMREAD_GRAYSCALE)
assert f is not None

gamma = [0.5, 2]
for g in gamma:
    table = np.array([((i/255)** g) * 255 for i in np.arange(0, 256)]).astype('uint8')

    h = cv.LUT(f, table)

    cv.imshow('Original',f)
    cv.imshow('Gamma Corrected: {gamma}', h)
    cv.waitKey(0)

cv.destroyAllWindows()

