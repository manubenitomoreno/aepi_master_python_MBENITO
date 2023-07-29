from cards import Card, Deck
from dataclasses import dataclass
from random import shuffle

@dataclass
class Player:
    name: str
    hand: Card = None
    points: int = 0
    
@dataclass
class Game:
    deck: Deck = Deck()
    nplayers: int = 2
    nplays: int = 5
    
    
    def make_players(self):
        return [Player(f"player_{n}") for n in range(0,self.nplayers)]
    
    def assign_card(self, deck, player):
        shuffle(deck.cards)
        player.hand = deck.cards.pop()
        
    def play(self, players):
        highest_card = None
        winner = None
        for player in players:
            if highest_card is None or player.hand > highest_card:
                highest_card = player.hand
                winner = player
        
        winner.points += 1     
        print(f"Winner is {winner.name}")
        
    def game(self):
        
        print(f"xxx New Game Started xxx")
        players = self.make_players()
        for current_play in range(self.nplays):
            print(f"Play number {current_play}")
            for player in players:
                self.assign_card(self.deck, player)
                #print(f"\n{player.name} >>> \n",print(player.hand))
            print(players[0])
            print(players[1])
            self.play(players)
        
        overall_winner = None
        highest_score = None
        for player in players:
            if highest_score is None or player.points > highest_score:
                highest_score = player.points
                overall_winner = player
        
        print("xxx Game Over xxx")
        print(f"xxx {overall_winner.name} Wins xxx")
        
        

    
