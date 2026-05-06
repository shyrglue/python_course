import random
suits="CDHS"
ranks="23456789TJQKA"
points= {'A':4,'K':3,'Q':2,'J':1,'T':0,'9':0,'8':0,'7':0,'6':0,'5':0,'4':0,'3':0,'2':0} 
#attributes of cards
cards=[rank+suit for suit in suits for rank in ranks]   
givencards=random.sample(cards,13)                      
#deal cards
sum=0
for card in givencards:
    sum+=points.get(card[0])
#calculate points
print("Your cards are "+' '.join(givencards))
print("Total point is: "+str(sum))