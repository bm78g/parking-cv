# Computer Vision Parking Availability Identifier

### Plan
Given an image of a parking lot, the program must identify which spots are occupied and which are available.
The image will be retrieved from AWS S3 through an event system.

The program will statically identify the location of each spot using coordinates relative to the image.

Then, it will use a YOLO model to identify vehicles in the image and determine their location, which will be compared to the static bounds of the spots to determine occupancy.