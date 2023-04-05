import cv2
import numpy as np

# Load the image
image = cv2.imread("studysession\images\word1.png")

# Converting color image to grayscale image
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

if gray is None:
    print("Error: Could not load image")
    exit()

#image = cv2.imread('brr.jpg', cv2.IMREAD_GRAYSCALE)

_, thresh = cv2.threshold(gray, 127, 255, cv2.THRESH_BINARY_INV)

# Find the contours in the image
contours, _ = cv2.findContours(thresh, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)


contour_image = thresh.copy()
contour_image = cv2.cvtColor(contour_image, cv2.COLOR_GRAY2BGR)
cv2.drawContours(contour_image, contours, -1, (0, 255, 0), 1)

cv2.imshow("Contours", contour_image)
cv2.waitKey(0)
cv2.destroyAllWindows()


#Create an empty string to store the result
result = ""


patterns = ["100000", "110000", "100100", "100010", "110100", "110010", "010100", "010010", "101000", "011000", "001000", "101100", "101010", "101001", "011010", "011001"]

#Loop through all the contours in the image
for contour in contours:

  #Get the bounding rectangle around the contour
  x, y, w, h = cv2.boundingRect(contour) #mask to extract only the contour
  mask = np.zeros(thresh.shape, np.uint8)
  cv2.drawContours(mask, [contour], 0, 255, -1)
#Extract the contour using the mask
  dot = cv2.bitwise_and(thresh, thresh, mask=mask)
#Resize the contour to a standard size
  dot = cv2.resize(dot, (10, 10))

  #Flatten the array into a 1D array
  dot = dot.reshape(-1)

     #Convert the array to a string
  dot = "".join(str(x) for x in dot)

        #Find the index of the pattern in the list
  index = patterns.index(dot)

  #Add the corresponding character to the result string
  result += chr(index + 65)

# text file
with open("result.txt", "w") as f:
  f.write(result)


