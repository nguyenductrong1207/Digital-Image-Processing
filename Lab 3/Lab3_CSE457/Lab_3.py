#!/usr/bin/env python
# coding: utf-8

# In[2]:


import cv2
import matplotlib.pyplot as plt
import numpy as np


# In[19]:


image = cv2.imread('0001.jpeg',1)
window_name = 'img'
cv2.imshow(window_name,image)
cv2.waitKey(0)
cv2.destroyAllWindows()


# In[4]:


cropped_image = image[80:280,150:330]
cv2.imshow(window_name,cropped_image)
cv2.waitKey(0)
cv2.destroyAllWindows()


# In[5]:


resize_image = cv2.resize(image, [500,500])
cv2.imshow(window_name,resize_image)
cv2.waitKey(0)
cv2.destroyAllWindows()


# In[5]:


resize_image = cv2.resize(image, [500,500], interpolation=cv2.INTER_NEAREST)
cv2.imshow(window_name,resize_image)
cv2.waitKey(0)
cv2.destroyAllWindows()


# In[9]:


resize_image = cv2.resize(image, [500,500], interpolation=cv2.INTER_LINEAR)
cv2.imshow(window_name,resize_image)
cv2.waitKey(0)
cv2.destroyAllWindows()


# In[8]:


resize_image = cv2.resize(image, [500,500], interpolation=cv2.INTER_CUBIC)
cv2.imshow(window_name,resize_image)
cv2.waitKey(0)
cv2.destroyAllWindows()


# In[10]:


rotate_image = cv2.rotate(image, rotateCode=cv2.ROTATE_90_CLOCKWISE)
cv2.imshow(window_name,rotate_image)
cv2.waitKey(0)
cv2.destroyAllWindows()


# In[11]:


rotate_image = cv2.rotate(image, rotateCode=cv2.ROTATE_180)
cv2.imshow(window_name,rotate_image)
cv2.waitKey(0)
cv2.destroyAllWindows()


# In[12]:


rotate_image = cv2.rotate(image, rotateCode=cv2.ROTATE_90_COUNTERCLOCKWISE)
cv2.imshow(window_name,rotate_image)
cv2.waitKey(0)
cv2.destroyAllWindows()


# In[20]:


cricle_image = cv2.circle(image, [150,150],100,(255,255,255),2)
cv2.imshow(window_name,cricle_image)
cv2.waitKey(0)
cv2.destroyAllWindows()


# In[21]:


rectangle_image = cv2.rectangle(image,[45,65],[200,150],(0,0,0),5)
cv2.imshow(window_name,rectangle_image)
cv2.waitKey(0)
cv2.destroyAllWindows()


# In[22]:


font = cv2.FONT_HERSHEY_SIMPLEX
text_image = cv2.putText(image,'FLOWER',[50,50],font,2,(255,255,203),2)
cv2.imshow(window_name,text_image)
cv2.waitKey(0)
cv2.destroyAllWindows()


# In[ ]:




