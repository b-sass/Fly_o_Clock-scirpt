
# arr = [1,2,3]


# while True:

#     for i in arr:
#         print(i)
import numpy as np
import cv2 as cv
from PIL import ImageGrab
import os
import time


images = ["LowerLeft", "LowerRight", "UpperRight", "UpperLeft"]

#*Default Coordinates of the planet
offset = 105
x = 1222
y = 179
#*LOWER RIGHT COORDS
coords = [x, y, x+offset, y+offset]
#*Takes a screenshot of the planet
path = os.path.join("assets", "planet.png")
img = cv.imread(path)

for i in range(0, 3000):
    ScreenShot = ImageGrab.grab(bbox = coords)
    ScreenShot = np.asarray(ScreenShot)

    ScreenShot = cv.cvtColor(ScreenShot, cv.COLOR_BGR2RGB)



    cv.imshow("image", img)
    cv.imshow("Screenshot", ScreenShot)
    cv.waitKey(1)


    Equal = np.array_equal(ScreenShot, img)


    if Equal:
        print("Equal", i)
    else:
        print("!Equal", i)

print(time.process_time())


    
    


# IMG = cv.cvtColor(IMG, cv.COLOR_BGR2RGB)
# cv.imshow("sda",img)
# cv.waitKey(0)

# difference = img - IMG
# print(difference)
# #equal check
# valid = bool(difference.all())
# isEqual = not valid
# print(isEqual)

# # currentPos = images[0]
# # nextPos = images[1]

# while True:
#     i = 0
#     for position in images:
#         file = "J:/programy py/skrypt_fly-o-clock/{}.png".format(position)
#         # ScreenShot = ImageGrab.grab(bbox = )