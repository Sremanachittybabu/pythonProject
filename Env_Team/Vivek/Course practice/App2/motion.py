import cv2
import numpy as np

# Open the webcam
cap = cv2.VideoCapture(0)

# Check if the webcam is opened successfully
if not cap.isOpened():
    print("Error: Couldn't open the webcam.")
    exit()

# Read the first frame
ret, frame1 = cap.read()

# Convert the frame to grayscale
gray1 = cv2.cvtColor(frame1, cv2.COLOR_BGR2GRAY)

while True:
    # Read the next frame
    ret, frame2 = cap.read()

    # Convert the frame to grayscale
    gray2 = cv2.cvtColor(frame2, cv2.COLOR_BGR2GRAY)

    # Calculate the absolute difference between the two frames
    diff = cv2.absdiff(gray1, gray2)

    # Apply a threshold to highlight the regions with significant changes
    _, threshold = cv2.threshold(diff, 30, 255, cv2.THRESH_BINARY)

    # Find contours in the thresholded image
    contours, _ = cv2.findContours(threshold, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

    # Draw rectangles around the detected motion
    for contour in contours:
        if cv2.contourArea(contour) > 1000:
            x, y, w, h = cv2.boundingRect(contour)
            cv2.rectangle(frame2, (x, y), (x + w, y + h), (0, 255, 0), 2)

    # Display the original frame with motion detection
    cv2.imshow('Motion Detector', frame2)

    # Update the previous frame
    gray1 = gray2.copy()

    # Break the loop if 'q' key is pressed
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Release the webcam and close the OpenCV window
cap.release()
cv2.destroyAllWindows()
