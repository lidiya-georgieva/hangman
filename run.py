#!/usr/bin/python
# -*- coding: UTF-8 -*-
import os, sys
import pygame
from pygame.locals import *
from category import *
from play import *

class Hangman:
    def init_categories(self):
        """Initialize the categories for the game"""
        category_y = 150
        categories = list()
        categories_names = ['враца баце', 'БГ филми', 'БГ история', 'БГ манджи', 'рандом']
        for category in categories_names:
            categories.append(Category(category, screen, (370, category_y)))
            category_y += 50
        return categories   
    
    def draw_text_choose_category(self, screen):
        pygame.font.init()
        my_font = pygame.font.Font('fonts\stylo_.ttf', 40)
        menu_offer = my_font.render("Изберете", True, (181, 76, 90))
        screen.blit(menu_offer, (280, 45))
        menu_offer = my_font.render("категория", True, (181, 76, 90))
        screen.blit(menu_offer, (360, 75))
        
   
    def continue_playing(self, screen):
        """Display play or quit options"""
        return [Category("Продължи", screen, (370, 150)), Category("Изход", screen, (370, 200))]
        
        
        
    def main(self, screen):
        print("how many")
        play_or_quit = list()
        clock = pygame.time.Clock()
        background = pygame.image.load('images\hangman_bg.png')
        screen.blit(background,(0, 0))
        
        self.draw_text_choose_category(screen)
        categories = self.init_categories()
        continue_p = None
        player = None
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
                    for category in categories:
                        category.mouse_over(event.pos)
                    for option in play_or_quit:
                        option.mouse_over(event.pos)
                        option.draw(screen)   
                        pygame.display.update()
                
                if event.type == MOUSEBUTTONDOWN and len(play_or_quit):
                    if play_or_quit[0].mouse_over(event.pos):
                        pass
                    elif play_or_quit[1].mouse_over(event.pos):
                        return
                        
                if event.type == MOUSEBUTTONDOWN and i < 11:
                    if categories[0].mouse_over(event.pos):
                        player = Play(screen, 'vraca')
                        flag = True
                   
                    """if player and player.handle_mouse_events(event.pos, i):
                        print("Partyy")
                    if player and not player.handle_mouse_events(event.pos, i):
                        print("hereee")
                        i += 1
                    if i > 10:
                        pygame.display.update()
                        pygame.time.delay(1000)
                        background = pygame.image.load('images\hangman_bg.png')
                        screen.blit(background, (0, 0))
                        play_or_quit = self.continue_playing(screen)"""
                    if player and not player.handle_mouse_events(event.pos, i):
                        i += 1
                    if i > 10 or (player and player.handle_mouse_events(event.pos, i) == "WINNER"):
                        pygame.display.update()
                        pygame.time.delay(1000)
                        background = pygame.image.load('images\hangman_bg.png')
                        screen.blit(background, (0, 0))
                        play_or_quit = self.continue_playing(screen)
                    
               
                
            if not flag:
                for category in categories:
                        category.draw(screen)
                     
            pygame.display.update()
            
            
            
if __name__ == '__main__':
    pygame.init()
    screen = pygame.display.set_mode((600, 515), 0, 32)
    pygame.display.set_caption('Challenge accepted!')
    Hangman().main(screen)