class Card:

    def __init__(self, color, shape, fill, number):
        self.color = color
        self.shape = shape
        self.fill = fill
        self.number = number
        self.nr = color*27 + shape*9 + fill*3 + number

    def __eq__(self, other):
        return self.nr == other.nr

    def __lt__(self, other):
        return self.nr < other.nr

    def __hash__(self):
        return hash(self.nr)

    def __repr__(self):
        return str(self.nr)

    def from_list(card_as_list):
        return Card(card_as_list[0], card_as_list[1], card_as_list[2],
                    card_as_list[3])

    def to_list(self):
        return [self.color, self.shape, self.fill, self.number]

    def from_str(card_as_string):
        temp_list = card_as_string.split(" ")
        colors = {"red": 0, "green": 1, "purple": 2}
        shapes = {"wiggle": 0, "oval": 1, "rectangle": 2}
        fills = {"empty": 0, "shaded": 1, "filled": 2}
        return Card(colors[temp_list[0]], shapes[temp_list[1]],
                    fills[temp_list[2]], int(temp_list[3])-1)

    def to_str(self):
        colors = {0: "red", 1: "green", 2: "purple"}
        shapes = {0: "wiggle", 1: "oval", 2: "rectangle"}
        fills = {0: "empty", 1: "shaded", 2: "filled"}
        return " ".join([colors[self.color], shapes[self.shape],
                        fills[self.fill], str(self.number + 1)])


def correct_set(card1, card2, card3):
    list1 = card1.to_list()
    list2 = card2.to_list()
    list3 = card3.to_list()
    for i in range(4):
        W = set([list1[i], list2[i], list3[i]])
        if(len(W) == 2):
            return False
    return True


class Board:

    def __init__(self):
        self.cards = set()
        self.sets = set()

    def __repr__(self):
        return "<< " + " ".join(list(map(str, list(self.cards)))) + " >>"

    def number_of_cards(self):
        return len(self.cards)

    def add_card(self, card):
        for i in self.cards:
            for j in self.cards:
                if i < j:
                    if(correct_set(i, j, card)):
                        self.sets.add((i, j, card))
        self.cards.add(card)

    def remove_card(self, card):
        if(card in self.cards):
            toremove = []
            for myset in self.sets:
                if card in myset:
                    toremove.append(myset)
            for myset in toremove:
                self.sets.remove(myset)
            self.cards.remove(card)
        else:
            raise Exception("this card doesn't exist in board")

    def collect_set(self, card1, card2, card3):
        if(correct_set(card1, card2, card3)):
            for card in [card1, card2, card3]:
                self.remove_card(card)
        else:
            raise Exception("incorrect set")

    def find_sets(self):
        return self.sets

    
def type_of_the_set(card1, card2, card3):
    if not correct_set(card1, card2, card3):
        raise Exception("this set is bad")
    typ = []
    if card1.color == card2.color and card1.color == card3.color:
        typ.append("same color")
    else:
        typ.append("diff color")
    if card1.shape == card2.shape and card1.shape == card3.shape:
        typ.append("same shape")
    else:
        typ.append("diff shape")
    if card1.fill == card2.fill and card1.fill == card3.fill:
        typ.append("same fill")
    else:
        typ.append("diff fill")    
    if card1.number == card2.number and card1.number == card3.number:
        typ.append("same number")
    else:
        typ.append("diff number")   
    return ", ".join(typ)