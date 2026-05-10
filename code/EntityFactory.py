#!/usr/bin/python
# -*- coding: utf-8 -*-
import random
import pygame

from code.Background import Background
from code.Const import WIN_WIDTH, WIN_HEIGHT
from code.Player import Player


class EntityFactory:

    @staticmethod
    def get_entity(entity_name: str, level_name: str = ''):
        match entity_name:
            case 'msg1Bg':
                return Background('msg1Bg', (0, 0))
            case 'Level1Bg':
                return Background('Level1Bg', (0, 0))
            case 'msg2Bg':
                return Background('msg2Bg', (0, 0))
            case 'Level2Bg':
                return Background('Level2Bg', (0, 0))
            case 'Level3Bg':
                list_bg = []
                for i in range(2):
                    bg = Background(f'Level3Bg{i}', (0, -300))
                    bg.time_sleep(0.5)
                    list_bg.append(bg)
                return list_bg
            case 'msg3Bg':
                return Background('msg3Bg', (0, 0))
            case 'msg4Bg':
                return Background('msg4Bg', (0, 0))
            case 'msg5Bg':
                return Background('msg5Bg', (0, 0))
            case 'finalBg':
                return Background('finalBg', (0, 0))
            case 'Player1':
                player1_pos = (10, WIN_HEIGHT - 132)
                return Player('Player1', player1_pos, level_name)
