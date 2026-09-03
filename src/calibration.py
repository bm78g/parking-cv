import cv2

sample_img = cv2.imread('data/sample.jpg')

if sample_img is None:
    print("Error: Could not read image")
    exit(1)

cv2.imshow("Sample Image", sample_img)
cv2.waitKey(0)
cv2.destroyAllWindows()