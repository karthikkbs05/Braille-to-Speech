import cv2
import numpy as np
#load data
a = 0
b = 0
c = 0
d = 0
e = 0
f = 0
# Load the image
img = cv2.imread("images\image.jpg")

#divide the page``1 
height, width = img.shape[:2]
partheight = height/3
partwidth = width/2

partwidth = int(partwidth)
partheight = int(partheight)

print(partheight)
print(partwidth)

# Convert the image to grayscale
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

# Apply thresholding to convert the image to binary
_, thresh = cv2.threshold(gray, 50, 255, cv2.THRESH_BINARY_INV + cv2.THRESH_OTSU)

# Apply HoughCircles method to detect circles
circles = cv2.HoughCircles(thresh, cv2.HOUGH_GRADIENT, 1, 20, param1=20, param2=20, minRadius=0, maxRadius=0)

# If circles are detected, draw them and output their positions
if circles is not None:
    circles = np.round(circles[0, :]).astype("int")
    for (x, y, r) in circles:
        cv2.circle(img, (x, y), r, (0, 255, 0), 2)
        print("Circle detected at position ({}, {})".format(x, y))
        if x < partwidth and y < partheight:
            if a == 0:
                a = 1
            else:
                a = 0    
            
        if x > partwidth and y < partheight and not b == 1:
            if b == 0:
                b = 1
            else:
                b = 0 

        if x < partwidth and y > partheight and y < 2*partheight and not c == 1:
            if c == 0:
                c = 1
            else:
                c = 0  

        if x > partwidth and y > partheight and y < 2*partheight and not d == 1:
            if d == 0:
                d = 1
            else:
                d = 0  

        if x < partwidth and y < 3*partheight and y > 2*partheight and not e == 1:
            if e == 0:
                e = 1
            else:
                e = 0 
        if x > partwidth and y < 3*partheight and y > 2*partheight and not f == 1:
            if f == 0:
                f = 1
            else:
                f = 0 
        # Limit to 6 circles at most
        if len(circles) == 6:
            break
else:
    print("No circles detected in the image.")

# Display the image with circles detected
cv2.imshow('Circles Detected', img)

finalbin = np.array([a,b,c,d,e,f])
print(finalbin)

B = (1,0,1,0,0,0)
M = (1,1,0,0,1,0)
S = (0,1,1,0,1,0)
C = (1,1,0,0,0,0)
E = (1,0,0,1,0,0)

if np.all(finalbin == B):
    print('b')
    text = "b"
elif np.all(finalbin == M):
    print('m')
    text = "m"
elif np.all(finalbin == S):
    print('s')
    text = "s"
elif np.all(finalbin == C):
    print('c')
    text = "c"        
elif np.all(finalbin == E):
    print('e')
    text = "e"
else:
    text = "sorry no text" 


cv2.waitKey(0)

