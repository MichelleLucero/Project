import csv
import nltk
from nltk.stem import PorterStemmer
from nltk.tokenize import sent_tokenize, word_tokenize
ps = PorterStemmer()

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
"""
def find_word(dict, word): #works specifically for the csv file 
    fw = {}
    for name_of_cat in dict:
        statement = name_of_cat['Quote']
        if word in statement: 
            execute = name_of_cat['Quote #']
            fw.setdefault(word,[])
            fw[word].append(execute)   
    return fw
"""



def search(w1, w2, key, dict):
    l = {} #ultimate dictionary result
    w1_val = [] #list of values taken from w1 dict (one)
    w2_val = [] #list of values taken from w2 dict (two)
    w1_w2_val = [] #list of values from w1 and list of values from w2(for the OR). List before the duplicates are removed
    w1_and_w2 = [] #list of values from w1 and w2(for the NOT)
    #turning w1 and w2 into dicts

    #wt1 = str(word_tokenize(w1)) 
    #wt2 = str(word_tokenize(w2)) 

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
        k = w1 + ' OR ' + w2
        for val in w1_val:
            w1_w2_val.append(val)
        for vals in w2_val:
            w1_w2_val.append(vals)
        both_values = list(set(w1_w2_val)) #removing duplicates from w1_w2_val  
        l.setdefault(k, both_values) 


    elif key.lower() == "and":
        
        k = w1 + " AND " + w2
        for val in w1_val:
            for vals in w2_val:
                if val == vals:
                    l.setdefault(k, [])
                    l[k].append(val)
    
    elif key.lower() == "not":
        k = w1 + " NOT " + w2
        for val in w1_val:
            for vals in w2_val:
                if val == vals:
                    w1_and_w2.append(val)
        for i in w1_val:
            if i not in w1_and_w2:
                l.setdefault(k,[])
                l[k].append(i)
                
    return l


def init_nltk():
    global tokenizer
    global tagger
    tokenizer = nltk.tokenize.RegexpTokenizer(r'\w+|[^\w\s]+')
    tagger = nltk.UnigramTagger(nltk.corpus.brown.tagged_sents())

def tag(text):
    global tokenizer
    global tagger
    if not tokenizer:
        init_nltk()
    tokenized = tokenizer.tokenize(text)
    tagged = tagger.tag(tokenized)
    tagged.sort(lambda x,y:cmp(x[1],y[1]))
    return tagged

    

example_words = ["living","planning","growing"]

            


d = csv_d('famous_quotes.csv')

print(search("is", "life", "not", d))

#add possible ways of implementing stem library
example_words = ["planning","growing","living"]
for w in example_words:
    print(ps.stem(w))
#antoher form of implemention
print (d.concordance("hard"))
print (d.dispersion_plot(["help", "live"])) #print a plot 



print('The nltk version is {}.'.format(nltk.__version__)) 
#just to check the nltk version 

'''
for key, val in iindex(d, remorse_word).items():
    print(key)
    print(' = ' + str(val), '\n')
'''

