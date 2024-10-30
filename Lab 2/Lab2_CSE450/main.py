import cv2
import matplotlib.pyplot as plt
import numpy as np

# image = cv2.imread('pic.jpg',0)
# window_name = 'img'
# cv2.imshow(window_name,image)
# cv2.waitKey(0)
# cv2.destroyAllWindows()

# histogram = cv2.calcHist([image],[0],None,[256],[0,256])
# plt.plot(histogram, color='k')
# plt.show()

img = cv2.imread('pic.jpg')
for i,col in enumerate(['b','g','r']):
    hist = cv2.calcHist([img],[i],None,[256],[0,256])
    plt.plot(hist, color=col)
    plt.xlim([0,256])
    plt.show()