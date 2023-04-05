import cv2
import pytesseract
import pyttsx3

cap = cv2.VideoCapture(0)

# Check if camera opened successfully
if not cap.isOpened():
    print("Error opening video stream or file")
while cap.isOpened():
    # Read frame from camera
    ret, frame = cap.read()

    if ret:
        # Display the resulting frame
        cv2.imshow('Camera', frame)
        
        if cv2.waitKey(1) & 0xFF == ord(' '):

            cv2.imwrite("C:/Users/ybang/OneDrive/Desktop/object detect/images/image.jpg", frame)
            break
        # Press 'q' to quit
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break
    else:
        break

# Release the VideoCapture object and close all windows
cap.release()
cv2.destroyAllWindows()

img = cv2.imread('images/text2.png')
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
text = pytesseract.image_to_string(gray)
engine = pyttsx3.init()
engine.save_to_file(text, 'output.mp3')
engine.runAndWait()

