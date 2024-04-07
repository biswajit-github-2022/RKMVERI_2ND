import cv2
import numpy as np

# Initialize video capture object
cap = cv2.VideoCapture('/home/biswajitrana/Videos/Untitled.mp4')  # Replace 'your_video.mp4' with the path to your video file

# Get video frame width and height
frame_width = int(cap.get(3))
frame_height = int(cap.get(4))

# Create VideoWriter object to save the output video
out = cv2.VideoWriter('output_video.mp4', cv2.VideoWriter_fourcc(*'mp4v'), 30, (frame_width, frame_height))

# Create background subtractor object
backSub = cv2.createBackgroundSubtractorMOG2()

while True:
    ret, frame = cap.read()
    if not ret:
        break
    
    # Apply background subtraction
    fgMask = backSub.apply(frame)

    # Find contours in the foreground mask
    contours, _ = cv2.findContours(fgMask, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

    # Iterate through detected contours
    for contour in contours:
        # Get bounding box of contour
        x, y, w, h = cv2.boundingRect(contour)
        
        # Filter out small objects
        if cv2.contourArea(contour) > 1000:
            # Draw yellow bounding box around moving object
            cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 255), 2)

    # Write frame with bounding box to output video
    out.write(frame)
    
    # Display the resulting frame
    cv2.imshow('Moving Object Detection', frame)
    
    # Press 'q' to exit
    if cv2.waitKey(25) & 0xFF == ord('q'):
        break

# Release video capture object, release output video object, and close windows
cap.release()
out.release()
cv2.destroyAllWindows()
