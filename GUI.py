import tkinter
import numpy as np
import cv2
__all__ = [cv2, np, tkinter]

def create_webcam(mirror=False):
    vid = cv2.VideoCapture(0)
    while True:
        ret_val, img = vid.read()
        if mirror:
            img = cv2.flip(img, 1)
        cv2.imshow('my webcam', img)
        if cv2.waitKey(1) == 27:
            break  # esc to quit
    cv2.destroyAllWindows()

def main():
    create_webcam(mirror = True)

main()

