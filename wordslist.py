import sys

#extremely barebones .py file for lingumi challenge

#list of lists of available words with multiple type values "word string", "id string", "number of times learned Int", "has already colelcted Bool"
#
Words = [["apple", "sticker1", 0, False],
		 ["bubble", "sticker2", 0, False],
		 ["cubble", "sticker3", 0, False],
		 ["dubble", "sticker4", 0, False],
		 ["eubble", "sticker5", 0, False],
		 ["fubble", "sticker6", 0, False],
		 ["gubble", "sticker7", 0, False],
		 ["hubble", "sticker8", 0, False],
		 ["iubble", "sticker9", 0, False],
		 ["jubble", "sticker10", 0, False],
		 ["kubble", "sticker11", 0, False],
		 ["lubble", "sticker12", 0, False],
		 ["mubble", "sticker13", 0, False],
		 ["nubble", "sticker14", 0, False],
		 ["oubble", "sticker15", 0, False],
		 ["pubble", "sticker16", 0, False],
		 ["qubble", "sticker17", 0, False]]


#List of learned words is always assumed to be sorted in ascending order if not, sorted(Learned) sorts the strings by ascending
Learned = ["sticker1","sticker1"]


#word_set= set(map(tuple, Words))			dont need this
#learned_set = set(map(tuple, Learned))		dont need this either

if Learned != 0:	#checks if you've 'learned' anything in the previous lesson

	Learned = sorted(Learned) #sorts learned strings in ascending order
	indexW =0					#indexes which word & which sticker is being compared during the loop
	indexS = 0


	while indexS< len(Learned):  	

		if Learned[indexS] in Words[indexW]:
			Words[indexW][3] = True				#if first sticker learned is in the current index of Word[indexW], sets 'hasAlreadyCollected' to True
			Words[indexW][2] += 1				# and increments numberofTimesCollected by 1

#			print("I have just registered " + Learned[indexS] + " as a sticker you collected in the last lesson")		uncomment to check if learned ID has registered and updated the list	
			indexS += 1

		else:
			indexW += 1


learnedWords = []
learnedWords=sorted(Words, key = lambda word:word[2], reverse = True)		#new list of Words that is now sorted by number of times learned, INT in descending order

#print(learnedWords) uncomment to check if learnedWords is actually sorted by number of times collected in descending order

lw_Index=0
achievementsToPrint=[]

while lw_Index < len(learnedWords):			#while loop to cycle through learnedWords and create a new list with elements from learnedWords that excludes all words have not been learned

	if learnedWords[lw_Index][3]== True:
		achievementsToPrint.append(learnedWords[lw_Index])
		lw_Index += 1
	elif learnedWords[lw_Index][3] ==False:

		break											

achievementsToPrint = sorted(achievementsToPrint, key = lambda word:word[2])

final_Print = 0

if len(achievementsToPrint) < 3:
	print("you havent learned enough words to print achievements")
else:
	while final_Print < 3:								#sorted achievements to print by number of times collected in ascending order, 
		print(achievementsToPrint[final_Print][1])		#prints the first three IDs in achievements to print, as it only contains hasCollected =True and is sorted by number of times learned = descending
		final_Print += 1								#prints the sticker that has been collected the fewest times first, as if im right, consistent with most video games achievements that have been collected before hold a lower weightage





#uncomment to Check if Words list updates after running script, no formatting, avoid for large datasets
#print("your current state of tickets: ", Words)




