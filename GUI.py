from tkinter import *
#import numpy as np
#import cv2
#__all__ = [cv2, np, tkinter]

#vid = cv2.VideoCapture(-1, cv2.CAP_DSHOW)

m = Tk() #Creating window
m.title("Based Program") #Names the window
m.geometry("1920x1080") #Dimesions of window
m.resizable(width=False, height=False) #Make it non-resizeable

actbutton = Button(m, text = "Activate") #add command =  whatever it needs to do
actbutton.place(x=1725, relheight= .1, relwidth= .1)
debutton = Button(m, text = "Deactivate") #add command =  whatever it needs to do
debutton.place(x=1725,y=108, relheight= .1, relwidth= .1)



mainloop()
