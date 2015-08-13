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
