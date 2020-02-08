from tkinter import *
import numpy as np
import cv2



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

def GUIWindow():
    m = Tk()
    m.title("Based Program")
    m.geometry("1920x1080")
    m.resizable(width=False, height=False)

    actbutton = Button(m, text="Activate", bg='green')  # add command =  whatever it needs to do
    actbutton.place(x=1725, relheight=.1, relwidth=.1)
    debutton = Button(m, text="Deactivate", bg='red')  # add command =  whatever it needs to do
    debutton.place(x=1725, y=108, relheight=.1, relwidth=.1)

    namelabel = Label(m, text="Name")
    namelabel.place()
    m.mainloop()



def main():
    #create_webcam(mirror=True)
    GUIWindow()

main()
