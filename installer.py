"""This is a module to install some module that PDK needs"""
import os


def install_all():
    """
    This function installs all the module PDK needs
    :return: None
    """
    os.system('pip install baidu-aip')
    os.system('pip install pygame')
    os.system('pip install tkinter')
    os.system('pip install Pillow')


if __name__ == '__main__':
    install_all()
