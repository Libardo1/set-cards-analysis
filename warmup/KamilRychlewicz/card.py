class Card:
	def __init__(self,chlist):
		self.chlist=chlist
	def __lt__(self,other):
		return(self.chlist<other.chlist)
	def to_list(self):
		return self.chlist
	def to_str(self):
		result=""
		result+=({0:"red ", 1:"green ", 2:"purple "}[self.chlist[0]])
		result+=({0:"rectangle ", 1:"wiggle ", 2:"oval "}[self.chlist[1]])
		result+=({0:"empty ", 1:"shaded ", 2:"filled "}[self.chlist[2]])
		result+=({0:"1", 1:"2", 2:"3"}[self.chlist[3]])
		return result
	@staticmethod
	def from_list(chlist):
		return Card(chlist)
	@staticmethod
	def from_str(string):
		words=string.split(" ")
		return Card([
		{"red":0, "green":1, "purple":2}[words[0]],
		{"rectangle":0, "wiggle":1, "oval":2}[words[1]],
		{"empty":0, "shaded":1, "filled":2}[words[2]],
		{"1":0, "2":1, "3":2}[words[3]]])
	

class Board:
	def __init__(self):
		self.cards_set=set()
		self.sets_set=set()
	def add_card(self,card):
		for x in self.cards_set:
			for y in self.cards_set:
				if (x<y) & check_set(x,y,card):
						self.sets_set.add((x,y,card))
		self.cards_set.add(card)
	def remove_card(self,card):
		self.cards_set.remove(card)
		toremove=[]
		for s in self.sets_set:
			if card in s:
				toremove.append(s)
		for s in toremove:
			self.sets_set.remove(s)
	def collect_set(self,card1,card2,card3):
		if check_set(card1,card2,card3):
			self.remove_card(card1)
			self.remove_card(card2)
			self.remove_card(card3)
		else:
			raise Exception("Not a set")
	def find_sets(self):
		return self.sets_set
	def number_of_cards(self):
		return len(self.cards_set)
		

def check_set(card1,card2,card3):
	result=True
	for i in range(0,4):
		result=result&((card1.chlist[i]+card2.chlist[i]+card3.chlist[i])%3==0)
	return result
