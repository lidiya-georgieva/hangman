#!/usr/bin/python
# -*- coding: UTF-8 -*-
import os
import sys
import random
import pygame
from pygame.locals import *


class Player:

    def __init__(self, screen, chosen_category, generated_words):
        """Initialize the game field"""
        self.background = pygame.image.load('images\hangman_empty.png')
        screen.blit(self.background, (0, 0))
        pygame.font.init()
        self.my_font = pygame.font.Font('fonts\stylo_.ttf', 30)
        self.generated_words = generated_words
        self.letters = list()
        self.chosen_letters = list()
        self.right_letters = list()
        self.alphabet = self.alphabet_list()
        self.screen = screen
        self.word = self.load_word(chosen_category)
        self.display_underlines()
        self.display_alphabet()

    def display_underlines(self):
        """Display the underlines,
        each line for each letter in the must-guess word"""
        ith_line = 0
        self.underline_count = 0
        for char in self.word:
            if char != ' ':
                underline_image = pygame.image.load('images/underline_word.png')
                self.screen.blit(underline_image, (400 + ith_line * 35, 200))
                self.underline_count += 1
            ith_line += 1

    def alphabet_list(self):
        """Return list with bulgarian letters"""
        with open('dict_files/bulgarian_alphabet.txt') as source_file:
            alphabet = source_file.readlines()
        return [(letter.strip()) for letter in alphabet]

    def display_alphabet(self):
        """Show the letters in bulgarian alphabet in 6x5 rectangle"""
        letter_space = 0
        slice = 0
        while slice < 30:
            for character in self.alphabet[slice: slice + 6]:
                letter = Letter((400 + letter_space, 300 + slice * 6), self.my_font, character, self.screen)
                self.letters.append(letter)
                letter_space += 30
            slice += 6
            letter_space = 0

    def load_word(self, category_name):
        """Load a random word from a file"""
        filename = 'dict_files/' + category_name + '.txt'
        with open(filename) as source_file:
            buffer = source_file.readlines()

        if len(buffer) == len(self.generated_words):
            return 
        word = random.choice(buffer).strip()
        while word in self.generated_words:
            word = random.choice(buffer).strip()
        self.generated_words.append(word)
        return word

    def handle_mouse_events(self, pos, ith_part_of_hangman):
        """Handle mouse events"""
        (x, y) = pos
        for letter in self.letters:
            if len(self.right_letters) == self.underline_count:
                return "WINNER"
            elif ith_part_of_hangman > 10:
                self.display_not_guessed_letters()
            elif letter.mouse_over(pos) and letter not in self.chosen_letters:
                self.screen.blit(self.background, letter.pos, pygame.Rect(x, y, 25, 25))
                self.chosen_letters.append(letter)
                if letter.name not in self.word:
                    self.load_part_i(ith_part_of_hangman)
                    return False
                else:
                    indices = [n for n in range(len(self.word)) if self.word.find(letter.name, n) == n]
                    self.display_guessed_letters(indices, letter.name)
        return True

    def display_not_guessed_letters(self):
        """Display the not guessed letters in case of loss"""
        for char in self.word:
            if char not in self.right_letters:
                indices = [n for n in range(len(self.word)) if self.word.find(char, n) == n]
                for index in indices:
                    show_letter = self.my_font.render(char, True, (247, 228, 99))
                    self.screen.blit(show_letter, (400 + index * 35, 170))

    def display_guessed_letters(self, indices, letter, color=(48, 79, 157)):
        """Display the right guessed letters"""
        for index in indices:
            self.right_letters.append(letter)
            show_letter = self.my_font.render(letter, True, color)
            self.screen.blit(show_letter, (400 + index * 35, 170))

    def load_part_i(self, i):
        """Load a part of the hangman"""
        image = pygame.image.load('images\hangman_' + str(i) + '.png')
        parts_positions_on_screen = {1: (8, 450), 2: (95, 45), 3: (110, 36), 
                                     4: (260, 47), 5: (202, 110), 6: (260, 220), 
                                     7: (180, 230), 8: (270, 230), 9: (270, 350), 
                                     10: (210, 350)}
        self.screen.blit(image, parts_positions_on_screen[i])


class Letter:

    def __init__(self, pos, my_font, letter, screen):
        self.my_font = my_font
        self.pos = pos
        self.normal = self.my_font.render(letter, True, (181, 76, 90))
        self.highlight = self.my_font.render(letter, True, (181, 76, 90), (255, 255, 0))
        self.image = self.normal
        self.show = screen.blit(self.image, self.pos)
        self.name = letter

    def mouse_over(self, pos):
        if self.show.collidepoint(pos):
            self.image = self.highlight
            return True
        else:
            self.image = self.normal
            return False

    def draw(self, screen):
        self.show = screen.blit(self.image, self.pos) 