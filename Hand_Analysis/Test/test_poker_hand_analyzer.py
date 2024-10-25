import unittest

from Hand_Analysis.card import Card, Suit, Rank
from Hand_Analysis.hand_analyzer import PokerHandAnalyzer  # Adjust this import based on your actual module structure


class TestPokerHandAnalyzer(unittest.TestCase):

    def create_card(self, suit, rank):
        """Helper function to create a card."""
        return Card(suit, rank)

    def test_royal_flush(self):
        cards = [
            self.create_card(Suit.HEARTS, Rank.TEN),
            self.create_card(Suit.HEARTS, Rank.JACK),
            self.create_card(Suit.HEARTS, Rank.QUEEN),
            self.create_card(Suit.HEARTS, Rank.KING),
            self.create_card(Suit.HEARTS, Rank.ACE),
            self.create_card(Suit.DIAMONDS, Rank.NINE),
            self.create_card(Suit.CLUBS, Rank.EIGHT)
        ]
        analyzer = PokerHandAnalyzer(cards)
        self.assertEqual(analyzer.get_best_hand(), (1))

    def test_royal_flush_edge_case(self):
        cards = [
            self.create_card(Suit.HEARTS, Rank.ACE),
            self.create_card(Suit.HEARTS, Rank.KING),
            self.create_card(Suit.HEARTS, Rank.QUEEN),
            self.create_card(Suit.HEARTS, Rank.JACK),
            self.create_card(Suit.HEARTS, Rank.TEN),
            self.create_card(Suit.DIAMONDS, Rank.ACE),
            self.create_card(Suit.CLUBS, Rank.ACE)
        ]
        analyzer = PokerHandAnalyzer(cards)
        self.assertEqual(analyzer.get_best_hand(), (1, "Royal Flush"))

    def test_royal_flush_invalid(self):
        cards = [
            self.create_card(Suit.HEARTS, Rank.ACE),
            self.create_card(Suit.HEARTS, Rank.KING),
            self.create_card(Suit.HEARTS, Rank.QUEEN),
            self.create_card(Suit.HEARTS, Rank.JACK),
            self.create_card(Suit.DIAMONDS, Rank.TEN),
            self.create_card(Suit.DIAMONDS, Rank.NINE),
            self.create_card(Suit.DIAMONDS, Rank.EIGHT)
        ]
        analyzer = PokerHandAnalyzer(cards)
        self.assertNotEqual(analyzer.get_best_hand(), (1, "Royal Flush"))

    def test_royal_flush_missing_card(self):
        cards = [
            self.create_card(Suit.HEARTS, Rank.TEN),
            self.create_card(Suit.HEARTS, Rank.JACK),
            self.create_card(Suit.HEARTS, Rank.QUEEN),
            self.create_card(Suit.HEARTS, Rank.KING),
            self.create_card(Suit.SPADES, Rank.ACE),
            self.create_card(Suit.DIAMONDS, Rank.NINE),
            self.create_card(Suit.CLUBS, Rank.EIGHT)
        ]
        analyzer = PokerHandAnalyzer(cards)
        self.assertNotEqual(analyzer.get_best_hand(), (1, "Royal Flush"))

    def test_straight_flush(self):
        cards = [
            self.create_card(Suit.HEARTS, Rank.NINE),
            self.create_card(Suit.HEARTS, Rank.TEN),
            self.create_card(Suit.HEARTS, Rank.JACK),
            self.create_card(Suit.HEARTS, Rank.QUEEN),
            self.create_card(Suit.HEARTS, Rank.KING),
            self.create_card(Suit.DIAMONDS, Rank.ACE),
            self.create_card(Suit.CLUBS, Rank.ACE)
        ]
        analyzer = PokerHandAnalyzer(cards)
        self.assertEqual(analyzer.get_best_hand(), (2, "Straight Flush"))

    def test_straight_flush_with_ace_low(self):
        cards = [
            self.create_card(Suit.HEARTS, Rank.ACE),
            self.create_card(Suit.HEARTS, Rank.TWO),
            self.create_card(Suit.HEARTS, Rank.THREE),
            self.create_card(Suit.HEARTS, Rank.FOUR),
            self.create_card(Suit.HEARTS, Rank.FIVE),
            self.create_card(Suit.DIAMONDS, Rank.SIX),
            self.create_card(Suit.CLUBS, Rank.SEVEN)
        ]
        analyzer = PokerHandAnalyzer(cards)
        self.assertEqual(analyzer.get_best_hand(), (2, "Straight Flush"))

    def test_straight_flush_with_flush(self):
        cards = [
            self.create_card(Suit.HEARTS, Rank.NINE),
            self.create_card(Suit.HEARTS, Rank.TEN),
            self.create_card(Suit.HEARTS, Rank.JACK),
            self.create_card(Suit.HEARTS, Rank.QUEEN),
            self.create_card(Suit.HEARTS, Rank.KING),
            self.create_card(Suit.DIAMONDS, Rank.ACE),
            self.create_card(Suit.CLUBS, Rank.ACE)
        ]
        analyzer = PokerHandAnalyzer(cards)
        self.assertEqual(analyzer.get_best_hand(), (2, "Straight Flush"))

    def test_straight_flush_invalid(self):
        cards = [
            self.create_card(Suit.HEARTS, Rank.NINE),
            self.create_card(Suit.HEARTS, Rank.TEN),
            self.create_card(Suit.HEARTS, Rank.JACK),
            self.create_card(Suit.DIAMONDS, Rank.QUEEN),
            self.create_card(Suit.HEARTS, Rank.KING),
            self.create_card(Suit.DIAMONDS, Rank.ACE),
            self.create_card(Suit.CLUBS, Rank.ACE)
        ]
        analyzer = PokerHandAnalyzer(cards)
        self.assertNotEqual(analyzer.get_best_hand(), (2, "Straight Flush"))

    def test_four_of_a_kind(self):
        cards = [
            self.create_card(Suit.HEARTS, Rank.TEN),
            self.create_card(Suit.DIAMONDS, Rank.TEN),
            self.create_card(Suit.CLUBS, Rank.TEN),
            self.create_card(Suit.SPADES, Rank.TEN),
            self.create_card(Suit.HEARTS, Rank.ACE),
            self.create_card(Suit.DIAMONDS, Rank.KING),
            self.create_card(Suit.CLUBS, Rank.QUEEN)
        ]
        analyzer = PokerHandAnalyzer(cards)
        self.assertEqual(analyzer.get_best_hand(), (3, "Four of a Kind"))

    def test_four_of_a_kind_with_pair(self):
        cards = [
            self.create_card(Suit.HEARTS, Rank.TEN),
            self.create_card(Suit.DIAMONDS, Rank.TEN),
            self.create_card(Suit.CLUBS, Rank.TEN),
            self.create_card(Suit.SPADES, Rank.TEN),
            self.create_card(Suit.HEARTS, Rank.ACE),
            self.create_card(Suit.DIAMONDS, Rank.ACE),
            self.create_card(Suit.CLUBS, Rank.QUEEN)
        ]
        analyzer = PokerHandAnalyzer(cards)
        self.assertEqual(analyzer.get_best_hand(), (3, "Four of a Kind"))

    def test_four_of_a_kind_invalid(self):
        cards = [
            self.create_card(Suit.HEARTS, Rank.TEN),
            self.create_card(Suit.DIAMONDS, Rank.TEN),
            self.create_card(Suit.CLUBS, Rank.NINE),
            self.create_card(Suit.SPADES, Rank.TEN),
            self.create_card(Suit.HEARTS, Rank.ACE),
            self.create_card(Suit.DIAMONDS, Rank.KING),
            self.create_card(Suit.CLUBS, Rank.QUEEN)
        ]
        analyzer = PokerHandAnalyzer(cards)
        self.assertNotEqual(analyzer.get_best_hand(), (3, "Four of a Kind"))

    def test_full_house(self):
        cards = [
            self.create_card(Suit.HEARTS, Rank.TEN),
            self.create_card(Suit.DIAMONDS, Rank.TEN),
            self.create_card(Suit.CLUBS, Rank.TEN),
            self.create_card(Suit.SPADES, Rank.NINE),
            self.create_card(Suit.HEARTS, Rank.NINE),
            self.create_card(Suit.DIAMONDS, Rank.ACE),
            self.create_card(Suit.CLUBS, Rank.QUEEN)
        ]
        analyzer = PokerHandAnalyzer(cards)
        self.assertEqual(analyzer.get_best_hand(), (4, "Full House"))

    def test_full_house_invalid(self):
        cards = [
            self.create_card(Suit.HEARTS, Rank.TEN),
            self.create_card(Suit.DIAMONDS, Rank.NINE),
            self.create_card(Suit.CLUBS, Rank.NINE),
            self.create_card(Suit.SPADES, Rank.TEN),
            self.create_card(Suit.HEARTS, Rank.ACE),
            self.create_card(Suit.DIAMONDS, Rank.KING),
            self.create_card(Suit.CLUBS, Rank.QUEEN)
        ]
        analyzer = PokerHandAnalyzer(cards)
        self.assertNotEqual(analyzer.get_best_hand(), (4, "Full House"))

    def test_flush(self):
        cards = [
            self.create_card(Suit.HEARTS, Rank.TEN),
            self.create_card(Suit.HEARTS, Rank.JACK),
            self.create_card(Suit.CLUBS, Rank.QUEEN),
            self.create_card(Suit.HEARTS, Rank.KING),
            self.create_card(Suit.HEARTS, Rank.ACE),
            self.create_card(Suit.DIAMONDS, Rank.NINE),
            self.create_card(Suit.HEARTS, Rank.EIGHT)
        ]
        analyzer = PokerHandAnalyzer(cards)
        self.assertEqual(analyzer.get_best_hand(), (5))

    def test_flush_with_straight(self):
        cards = [
            self.create_card(Suit.HEARTS, Rank.TEN),
            self.create_card(Suit.HEARTS, Rank.JACK),
            self.create_card(Suit.HEARTS, Rank.QUEEN),
            self.create_card(Suit.HEARTS, Rank.KING),
            self.create_card(Suit.DIAMONDS, Rank.NINE),
            self.create_card(Suit.HEARTS, Rank.TWO),
            self.create_card(Suit.SPADES, Rank.ACE)
        ]
        analyzer = PokerHandAnalyzer(cards)
        self.assertEqual(analyzer.get_best_hand(), (5, "Flush"))

    def test_flush_invalid(self):
        cards = [
            self.create_card(Suit.HEARTS, Rank.TEN),
            self.create_card(Suit.DIAMONDS, Rank.TEN),
            self.create_card(Suit.CLUBS, Rank.JACK),
            self.create_card(Suit.SPADES, Rank.QUEEN),
            self.create_card(Suit.HEARTS, Rank.ACE),
            self.create_card(Suit.DIAMONDS, Rank.NINE),
            self.create_card(Suit.CLUBS, Rank.EIGHT)
        ]
        analyzer = PokerHandAnalyzer(cards)
        self.assertNotEqual(analyzer.get_best_hand(), (5, "Flush"))

    def test_straight(self):
        cards = [
            self.create_card(Suit.HEARTS, Rank.NINE),
            self.create_card(Suit.DIAMONDS, Rank.TEN),
            self.create_card(Suit.CLUBS, Rank.JACK),
            self.create_card(Suit.SPADES, Rank.QUEEN),
            self.create_card(Suit.HEARTS, Rank.KING),
            self.create_card(Suit.DIAMONDS, Rank.ACE),
            self.create_card(Suit.CLUBS, Rank.EIGHT)
        ]
        analyzer = PokerHandAnalyzer(cards)
        self.assertEqual(analyzer.get_best_hand(), (6, "Straight"))

    def test_straight_with_ace_high(self):
        cards = [
            self.create_card(Suit.HEARTS, Rank.TEN),
            self.create_card(Suit.DIAMONDS, Rank.JACK),
            self.create_card(Suit.CLUBS, Rank.QUEEN),
            self.create_card(Suit.SPADES, Rank.KING),
            self.create_card(Suit.HEARTS, Rank.ACE),
            self.create_card(Suit.DIAMONDS, Rank.NINE),
            self.create_card(Suit.CLUBS, Rank.EIGHT)
        ]
        analyzer = PokerHandAnalyzer(cards)
        self.assertEqual(analyzer.get_best_hand(), (6, "Straight"))

    def test_straight_with_flush(self):
        cards = [
            self.create_card(Suit.HEARTS, Rank.TEN),
            self.create_card(Suit.HEARTS, Rank.JACK),
            self.create_card(Suit.HEARTS, Rank.QUEEN),
            self.create_card(Suit.HEARTS, Rank.KING),
            self.create_card(Suit.DIAMONDS, Rank.ACE),
            self.create_card(Suit.SPADES, Rank.NINE),
            self.create_card(Suit.CLUBS, Rank.EIGHT)
        ]
        analyzer = PokerHandAnalyzer(cards)
        self.assertEqual(analyzer.get_best_hand(), (6, "Straight"))


if __name__ == '__main__':
    unittest.main()
