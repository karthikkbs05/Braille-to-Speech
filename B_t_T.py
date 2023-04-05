import cv2
import numpy as np
from gtts import gTTS

# Load the image
img = cv2.imread("studysession\images\E.jpeg")

# Get the size of the image
height, width, _ = img.shape

# Calculate the size of each part
part_height = height // 3
part_width = width // 2

# Create 6 ROIs
roi1 = img[0:part_height, 0:part_width]
roi2 = img[0:part_height, part_width:2*part_width]
roi3 = img[part_height:2*part_height, 0:part_width]
roi4 = img[part_height:2*part_height, part_width:2*part_width]
roi5 = img[2*part_height:3*part_height, 0:part_width]
roi6 = img[2*part_height:3*part_height, part_width:2*part_width]

# Display each ROI
cv2.imshow("ROI1", roi1)
cv2.imshow("ROI2", roi2)
cv2.imshow("ROI3", roi3)
cv2.imshow("ROI4", roi4)
cv2.imshow("ROI5", roi5)
cv2.imshow("ROI6", roi6)


def detect_black_mark(img):
    # Convert the image to grayscale
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

    # Threshold the grayscale image
    _, thresholded = cv2.threshold(gray, 127, 255, cv2.THRESH_BINARY)

    # Find the location of the black mark
    rows, cols = np.where(thresholded == 0)

    # Check if a black mark was detected
    if rows.size == 0 and cols.size == 0:
        return 0
    else:
        return 1

# Detect the black mark in each image
output1 = detect_black_mark(roi1)
output2 = detect_black_mark(roi2)
output3 = detect_black_mark(roi3)
output4 = detect_black_mark(roi4)
output5 = detect_black_mark(roi5)
output6 = detect_black_mark(roi6)

# Print the results
print("Output for 1 of the image:", output1)
print("Output for 2 of the image:", output2)
print("Output for 3 of the image:", output3)
print("Output for 4 of the image:", output4)
print("Output for 5 of the image:", output5)
print("Output for 6 of the image:", output6)


finalbin = np.array([output1,output2,output3,output4,output5,output6])
print(finalbin)

# braille library
b = (1,0,1,0,0,0)
m = (1,1,0,0,1,0)
s = (0,1,1,0,1,0)
c = (1,1,0,0,0,0)
e = (1,0,0,1,0,0)

# print the interpreted text 
if np.all(finalbin == b):
    print('b')
    text = "b"
elif np.all(finalbin == m):
    print('m')
    text = "m"
elif np.all(finalbin == s):
    print('s')
    text = "s"
elif np.all(finalbin == c):
    print('c')
    text = "c"        
elif np.all(finalbin == e):
    print('e')
    text = "e"
else:
    text = "sorry no text"        

tts = gTTS(text=text, lang='en')
tts.save("outputAud.mp3")

cv2.waitKey(0)
cv2.destroyAllWindows()