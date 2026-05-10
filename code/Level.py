#!/usr/bin/python
# -*- coding: utf-8 -*-
import random
import sys

import pygame
from pygame import Surface, Rect
from pygame.font import Font

from code.Const import C_WHITE, WIN_HEIGHT, C_GREEN, C_BLACK, C_BROWN, WIN_WIDTH, LEVEL2_PLATFORMS, LEVEL2_SIGN, LEVEL3_PLATFORMS, LEVEL3_SIGN
from code.Entity import Entity
from code.EntityFactory import EntityFactory
from code.Player import Player

class Level:
    def __init__(self, window: Surface, name: str, time_sec: int = 0):
        self.window = window
        self.name = name
        self.time_sec = time_sec
        self.entity_list: list[Entity] = []

        if self.name == 'Level3':
            bg = EntityFactory.get_entity('Level3Bg')
            self.backgrounds = bg if isinstance(bg, list) else [bg]  
            self.current_bg_index = 0 
            self.last_bg_switch_time = 0  
            self.bg_switch_interval = 2000  
        else:
            bg = EntityFactory.get_entity(self.name + 'Bg')
            if bg is None:
                raise ValueError(f"No background entity found for level '{self.name}'")
            if isinstance(bg, list):
                self.entity_list.extend(bg)
            else:
                self.entity_list.append(bg)

        player = EntityFactory.get_entity('Player1', self.name)
        if player is None:
            raise ValueError(f"No player entity found for level '{self.name}'")
        if self.name == 'Level3' and isinstance(player, Player):
            player.surf = player.sprites2['stand'][0]  
            self.entity_list.extend([player])
        elif isinstance(player, Player):
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
            level2_platforms = LEVEL2_PLATFORMS
            level2_sign = LEVEL2_SIGN
            level3_platforms = LEVEL3_PLATFORMS
            level3_sign = LEVEL3_SIGN
            while True:
                if f'./asset/{self.name}.mp3':    
                    pygame.mixer_music.load(f'./asset/{self.name}.mp3')
                    pygame.mixer_music.set_volume(0.3)
                    pygame.mixer_music.play(-1)
                clock.tick(60)
                current_time = pygame.time.get_ticks()

                if self.name == 'Level3':
                    if current_time - self.last_bg_switch_time > self.bg_switch_interval:
                        self.current_bg_index = 1 - self.current_bg_index  # Alterna entre 0 e 1
                        self.last_bg_switch_time = current_time

                if self.name == 'Level3':
                    self.window.blit(source=self.backgrounds[self.current_bg_index].surf, dest=self.backgrounds[self.current_bg_index].rect)

                for ent in self.entity_list:
                    if not (self.name == 'Level3' and isinstance(ent, Entity) and ent in self.backgrounds):
                        self.window.blit(source=ent.surf, dest=ent.rect)

                player = None
                for ent in self.entity_list:
                    if isinstance(ent, Player):
                        player = ent
                        if self.name == 'Level2':
                            ent.move(level2_platforms)
                        elif self.name == 'Level3':
                            ent.move(level3_platforms)
                    else:
                        ent.move()

                for event in pygame.event.get():
                    if event.type == pygame.QUIT:
                        pygame.quit()
                        sys.exit()

                if player is None:
                    return False
                
                # mensagem ao tentar retornar
                if player.rect.left < 0:
                    pygame.draw.rect(self.window, C_BLACK, (WIN_WIDTH / 2 - 170, WIN_HEIGHT / 2 - 50, 300, 100))
                    self.level_text(30, "Não há como voltar atrás.", C_WHITE, (WIN_WIDTH / 2 - 150, WIN_HEIGHT / 2))

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

                    if player.rect.colliderect(level2_sign[0]) and player.rect.colliderect(level2_sign[1]):
                        pygame.draw.rect(self.window, C_BLACK, (WIN_WIDTH / 2 - 170, WIN_HEIGHT / 2 - 50, 300, 100))
                        self.level_text(30, "Sempre haverá desafios.", C_WHITE, (WIN_WIDTH / 2 - 150, WIN_HEIGHT / 2))

                    if player.rect.top > WIN_HEIGHT:
                        Level(self.window, 'msg3', time_sec=6).run()
                        return False
                elif self.name == 'Level3':
                    for platform in level3_platforms:
                        pygame.draw.rect(self.window, C_GREEN, platform)
                    for sign in level3_sign:
                        pygame.draw.rect(self.window, C_BROWN, sign)
                    if player.rect.colliderect(level3_sign[0]) and player.rect.colliderect(level3_sign[1]):
                        pygame.draw.rect(self.window, C_BLACK, (WIN_WIDTH / 2 - 170, WIN_HEIGHT / 2 - 50, 450, 100))
                        self.level_text(30, "O caminho é incerto, mas siga em frente.", C_WHITE, (WIN_WIDTH / 2 - 150, WIN_HEIGHT / 2))
                    if player.rect.top > WIN_HEIGHT:
                        Level(self.window, 'msg3', time_sec=6).run()
                        return False

                pygame.display.flip()

    def level_text(self, text_size: int, text: str, text_color: tuple, text_pos: tuple):
        text_font: Font = pygame.font.SysFont(name="Asap", size=text_size)
        text_surf: Surface = text_font.render(text, True, text_color).convert_alpha()
        text_rect: Rect = text_surf.get_rect(left=text_pos[0], top=text_pos[1])
        self.window.blit(source=text_surf, dest=text_rect)

    def level_line(self, line_color: tuple, line_start_pos: tuple, line_end_pos: tuple, line_width: int):
        pygame.draw.line(self.window, line_color, line_start_pos, line_end_pos, line_width)
