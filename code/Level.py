#!/usr/bin/python
# -*- coding: utf-8 -*-
import random
import sys

import pygame
from pygame import Surface, Rect
from pygame.font import Font

from code.Const import C_WHITE, WIN_HEIGHT, MENU_OPTION, SPAWN_TIME, C_GREEN, C_CYAN, C_BLACK, WIN_WIDTH
from code.Entity import Entity
from code.EntityFactory import EntityFactory
#from code.EntityMediator import EntityMediator
from code.Player import Player


class Level:
    def __init__(self, window: Surface, name: str, time_sec: int = 0):
        self.window = window
        self.name = name
        self.time_sec = time_sec
        self.entity_list: list[Entity] = []
        bg = EntityFactory.get_entity(self.name + 'Bg')
        if isinstance(bg, list):
            self.entity_list.extend(bg)
        else:
            self.entity_list.append(bg)
        player = EntityFactory.get_entity('Player1')
        self.entity_list.append(player)

    def run(self):
        clock = pygame.time.Clock()
        if self.time_sec > 0:
            start_ticks = pygame.time.get_ticks()
            while True:
                clock.tick(60)
                for ent in self.entity_list:
                    self.window.blit(source=ent.surf, dest=ent.rect)
                pygame.display.flip()
                for event in pygame.event.get():
                    if event.type == pygame.QUIT:
                        pygame.quit()
                        sys.exit()
                seconds = (pygame.time.get_ticks() - start_ticks) / 1000
                if seconds >= self.time_sec:
                    return
        else:
            while True:
                clock.tick(60)
                for ent in self.entity_list:
                    self.window.blit(source=ent.surf, dest=ent.rect)
                    ent.move()
                for event in pygame.event.get():
                    if event.type == pygame.QUIT:
                        pygame.quit()
                        sys.exit()

                    found_player = False
                    for ent in self.entity_list:
                        if isinstance(ent, Player):
                            found_player = True

                    if not found_player:
                        return False
                self.level_line(C_BLACK, (0, WIN_HEIGHT - 100), (WIN_WIDTH, WIN_HEIGHT - 100), 5)
                pygame.display.flip()

    def level_text(self, text_size: int, text: str, text_color: tuple, text_pos: tuple):
        text_font: Font = pygame.font.SysFont(name="Asap", size=text_size)
        text_surf: Surface = text_font.render(text, True, text_color).convert_alpha()
        text_rect: Rect = text_surf.get_rect(left=text_pos[0], top=text_pos[1])
        self.window.blit(source=text_surf, dest=text_rect)

    def level_line(self, line_color: tuple, line_start_pos: tuple, line_end_pos: tuple, line_width: int):
        pygame.draw.line(self.window, line_color, line_start_pos, line_end_pos, line_width)
