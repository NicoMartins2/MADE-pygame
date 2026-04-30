#!/usr/bin/python
# -*- coding: utf-8 -*-
import pygame.key

from code.Const import PLAYER_SPEED, WIN_HEIGHT, WIN_WIDTH, PLAYER_KEY_UP, PLAYER_KEY_LEFT, \
    PLAYER_KEY_RIGHT
from code.Entity import Entity



class Player(Entity):
    def __init__(self, name: str, position: tuple, level_name: str = ''):
        super().__init__(name, position)
        self.level_name = level_name
        self.animated = level_name == 'Level2'
        if self.animated:
            self.sprites = {
                'stand': pygame.image.load('./asset/char1_stand.png').convert_alpha(),
                'left': [pygame.image.load('./asset/char1_left1.png').convert_alpha(),
                         pygame.image.load('./asset/char1_left2.png').convert_alpha()],
                'right': [pygame.image.load('./asset/char1_right1.png').convert_alpha(),
                          pygame.image.load('./asset/char1_right2.png').convert_alpha()]
            }
            self.current_sprite = 'stand'
            self.animation_index = 0
            self.animation_timer = 0
            self.animation_speed = 10  # Frames por segundo para animação
        else:
            self.sprites = None

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
            if self.rect.bottom >= WIN_HEIGHT - 100:
                self.rect.bottom = WIN_HEIGHT - 100
                self.is_jumping = False
                self.velocity_y = 0
        else:
            # Se não está pulando, só atualiza a posição vertical se necessário
            self.velocity_y = 0

        # Movimento horizontal
        moving_left = pressed_key[PLAYER_KEY_LEFT[self.name]] and self.rect.left > 0
        moving_right = pressed_key[PLAYER_KEY_RIGHT[self.name]]

        if moving_left:
            self.rect.centerx -= PLAYER_SPEED[self.name]
        if moving_right:
            self.rect.centerx += PLAYER_SPEED[self.name]

        # Animação de sprites se ativada
        if self.animated:
            self.animation_timer += 1
            if moving_left:
                self.current_sprite = 'left'
            elif moving_right:
                self.current_sprite = 'right'
            else:
                self.current_sprite = 'stand'

            if self.current_sprite == 'stand':
                self.surf = self.sprites['stand']
            else:
                if self.animation_timer >= 60 // self.animation_speed:  # 60 FPS
                    self.animation_index = (self.animation_index + 1) % len(self.sprites[self.current_sprite])
                    self.animation_timer = 0
                self.surf = self.sprites[self.current_sprite][self.animation_index]