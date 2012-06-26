#!/usr/bin/python
# -*- coding: UTF-8 -*-
import os, sys
import pygame
from pygame.locals import *
from category import *
from play import *

class Hangman:
    def main(self, screen):
        clock = pygame.time.Clock()
        background = pygame.image.load('images\hangman_bg.png')
        screen.blit(background,(0, 0))
        
        pygame.font.init()
        my_font = pygame.font.Font('fonts\stylo_.ttf', 40)
        menu_offer = my_font.render("Изберете", True, (181, 76, 90))
        screen.blit(menu_offer, (280, 45))
        menu_offer = my_font.render("категория", True, (181, 76, 90))
        screen.blit(menu_offer, (360, 75))
        
        cat1 = Category('враца баце', screen, (370, 150))
        cat2 = Category('БГ филми', screen, (370, 200))
        cat3 = Category('БГ история', screen, (370, 250))
        cat4 = Category('БГ манджи', screen, (370, 300))
        cat5 = Category('рандом', screen, (370, 350))
        
        i = 1
        flag = False
        while True:
            clock.tick(30)

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
                if event.type == MOUSEBUTTONDOWN and i < 11:
                    if cat1.mouseOver(event.pos):
                        player = Play(screen, 'vraca')
                        flag = True
                    if player.random_word_lenght == len(player.chosen_letters) and i <= 10:
                        print("You win")
                    if not player.handle_mouse_events(event.pos, i):
                        i += 1
                    if i > 10:
                        print("Game over")
                    
                if event.type == pygame.KEYDOWN:
                   player.handle_events()
                
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