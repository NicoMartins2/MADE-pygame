#!/usr/bin/python
# -*- coding: utf-8 -*-
import random
import sys

import pygame
from pygame import Surface, Rect
from pygame.font import Font

from code.Const import C_WHITE, WIN_HEIGHT, C_GREEN, C_BLACK, C_BROWN, WIN_WIDTH
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
        player = EntityFactory.get_entity('Player1', self.name)
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
            level2_platforms = []
            if self.name == 'Level2':
                level2_platforms = [
                    pygame.Rect(0, WIN_HEIGHT - 100, 800, 100),
                    pygame.Rect(900, WIN_HEIGHT - 100, 800, 100)
                ]
                level2_sign = [
                    pygame.Rect(750, WIN_HEIGHT - 150, 10, 50),
                    pygame.Rect(725, WIN_HEIGHT - 140, 50, 20)
                ]
            while True:
                clock.tick(60)
                player = None
                for ent in self.entity_list:
                    self.window.blit(source=ent.surf, dest=ent.rect)
                    if isinstance(ent, Player):
                        player = ent
                        ent.move(level2_platforms if self.name == 'Level2' else None)
                    else:
                        ent.move()

                for event in pygame.event.get():
                    if event.type == pygame.QUIT:
                        pygame.quit()
                        sys.exit()

                if player is None:
                    return False

                if player.rect.right > WIN_WIDTH:
                    return True

                if self.name == 'Level1':
                    self.level_line(C_BLACK, (0, WIN_HEIGHT - 100), (WIN_WIDTH, WIN_HEIGHT - 100), 5)
                elif self.name == 'Level2':
                    left_platform = pygame.Rect(0, WIN_HEIGHT - 100, 800, 100)
                    right_platform = pygame.Rect(900, WIN_HEIGHT - 100, 800, 100)
                    pygame.draw.rect(self.window, C_GREEN, left_platform)
                    pygame.draw.rect(self.window, C_GREEN, right_platform)
                    pygame.draw.rect(self.window, C_BROWN, (750, WIN_HEIGHT - 150, 10, 50))
                    pygame.draw.rect(self.window, C_BROWN, (725, WIN_HEIGHT - 140, 50, 20))
                    if player.rect.top > WIN_HEIGHT:
                        Level(self.window, 'msg3', time_sec=6).run()
                        return False
                    
                    if player.rect.colliderect(level2_sign[0]) and player.rect.colliderect(level2_sign[1]):
                        pygame.draw.rect(self.window, C_BLACK, (WIN_WIDTH / 2 - 170, WIN_HEIGHT / 2 - 50, 300, 100))
                        self.level_text(30, "Sempre haverá desafios.", C_WHITE, (WIN_WIDTH / 2 - 150, WIN_HEIGHT / 2))

                pygame.display.flip()

    def level_text(self, text_size: int, text: str, text_color: tuple, text_pos: tuple):
        text_font: Font = pygame.font.SysFont(name="Asap", size=text_size)
        text_surf: Surface = text_font.render(text, True, text_color).convert_alpha()
        text_rect: Rect = text_surf.get_rect(left=text_pos[0], top=text_pos[1])
        self.window.blit(source=text_surf, dest=text_rect)

    def level_line(self, line_color: tuple, line_start_pos: tuple, line_end_pos: tuple, line_width: int):
        pygame.draw.line(self.window, line_color, line_start_pos, line_end_pos, line_width)
