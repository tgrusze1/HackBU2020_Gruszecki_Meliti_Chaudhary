from tkinter import *
import numpy as np
import cv2
from PIL import Image, ImageTk
from HackBU2020_Gruszecki_Meliti_Chaudhary import get_name

root = Tk()
root.bind('<Escape>', lambda e: root.quit())
lmain = Label(root)
lmain.pack()
vid = cv2.VideoCapture(0)
vid.set(cv2.CAP_PROP_FRAME_WIDTH, 800)
vid.set(cv2.CAP_PROP_FRAME_HEIGHT, 800)
if not vid.isOpened():
    vid.open()


def activate_button():
    name = get_name.get_name(vid)
    name_in = Label(root, text=name)  # replace tdogg with function that takes the name
    name_in.place(y=930, x=50, relheight=.15, relwidth=.15)


def get_frame():
    """
    Gets current frame.
    """
    ret_val, frame = vid.read()  # Returns next frame
    frame = cv2.flip(frame, 1)
    cv2img = cv2.cvtColor(frame, cv2.COLOR_BGR2RGBA)
    img = Image.fromarray(cv2img)
    current_frame = ImageTk.PhotoImage(image=img)
    lmain.imagetk = current_frame
    lmain.configure(image=current_frame)
    lmain.after(1, get_frame)


def GUIWindow(width=1920, height=1080):
    root.title("Based Program")
    root.geometry(str(width) + "x" + str(height))
    root.resizable(width=False, height=False)
    root["bg"] = 'pink'

    actbutton = Button(root, text="Activate", bg='green', command=activate_button)  # add command =  whatever it needs to do
    actbutton.place(relx=0, rely=0, relheight=.1, relwidth=.1, anchor=NW)
    debutton = Button(root, text="Deactivate", bg='red')  # add command =  whatever it needs to do
    debutton.place(relx=0, y=100, relheight=.1, relwidth=.1, anchor=NW)

    name_label = Label(root, text="Name")
    name_label.place(y=850, x=80, relheight=.1, relwidth=.1)

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


def on_closing():
    vid.release()
    root.destroy()


GUIWindow()
get_frame()
root.protocol("WM_DELETE_WINDOW", on_closing)
root.mainloop()
