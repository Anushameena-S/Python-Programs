#!/usr/bin/env python
# coding: utf-8

# In[2]:


import cv2,time
video=cv2.VideoCapture(0)
time.sleep(3)
video.release()


# In[5]:


import cv2,time
video1=cv2.VideoCapture(0)
check,frame=video1.read()
print(check)
print(frame)
print(frame.ndim)
print(frame.shape)
time.sleep(3)
video.release()


# In[11]:


import cv2,time
video3=cv2.VideoCapture(0)
check,frame=video3.read()
time.sleep(3)
cv2.imshow('Capturing frame',frame)
cv2.waitKey(0)
video3.release()
cv2.destroyAllWindows()


# In[12]:


import cv2,time
video4=cv2.VideoCapture(0)
while True:
    check,frame=video4.read()
    gray=cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
    cv2.imshow('Capturing gray frame',gray)
    key=cv2.waitKey(1)
    if key==ord('q'):
        break
video4.release()
cv2.destroyAllWindows()


# In[6]:


import cv2,time
first_frame=None
video5=cv2.VideoCapture(0)
while True:
    check,frame=video5.read()
    gray1=cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
    gray1=cv2.GaussianBlur(gray1,(21,21),0)
    if first_frame is None:
        first_frame=gray1
        continue
    delta_frame=cv2.absdiff(first_frame,gray1)
    thresh_delta=cv2.threshold(delta_frame,30,255,cv2.THRESH_BINARY)[1]
    thresh_delta=cv2.dilate(thresh_delta,None,iterations=0)
    (cnts, _)=cv2.findContours(thresh_delta.copy(), cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
    for contour in cnts:
            if cv2.contourArea(contour)<3000:
                continue
            (x,y,w,h)=cv2.boundingRect(contour)
            cv2.rectangle(frame,(x,y),(x+w, y+h),(0,255,0),3)
    cv2.imshow('Original Frame',frame)
    cv2.imshow('Capturing gray frame....', gray1)
    cv2.imshow('Delta Frame....',delta_frame)
    cv2.imshow('Threshhold frame', thresh_delta)
    key=cv2.waitKey(1)
    if key==ord('q'):
        break
video5.release()
cv2.destroyAllWindows()


# In[ ]:





# In[ ]:





# In[ ]:




