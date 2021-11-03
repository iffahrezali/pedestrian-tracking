import cv2
import timeit
import os

start = timeit.default_timer()

# Create our body classifier
body_classifier = cv2.CascadeClassifier(
    'C:/Users/60128/PycharmProjects/Pedestrian Detection FYP/haarcascades/haarcascade_fullbody.xml')


def video_to_frames(input_loc, output_loc):
    try:
        os.mkdir(output_loc)
    except OSError:
        pass

    # Start capturing the feed
    cap = cv2.VideoCapture(input_loc)

    count = 0
    print ("Converting video..\n")
    # Start converting the video

    while cap.isOpened():
        # Extract the frame
        cap.set(cv2.CAP_PROP_POS_MSEC, (count * 1000))
        # Extract the frame
        ret, frame = cap.read()

        if ret:
            gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

            # Pass frame to our body classifier
            bodies = body_classifier.detectMultiScale(gray, scaleFactor=1.1, minNeighbors=5)

            # Extract bounding boxes for any bodies identified
            for (x, y, w, h) in bodies:
                cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 255), 2)
                cv2.imshow('Pedestrians', frame)

            if cv2.waitKey(1) == 13:  # 13 is the Enter Key
                break

        else:
            break

        if not ret:
            continue

        # Write the results back to output location.
        cv2.imwrite(output_loc + "/%#05d.jpg" % (count+1), frame)
        count = count + 1

    cap.release()
    cv2.destroyAllWindows()

if __name__=="__main__":

    input_loc = 'C:/Users/60128/Desktop/FYP1 References/productionID.mp4'
    output_loc = 'C:/Users/60128/Desktop/Pedestrian/Haar like'
    video_to_frames(input_loc, output_loc)

# All the program statements
stop = timeit.default_timer()
execution_time = stop - start

print("Program Executed in " + str(execution_time))  # It returns time

