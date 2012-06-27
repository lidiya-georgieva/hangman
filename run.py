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
        """Draw the text 'Изберете катеогрия'"""
        menu_offer = self.my_font.render("Изберете", True, (181, 76, 90))
        screen.blit(menu_offer, (280, 45))
        menu_offer = self.my_font.render("категория", True, (181, 76, 90))
        screen.blit(menu_offer, (360, 75))
        
   
    def continue_playing(self, screen, is_winner):
        """Display play or quit options"""
        pygame.font.init()
        self.my_font = pygame.font.Font('fonts\stylo_.ttf', 40)
        if is_winner:
            message = self.my_font.render("Браво бе! Позна!", True, (181, 76, 90))  
        else:
            message = self.my_font.render("Epic Fail!!! ", True, (181, 76, 90))
        screen.blit(message, (230, 40))  
        return [Category("Продължи", screen, (370, 150)), Category("Изход", screen, (370, 200))]
        
    def display_losses_wins(self, losses, wins):
        pygame.font.init()
        self.my_font = pygame.font.Font('fonts\stylo_.ttf', 20)
        losses = self.my_font.render(str(losses) + " загуби", True, (83, 103, 150)) 
        screen.blit(losses, (530, 10))
        print("\n")
        wins = self.my_font.render(str(wins) + " победи", True, (83, 103, 150)) 
        screen.blit(wins, (530, 30))
        
     
    def display_the_not_guessed_word(self, word):
        pygame.font.init()
        self.my_font = pygame.font.Font('fonts\stylo_.ttf', 40)
        word = self.my_font.render(word + " загуби", True, (83, 103, 150)) 
        screen.blit(word, (130, 20))
        
    def main(self, screen, losses=0, wins=0, generated_words=list()):
        
        
        pygame.font.init()
        self.my_font = pygame.font.Font('fonts\stylo_.ttf', 40)
        
        play_or_quit = list()
        clock = pygame.time.Clock()
        background = pygame.image.load('images\hangman_bg.png')
        screen.blit(background,(0, 0))
        
        self.draw_text_choose_category(screen)
        self.display_losses_wins(losses, wins)
        
        categories = self.init_categories()
        
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
                        
                        return self.main(screen, losses, wins, generated_words)
                    elif play_or_quit[1].mouse_over(event.pos):
                        return
                        
                if event.type == MOUSEBUTTONDOWN and i < 11:
                    #for cat in categories:
                    if categories[0].mouse_over(event.pos):
                        player = Play(screen, categories[0].name, generated_words)
                        flag = True
                    elif categories[1].mouse_over(event.pos):
                        player = Play(screen, categories[1].name, generated_words)
                        flag = True  
                        
                    if player:
                        if not player.handle_mouse_events(event.pos, i):
                            i += 1
                        if i > 10 or player.handle_mouse_events(event.pos, i) == "WINNER":
                            if player.handle_mouse_events(event.pos, i) == "WINNER":
                                is_winner = True
                                wins += 1
                            else: 
                                is_winner = False
                                losses += 1
                                #self.display_the_not_guessed_word(player.handle_mouse_events(event.pos, i))
                            pygame.display.update()
                            pygame.time.delay(2000)
                            background = pygame.image.load('images\hangman_bg.png')
                            screen.blit(background, (0, 0))
                            play_or_quit = self.continue_playing(screen, is_winner)
                    
               
                
            if not flag:
                for category in categories:
                        category.draw(screen)
                     
            pygame.display.update()
            
            
            
if __name__ == '__main__':
    pygame.init()
    screen = pygame.display.set_mode((700, 515), 0, 32)
    pygame.display.set_caption('Challenge accepted!')
    Hangman().main(screen)