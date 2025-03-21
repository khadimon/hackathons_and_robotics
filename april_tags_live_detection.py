import cv2
from pupil_apriltags import Detector
import cv2
import numpy as np

at_detector = Detector(
   families="tag25h9",
   nthreads=1,
   quad_decimate=1.0,
   quad_sigma=0.0,
   refine_edges=1,
   decode_sharpening=0.25,
   debug=0
)



# Detecting and drawing bounding box of apriltag
def detect_bounding_box(vid):

    # Converting this frame to grayscale
    gray_image = cv2.cvtColor(vid, cv2.COLOR_BGR2GRAY)
    # Running AprilTags detect() function on frame
    tags = at_detector.detect(gray_image)
    
    #print(tags)

    # Trying to read apriltags on screen
    try:
        # Printing corner attribute from detect()'s returned list
        print(tags[0].corners)
        # Assigning four (x,y) pixel positions of each corner of apriltag, ()from apriltag attribute
        (ptA, ptB, ptC, ptD) = tags[0].corners

        ptB = (int(ptB[0]), int(ptB[1]))
        ptC = (int(ptC[0]), int(ptC[1]))
        ptD = (int(ptD[0]), int(ptD[1]))
        ptA = (int(ptA[0]), int(ptA[1]))

        # Drawing rectangle from each point onto frame
        cv2.line(vid, ptA, ptB, (0, 255, 0), 2)
        cv2.line(vid, ptB, ptC, (0, 255, 0), 2)
        cv2.line(vid, ptC, ptD, (0, 255, 0), 2)
        cv2.line(vid, ptD, ptA, (0, 255, 0), 2)

    except:
        print("No Tags found!") # Printing this if no tags found

    # Returning Full Tags Data
    return tags

# Creating video capture object
video_capture = cv2.VideoCapture(0)


while True:

    result, video_frame = video_capture.read()  # read frames from the video
    if result is False:
        break  # terminate the loop if the frame is not read successfully

    info = detect_bounding_box(
        video_frame
    )  # apply the function we created to the video frame

    cv2.imshow(
        "AprilTags Detection Project", video_frame
    )  # display the processed frame in a window
    #print(str(info))

    # Quit if "q" key is selected
    if cv2.waitKey(1) & 0xFF == ord("q"):
        break
video_capture.release()
cv2.destroyAllWindows()