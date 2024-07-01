import tkinter
import os
import tkinter.messagebox
import requests
from PIL import ImageTk,Image
from tkinter import messagebox
root = tkinter.Tk()
background_image=ImageTk.PhotoImage(Image.open("assets\\rose.jpg"))
image_panel=tkinter.Label(root,image=background_image)
image_panel.pack(fill="both",expand="yes")

username_textvar = tkinter.StringVar()
password_textvar = tkinter.StringVar()

aimbot_var = tkinter.IntVar()
esp_var = tkinter.IntVar()
ragehack_var = tkinter.IntVar()
norecoil_var = tkinter.IntVar()
nospread_var = tkinter.IntVar()

class EntryWithPlaceholder(tkinter.Entry):
    def __init__(self, master=None, placeholder="PLACEHOLDER", color='grey',**kwargs):
        super().__init__(master,kwargs)

        self.placeholder = placeholder
        self.placeholder_color = color
        self.default_fg_color = self['fg']

        self.bind("<FocusIn>", self.foc_in)
        self.bind("<FocusOut>", self.foc_out)

        self.put_placeholder()

    def put_placeholder(self):
        self.insert(0, self.placeholder)
        self['fg'] = self.placeholder_color

    def foc_in(self, *args):
        if self['fg'] == self.placeholder_color:
            self.delete('0', 'end')
            self['fg'] = self.default_fg_color

    def foc_out(self, *args):
        if not self.get():
            self.put_placeholder()

def delete_children(wid, indent=0):
    children = wid.winfo_children()
    for item in children:
        item.pack_forget()

def load_menuscreen():
    delete_children(image_panel)
    menu_screen()

def menu_screen():
    tkinter.Checkbutton(image_panel,text="AIMBOT",variable=aimbot_var,onvalue=1, offvalue=0,).pack()
    tkinter.Checkbutton(image_panel,text="ESP",variable=esp_var,onvalue=1, offvalue=0,).pack()
    tkinter.Checkbutton(image_panel,text="RAGE HACK",variable=ragehack_var,onvalue=1, offvalue=0,).pack()
    tkinter.Checkbutton(image_panel,text="NO RECOIL",variable=norecoil_var,onvalue=1, offvalue=0,).pack()
    tkinter.Checkbutton(image_panel,text="NO SPREAD",variable=nospread_var,onvalue=1, offvalue=0,).pack()


def login_command():
    username = username_textvar.get()
    password = password_textvar.get()
    login = username + ":" + password    
    
    response = requests.get('https://pastebin.com/raw/hjppn3Rr')
    database = response.text.splitlines()

    if login in database:
        tkinter.messagebox.showinfo(message="Login Successfully")
        load_menuscreen()
    else:
        tkinter.messagebox.showerror(message="Login not found")

def mainscreen():
    username_textbox = EntryWithPlaceholder(image_panel,textvariable=username_textvar,placeholder="username")
    password_textbox = EntryWithPlaceholder(image_panel,textvariable=password_textvar,show="*",placeholder="password")

    username_textbox.pack()
    password_textbox.pack()

    main_button = tkinter.Button(image_panel,text="login",command=login_command)
    main_button.pack()

root.protocol("WM_DELETE_WINDOW")
root.title("Acarina")
root.geometry("600x400")
root.iconbitmap("Assets\\rose.ico")
mainscreen()
root.mainloop()