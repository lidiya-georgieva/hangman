#!/usr/bin/python
# -*- coding: UTF-8 -*-
import os
import sys
import pygame
from pygame.locals import *
from category import *
from player import *


class Hangman:
    def __init__(self, screen):
        self.screen = screen

    def init_categories(self):
        """Initialize the categories for the game"""
        category_y = 150
        categories = list()
        categories_names = ['враца баце', 'БГ филми', 'БГ манджи', 'БГ история', 'БГ книги']
        for category in categories_names:
            categories.append(Category(category, self.screen, (370, category_y)))
            category_y += 50
        return categories   

    def draw_text_choose_category(self, screen):
        """Draw the text 'Изберете категория'"""
        my_font = self.init_font(40)
        menu_offer = my_font.render("Изберете", True, (181, 76, 90))
        screen.blit(menu_offer, (280, 45))
        menu_offer = my_font.render("категория", True, (181, 76, 90))
        screen.blit(menu_offer, (360, 75))

    def play_or_quit_options(self, screen, is_winner):
        """Display play or quit options"""
        my_font = self.init_font(40)
        if is_winner:
            message = my_font.render("Браво бе! Позна!", True, (181, 76, 90))  
        else:
            message = my_font.render("Epic Fail!!! ", True, (181, 76, 90))
        screen.blit(message, (230, 40))  
        return [Category("Продължи", screen, (370, 150)), Category("Изход", screen, (370, 200))]

    def display_losses_wins(self, losses, wins):
        """Display the number of losses and wins"""
        my_font = self.init_font(20)
        losses = my_font.render(str(losses) + " загуби", True, (83, 103, 150)) 
        screen.blit(losses, (530, 10))
        wins = my_font.render(str(wins) + " победи", True, (83, 103, 150)) 
        screen.blit(wins, (530, 30))

    def init_font(self, font_size):
        """Initialize font with size font_size"""
        pygame.font.init()
        return pygame.font.Font('fonts\stylo_.ttf', font_size)
    
    def player_functionality(self, player, pos):
        if not player.handle_mouse_events(pos, self.ith_part_of_hangman):
            self.ith_part_of_hangman += 1
        
        if player.handle_mouse_events(pos, self.ith_part_of_hangman) == "WINNER":
            is_winner = True
            self.wins += 1
        elif self.ith_part_of_hangman > 10: 
            is_winner = False
            self.losses += 1
        else: return
        pygame.display.update()
        pygame.time.delay(2000)
        background = pygame.image.load('images\hangman_bg.png')
        screen.blit(background, (0, 0))
        self.play_or_quit = self.play_or_quit_options(screen, is_winner)
    
    def hover_effect_play_quit_options(self, pos):
        for option in self.play_or_quit:
            option.mouse_over(pos)
            option.draw(screen)   
            pygame.display.update()
     
    def player_init(self, categories, pos, screen, generated_words):
        self.in_cat = True
        if categories[0].mouse_over(pos):
            self.player = Player(screen, categories[0].name, generated_words)
        elif categories[1].mouse_over(pos):
            self.player = Player(screen, categories[1].name, generated_words) 
        elif categories[2].mouse_over(pos):
            self.player = Player(screen, categories[2].name, generated_words)
        elif categories[3].mouse_over(pos):
            self.player = Player(screen, categories[3].name, generated_words)
        elif categories[4].mouse_over(pos):
            self.player = Player(screen, categories[4].name, generated_words)
        
    def main(self, losses=0, wins=0, generated_words=list()):
        clock = pygame.time.Clock()
        background = pygame.image.load('images\hangman_bg.png')
        screen.blit(background,(0, 0))
        
        self.play_or_quit = list()
        self.player = None
        self.ith_part_of_hangman = 1
        self.draw_text_choose_category(screen)
        self.display_losses_wins(losses, wins)
        categories = self.init_categories()
        hover_effect_off = False
        self.wins = wins
        self.losses = losses
        self.in_cat = False
        
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
                    self.hover_effect_play_quit_options(event.pos)
                    
                if event.type == MOUSEBUTTONDOWN:
                    if len(self.play_or_quit):
                        if self.play_or_quit[0].mouse_over(event.pos):
                            return self.main(self.losses, self.wins, generated_words)
                        elif self.play_or_quit[1].mouse_over(event.pos):
                            return     
                    elif self.ith_part_of_hangman < 11 and not self.in_cat:
                        self.player_init(categories, event.pos, screen, generated_words)
                        hover_effect_off = True  
                    elif self.player and self.ith_part_of_hangman < 11 and self.in_cat:
                        self.player_functionality(self.player, event.pos)   

            if not hover_effect_off:
                for category in categories:
                    category.draw(screen)     
                    
            pygame.display.update()
            
                       
if __name__ == '__main__':
    pygame.init()
    screen = pygame.display.set_mode((720, 515), 0, 32)
    pygame.display.set_caption('Challenge accepted!')
    Hangman(screen).main()