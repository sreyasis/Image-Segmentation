import numpy as np
import cv2 
from matplotlib import pyplot as plt

#original image
img=cv2.imread("binary.png",0)

#kernal
kernel = np.ones((5,5),np.uint8)


#erosion
erosion = cv2.erode(img,kernel,iterations = 4)


#dilation
dilation = cv2.dilate(img,kernel,iterations = 4)


#opening
opening = cv2.morphologyEx(img, cv2.MORPH_OPEN, kernel)


#closing
closing = cv2.morphologyEx(img, cv2.MORPH_CLOSE, kernel)



plt.subplot(321),plt.imshow(img, 'gray')
plt.title('Input Image'), plt.xticks([]), plt.yticks([])
plt.subplot(322),plt.imshow(kernel, 'gray')
plt.title("Kernel"), plt.xticks([]), plt.yticks([])

plt.subplot(323),plt.imshow(erosion, 'gray')
plt.title("erosion"), plt.xticks([]), plt.yticks([])
plt.subplot(324),plt.imshow(dilation, 'gray')
plt.title("Dilation"), plt.xticks([]), plt.yticks([])

plt.subplot(325),plt.imshow(opening, 'gray')
plt.title("opening"), plt.xticks([]), plt.yticks([])
plt.subplot(326),plt.imshow(closing, 'gray')
plt.title("closing"), plt.xticks([]), plt.yticks([])

plt.tight_layout()
plt.show()
cv2.waitKey(0)
cv2.destroyAllWindows()

