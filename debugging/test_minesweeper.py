#!/usr/bin/python3
import unittest
from minesweeper import Minesweeper

class TestMinesweeper(unittest.TestCase):
    def test_initialization(self):
        """Test if the game initializes correctly"""
        game = Minesweeper(width=5, height=5, mines=5)
        self.assertEqual(len(game.mines), 5)
        self.assertEqual(len(game.field), 5)
        self.assertEqual(len(game.field[0]), 5)

    def test_count_mines(self):
        """Test mine counting around a cell"""
        game = Minesweeper(width=3, height=3, mines=1)
        game.mines = {4}  # Centre de la grille 3x3
        self.assertEqual(game.count_mines_nearby(0, 0), 1)
        self.assertEqual(game.count_mines_nearby(1, 1), 0)

    def test_win_condition(self):
        """Test winning condition"""
        game = Minesweeper(width=2, height=2, mines=1)
        game.mines = {0}  # Mine en (0,0)
        game.reveal(1, 0)
        game.reveal(0, 1)
        game.reveal(1, 1)
        self.assertTrue(game.all_non_mine_cells_revealed())

    def test_lose_condition(self):
        """Test losing condition"""
        game = Minesweeper(width=2, height=2, mines=1)
        game.mines = {0}  # Mine en (0,0)
        self.assertFalse(game.reveal(0, 0))

    def test_reveal_empty_cell(self):
        """Test revealing an empty cell"""
        game = Minesweeper(width=3, height=3, mines=1)
        game.mines = {0}  # Mine en (0,0)
        self.assertTrue(game.reveal(2, 2))
        self.assertTrue(game.revealed[2][2])

if __name__ == '__main__':
    unittest.main(verbosity=2) 