from tkinter import *
import numpy as np
import cv2
from PIL import Image, ImageTk

root = Tk()
root.bind('<Escape>', lambda e: root.quit())
lmain = Label(root)
lmain.pack()

def get_frame():
    """
    Gets current frame.
    """
    vid = cv2.VideoCapture(0)
    vid.set(cv2.CAP_PROP_FRAME_WIDTH, 800)
    vid.set(cv2.CAP_PROP_FRAME_HEIGHT, 800)
    if not vid.isOpened():
        vid.open()
    ret_val, frame = vid.read()  # Returns next frame
    vid.release()
    frame = cv2.flip(frame,1)
    cv2img = cv2.cvtColor(frame, cv2.COLOR_BGR2RGBA)
    img = Image.fromarray(cv2img)
    current_frame = ImageTk.PhotoImage(image=img)
    lmain.imagetk = current_frame
    lmain.configure(image=current_frame)
    lmain.after(100, get_frame)


def GUIWindow(width=1920, height=1080):
    root.title("Based Program")
    root.geometry(str(width) + "x" + str(height))
    root.resizable(width=False, height=False)

    actbutton = Button(root, text="Activate", bg='green')  # add command =  whatever it needs to do
    actbutton.place(relx=0, rely=0, relheight=.1, relwidth=.1, anchor=NW)
    debutton = Button(root, text="Deactivate", bg='red')  # add command =  whatever it needs to do
    debutton.place(relx=0, y=100, relheight=.1, relwidth=.1, anchor=NW)

    name = Label(root, text="Name")
    name.place(y=850, x=80, relheight=.1, relwidth=.1)

    name_in = Label(root, text="Thomas Gruszecki")  # replace tdogg with function that takes the name
    name_in.place(y=930, x=50, relheight=.15, relwidth=.15)

    top = Label(root, text="Top")
    top.place(y=865, x=345 + 100, relheight=.07, relwidth=.07)

    top = Label(root, text="Shirt")  # replace shirt with function that takes the top article
    top.place(y=975, x=350 + 100, relheight=.07, relwidth=.07)

    bot = Label(root, text="Bottom")
    bot.place(y=865, x=545 + 200, relheight=.07, relwidth=.07)

    bot_in = Label(root, text="Pants")  # replace shirt with function that takes the bottom article
    bot_in.place(y=975, x=550 + 200, relheight=.07, relwidth=.07)

    shoe = Label(root, text="Footwear")
    shoe.place(y=865, x=745 + 300, relheight=.07, relwidth=.07)

    shoe_in = Label(root, text="Sneakers")  # replace shirt with function that takes the shoe
    shoe_in.place(y=975, x=750 + 300, relheight=.07, relwidth=.07)

GUIWindow()
get_frame()
root.mainloop()
