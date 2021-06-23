import tkinter as tk
import os
from tkinter import *
from tkinter.filedialog import askopenfilename
import pandas as pd
import numpy as np
from PIL import Image
from PIL import ImageTk


class MainWindow:

    def __init__(self, main):
        main.title("Image -> Evennia Code")
        main.rowconfigure(0, minsize=400, weight=1)
        main.rowconfigure(1, minsize=400, weight=1)
        main.columnconfigure(1, minsize=800, weight=1)

        self.fr_inputs = Frame(main)

        self.character = "@"
        self.lbl_char = Label(self.fr_inputs, text="Character: ")
        self.ent_char = Entry(self.fr_inputs)
        self.ent_char.insert(0, self.character)

        self.text_size = 40
        self.lbl_size = Label(self.fr_inputs, text="Width of text: ")
        self.ent_size = Entry(self.fr_inputs)
        self.ent_size.insert(0, self.text_size)

        self.lbl_file = Label(self.fr_inputs, text="No file selected.")
        self.btn_file = Button(self.fr_inputs, text="Select file to process.", command=self.do_pick_file)

        self.btn_go = Button(self.fr_inputs, text="GO!", fg="green", command=self.go_convert_image)

        self.btn_copy = Button(self.fr_inputs, text="Copy to Clipboard", command=self.copy_to_clipboard)

        self.btn_quit = Button(self.fr_inputs, text="QUIT", fg="red", command=main.destroy)

        self.lbl_char.grid(row=0, column=0, sticky="ew", padx=5, pady=5)
        self.ent_char.grid(row=0, column=1, sticky="ew", padx=5, pady=5)
        self.lbl_size.grid(row=1, column=0, sticky="ew", padx=5)
        self.ent_size.grid(row=1, column=1, sticky="ew", padx=5)
        self.lbl_file.grid(row=2, column=1, sticky="ew", padx=5)
        self.btn_file.grid(row=2, column=0, sticky="ew", padx=5)
        self.btn_go.grid(row=3, sticky="ew", padx=5)
        self.btn_copy.grid(row=4, sticky="ew", padx=5)
        self.btn_quit.grid(row=5, sticky="ew", padx=5)

        self.display_canvas = Canvas(main, height=400, width=400)
        if self.lbl_file["text"] == "No file selected.":
            self.image_name = "C:/Users/Elaina/PycharmProjects/art/images/idacat.gif"
            self.img = ImageTk.PhotoImage(Image.open(self.image_name))
            self.display_image = self.display_canvas.create_image(0, 0, anchor=NW, image=self.img)

        self.display_text = Text(main)

        self.fr_inputs.grid(row=0, column=0, sticky="ns")
        self.display_canvas.grid(row=0, column=1, sticky="nsew")
        self.display_text.grid(row=1, column=1, sticky="nsew")

    def do_pick_file(self):
        picked_file_types = [('Image files', '*.jpg *.png *.gif')]
        self.image_name = askopenfilename(initialdir=os.getcwd(), title="Please select an image:",
                                          filetypes=picked_file_types)
        self.lbl_file["text"] = self.image_name
        img_new = Image.open(self.image_name)
        (orig_w, orig_h) = img_new.size
        if orig_w >= orig_h:
            new_w = 400
            new_h = round(orig_h/orig_w * 400)
        else:
            new_h = 400
            new_w = round(orig_w/orig_h * 400)
        self.img = ImageTk.PhotoImage(img_new.resize((new_w, new_h)))
        self.display_canvas.itemconfig(self.display_image, image=self.img)

    def copy_to_clipboard(self):
        clip = pd.DataFrame([self.display_text.get("1.0", tk.END)])
        clip.to_clipboard(excel=False, header=False, index=False)

    def go_convert_image(self):
        if self.lbl_file["text"] == "No file selected.":
            self.do_pick_file()
        image_file = Image.open(self.image_name)
        cursor = 2  # ratio of cursor as pixel
        (orig_w, orig_h) = image_file.size
        aspect_ratio = orig_h / (orig_w * cursor)
        new_w = float(self.ent_size.get())
        new_h = round(aspect_ratio * new_w)
        image_array = np.array(image_file.resize((self.text_size, new_h)))
        (w, h, colors) = image_array.shape
        color_string = ''
        last_color = ''
        for x in range(0, w - 1):
            for y in range(0, h - 1):
                new_color = color_convert(image_array, x, y)
                if new_color != "000":
                    marker = self.ent_char.get()
                else:
                    marker = " "
                if new_color == last_color:
                    color_string = color_string + marker
                else:
                    color_string = color_string + "|" + new_color + marker
                last_color = new_color
            color_string = color_string[0:len(color_string) - 1] + "|" + last_color + "|_|/"
        self.display_text.delete("1.0", tk.END)
        self.display_text.insert(tk.END, '<ascii>' + color_string + '</ascii>')


def color_convert(image_array, x, y):
    colors = (0, 95, 135, 175, 215, 255)
    red = str(colors.index(min(colors, key=lambda n: abs(n - image_array[x, y, 0]))))
    grn = str(colors.index(min(colors, key=lambda n: abs(n - image_array[x, y, 1]))))
    blu = str(colors.index(min(colors, key=lambda n: abs(n - image_array[x, y, 2]))))
    color_string = red + grn + blu
    return color_string


window = Tk()
MainWindow(window)
window.mainloop()
