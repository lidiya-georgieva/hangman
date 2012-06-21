#!/usr/bin/python
# -*- coding: UTF-8 -*-
import os, sys
import pygame
from pygame.locals import *

class Category:
    def __init__(self, category, screen, pos, callback=None):
        pygame.font.init()
        self.my_font = pygame.font.Font('fonts\stylo_.ttf', 30)
        self.normal = self.my_font.render(category, True, (49, 43, 45), (195, 190, 187))
        self.highlight = self.my_font.render(category, True, (49, 43, 45), (165, 175, 184))
        self.image = self.normal
        self.pos = pos
        self.show = screen.blit(self.image, self.pos)
        self.callback = callback
    
    def draw(self, screen):
        self.show = screen.blit(self.image, self.pos)
    
    def mouseOver(self, pos):
        if self.show.collidepoint(pos):
            self.image = self.highlight
            return True
        else:
            self.image = self.normal
            return False
            
    def callback(self, x=None):
        if self.callback:
            if x:
                self.callback(x)
            else:
                self.callback()
        
    
