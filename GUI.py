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


def GUIWindow(width=1920, height=1080):
    m = Tk()
    m.title("Based Program")
    m.geometry(str(width) + "x" + str(height))
    m.resizable(width=False, height=False)

    actbutton = Button(m, text="Activate", bg='green')  # add command =  whatever it needs to do
    actbutton.place(relx=1, rely=0, relheight=.1, relwidth=.1, anchor=NE)
    debutton = Button(m, text="Deactivate", bg='red')  # add command =  whatever it needs to do
    debutton.place(relx=1, y=100, relheight=.1, relwidth=.1, anchor=NE)

    name = Label(m, text="Name")
    name.place(y=850, x=80, relheight=.1, relwidth=.1)

    name_in = Label(m, text="Thomas Gruszecki")  # replace tdogg with function that takes the name
    name_in.place(y=930, x=50, relheight=.15, relwidth=.15)

    top = Label(m, text="Top")
    top.place(y=865, x=345 + 100, relheight=.07, relwidth=.07)

    top = Label(m, text="Shirt")  # replace shirt with function that takes the top article
    top.place(y=975, x=350 + 100, relheight=.07, relwidth=.07)

    bot = Label(m, text="Bottom")
    bot.place(y=865, x=545 + 200, relheight=.07, relwidth=.07)

    bot_in = Label(m, text="Pants")  # replace shirt with function that takes the bottom article
    bot_in.place(y=975, x=550 + 200, relheight=.07, relwidth=.07)

    shoe = Label(m, text="Footwear")
    shoe.place(y=865, x=745 + 300, relheight=.07, relwidth=.07)

    shoe_in = Label(m, text="Sneakers")  # replace shirt with function that takes the shoe
    shoe_in.place(y=975, x=750 + 300, relheight=.07, relwidth=.07)


    m.mainloop()


def main():
    # create_webcam(mirror=True)
    GUIWindow(1920, 1080)


main()
