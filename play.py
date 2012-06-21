#!/usr/bin/python
# -*- coding: UTF-8 -*-
import os, sys
import pygame
from pygame.locals import *

class Play:
    def main(self, screen):
        background = pygame.image.load('images\hangman_play.png')
        screen.blit(background,(0, 0))