# import cv2
# import numpy as np

# # Initialize video capture object
# cap = cv2.VideoCapture('/home/biswajitrana/Videos/Untitled.mp4')  # Replace 'your_video.mp4' with the path to your video file

# # Get video frame width and height
# frame_width = int(cap.get(3))
# frame_height = int(cap.get(4))

# # Create VideoWriter object to save the output video
# out = cv2.VideoWriter('output_video.mp4', cv2.VideoWriter_fourcc(*'mp4v'), 30, (frame_width, frame_height))

# # Create background subtractor object
# backSub = cv2.createBackgroundSubtractorMOG2()

# while True:
#     ret, frame = cap.read()
#     if not ret:
#         break
    
#     # Apply background subtraction
#     fgMask = backSub.apply(frame)

#     # Find contours in the foreground mask
#     contours, _ = cv2.findContours(fgMask, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

#     # Iterate through detected contours
#     for contour in contours:
#         # Get bounding box of contour
#         x, y, w, h = cv2.boundingRect(contour)
        
#         # Filter out small objects
#         if cv2.contourArea(contour) > 1000:
#             # Draw yellow bounding box around moving object
#             cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 255), 2)

#     # Write frame with bounding box to output video
#     out.write(frame)
    
#     # Display the resulting frame
#     cv2.imshow('Moving Object Detection', frame)
    
#     # Press 'q' to exit
#     if cv2.waitKey(25) & 0xFF == ord('q'):
#         break

# # Release video capture object, release output video object, and close windows
# cap.release()
# out.release()
# cv2.destroyAllWindows()







import cv2
import numpy as np

# Function to filter out small contours and get the largest contour
def get_largest_contour(contours):
    largest_contour = None
    max_area = 0
    for contour in contours:
        area = cv2.contourArea(contour)
        if area > max_area:
            largest_contour = contour
            max_area = area
    return largest_contour

# Function to detect and track moving objects
def detect_and_track_objects(frame, backSub):
    # Apply background subtraction
    fgMask = backSub.apply(frame)

    # Perform morphological operations to enhance object detection
    kernel = np.ones((5,5),np.uint8)
    fgMask = cv2.morphologyEx(fgMask, cv2.MORPH_CLOSE, kernel)
    
    # Find contours in the foreground mask
    contours, _ = cv2.findContours(fgMask, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

    # Get the largest contour
    largest_contour = get_largest_contour(contours)
    
    if largest_contour is not None:
        # Get bounding box of the largest contour
        x, y, w, h = cv2.boundingRect(largest_contour)
        
        # Draw yellow bounding box around the largest contour
        cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 255), 2)

    return frame

# Initialize video capture object
cap = cv2.VideoCapture('D:\\biswajit.mp4')  # Replace 'your_video.mp4' with the path to your video file

# Get video frame width and height
frame_width = int(cap.get(3))
frame_height = int(cap.get(4))

# Create VideoWriter object to save the output video
out = cv2.VideoWriter('D:\\output_video100.mp4', cv2.VideoWriter_fourcc(*'mp4v'), 30, (frame_width, frame_height))

# Create background subtractor object
backSub = cv2.createBackgroundSubtractorMOG2()

while True:
    ret, frame = cap.read()
    if not ret:
        break

    # Detect and track moving objects
    processed_frame = detect_and_track_objects(frame, backSub)
    
    # Write processed frame to output video
    out.write(processed_frame)
    
    # Display the resulting frame
    cv2.imshow('Moving Object Detection', processed_frame)
    
    # Press 'q' to exit
    if cv2.waitKey(25) & 0xFF == ord('q'):
        break

# Release video capture object, release output video object, and close windows
cap.release()
out.release()
cv2.destroyAllWindows()
