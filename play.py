#!/usr/bin/python
# -*- coding: UTF-8 -*-
import os, sys, random
import pygame
from pygame.locals import *


class Play:
    def __init__(self, screen, chosen_category):
        background = pygame.image.load('images\hangman_empty.png')
        screen.blit(background, (0, 0))
        random_word_lenght = len(self.load_word(chosen_category))
        self.screen = screen

        i = 0
        while i < random_word_lenght:
            underline_image = pygame.image.load('images/underline_word.png')
            screen.blit(underline_image, (400 + i*35, 200))
            i = i + 1
        self.letters = list()
        pygame.font.init()
        self.my_font = pygame.font.Font('fonts\stylo_.ttf', 30)
        self.display_alphabet(screen)
    
    def alphabet_list(self):
        """Return list with bulgarian letters"""
        with open('dict_files/bulgarian_alphabet.txt') as source_file:
            alphabet = source_file.readlines()
        alphabet = [(letter.strip()) for letter in alphabet]
        return alphabet
    
    def display_alphabet(self, screen):
        """Show the letters in bulgarian alphabet in 6x5 rectangle"""
        alphabet = self.alphabet_list()
        letter_space = 0
        slice = 0
        while slice < 30:
            for letter in alphabet[slice : slice + 6]:
                self.letters.append(Letter((400 + letter_space, 300 + slice * 6), self.my_font, letter, screen))
                letter_space += 30
            slice += 6
            letter_space = 0
            
        
    def main(self, screen):
        background = pygame.image.load('images\hangman_play.png')
        screen.blit(background,(0, 0))
    
    def load_word(self, category_name):
        """Load a random word from a file"""
        filename = 'dict_files/' + category_name + '.txt'
        with open(filename) as source_file:
            buffer = source_file.readlines()
        self.word = random.choice(buffer)
        return self.word
        
    def handle_events(self):
        """Handle keyboard events"""
        key = pygame.key.get_pressed()
        if key[pygame.K_a]:
            print("letter a is pressed")
        #pygame.display.flip()
    
    def handle_mouse_events(self, pos, i):
        """Handle mouse events"""
        for letter in self.letters:
            if letter.mouse_over(pos):
                if letter.let not in self.word:
                    self.load_part_i(i)
                    return False
                else:
                    index = self.word.index(letter.let)
                    self.display_guessed_letter(index, letter.let)
                    return True
        return True
        
    def display_guessed_letter(self, index, letter):
        show_letter = self.my_font.render(letter, True, (48, 79, 157))
        self.screen.blit(show_letter, (400 + index*35, 170))
     
    def load_part_i(self, i):
        """Load a part of the hangman"""
        image = pygame.image.load('images\hangman_' + str(i) + '.png')
        if i == 1:
            self.screen.blit(image, (8, 450))
        elif i == 2:
            self.screen.blit(image, (95, 45))
        elif i == 3:
            self.screen.blit(image, (110, 36))
        elif i == 4:
            self.screen.blit(image, (260, 47))
        elif i == 5:
            self.screen.blit(image, (202, 110))
        elif i == 6: 
            self.screen.blit(image, (260, 220))
        elif i == 7: 
            self.screen.blit(image, (180, 230))
        elif i == 8: 
            self.screen.blit(image, (270, 230))
        elif i == 9: 
            self.screen.blit(image, (270, 350))
        elif i == 10: 
            self.screen.blit(image, (210, 350))
 
 
class Letter:
    def __init__(self, pos, my_font, letter, screen):
        self.my_font = my_font
        self.pos = pos
        self.normal = self.my_font.render(letter, True, (181, 76, 90), (195, 190, 187))
        self.highlight = self.my_font.render(letter, True, (181, 76, 90), (165, 175, 184))
        self.image = self.normal
        self.show = screen.blit(self.image, self.pos)
        self.let = letter
        
        
    def mouse_over(self, pos):
        if self.show.collidepoint(pos):
            self.image = self.highlight
            return True
        else:
            self.image = self.normal
            return False
        
    def draw(self, screen):
        self.show = screen.blit(self.image, self.pos)
    
       
       
       
       
       