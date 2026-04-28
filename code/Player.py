#!/usr/bin/python
# -*- coding: utf-8 -*-
import pygame.key

from code.Const import PLAYER_SPEED, WIN_HEIGHT, WIN_WIDTH, PLAYER_KEY_UP, PLAYER_KEY_DOWN, PLAYER_KEY_LEFT, \
    PLAYER_KEY_RIGHT
from code.Entity import Entity


class Player(Entity):
    def __init__(self, name: str, position: tuple):
        super().__init__(name, position)

    def move(self):
        pressed_key = pygame.key.get_pressed()
        # Inicialização dos atributos de pulo apenas se não existirem
        if not hasattr(self, 'is_jumping'):
            self.is_jumping = False
        if not hasattr(self, 'velocity_y'):
            self.velocity_y = 0
        self.jump_height = 200
        self.jump_speed = 15
        self.gravity = 0.8

        # Pulo só é permitido se não estiver pulando
        if pressed_key[PLAYER_KEY_UP[self.name]] and not self.is_jumping:
            self.is_jumping = True
            self.velocity_y = -self.jump_speed

        # Atualiza a física do pulo
        if self.is_jumping:
            self.velocity_y += self.gravity
            self.rect.centery += self.velocity_y
            # Verifica se atingiu o chão
            if self.rect.bottom >= WIN_HEIGHT - 102:
                self.rect.bottom = WIN_HEIGHT - 102
                self.is_jumping = False
                self.velocity_y = 0
        else:
            # Se não está pulando, só atualiza a posição vertical se necessário
            self.velocity_y = 0

        # Movimento horizontal
        if pressed_key[PLAYER_KEY_LEFT[self.name]] and self.rect.left > 0:
            self.rect.centerx -= PLAYER_SPEED[self.name]
        if pressed_key[PLAYER_KEY_RIGHT[self.name]]:
            self.rect.centerx += PLAYER_SPEED[self.name]