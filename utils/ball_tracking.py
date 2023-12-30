from ultralytics import YOLO
import os
import cv2
import numpy as np

video_path = os.path.join(os.getcwd(), "testing-datasets/side.mp4")
ball_rim_model_path = os.path.join(os.getcwd(), "model_pt/ball_rimV8.pt")

ball_rim_model = YOLO(ball_rim_model_path)

# load video
cap = cv2.VideoCapture(video_path)

# get video properties
fps = int(cap.get(cv2.CAP_PROP_FPS))
width = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
height = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))

# write out video
fourcc = cv2.VideoWriter_fourcc(*"MJPG")
out = cv2.VideoWriter("output.mp4", fourcc, fps, (width, height))

ball_location = None  # xywh: [x, y, w, h] center of the box, width, height
ball_tracking = []  # list of ball location

# loop through the video frames
while cap.isOpened():
    success, frame = cap.read()

    if success:
        # run yolo inference on the frame, classes= {0: "ball", 1: "rim"}
        ball = ball_rim_model.predict(frame, classes=[0], max_det=1, conf=0.5)

        # check if results contains ball
        if ball[0].boxes.__len__() != 0:
            ball_location = ball[0].boxes.xywh[0].numpy().astype(int)  # xywh: [x, y, w, h] center of the box, width, height
            # print(f"get ball_location: {ball_location}")
            ball_tracking.append(ball_location)

        # track current the ball
        if len(ball_tracking) > 1:
            # draw the ball tracking
            for i in range(len(ball_tracking) - 1):
                cv2.line(frame, tuple(ball_tracking[i][:2]), tuple(ball_tracking[i + 1][:2]), (0, 0, 255), 2)

        # visualize the results on the frame
        # args: conf=False, labels=False, boxes=False
        annotated_frame = ball[0].plot(conf=False, labels=False, boxes=False)  # ball bounding box

        # write out video
        out.write(annotated_frame)
        # display the annotated frame
        cv2.imshow("Ball Tracking", annotated_frame)

        # break the loop if 'q' is pressed
        if cv2.waitKey(1) & 0xFF == ord("q"):
            break
    else:
        break

# Release the video capture object and video writer object
cap.release()
out.release()
cv2.destroyAllWindows()
