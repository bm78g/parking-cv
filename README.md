# Computer Vision Parking Availability Identifier

### Plan
Given an image of a parking lot, the program must identify which spots are occupied and which are available.
The image will be retrieved from AWS S3 through an event system, but will only use the sample image for now
for development purposes.

The program will statically identify the location of each spot using coordinates relative to the image.

Then, it will use a YOLO model to identify vehicles in the image and determine their location, which will be compared to the static bounds of the spots to determine occupancy.

The occupancy data will be stored as JSON and stored inside DynamoDB for backend retrieval.

### Stack
The program will be built in Python with OpenCV for coordinates calibration and YOLO for object detection.
It will also use AWS CDK for cloud infrastructure.