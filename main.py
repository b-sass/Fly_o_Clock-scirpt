import cv2 as cv
import numpy as np
from PIL import ImageGrab
import keyboard
import os
import time
##?         Lower Left         -   Lower Right     -       Upper Right    -    Upper Left
#! 1st version coords = [[868, 600, 908, 640],[1010, 600, 1050,640],[1010, 460, 1050, 500],[868, 460, 908, 500]]
#coords = [[875, 605, 915, 645 ],[1015, 595, 1055, 635],[1015, 455, 1055, 495],[864, 463, 904, 503]]
coords = [[887, 617, 907, 637],[1030, 600, 1050, 620],[1012, 461, 1032, 481],[867, 477, 887, 497]]

#! 1st version pos = ["LowerLeft.png", "LowerRight.png", "UpperRight.png", "UpperLeft.png"]
pos = ["LL.png", "LR.png", "UR.png", "UL.png"]

def PILtoCVConvert(img):
    #*PIL image is converted to an array 
    image = np.asarray(img)
    #*Color correction is applied
    RGBImage = cv.cvtColor(image, cv.COLOR_BGR2RGB)

    return RGBImage


def isEqual(image, screenshot, position):

    screenshot = ImageGrab.grab(bbox = position)
    screenshot = PILtoCVConvert(screenshot)
    return np.array_equal(image, screenshot) #True or False

        



#!## NOT NEEDED ANYMORE | FOUND BETTER WAY TO DO IT ##!#

# def ArrayToBool(img1, img2):
#     #difference between images is calculated
#     #img1 = cv.cvtColor(img1, cv.COLOR_RGB2GRAY)
#     difference = img1 - img2
#     print(difference)
#     #Boolean is calculated based on the image array
#     isvalid = bool(difference.all())
#     print(isvalid)
#     #Bool value is inverted (True -> False / Flase -> True)
#     equal = not isvalid
    
#     #If the images are the same True is returned, if not, False is returned
#     return equal

def main():
    while True:
        i = 0
        for position in coords:
            ##*Taking a screenshot of next coordinates
            ScreenShot = ImageGrab.grab(bbox = position)

            ##*Image ready for OpenCV
            ScreenShot = PILtoCVConvert(ScreenShot)
            
            ##*Make opencv read the image taken beforehand
            path = os.path.join("assets", pos[i])
            img = cv.imread(path)
            
            # cv.imshow("Image", img)
            # cv.imshow("Screenshot", ScreenShot)
            # cv.destroyAllWindows()

            ##*Compare 2 images
            Equal = False
            while not Equal:
                Equal = isEqual(img, ScreenShot, position)
                print(Equal)

            
            ##*Jump function
            keyboard.press_and_release("space")
            time.sleep(0.25)
            i += 1



if __name__ == "__main__":
    print(3)
    time.sleep(1)
    print(2)
    time.sleep(1)
    print(1)
    time.sleep(1)
    print("start")
    main()












