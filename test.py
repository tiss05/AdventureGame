import unittest
import re
import numpy as np
import random
import tracemalloc
from game import AdventureGame

class TestAdventureGame(unittest.TestCase):

    def setUp(self):
        self.game = AdventureGame()
        self.game.marker = 'T'
        self.game.user_name = 'Test'

    def test_movement_sequence(self):
        """Test if movement sequence 'NESSOONNNEEESSSSOOOONNNNN' updates correctly."""
        print("\033[1mTest 1 - Test if movement sequence updates correctly.\033[0m")
        direction_sequence = "NESSOONNNEEESSSSOOOONNNNN"
        for direction in direction_sequence:
            self.game.move_player(direction)
        expc_row = 2
        expc_col = 3
        self.assertEqual(self.game.marker, 'T')
        self.assertEqual(self.game.row, expc_row)
        self.assertEqual(self.game.col, expc_col)
        unique_visited = len(self.game.visited)
        self.assertGreaterEqual(len(self.game.adopted), unique_visited)

    
    def test_edge_case_all_directions(self):
        print("\033[1mTest 2 - Test edge case with all directions.\033[0m")
        self.game.row = self.game.grid_size // 2
        self.game.col = self.game.grid_size // 2
        initial_adopted = len(self.game.adopted)
        direction_sequence = "NSEO" * 10 
        for direction in direction_sequence:
            self.game.move_player(direction)
        self.assertGreater(len(self.game.adopted), initial_adopted)
        self.assertLessEqual(len(self.game.adopted), initial_adopted + 8)

    def test_initial_position(self):
        """Test if the user starts at the default position with the correct grid and initial animal."""
        print("\033[1mTest 3 - Test if the user starts at the default position.\033[0m")
        self.assertEqual(self.game.grid.shape, (10, 10))
        self.assertEqual(self.game.row, 5)
        self.assertEqual(self.game.col, 5)
        self.assertEqual(self.game.grid[5, 5], False)
        self.assertEqual(len(self.game.adopted), 1)
        self.assertEqual(self.game.adopted, ['Labrador'])

    def test_small_input(self):
        """Test a large number of moves to ensure the game logic handles long input."""
        print("\033[1mTest 4 - Test small input (100.000 steps).\033[0m")
        initial_adopted = len(self.game.adopted)
        direction_sequence = "ONES" * 25000
        for direction in direction_sequence:
            self.game.move_player(direction)
        self.assertGreater(len(self.game.adopted), initial_adopted)

    def test_large_input(self):
        """Test large input (6.000.000 steps)."""
        print("\033[1mTest 5 - Test large input (6,000,000 steps).\033[0m")
        initial_adopted = len(self.game.adopted)
        direction_sequence = "NNNSSS" * 1000000
        for direction in direction_sequence:
            self.game.move_player(direction)
        self.assertGreater(len(self.game.adopted), initial_adopted)


    def test_no_extra_animals_for_revisiting(self):
        """Test if moving south and north doesn't increase animal count."""
        print("\033[1mTest 6 - Test if moving south and north doesn't increase animal count.\033[0m")
        initial_adopted = len(self.game.adopted)
        for direction in "SSS":
            self.game.move_player(direction)
        after_south = len(self.game.adopted)
        for direction in "NNN":
            self.game.move_player(direction)
        self.assertEqual(len(self.game.adopted), after_south)

    def test_track_memory_usage(self):
        """Test about tracking memory usage with large input."""
        print("\033[1mTest 7 - Test about tracking memory usage.\033[0m")
        tracemalloc.start()
        initial_adopted = len(self.game.adopted)
        direction_sequence = "NNNNNSSSSS" * 500000
        for direction in direction_sequence:
            self.game.move_player(direction)
        self.assertGreater(len(self.game.adopted), initial_adopted)
        current, peak = tracemalloc.get_traced_memory()
        print(f"Utilização atual da memória: {current / 10**6:.6f} MB")
        print(f"Pico de utilização de memória: {peak / 10**6:.6f} MB")
        tracemalloc.stop()

if __name__ == "__main__":
    suite = unittest.TestSuite()
    suite.addTest(TestAdventureGame('test_movement_sequence'))
    suite.addTest(TestAdventureGame('test_edge_case_all_directions'))
    suite.addTest(TestAdventureGame('test_initial_position'))
    suite.addTest(TestAdventureGame('test_small_input'))
    suite.addTest(TestAdventureGame('test_large_input'))
    suite.addTest(TestAdventureGame('test_no_extra_animals_for_revisiting'))
    suite.addTest(TestAdventureGame('test_track_memory_usage'))
    runner = unittest.TextTestRunner()
    runner.run(suite)