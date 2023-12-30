from ultralytics import YOLO
import os

# load model
pt_path = os.path.join(os.getcwd(), "model_pt/ball_rimV8.pt")
model = YOLO(pt_path)

# show how many class in the model
print(model.names)

# inference
source = os.path.join(os.getcwd(), "testing-datasets/side.mp4")
results = model(source, save=True, conf=0.3, show_labels=True, boxes=True, show_conf=False, stream=False)
