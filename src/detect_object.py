import cv2
from ultralytics import YOLO
import json
from pathlib import Path

model = YOLO("yolov8s-visdrone.pt")
VEHICLE_CLASSES = [3, 4, 5, 8, 9]

# CHANGE THESE FOR DIFFERENT IMAGES AND VERSIONS
filename = "sample.jpg"
version = 0

bound_path = f"data/bounds/{Path(filename).stem}/{version:04d}.json"
img_path = f"data/images/{filename}"

with open("data/bounds/sample/0000.json") as file:
    spots = json.load(file)

img = cv2.imread(img_path)

results = model.predict(img, conf=0.4, verbose=False)

annotated_img = results[0].plot()
cv2.imshow("display", annotated_img)

while True:
    key = cv2.waitKey(1) & 0xFF
    if key == ord('s'):
        break