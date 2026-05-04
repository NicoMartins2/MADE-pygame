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
        self.animated = level_name == 'Level2' or level_name == 'Level3'
        if self.animated:
            self.sprites1 = {
                'stand': pygame.image.load('./asset/char1_stand.png').convert_alpha(),
                'left': [pygame.image.load('./asset/char1_left1.png').convert_alpha(),
                         pygame.image.load('./asset/char1_left2.png').convert_alpha()],
                'right': [pygame.image.load('./asset/char1_right1.png').convert_alpha(),
                          pygame.image.load('./asset/char1_right2.png').convert_alpha()]
            }
            self.sprites2 = {
                'stand': [pygame.image.load('./asset/char2_stand.png').convert_alpha(),
                          pygame.image.load('./asset/char2_stand1.png').convert_alpha(),
                          pygame.image.load('./asset/char2_stand2.png').convert_alpha()],
                'left': [pygame.image.load('./asset/char2_left1.png').convert_alpha(),
                         pygame.image.load('./asset/char2_left2.png').convert_alpha(),
                         pygame.image.load('./asset/char2_left3.png').convert_alpha(),
                         pygame.image.load('./asset/char2_left4.png').convert_alpha(),
                         pygame.image.load('./asset/char2_left5.png').convert_alpha(),
                         pygame.image.load('./asset/char2_left6.png').convert_alpha()],
                'right': [pygame.image.load('./asset/char2_right1.png').convert_alpha(),
                          pygame.image.load('./asset/char2_right2.png').convert_alpha(),
                          pygame.image.load('./asset/char2_right3.png').convert_alpha(),
                          pygame.image.load('./asset/char2_right4.png').convert_alpha(),
                          pygame.image.load('./asset/char2_right5.png').convert_alpha(),
                          pygame.image.load('./asset/char2_right6.png').convert_alpha()]
            }
            self.current_sprite = 'stand'
            self.animation_index = 0
            self.animation_timer = 0
            self.animation_speed = 10  # Frames por segundo para animação
        else:
            self.sprites = None

    def move(self, platforms=None):
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
        self.velocity_y += self.gravity
        self.rect.centery += self.velocity_y

        if platforms:
            support = self._find_support(platforms)
            if support and self.velocity_y >= 0 and self.rect.bottom >= support.top:
                self.rect.bottom = support.top
                self.is_jumping = False
                self.velocity_y = 0
        else:
            if self.rect.bottom >= WIN_HEIGHT - 100:
                self.rect.bottom = WIN_HEIGHT - 100
                self.is_jumping = False
                self.velocity_y = 0

        # Movimento horizontal
        moving_left = pressed_key[PLAYER_KEY_LEFT[self.name]] and self.rect.left > 0
        moving_right = pressed_key[PLAYER_KEY_RIGHT[self.name]]

        if moving_left:
            self.rect.centerx -= PLAYER_SPEED[self.name]
        if moving_right:
            self.rect.centerx += PLAYER_SPEED[self.name]

        # Animação de sprites se ativada
        if self.level_name == 'Level2':
            if self.animated:
                self.animation_timer += 1
                if moving_left:
                    self.current_sprite = 'left'
                elif moving_right:
                    self.current_sprite = 'right'
                else:
                    self.current_sprite = 'stand'

                if self.current_sprite == 'stand':
                    self.surf = self.sprites1['stand']
                else:
                    if self.animation_timer >= 60 // self.animation_speed:  # 60 FPS
                        self.animation_index = (self.animation_index + 1) % len(self.sprites1[self.current_sprite])
                        self.animation_timer = 0
                    self.surf = self.sprites1[self.current_sprite][self.animation_index]
        else:
            if self.animated:
                self.animation_timer += 1
                if moving_left:
                    self.current_sprite = 'left'
                elif moving_right:
                    self.current_sprite = 'right'
                else:
                    self.current_sprite = 'stand'

                if self.current_sprite == 'stand':
                    self.surf = self.sprites2['stand']
                else:
                    if self.animation_timer >= 60 // self.animation_speed:  # 60 FPS
                        self.animation_index = (self.animation_index + 1) % len(self.sprites2[self.current_sprite])
                        self.animation_timer = 0
                    self.surf = self.sprites2[self.current_sprite][self.animation_index]

    def _find_support(self, platforms):
        for platform in platforms:
            if self.rect.right > platform.left and self.rect.left < platform.right:
                if self.rect.bottom >= platform.top - 10 and self.rect.bottom <= platform.top + 20:
                    return platform
        return None
