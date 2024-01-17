import cv2
import time
import KeyPressModule as kp

# Create a VideoCapture object to access the camera (0 represents the default camera)
cap = cv2.VideoCapture(0)

# Variables for resizing
dim = (360, 240)

kp.init()

def getKeyboardInput():
    if kp.getKey("z"):
        filename = f'{time.time()}.jpg'
        cv2.imwrite(filename, resized_img)
        print(f"Frame saved as {filename}")
        time.sleep(0.3)


# Continuously capture frames from the camera until 'q' is pressed
while True:

    getKeyboardInput()

    # Read a img from the camera
    ret, img = cap.read()

    # Resize the img
    resized_img = cv2.resize(img, dim)

    # Display the resized img
    cv2.imshow('Camera', resized_img)

    # Wait for 'q' key to be pressed to exit
    if cv2.waitKey(1) == ord('q'):
        break

# Release the VideoCapture object and close any open windows
cap.release()
cv2.destroyAllWindows()
