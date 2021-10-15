import cv2
import os


def file_checker(string):
    path = input(f"Enter path of {string}: ")
    if os.path.exists(path):
        pass
    else:
        print("That's not a valid path try again!")
        path = file_checker(string)
    return path


file = file_checker("Image")
tem = file_checker("Template")

image = cv2.imread(file)
template = cv2.imread(tem, 0)
W, H, _ = image.shape
if W > 1280 or H > 720:
    image = cv2.resize(image, (0, 0), fx=0.5, fy=0.5)
    template = cv2.resize(template, (0, 0), fx=0.5, fy=0.5)
img = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
h, w = template.shape
result = cv2.matchTemplate(img, template, cv2.TM_CCOEFF)
_, _, _, location = cv2.minMaxLoc(result)
cv2.rectangle(image, location, (location[0] + w, location[1] + h), (255, 255, 255), 5)
cv2.imshow(file, image)
cv2.waitKey(0)
cv2.destroyAllWindows()
