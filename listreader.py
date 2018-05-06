import csv
import codecs
import ast

reader = csv.reader(open('words.txt', 'r'), delimiter = ' ')

Words = []

for line in reader:
	Words.append(line[0:4])
#	map(unicode.strip, Words)

Words.remove(Words[0])

#Words = ast.literal_eval(Words[0:4])
indexX= 0

while len(Words)< indexX:
	Words[indexX][2]= int(Words[indexX][2])
	indexX += 1
#print(Words)
#Words[indexX][2]= int(Words[indexX][2])
print(Words)