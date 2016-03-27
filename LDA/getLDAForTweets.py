from nltk.tokenize import RegexpTokenizer
from nltk.corpus import stopwords
from stop_words import get_stop_words
from nltk.stem.porter import PorterStemmer
from gensim import corpora, models
from collections import defaultdict
from pprint import pprint
from datetime import datetime
from textblob import TextBlob

import gensim
import os
import re
#author: https://rstudio-pubs-static.s3.amazonaws.com/79360_850b2a69980c4488b1db95987a24867a.html
#modified: ranjanmanish
tokenizer = RegexpTokenizer(r'\w+')

dictionary = []
dictFile = open("dict.txt")
for word in dictFile:
    word = word.strip()
    dictionary.append(word.lower())

negList = open("negative-words.txt")

for negWord in negList:
    negWord = negWord.strip()
    dictionary.append(negWord.lower())

foulList = open("foulWordList.txt")

for foulWord in foulList:
    foulWord = foulWord.split(":")[0]
    foulWord = foulWord.strip()
    dictionary.append(foulWord.lower())

# create English stop words list
en_stop = get_stop_words('en')
cachedStopWords = stopwords.words("english")

#increasing the stop word list as the twitter data set is noisy
en_stop.extend(["demibestfans2016", "u", "rt", "t", "s", "updat", "channel", "de", "que", "la", "en", "eurekamag", "na", "sa", "ang", "keo", "ka", "lang", "le", "je", "est", "c", "pa", "j", "ik", "un", "et", "il", "wt", "fpjb", "fnfjb", "rbjb", "amp", "ini", "ada", "amant", "pushawardskathniel", "kathniel", "00", "05", "04", "15", "16", "14", "18", "aku", "niond", "da", "ich", "ero", "rtandfollow", "da", "ich", "und", "ist", "ero", "m", "da", "com", "em", "um", "meu", "na", "pra", "weather", "properti", "googl", "0mm", "co", "thttps", "https", "http", "n", "t", "u", "for", "us", "is:", "it.", "on", "i'll", "also", "of", "via", "follow", "mali", "rt", "got", "nowplay", "periscop", "stat", "replay", "katch", "biztip", "via", "radio", "commerci", "na", "sa", "ang", "ko", "ng", "mo", "aka", "ka", "ve", "ke", "kixmi", "capricorn", "tarnat", "today", "sagittariu", "tauru", "votingdevonne23", "ff", "0", "new", "go", "mm", "aku", "yang", "yg", "ni", "tak", "ada", "nak", "ya", "dutchschultz", "strictlybid", "lovat", "iheartaward", "bestfanarmi", "que", "la", "el", "en", "y", "lo", "es", "ain", "wit", "votingdevonne23", "giveyourheartdd", "amant", "ootd", "bandana", "updat", "get", "channel", "pushawardskathniel", "kathniel", "cbb", "uri", "santiago", "ain'", 'ain', "por", "para", "una", "der", "ein", "aja", "kamu", "sama", "untuk", "lagi", "ako", "kau", "dah", "dia", "kalu", "lah", "bilai", "apa", "lagi", "pushawardskathniels", "hahaha", "haha", "hahahaha", "bestfanarmy", "can", "don"])

# Create p_stemmer of class PorterStemmer
p_stemmer = PorterStemmer()
    
# create sample documents
doc_set=[]

# get the current path
path = os.getcwd()
# bring the path to speed
#path = path + "/ALLIN"
path = path + "/NewDATAForExp/CSVs_NF_renamed"
#path = path + "/FILTERED_ALL"
#path = path + "/TEMP"

#get the list of files
lst = os.listdir(path)
nameList = []
# Now take the files one by one and create one doc per user and add to list
startTime = datetime.now()

for fileName in lst:
    name = fileName.split(".")[0]
    nameList.append(name)
    temp = ""
    fileadd = path + "/"+fileName
    fileContent = open(fileadd)
    for line in fileContent:
        try:
            line = line.split(",")[2]
            # get rid of urls
            line = re.sub('((www\.[^\s]+)|(https?://[^\s]+))','',line)
            #to replace #words to just words 
            #line = re.sub(r'#([^\s]+)', r'\1', line)
            line = re.sub(r'#([^\s]+)', '', line)
            # userNames - no use- get rid
            line = re.sub('@[^\s]+','', line)
            # new lines were creating issues
            line = line.strip('\'"')
            # throwing exception because of unicode error - Fixed that
            line = unicode(line, "utf8")
            # prepare string
            temp = temp + str(line)
            #print temp
        except:
            pass
    doc_set.append(temp)

# list for tokenized documents in loop
texts = []

# loop through document list
for i in doc_set:
    filtered_tokens = []
    frequency = defaultdict(int)
    # clean and tokenize document string
    raw = i.lower()
    tokens = tokenizer.tokenize(raw)
    # remove stop words from tokens
    
    stopped_tokens = [i for i in tokens if not i in en_stop]

    
    #dict_tokens = [i for i in stopped_tokens if  i in dictionary]
    
    # stopwords from nltk package as well although there is not much difference 
    # dictionary approach is killing us time uwise
    #stopped_tokens = [i for i in tokens if not i in cachedStopWords]
    
    # stem tokens
    # stemmed_tokens = [p_stemmer.stem(i) for i in stopped_tokens]
    #stemmed_tokens = [p_stemmer.stem(i) for i in dict_tokens]

    for element in stopped_tokens:
        if len(element) > 2:
            filtered_tokens.append(element)
    

    # how about trying stemming once all the two length words are out 
    stemmed_tokens = [p_stemmer.stem(i) for i in filtered_tokens]

    # now going to give a attempt try to correct the words - removing the stemmer for now problem: # spell correction gave us 2 min / document not a feasible option hence
    spellcorrected_tokens = []
    '''for element in stemmed_tokens:
        b = TextBlob(element)
        word = b.correct()
        spellcorrected_tokens.append(str(word))
    '''
    texts.append(stemmed_tokens)
    #texts.append(filtered_tokens)
    #texts.append(spellcorrected_tokens)

#if word has appeared just once in corpus - throw that out 
for text in texts:
    for token in text:
        frequency[token] += 1


texts = [[token for token in text if frequency[token] > 3] for text in texts]


# turn our tokenized documents into a id <-> term dictionary
dictionary = corpora.Dictionary(texts)

# convert tokenized documents into a document-term matrix
corpus = [dictionary.doc2bow(text) for text in texts]

# generate LDA model
ldamodel = gensim.models.ldamodel.LdaModel(corpus, num_topics=30, id2word = dictionary, passes=20)

print(ldamodel.print_topics(num_topics=30, num_words = 15))

ldamodel.save('./data/lda_twitter_6310user_30topics.model')

counter = 0

for item  in corpus:
    print nameList[counter], 
    counter = counter + 1
    print ldamodel[item]

print datetime.now() - startTime
