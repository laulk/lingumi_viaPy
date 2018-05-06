lingumi_viaPy

An extremely barebones program created in about 45minutes in python. 






How to test the program "wordlist.py":
Simply use your favourite text editor and build or terminal and input :python3 wordlist.py

within the file, it already has set parameters to test, a list of pre-defined words = Words[] which is a list of lists that consist of string-theword, string-ID/Achievement sticker, int-numberoftimesCollected, bool- hascollected.

Learned=[] represents the list of words learned in the last session.

What it is supposed to do, in this current iteration, the test parameters are Learned=["sticker10", "sticker1", "sticker5"]

The program will sort the alphanumerical string list that represents the ID of the words that you have just learned,
appends the Words list with accordance to its numberoftimesCollected & hasCollected in this case:
for words 'jubble', 'apple' and 'eubble' will have their hasCollected bool = True and numberoftimesCollected += 1

the program will then sort by numberofcollected, in descending order and then create a new list achievementsToPrint=[] to be filled with the words that has their "hasCollected" bool value to be True.

finally it will sort again by numberoftimes but in ascending order and print the top 3 stickerIDs
meaning a word that has only been learned once will take precedence over the others as, to my experience video games give new achievements more weightage & reward over previously claimed achievements.


Some test cases i have tried :

	Learned = ["sticker1","sticker17","sticker17"]
	-this will print. "you havent learned enough words to print achievements"
	-eventhough 3 instances of words learned, there is a duplicate, and total number of words learned = 2 it will not print any stickers for you.

	Changing int values and bool values of different words in Words[] to simulate words that were learned in a previous lesson but not in the latest lesson. Learned = ["sticker1", "sticker5"]  Words = [[sticker2 , 1, True]]
	sticker2 was learned previously, latest lesson only learned sticker 1 & 5 but will still print your collected stickers.


Final notes:

	The algorithm used mostly implemented python's timsort,
	the code is far from elegant, given more time and focus could definitely take into account data sets that range in the thousands.
	the basic skeleton of the code is just from thinking about the simplest way to implement this when manipulating lists with multiple data types, something that was beyond me in terms of C#.





