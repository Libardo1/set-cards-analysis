from exercise import *
import unittest

class TestStringMethods(unittest.TestCase):
    def test_card_from_list_to_str(self):
        A = Card.from_list([2,0,0,2])
        self.assertEqual(A.to_str(), 'purple wiggle empty 3')
    def test_card_from_str_to_list(self):
        A = Card.from_str("red wiggle empty 2")
        self.assertEqual(A.to_list(), [0,0,0,1])
    def test_card_from_list_properties(self):
        A = Card.from_list([1,1,1,1])
        self.assertTrue(A.shape == 1)
        self.assertTrue(A.color == 1)
        self.assertTrue(A.number == 1)
        self.assertTrue(A.fill == 1)
    def test_board_add_and_remove_card(self):
        X = Board()
        A = Card.from_list([2,0,0,2])
        self.assertTrue(X.number_of_cards() == 0)
        X.add_card(A)
        self.assertTrue(X.number_of_cards() == 1)
        X.remove_card(A)
        self.assertTrue(X.number_of_cards() == 0)
    def test_board_first_set(self):
        X = Board()
        A = Card.from_list([0,0,0,0])
        B = Card.from_list([0,0,0,1])
        C = Card.from_list([0,0,0,2])
        X.add_card(A)
        X.add_card(B)
        X.add_card(C)
        self.assertTrue(len(X.find_sets()) == 1)
        X.collect_set(A,B,C)
        self.assertTrue(len(X.find_sets()) == 0)
    def test_board_invalid_set(self):
        X = Board()
        A = Card.from_list([0,0,0,0])
        B = Card.from_list([0,0,0,1])
        C = Card.from_list([0,0,1,2])
        X.add_card(A)
        X.add_card(B)
        X.add_card(C)
        self.assertTrue(len(X.find_sets()) == 0)
        with self.assertRaises(Exception) as raises_cm:
            X.collect_set(A,B,C)
        exception = raises_cm.exception
        self.assertRaises(exception)
    def test_board_two_sets_on_board(self):
        X = Board()
        A = Card.from_list([0,0,0,0])
        B = Card.from_list([0,0,0,1])
        C = Card.from_list([0,0,0,2])
        D = Card.from_list([1,0,0,0])
        E = Card.from_list([2,0,0,0])
        X.add_card(A)
        X.add_card(B)
        X.add_card(C)
        self.assertTrue(len(X.find_sets()) == 1)
        X.add_card(D)
        self.assertTrue(len(X.find_sets()) == 1)
        X.add_card(E)
        self.assertTrue(len(X.find_sets()) == 2)
        X.remove_card(D)
        self.assertTrue(len(X.find_sets()) == 1)
        X.add_card(D)
        self.assertTrue(len(X.find_sets()) == 2)
        X.collect_set(A,D,E)
        self.assertTrue(len(X.find_sets()) == 0)

if __name__ == '__main__':
    unittest.main()
