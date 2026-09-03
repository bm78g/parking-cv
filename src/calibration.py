import cv2
import sys
import json
import numpy as np

img = cv2.imread('data/sample.jpg')

if img is None:
    sys.exit("Image not found")

vertices = []
polygons = []

def click_event(event, x, y, flags, param):
    global vertices, polygons
    if event == cv2.EVENT_LBUTTONDOWN:
        cv2.circle(img, center=(x, y), radius=3, color=(0, 0, 255), thickness=-1)
        vertices.append([x, y])
        if len(vertices) == 4:
            polygons.append(vertices.copy())
            vertices = []

            pts = np.array(polygons[len(polygons) - 1], np.int32)
            print(pts)
            pts = pts.reshape((-1, 1, 2))
            print(pts)
            cv2.polylines(img, [pts], True, (0, 255, 255))
        cv2.imshow("display", img)

cv2.imshow("display", img)
cv2.setMouseCallback("display", click_event)

while True:
    key = cv2.waitKey(1) & 0xFF
    if key == ord('s'):
        break

cv2.destroyAllWindows()