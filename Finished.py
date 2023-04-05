import cv2
import numpy as np
import pyttsx3

# Create a VideoCapture object to capture video from the default camera
cap = cv2.VideoCapture(0)

# Check if camera opened 
if not cap.isOpened():
    print("Error opening video stream or file")

# Get camera frame dimensions
width = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
height = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))

# Calculate A4 size box dimensions
box_width = int(0.7 * height)
box_height = int(1.3 * box_width)
box_x = int((width - box_width) / 2)
box_y = int((height - box_height) / 2)
box_top_left = (box_x, box_y)
box_bottom_right = (box_x + box_width, box_y + box_height)

# Loop through frames 
while cap.isOpened():
    # Read frame from camera
    ret, frame = cap.read()

    if ret:
        # Draw the A4 size box on the frame
        cv2.rectangle(frame, box_top_left, box_bottom_right, (0, 255, 0), 2)

        # Display the resulting frame
        cv2.imshow('Camera', frame)
        
        if cv2.waitKey(1) & 0xFF == ord(' '):
            # Crop the captured image to the size of the green box
            roi = frame[box_y:box_y + box_height, box_x:box_x + box_width]
            # Save the ROI 
            cv2.imwrite("C:/Users/ybang/OneDrive/Desktop/object detect/images/image.jpg", roi)
            break
        # Press 'q' to quit
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break
    else:
        break

# Release the VideoCapture object and close all windows
cap.release()
cv2.destroyAllWindows()

#load data
a = 0
b = 0
c = 0
d = 0
e = 0
f = 0

# Load the image
img = cv2.imread("images\image.jpg")

#divide pages into 2x3 matrix
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
A = (1,0,0,0,0,0)
D = (1,1,0,1,0,0)
F = (1,1,1,0,0,0)
G = (1,1,1,1,0,0)
H = (1,0,1,1,0,0)
I = (0,1,1,0,0,0)
J = (0,1,1,1,0,0)
K = (1,0,0,0,1,0)
L = (1,0,1,0,1,0)
N = (1,1,0,1,1,0)
O = (1,0,0,1,1,0)
P = (1,1,1,0,1,0)
Q = (1,1,1,1,1,0)
R = (1,0,1,1,1,0)
T = (0,1,1,1,1,0)
U = (1,0,0,0,1,1)
V = (1,0,1,0,1,1)
W = (0,1,1,1,0,1)
X = (1,1,0,0,1,1)
Y = (1,1,0,1,1,1)
Z = (1,0,0,1,1,1)

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


# Initialize the TTS engine
engine = pyttsx3.init()

# Set the TTS engine properties
engine.setProperty('rate', 150)
engine.setProperty('volume', 0.5)
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id)

engine.say(text)
engine.save_to_file(text, 'output.mp3')


# Run the TTS engine
engine.runAndWait()

cv2.waitKey(0)