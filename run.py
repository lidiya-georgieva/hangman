#!/usr/bin/python
# -*- coding: UTF-8 -*-
import os, sys
import pygame
from pygame.locals import *
from category import *
from play import *

class Hangman:
    def main(self, screen):
        background = pygame.image.load('images\hangman_bg.png')
        screen.blit(background,(0, 0))
        
        pygame.font.init()
        my_font = pygame.font.Font('fonts\stylo_.ttf', 40)
        menu_offer = my_font.render("Изберете", True, (181, 76, 90))
        screen.blit(menu_offer, (280, 45))
        menu_offer = my_font.render("категория", True, (181, 76, 90))
        screen.blit(menu_offer, (360, 75))
        
        def startButtonCb(screen): g = Play().main(screen)
        cat1 = Category('враца баце', screen, (370, 150), startButtonCb)
        cat2 = Category('БГ филми', screen, (370, 200))
        cat3 = Category('БГ история', screen, (370, 250))
        cat4 = Category('БГ манджи', screen, (370, 300))
        cat5 = Category('рандом', screen, (370, 350))
        
        flag = False
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    return
                if event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
                    return
                if event.type == MOUSEMOTION:
                    cat1.mouseOver(event.pos)
                    cat2.mouseOver(event.pos)
                    cat3.mouseOver(event.pos)
                    cat4.mouseOver(event.pos)
                    cat5.mouseOver(event.pos)
                if event.type == MOUSEBUTTONDOWN:
                    if cat1.mouseOver(event.pos):
                        cat1.callback(screen)
                        flag = True
                         
            if not flag:
                cat1.draw(screen)
                cat2.draw(screen)
                cat3.draw(screen)
                cat4.draw(screen)
                cat5.draw(screen)
            pygame.display.update()
            
            
            
if __name__ == '__main__':
    pygame.init()
    screen = pygame.display.set_mode((600, 515), 0, 32)
    pygame.display.set_caption('Challenge accepted!')
    Hangman().main(screen)