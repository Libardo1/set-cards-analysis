def check_set(card1,card2,card3):
	result=True
	for i in range(0,4):
		result=result&((card1[i]+card2[i]+card3[i])%3==0)
	return result

def find_sets(cards_list):
	result=[]
	n=len(cards_list)
	for i in range (0,n):
		for j in range (i+1,n):
			for k in range (j+1,n):
				if check_set(cards_list[i],cards_list[j],cards_list[k]):
					result.append([cards_list[i],cards_list[j],cards_list[k]])
	return result
	

class Board:
	def __init__(self):
		self.cards_set=set()
		self.sets_set=set()
	def add_card(self,card):
		for x in self.cards_set:
			for y in self.cards_set:
				if (x<y) & check_set(x,y,card):
						self.sets_set.add((x,y,tuple(card)))
		self.cards_set.add(tuple(card))
	def remove_card(self,card):
		self.cards_set.remove(tuple(card))
		toremove=[]
		for s in self.sets_set:
			if tuple(card) in s:
				toremove.append(s)
		for s in toremove:
			self.sets_set.remove(s)
	def collect_set(self,card1,card2,card3):
		if check_set(card1,card2,card3):
			self.cards_set.remove(tuple(card1))
			self.cards_set.remove(tuple(card2))
			self.cards_set.remove(tuple(card3))
		else:
			raise Exception("Not a set")
	def find_sets(self):
		return self.sets_set
