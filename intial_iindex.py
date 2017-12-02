`#my inverted index problem

import csv

def alpha(word): # splits everything making sure all the words are alphabetical
    total=""
    for i in word:
        if i.isalpha() or i == " ": 
            total = total + i
    return total.split()

def invertedindex(file):

    f = open(file)
    csv_reader = csv.reader(f)
    l = []
    for line in csv_reader:
        l.append(line)
    f.close()
    dictionary = {}
    for x in l:
        for i in alpha(x[8]): #number oc columns
            dictionary.setdefault(i, []) #gives it a start
            if x[0] not in dictionary[i]: 
                dictionary[i].append(x[0]) #creates a dictionary for us to work with 
    return dictionary

def find_the_word(l):
    executionnumber = invertedindex("offenders-clean.csv")
    for i in executionnumber:
        if i == l: 
            return executionnumber[i]
    

find_the_word = find_the_word("Warden")
print(find_the_word)
