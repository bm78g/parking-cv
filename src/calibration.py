import cv2
import sys
import json
import numpy as np
import math

vertices = []
polygons = []

def find_center():
    global vertices, polygons

    x_avg = y_avg = 0
    for vertex in vertices:
        x_avg += vertex[0]
        y_avg += vertex[1]
    x_avg /= 4
    y_avg /= 4
    center = (round(x_avg), round(y_avg))
    return center

def sort_vertices(center):
    global vertices, polygons

    angles = []
    for vertex in vertices:
        angle = math.atan2(vertex[1] - center[1], vertex[0] - center[0])
        angles.append(angle)

    # Sort vertices based on angle from center
    v_sorted = [x for _, x in sorted(zip(angles, vertices))]
    return v_sorted

def draw_bound():
    global vertices, polygons

    center = find_center()
    # Draw center for debug purposes
    cv2.circle(img, center=center, radius=3, color=(255, 0, 0), thickness=-1)

    # Vertices sorted to ensure shape is closed
    v_sorted = sort_vertices(center)
    polygons.append(v_sorted.copy())

    pts = np.array(polygons[len(polygons) - 1], np.int32)
    pts = pts.reshape((-1, 1, 2))
    cv2.polylines(img, [pts], True, (0, 255, 255))

def click_event(event, x, y, flags, param):
    global vertices, polygons
    if event == cv2.EVENT_LBUTTONDOWN:
        cv2.circle(img, center=(x, y), radius=3, color=(0, 0, 255), thickness=-1)
        vertices.append([x, y])

        # Draw polygon once enough vertices are selected
        if len(vertices) == 4:
            draw_bound()
            vertices = []

        cv2.imshow("display", img)

def store_bounds():
    global polygons
    bounds = []
    
    for poly in polygons:
        bound = {
            "vertices": poly,
        }
        bounds.append(bound)
    
    with open("data/bounds/bounds.json", "w") as file:
        json.dump(bounds, file, indent=4)

img = cv2.imread('data/images/sample.jpg')

if img is None:
    sys.exit("Image not found")

cv2.imshow("display", img)
cv2.setMouseCallback("display", click_event)

while True:
    key = cv2.waitKey(1) & 0xFF # Wait a millisecond for input
    if key == ord('s'):
        store_bounds()
        break

cv2.destroyAllWindows()