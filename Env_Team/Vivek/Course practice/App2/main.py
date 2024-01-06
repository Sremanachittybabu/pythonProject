import cv2

first_frame = None

vid = cv2.VideoCapture(0)

# Check if the webcam is opened successfully
if not vid.isOpened():
    print("Error: Couldn't open the webcam.")
    exit()

while True:
    # Read a frame from the webcam
    ret, frame = vid.read()
    gray = cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
    gray = cv2.GaussianBlur(gray,(21,21),0)

    if first_frame is None:
        first_frame = gray
        continue

    delta_frame = cv2.absdiff(first_frame,gray)

    # Check if the frame is read successfully
    if not ret:
        print("Error: Couldn't read a frame.")
        break

    # Display the frame
    cv2.imshow('Gray Frame', gray)
    cv2.imshow('delta frame',delta_frame)

    # Wait for a key press. If 'q' is pressed, break from the loop
    if cv2.waitKey(1) == ord('q'):
        break

# Release the webcam and close the OpenCV window
vid.release()
cv2.destroyAllWindows()