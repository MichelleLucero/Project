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
<<<<<<< HEAD
#credits
=======
    credits
>>>>>>> e57a5124f77fe7c460d1f2b97a1fe51d5381029e
    dictionary = {}
    
    for x in l:
        for i in alpha(x[8]): #number oc columns
            dictionary.setdefault(i, []) #gives it a start
            if x[0] not in dictionary[i]: 
                dictionary[i].append(x[0]) #creates a dictionary for us to work with 
    return dictionary

def find_the_word(l):
    executionnumber = invertedindex("famous_quotes.csv")
    for i in executionnumber:
        if i == l: 
            return executionnumber[i]

def search(word1, word2, key):
    #key "and", "or", "not"
<<<<<<< HEAD
    if key.lower() = "and":
        if 
            return find_the_world(word1) and find_the_word(word2)
    elif key.lower() = "or":
        return 


  

find_the_word = find_the_word("Warden")
=======
    find_the_word = find_the_word("not")
>>>>>>> e57a5124f77fe7c460d1f2b97a1fe51d5381029e
print(find_the_word)
