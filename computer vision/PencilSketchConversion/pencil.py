import numpy as np 
import cv2 as cv 
import tkinter as tk 
from tkinter import filedialog 
from tkinter import messagebox 
from PIL import Image,ImageTk 
 
images = {"original":None,"sketch":None}

def open_file():
    
    file_path = filedialog.askopenfilename()
    if not file_path:
        return
    img = cv.imread(file_path)
    display_image(img,original=True)
    sketch_image = convert_to_sketch(img)
    display_image(sketch_image,original=False)
    
def convert_to_sketch(img):
    img_gray = cv.cvtColor(img,cv.COLOR_BGR2GRAY)
    img_inverted = cv.bitwise_not(img_gray)
    blured_img = cv.GaussianBlur(img_inverted,(21,21),sigmaX=0,sigmaY=0)
    img_inverted = cv.bitwise_not(blured_img)
    sketch_img = cv.divide(img_gray,img_inverted,scale=256.0)
    return sketch_img


def display_image(img,original):
    img_rgb = cv.cvtColor(img,cv.COLOR_BGR2RGB) if original else img 
    img_pil = Image.fromarray(img_rgb)
    img_tk = ImageTk.PhotoImage(image=img_pil)
    
    if original:
        images["original"] = img_pil
    else:
        images["sketch"] = img_pil
        
    label = original_image_label if original else sketch_image_label 
    label.config(image=img_tk)
    label.image = img_tk 
    
def save_sketch():
    if images["sketch"] is None:
        messagebox.showerror("Error","No sketch to save")
        return 
    sketch_filepath = filedialog.askopenfilename(defaultextension="png",filetypes=[("PNG files","*.png")])
    if not sketch_filepath:
        return 
    images["sketch"].save(sketch_filepath,"PNG")
    messagebox.showinfo("Saved","Sketch saved to {}".format(sketch_filepath))
    
app = tk.Tk()
app.title("pencil Sketch Conversion")

frame = tk.Frame(app)
frame.pack(pady=10,padx=10)

original_image_label = tk.Label(frame)
original_image_label.grid(row=0,column=0,padx=5,pady=5)
sketch_image_label = tk.Label(frame)
sketch_image_label.grid(row=0,column=1,padx=5,pady=5)

btn_frame = tk.Frame(app)
btn_frame.pack(pady=10)

open_button = tk.Button(btn_frame,text="open Image",command=open_file)
open_button.grid(row=0,column=0,padx=5)

save_button = tk.Button(btn_frame,text="sketch save",command=save_sketch)
save_button.grid(row=0,column=1,padx=5)

app.mainloop()