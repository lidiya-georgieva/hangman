import unittest
import pygame
from run import *
from player import *


class HangmanTest(unittest.TestCase):
    def setUp(self):
        pygame.init()
        self.screen = pygame.display.set_mode((700, 515), 0, 32)
        self.hangman = Hangman(self.screen)
    
    def test_init_categories(self):
        categories = self.hangman.init_categories()
        self.assertEqual(len(categories), 5)

    def test_right_number_of_displayed_underlines(self):
        player = Player(self.screen, 'враца баце', list())
        self.assertEqual(len(player.word), player.underline_count)
    
    def test_loaded_word_not_empty(self):
        player = Player(self.screen, 'враца баце', list())
        word = player.load_word('враца баце')
        self.assertIsNotNone(word)
    
    def test_dictionary_files_existance(self):
        player = Player(self.screen, 'враца баце', list())
        self.assertRaises(IOError, player.load_word, 'враца бац')
    
    def test_right_loaded_bulgarian_alphabet(self):
        player = Player(self.screen, 'враца баце', list())
        self.assertEqual(len(player.alphabet), 30)
        self.assertEqual(len(player.letters), 30)
    
    """def test_font_file_existance(self):
        self.assertRaises(IOError, self.hangman.init_font, 40)"""
    
    def test_loaded_font_object_not_none(self):
        font = self.hangman.init_font(40)
        self.assertIsNotNone(font)
      
    #test_play_or_quit : извиквам и проверявам върнатия резултат
    
    #display_losses_wins(self, losses, wins):проверявам загубите дали са равни на еди какво си

    #mouse_over(self, pos):
if __name__ == "__main__":
    unittest.main()