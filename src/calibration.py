import cv2
import sys
import json
import numpy as np
import math

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

        # Draw polygon once enough vertices are selected
        if len(vertices) == 4:
            # TODO: Add way to sort the vertices to always draw closed shape
            x_avg = y_avg = 0
            for vertex in vertices:
                x_avg += vertex[0]
                y_avg += vertex[1]
            x_avg /= 4
            y_avg /= 4
            center = (round(x_avg), round(y_avg))

            # Draw center for debug purposes
            cv2.circle(img, center=center, radius=3, color=(255, 0, 0), thickness=-1)

            resp_angles = []
            for vertex in vertices:
                angle = math.atan2(vertex[1] - center[1], vertex[0] - center[0])
                resp_angles.append(angle)

            vertices_sorted = [x for _, x in sorted(zip(resp_angles, vertices))]

            polygons.append(vertices_sorted.copy())
            vertices = []

            pts = np.array(polygons[len(polygons) - 1], np.int32)
            pts = pts.reshape((-1, 1, 2))
            cv2.polylines(img, [pts], True, (0, 255, 255))
        cv2.imshow("display", img)

cv2.imshow("display", img)
cv2.setMouseCallback("display", click_event)

while True:
    key = cv2.waitKey(1) & 0xFF
    if key == ord('s'):
        break

cv2.destroyAllWindows()