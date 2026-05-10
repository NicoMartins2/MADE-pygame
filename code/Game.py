#!/usr/bin/python
# -*- coding: utf-8 -*-
import sys

import pygame

from code.Const import WIN_WIDTH, WIN_HEIGHT, MENU_OPTION, C_BLACK
from code.Level import Level
from code.Menu import Menu
from code.Player import Player


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
                msg1 = Level(self.window, 'msg1', time_sec=6)
                msg1.run()
                # level1
                level1 = Level(self.window, 'Level1')
                level1.run()
                # msg2
                msg2 = Level(self.window, 'msg2', time_sec=6)
                msg2.run()
                # level2
                level2 = Level(self.window, 'Level2')
                level2_result = level2.run()
                if level2_result is False: # ao cair no buraco, volta para o menu
                    continue
                # msg4
                msg4 = Level(self.window, 'msg4', time_sec=6)
                msg4.run()
                # level 3
                level3 = Level(self.window, 'Level3')
                level3_result = level3.run()
                if level3_result is False: # ao cair no buraco, volta para o menu
                    continue
                # msg5
                msg5 = Level(self.window, 'msg5', time_sec=6)
                msg5.run()
                # final
                final = Level(self.window, 'final', time_sec=15)
                final.run()
            else:
                pygame.quit()
                sys.exit()
            continue
