from dataclasses import dataclass, field
from collections import OrderedDict
from typing import List

SUITS = OrderedDict([
    ('Spades', '♠'),
    ('Diamonds', '♦'),
    ('Hearts', '♥'),
    ('Clubs', '♣')])

NUMBERS = list(range(2, 14))

@dataclass
class Card:
    """
    Represents a playing card with a suit and number.
    """

    suit: str
    number: int
    
    def __post_init__(self):
        
        """
        Validates the suit and number values of the card.
        Raises a ValueError if the values are invalid.
        """
        
        if self.suit not in SUITS: raise ValueError(f"Invalid suit value. Use one of {', '.join(SUITS.keys())}")
        if self.number not in NUMBERS: raise ValueError(f"Invalid number value. Use one within {NUMBERS[0]} and {NUMBERS[-1]}")
        
    def __repr__(self):
        """
        Returns a string representation of the card.
        """
        card_print =  "\n".join(
        [f"""{self.number}{'-'*9}""",
        f"""|{' '*9}|""",
        f"""|{' '*4}{SUITS[self.suit]}{' '*4}|""",
        f"""|{' '*9}|""",
        f"""{'-'*9}{self.number}"""])
        return card_print
        
    def __gt__(self, other):
        """
        Compares two cards based on their number and suit.
        Returns True if the current card is greater than the other card, False otherwise.
        TODO: Though it works as it is, Lesser than should be implemented too
        """
        if self.number == other.number:
            return SUITS[self.suit] < SUITS[other.suit]
        else:
            return self.number > other.number

def build_deck():
    return [Card(suit, number) for suit in SUITS for number in NUMBERS]

@dataclass
class Deck:
    cards: List[Card] = field(default_factory=build_deck)