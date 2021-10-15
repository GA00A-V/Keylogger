import numpy as np
import cv2
import os


def file_checker():
    path = input("Enter path of image file: ")
    if os.path.exists(path):
        print("OK: checking file")
    else:
        print("That's not a valid path try again!")
        path = file_checker()
    return path


file = file_checker()
b = input("Do you want to show corners with circles(Y/N): ")
a = input("Do you want to connect corners(Y/N): ")
image = cv2.imread(file)
image = cv2.resize(image, (1280, 720))
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
corners = cv2.goodFeaturesToTrack(gray, 100, 0.1, 10)

if corners is not None:
    if ("Y" in b) or ("y" in b):
        corners = np.int0(corners)
        for corner in corners:
            x, y = corner.ravel()
            cv2.circle(image, (x, y), 4, (255, 2, 244), 1)
    if ("Y" in a) or ("y" in a):
        for i in range(len(corners)):
            for j in range(i + 1, len(corners)):
                corner1 = tuple(map(lambda value: int(value), corners[i][0]))
                corner2 = tuple(map(lambda value: int(value), corners[j][0]))
                print(corner1)
                print(corner2)
                cv2.line(image, corner1, corner2, (255, 2, 23), 1)

cv2.imshow(file, image)
cv2.waitKey(0)
cv2.destroyAllWindows()
