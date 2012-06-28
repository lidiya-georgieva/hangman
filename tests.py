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
        self.assertIsNotNone(player.underline_count)
    
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
   
    def test_loaded_font_object_not_none(self):
        font = self.hangman.init_font(40)
        self.assertIsNotNone(font)
    
    def test_play_and_quit_options(self):
        options = self.hangman.play_or_quit_options(self.screen, True)
        self.assertEqual(len(options), 2)
      
    def test_player_init_in_main_class(self):
        self.hangman.player_init(self.hangman.init_categories(), (433, 158), self.screen, list())
        self.assertIsNotNone(self.hangman.player)
    
    def test_has_a_background(self):
        player = Player(self.screen, 'враца баце', list())
        self.assertNotEqual(player.background, None)
        self.assertIsNotNone(player.my_font)
    
    def test_mouse_over_letter(self):
        player = Player(self.screen, 'враца баце', list())
        letter = player.letters[0]
        self.assertFalse(letter.mouse_over((0, 0)))
        self.assertTrue(letter.mouse_over((512, 313)))
    
    def test_mouse_over_category(self):
        categories = self.hangman.init_categories()
        category = categories[0]
        self.assertFalse(category.mouse_over((0, 0)))
        self.assertTrue(category.mouse_over((435, 167)))


if __name__ == "__main__":
    unittest.main()