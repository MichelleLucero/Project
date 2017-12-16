import csv

def csv_d(file):
    l = []
    f = open(file)
    csv_dict_reader = csv.DictReader(f)
    for line in csv_dict_reader:
        l.append(line)
    f.close()
    return l

def find_word(dict, word): #works specifically for the csv file 
    fw = {}
    for name_of_cat in dict:
        statement = name_of_cat['Quote']
        if word in statement:   
            execute = name_of_cat['Quote #']
            fw.setdefault(word,[])
            fw[word].append(execute)   
    return fw

def search(w1, w2, key, dict):
    l = {} #ultimate dictionary result
    w1_val = [] #list of values taken from w1 dict (one)
    w2_val = [] #list of values taken from w2 dict (two)
    w1_w2_val = [] #list of values from w1 and list of values from w2(for the OR). List before the duplicates are removed
    w1_and_w2 = [] #list of vlues from w1 and w2
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
        k = w1 + ' or ' + w2
        for val in w1_val:
            w1_w2_val.append(val)
        for vals in w2_val:
            w1_w2_val.append(vals)
        both_values = list(set(w1_w2_val)) #removing duplicates from w1_w2_val  
        l.setdefault(k, both_values) 


    elif key.lower() == "and":
        
        k = w1 + " and " + w2
        for val in w1_val:
            for vals in w2_val:
                if val == vals:
                    l.setdefault(k, [])
                    l[k].append(val)
    
    elif key.lower() == "not":
        k = w1 + " not " + w2
        for val in w1_val:
            for vals in w2_val:
                if val == vals:
                    w1_and_w2.append(val)
        for i in w1_val:
            if i not in w1_and_w2:
                l.setdefault(k,[])
                l[k].append(i)
                
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

d = csv_d('famous_quotes.csv')

#print(search("sorry", "hate", "and", d))
print(search("sorry", "forgive", "not", d))


'''
for key, val in iindex(d, remorse_word).items():
    print(key)
    print(' = ' + str(val), '\n')
'''
