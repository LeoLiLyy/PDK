"""Tkinter is too complicated?"""
import tkinter as tk
from PIL import ImageTk
from tkinter import filedialog


class S:
    def __init__(self):
        pass

    @staticmethod
    def new_tkinter_window(bg_path='', width='1000', height='600', title='A Window', btn_path=None, x=0, y=0,
                           btn_width='1000', btn_height='600', ):
        """
        Tired of copying code to create a tkinter window again and again?
        :param bg_path: The path of the background of your new Tkinter window(default='')
        :param width: The width of the window(default='1000')
        :param height: The height of the window(default='600')
        :param title: The title(or name) of your Tkinter window(default='A Window')
        :param x: The x coordinates of your button(default='0')
        :param y: The y coordinates of your button(default='0')
        :param btn_path: Path (default=None)
        :param btn_width: Width (default='1000')
        :param btn_height: Height(default='600')
        :return: None
        """
        global window
        window = tk.Tk()
        window.geometry(str(width) + 'x' + str(height))
        window.resizable(0, 0)
        window.title(str(title))
        bg = ImageTk.PhotoImage(file=bg_path)
        bgLabel = tk.Label(window, image=bg, width=width, height=height)
        bgLabel.pack()
        btn_img = ImageTk.PhotoImage(file=btn_path)
        btn = tk.Button(window, image=btn_img, width=btn_width, height=btn_height, bd=0)
        btn.place(x=x, y=y)

    @staticmethod
    def new_tkinter_button(bg_path='', width='1000', height='600', x=0, y=0, command=None):
        """
        Tired of copying code to create a tkinter window again and again?
        :param bg_path: The path of the background of the button(default=None)
        :param width: The width of the button(default='1000')
        :param height: The height of the button(default='600')
        :param x: The X coordinate of the button(default=0)
        :param y: The Y coordinate of the button(default=0)
        :param command: The command that the button does(default=None)
        :return:
        """
        btn_img = ImageTk.PhotoImage(file=bg_path)
        btn = tk.Button(window, image=btn_img, width=width, height=height, command=command)
        btn.place(x=x, y=y)

    @staticmethod
    def choose_image(initialdir=None, x=0, y=0):
        """
        You know, just to open the select-image page.
        :param initialdir: initiadir, the initial path
        :param x: Do I have to repeat it again and again?
        :param y: Do I have to repeat it again and again?
        :return:
        """
        global imagePath, window
        imagePath = filedialog.askopenfilename(initialdir=str(initialdir), title='Choose an image.')
        Img = ImageTk.PhotoImage(file=imagePath)
        img = tk.Label(window, image=Img, width=367, height=275)
        img.place(x=x, y=y)
        window.mainloop()


"""
:param bg_path: The path of the background of your new Tkinter button(default='')
        :param width: The width of the button(default='1000')
        :param height: The height of the button(default='600')
        :param command: The command that the button does(default=None)
        :return: None
        """
