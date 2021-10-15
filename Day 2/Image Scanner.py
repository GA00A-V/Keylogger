import cv2
import os
import sys


def get_input():
    try:
        val = int(input("$ "))
    except ValueError:
        val = get_input()
    return val


def show():
    print("Select any option from below:")
    print("1: Open file")
    print("2: Exit Program")
    s = get_input()
    return s


def file_checker():
    file = input("Enter path of image file: ")
    if os.path.exists(file):
        print("OK: checking file")
    else:
        print("That's not a valid path try again!")
        file = file_checker()
    return file


def save(file):
    gray = cv2.imread(file, 0)
    thresh = cv2.adaptiveThreshold(gray, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY, 15, 8)
    output = input("Enter name of output file: ")
    if not (output.count(".") > 0):
        output += ".jpg"
    cv2.imwrite(output, thresh)
    print(f"Image saved as {output} at {os.getcwd()}")


if __name__ == "__main__":
    a = show()
    if a == 1:
        f = file_checker()
        save(f)
        print("Thanks! ")
    else:
        sys.exit(0)
