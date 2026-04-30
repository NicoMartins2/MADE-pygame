#!/usr/bin/python
# -*- coding: utf-8 -*-
import random

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
            case 'ground2Bg':
                return Background('ground2Bg', (0, WIN_HEIGHT - 100))
            case 'Player1':
                return Player('Player1', (10, WIN_HEIGHT - 132), level_name)
