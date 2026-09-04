import cv2
from ultralytics import YOLO
import json
from pathlib import Path

########################################################
#                OJBECT-TO-SPOT MATCHING               #
########################################################

# I'm assuming that getting the lower center of a bound will
# roughly calculate where the car touches the ground.
# It doesn't work as well for a perfect top-down view, but
# probably more practical for a more slanted camera angle.

# The contact coords will then be linked to the nearest center.
# However, there will need to be measures to prevent an unparked
# car from being matched to a spot.

def get_contact_cords():
    # Calculate a point horizontally center and slightly above lower bound
    pass

def match_vehicle(coords):
    # Match to closest center for now
    pass

def match_vehicles(results):
    # Extract coords and call match_vehicle
    for result in results:
        for box in result.boxes:
            coords = box.xyxy[0].tolist()
            match_vehicle(coords)

########################################################
#                    INITIALIZATION                    #
########################################################

model = YOLO("yolov8s-visdrone.pt")
CLASSES = [3, 4, 5, 8, 9]

# CHANGE THESE FOR DIFFERENT IMAGES AND VERSIONS
filename = "sample.jpg"
version = 0

bound_path = f"data/bounds/{Path(filename).stem}/{version:04d}.json"
img_path = f"data/images/{filename}"

with open("data/bounds/sample/0000.json") as file:
    spots = json.load(file)
img = cv2.imread(img_path)

# Display results for debug purposes
results = model.predict(img, classes=CLASSES, conf=0.4, verbose=False)

annotated_img = results[0].plot()
cv2.imshow("display", annotated_img)

# This is where the fun begins
match_vehicles(results)

while True:
    key = cv2.waitKey(1) & 0xFF
    if key == ord('s'):
        break