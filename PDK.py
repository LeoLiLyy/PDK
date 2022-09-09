"""This is a module for Python Development , it's a Python Development Kit that gives you some shortcut while you are coding"""


def read_file(file_path=None):
    """
    To tired copying how to read a file?
    :param file_path: The path of the file that you need computer to read(default=None)
    :return: result
    """
    with open(file_path, 'r', encoding='utf-8') as f:
        result = f.read()
    return result


def write_file(file_path=None, content=''):
    """
    To tired copying how to write a file?
    :param file_path: The path of the file that you need computer to write(default=None)
    :param content: The content you want to write(default='')
    :return: result
    """
    with open(file_path, 'w', encoding='utf-8') as f:
        result = f.write(content)
    return result


def read_binary_file(file_path=None):
    """
    To tired copying how to read a binary file?
    :param file_path: The path of the file that you need computer to read(default=None)
    :return: result
    """
    with open(file_path, 'rb') as f:
        result = f.read()
    return result


def write_binary_file(file_path=None, content=None):
    """
    To tired copying how to write a binary file?
    :param file_path: The path of the file that you need computer to write(default=None)
    :param content: The content you want to write(default=None)
    :return: result
    """
    with open(file_path, 'wb') as f:
        result = f.write(content)
    return result


def add_file(file_path=None, content=''):
    """
    To tired copying how to add a file?
    :param file_path: The path of the file that you need computer to add(default=None)
    :param content: The content you want to add(default='')
    :return: result
    """
    with open(file_path, 'a', encoding='utf-8') as f:
        result = f.write(content)
    return result


def resize(w, h, newW, newH, pil_image):
    """

    :param w:
    :param h:
    :param newW:
    :param newH:
    :param pil_image:
    :return:
    """
    f1 = 1.0 * newW / w
    f2 = 1.0 * newH / h
    factor = min([f1, f2])
    width = int(w * factor)
    height = int(h * factor)
    return pil_image.resize((width, height), Image.ANTIALIAS)
