#!/usr/bin/env python
# coding: utf-8

# In[1]:


import cv2
#img=cv2.imread("C:/Users/Akshaya/Documents/Anusha/Python Programs/08_Packages/07_OpenCV/computer.jpg",1)
img=cv2.imread("C:/Users/Akshaya/Documents/Anusha/Python Programs/08_Packages/07_OpenCV/computer.jpg",0)
print("The type of image is :", type(img))
print("The shape of image is :",img.shape)
print("The dimension of image is :", img.ndim)
print("The image contains:\n",img)
print(img[0][2])


# In[1]:


import cv2
img=cv2.imread("C:/Users/Akshaya/Documents/Anusha/Python Programs/08_Packages/07_OpenCV/computer.jpg",1)
cv2.imshow("Computer Image",img)
cv2.waitKey(0)
cv2.destroyAllWindows()
cv2.imwrite("Original Computer Image.jpg",img)


# In[1]:


import cv2
img=cv2.imread("C:/Users/Akshaya/Documents/Anusha/Python Programs/08_Packages/07_OpenCV/computer.jpg",0)
cv2.imshow("Computer Image",img)
cv2.waitKey(0)
cv2.destroyAllWindows()


# In[27]:


import cv2
img=cv2.imread("C:/Users/Akshaya/Documents/Anusha/Python Programs/08_Packages/07_OpenCV/computer.jpg",1)
resized_image=cv2.resize(img,(int(img.shape[1]*2),int(img.shape[0]*2)))
cv2.imshow("Computer Resized Image",resized_image)
cv2.waitKey(0)
cv2.destroyAllWindows()
cv2.imwrite("Computer Resized Image.jpg",resized_image)


# In[2]:


import numpy
import cv2
face_cascade=cv2.CascadeClassifier('C:/Users/Akshaya/Documents/Anusha/Python Programs/08_Packages/07_OpenCV/haarcascade_frontalface_default.xml')
img1=cv2.imread("C:/Users/Akshaya/Documents/Anusha/Python Programs/08_Packages/07_OpenCV/Facephoto.jpg")
cv2.imshow("Original Image",img1)
cv2.waitKey(0)
cv2.destroyAllWindows()
print(type(img1))
print(img1.shape)
print(img1.ndim)
print(img1)
gray_img = cv2.cvtColor(img1, cv2.COLOR_BGR2GRAY)
cv2.imshow("Gray Image",gray_img)
cv2.waitKey(0)
cv2.destroyAllWindows()
print(type(gray_img))
print(gray_img)
faces=face_cascade.detectMultiScale(gray_img,2,5)
print(type(faces))
print(faces)
for x,y,w,h in faces:
    img1=cv2.rectangle(img1,(x,y),(x+w,y+h),(0,255,0),3)
resized=cv2.resize(img1,(int(img1.shape[1]/2),int(img1.shape[0]/2)))
cv2.imshow("Face Detected",resized)
cv2.waitKey(0)
cv2.destroyAllWindows()


# In[5]:


import cv2
img2=cv2.imread("C:/Users/Akshaya/Documents/Anusha/Python Programs/08_Packages/07_OpenCV/computer.jpg")
print(type(img2))
print(img2.ndim)
print(img2.shape)


# In[ ]:





# In[ ]:




