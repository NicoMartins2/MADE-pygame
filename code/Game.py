#!/usr/bin/python
# -*- coding: utf-8 -*-
import sys

import pygame

from code.Const import WIN_WIDTH, WIN_HEIGHT, MENU_OPTION, C_BLACK
from code.Level import Level
from code.Menu import Menu


class Game:
    def __init__(self):
        pygame.init()
        pygame.display.set_caption('MADE')
        self.window = pygame.display.set_mode(size=(WIN_WIDTH, WIN_HEIGHT))

    def run(self):
        while True:
            menu = Menu(self.window)
            menu_return = menu.run()

            if menu_return == MENU_OPTION[0]:
                # Exibe msg1Bg por 6 segundos
                #level = Level(self.window, 'msg1', time_sec=6)
                #level.run()
                # Após 6 segundos, inicia o Level1
                level1 = Level(self.window, 'Level1')
                level1.run()
            else:
                pygame.quit()
                sys.exit()
