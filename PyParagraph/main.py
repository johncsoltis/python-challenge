#Import a text file filled with a paragraph of your choosing.
#Assess the passage for each of the following:
    #Approximate word count
    #Approximate sentence count
    #Approximate letter count (per word)
    #Average sentence length (in words)

#import regular expressions module
import re

#open paragraph
astros = open("astros.txt", 'r')
#read paragraph and assign to value
paragraph = astros.read()
#close paragraph
astros.close()

#assign empty lists and variables
lettercount = 0
wordcount = 0
lettercount_ls = []
wordcount_ls = []
letterlist = []

#split sentances
splitp = re.split("(?<=[.!?]) +", paragraph)

#count sentances
sentencecount = len(splitp)

#loop through paragraph to fill in empty variables
for sentence in splitp:
    words = sentence.split(" ")
    wordcount += len(words)
    #print(wordcount)
    wordcount_ls.append(len(words))
    #print(words)
    for word in words:
        #print(word)
        for char in word:
            lettercount += 1
            lettercount_ls.append(lettercount)
            lettercount = 0
word_len = round((sum(lettercount_ls)/wordcount),1)
sent_len = round((sum(wordcount_ls)/sentencecount),1)

print(f"Approximate Word Count: {wordcount}")
print(f"Approximate Sentence Count: {sentencecount}")
print(f"Average Letter Count: {word_len}")
print(f"Average Sentence Length: {sent_len}")