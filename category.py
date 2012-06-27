#!/usr/bin/python
# -*- coding: UTF-8 -*-
import os
import sys
import pygame
from pygame.locals import *


class Category:

    def __init__(self, category, screen, position):
        pygame.font.init()
        self.my_font = pygame.font.Font('fonts\stylo_.ttf', 30)
        self.normal = self.my_font.render(category, True, (49, 43, 45), (195, 190, 187))
        self.highlight = self.my_font.render(category, True, (49, 43, 45), (165, 175, 184))
        self.image = self.normal
        self.position = position
        self.show = screen.blit(self.image, self.position)
        self.name = category

    def draw(self, screen):
        self.show = screen.blit(self.image, self.position)

    def mouse_over(self, position):
        """Make hover effect"""
        if self.show.collidepoint(position):
            self.image = self.highlight
            return True
        else:
            self.image = self.normal
            return False
