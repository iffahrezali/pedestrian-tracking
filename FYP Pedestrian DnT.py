# Import the necessary packages
import os
import cv2
print(cv2.__version__)
import timeit
import imutils
import numpy as np
from imutils.object_detection import non_max_suppression

start = timeit.default_timer()

def video_to_frames(input_loc, output_loc):
    try:
        os.mkdir(output_loc)
    except OSError:
        pass

    # Start capturing the feed
    cap = cv2.VideoCapture(input_loc)

    count = 0
    print("Converting video...\n")

    # Create our body classifier
    body_classifier = cv2.CascadeClassifier(
        'C:/Users/60128/PycharmProjects/Pedestrian Detection FYP/haarcascades/haarcascade_fullbody.xml')
    lowerbody_classifier = cv2.CascadeClassifier(
        'C:/Users/60128/PycharmProjects/Pedestrian Detection FYP/haarcascades/haarcascade_lowerbody.xml')
    upperbody_classifier = cv2.CascadeClassifier(
        'C:/Users/60128/PycharmProjects/Pedestrian Detection FYP/haarcascades/haarcascade_upperbody.xml')

    # Initializing the HOG person detector
    hog = cv2.HOGDescriptor()
    hog.setSVMDetector(cv2.HOGDescriptor_getDefaultPeopleDetector())

    # Start converting the video
    while cap.isOpened():

        # Extract the frame
        cap.set(cv2.CAP_PROP_POS_MSEC, (count * 1000))
        ret, frame = cap.read()

        if (frame is None): break  # Check for empty frames

        # Read first frame
        if ret:
            frame = imutils.resize(frame,
                                   width=min(800, frame.shape[1]))

            gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

            # Pass frame to our body classifier
            bodies = body_classifier.detectMultiScale(gray, 1.1, 3)

            # Extract bounding boxes for any bodies identified
            for (x, y, w, h) in bodies:
                cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 255), 2)

                roi_gray = gray[y:y + h, x:x + w]
                roi_color = frame[y:y + h, x:x + w]

                # Pass frame to our lower body classifier
                lowerbodies = lowerbody_classifier.detectMultiScale(roi_gray)

                for (ex, ey, ew, eh) in lowerbodies:
                    cv2.rectangle(roi_color, (ex, ey), (ex + ew, ey + eh), (0, 255, 0), 2)

                    # Pass frame to our upper body classifier
                    upperbodies = upperbody_classifier.detectMultiScale(roi_gray)

                    for (ex, ey, ew, eh) in upperbodies:
                        cv2.rectangle(roi_color, (ex, ey), (ex + ew, ey + eh), (0, 255, 0), 2)

            # Detecting all the regions in the Image that has pedestrians inside it
            (regions, _) = hog.detectMultiScale(frame,
                                                winStride=(4, 4),
                                                padding=(4, 4),
                                                scale=1.05)

            # Extract bounding boxes for any bodies identified
            for (x, y, w, h) in regions:
                cv2.rectangle(frame, (x, y),
                              (x + w, y + h),
                              (0, 0, 255), 2)

            # Apply non-maxima suppression to the bounding boxes using a
            # fairly large overlap threshold to try to maintain overlapping
            # boxes that are still people
            regions = np.array([[x, y, x + w, y + h] for (x, y, w, h) in regions])
            pick = non_max_suppression(regions, probs=None, overlapThresh=30)

            # draw the final bounding boxes
            for (xA, yA, xB, yB) in pick:
                cv2.rectangle(frame, (xA, yA), (xB, yB), (0, 255, 0), 2)

            # Showing the output Image
            cv2.imshow("Image", frame)

            if cv2.waitKey(25) & 0xFF == ord('q'):
                break

        else:
            break

        if not ret:
            continue

        # Write the results back to output location.
        cv2.imwrite(output_loc + "/%#05d.jpg" % (count + 1), frame)

        count = count + 1

    # Release the feed
    cap.release()
    cv2.destroyAllWindows()

if __name__ == "__main__":
    input_loc = 'C:/Users/60128/Desktop/FYP1 References/productionID.mp4'
    output_loc = 'C:/Users/60128/Desktop/Pedestrian/Combination Method'
    video_to_frames(input_loc, output_loc)

# All the program statements
stop = timeit.default_timer()
execution_time = stop - start

print("Program Executed in " + str(execution_time))  # It returns time
