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

def get_contact_coords(coords):
    # Calculate a point horizontally center and slightly above lower bound
    x_center = (coords[0] + coords[2]) / 2

    height = coords[3] - coords[1]
    y_low = coords[3] - (height * 0.25)

    contact_coords = (round(x_center), round(y_low))

    cv2.circle(annotated_img, center=contact_coords, radius=3, color=(0, 0, 255), thickness=-1)
    cv2.imshow("display", annotated_img)

def match_vehicle(coords):
    # Match to closest center for now
    contact_pos = get_contact_coords(coords)

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