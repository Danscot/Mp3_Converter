
import customtkinter

from tkinter import filedialog

import os

from mp3 import *


class App(customtkinter.CTk):

    def __init__(self):
        super().__init__()

        self.wm_title("Danscot_converter")

        self.geometry("600x400")

        self.minsize(600, 400)

        self.maxsize(600, 400)

        self.file_path = str

        self.file_name = str

        self.generic_heading = customtkinter.CTkLabel(

            master=self,

            text="D a n s c o t   M P 3   C o n v e r t e r",

            text_color="white",

            font=("Calibri", 22),

        )

        self.path = customtkinter.StringVar()

        self.home_page()

    def home_page(self):

        self.generic_heading.pack(pady=20)

        # file selction button

        customtkinter.CTkButton(

            master=self,

            text="select a file to convert to audio",

            corner_radius=10,

            font=("calibri", 16),

            width=160,

            command=self.view_file,

            hover_color="#9748FF",

            background_corner_colors=None,

            fg_color='#9748FF'

        ).place(x=80, y=120)


        customtkinter.CTkButton(

            master=self,

            text="select a directory to save the file",

            corner_radius=10,

            font=("calibri", 16),

            width=160,

            command=self.get_directory,

            hover_color="#9748FF",

            background_corner_colors=None,

            fg_color='#9748FF'

        ).place(x=80, y=210)


        # convert button

        customtkinter.CTkButton(

            master=self,

            text="C O N V E R T",

            corner_radius=10,

            font=("calibri", 20),

            width=160,

            command=self.converter,

            hover_color="#9748FF",

            background_corner_colors=None,

            fg_color='#9748FF',


        ).place(x=220, y=330)

    def file_data(self):

        self.file_name = os.path.splitext(os.path.basename(self.file_path))[0]

        customtkinter.CTkLabel(

            master=self,

            text=f'F I L E  N A M E : {self.file_name}',

            text_color="white",

            font=("Calibri", 16),

        ).place(x=100, y=170)

    def view_file(self):

        self.file_path = filedialog.askopenfilename()

        self.file_data()

    def get_directory(self):

        self.dir_path = filedialog.askdirectory()

    def converter(self):

        mp3 = Mp3(self.file_path, self.dir_path)

        mp3.convert_to_audio()


test = App()

test.mainloop()