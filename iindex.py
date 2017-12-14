import csv

def csv_d(file):
    l = []
    f = open(file)
    csv_dict_reader = csv.DictReader(f)
    for line in csv_dict_reader:
        l.append(line)
    f.close()
    return l

def find_word(dict, word):
    fw = {}
    for name_of_cat in dict:
        statement = name_of_cat['Last Statement']
        if word in statement:   
            execute = name_of_cat['Execution #']
            fw.setdefault(word,[])
            fw[word].append(execute)   
    return fw

def search(w1, w2, key, dict):
    l = {} #ultimate dictionary result
    w1_val = [] #list of values taken from w1 dict (one)
    w2_val = [] #list of values taken from w2 dict (two)

    #turning w1 and w2 into dicts
    one = find_word(dict, w1)
    two = find_word(dict, w2)

    #getting the values out of the dictionary (as stated before)
    for v in one.values():
        for i in v:
            w1_val.append(i)
    for v in two.values():
        for i in v:
            w2_val.append(i)

     #key "and", "or", "not"
    if key.lower() == "or":

        #clean up list
        if find_word(dict, w1) != {}:
            for w in one.values():
                l.setdefault(w1,[])
                l[w1].append(w)
        if find_word(dict, w2) != {}:
            for w in two.values():
                l.setdefault(w2,[])
                l[w2].append(w)
    elif key.lower() == "and":
        
        k = w1 + " and " + w2
        for val in w1_val:
            for vals in w2_val:
                if val == vals:
                    l.setdefault(k, [])
                    l[k].append(val)
                
    return l
#apples in a bag
            
'''       
            and find_the_word(word2)
    elif key.lower() = "or":
        return 
'''
remorse_word = ['sorry', 'apologize', 'forgiveness', 'peace', 'forgive', 'god'
                'love', 'sad', 'terrible', 'bless']
anger_word = ['hate', 'hell', 'damn'] 

d = csv_d('offenders.csv')

#print(search("sorry", "hate", "or", d))
print(search("sorry", "hate", "and", d))


'''
for key, val in iindex(d, remorse_word).items():
    print(key)
    print(' = ' + str(val), '\n')
'''