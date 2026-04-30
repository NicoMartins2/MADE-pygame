#!/usr/bin/python
# -*- coding: utf-8 -*-

import pygame.image
from code.Entity import Entity
class SpriteAnim(Entity):
    def __init__(self, name: str, position: tuple):
        super().__init__(name, position)
        self.frames = []
        self.current_frame = 0
        self.load_frames()

    def load_frames(self):
        for i in range(1, 5):
            frame = pygame.image.load(f'./asset/{self.name}_{i}.png').convert_alpha()
            self.frames.append(frame)

    def move(self):
        self.current_frame += 0.1
        if self.current_frame >= len(self.frames):
            self.current_frame = 0
        self.surf = self.frames[int(self.current_frame)]