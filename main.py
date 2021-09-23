import cv2
import pytesseract
import PIL
from PIL import ImageTk, Image
from tkinter import filedialog
import os
from tkinter import *
import tkinter 
from tkinter import ttk 

m = tkinter.Tk()
m.title('Image to Text')
m.geometry('600x400') 
    


def openfn_convert():
    filename = filedialog.askopenfilename(title='open')

    #image to text
    img = cv2.imread(filename)
    text = pytesseract.image_to_string(img)
    # print(text)

    scrollbar = Scrollbar(m)

    #display image text
    converted_text = Text(m, height=3,yscrollcommand=scrollbar.set)
    converted_text.insert(1.0, text)
    converted_text.pack(side=BOTTOM,padx=20)

    return filename

#open image and display it 
def open_image():
    
    x = openfn_convert()
    img = PIL.Image.open(x)
    img = ImageTk.PhotoImage(img)
    panel = Label(m, image=img)
    panel.image = img
    panel.pack(side=TOP,padx=20, pady=20)



#open file button 
btn = Button(m, text='open image', command=open_image)
btn.pack(side=BOTTOM,padx=20, pady=20)

m.mainloop()
