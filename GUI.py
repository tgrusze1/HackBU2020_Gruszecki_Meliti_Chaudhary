import tkinter
import numpy as np
import cv2

__all__ = [cv2, np, tkinter]


def create_webcam(mirror=False):
    """
    Opens camera.
    """
    vid = cv2.VideoCapture(0)  # Creates video object
    while True:
        ret_val, img = vid.read()  # Returns next frame
        if mirror:  # Mirrors direction of movement in webcam
            img = cv2.flip(img, 1)
        cv2.imshow('my webcam', img)  # Opens webcam
        if cv2.waitKey(1) == 27:  # Press escape to exit out of webcam.
            break  # esc to quit
    cv2.destroyAllWindows()


def main():
    create_webcam(mirror=True)


main()
