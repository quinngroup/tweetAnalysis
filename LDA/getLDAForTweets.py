from nltk.tokenize import RegexpTokenizer
from stop_words import get_stop_words
from nltk.stem.porter import PorterStemmer
from gensim import corpora, models
import gensim
import os
#author: https://rstudio-pubs-static.s3.amazonaws.com/79360_850b2a69980c4488b1db95987a24867a.html
#modified: ranjanmanish
tokenizer = RegexpTokenizer(r'\w+')

# create English stop words list
en_stop = get_stop_words('en')

# Create p_stemmer of class PorterStemmer
p_stemmer = PorterStemmer()
    
# create sample documents
doc_set=[]

# get the current path
path = os.getcwd()
# bring the path to speed
path = path + "/TEMP"

#get the list of files
lst = os.listdir(path)

# Now take the files one by one and create one doc per user and add to list
for fileName in lst:
    temp = ""
    fileadd = path + "/"+fileName
    fileContent = open(fileadd)
    for line in fileContent:
        try:
            line = line.split(",")[2]
            print line
            line = re.sub(r'#([^\s]+)', r'\1', line)
            line = re.sub('((www\.[^\s]+)|(https?://[^\s]+))','',line)
            line = line.strip('\'"')
            #print line
            temp = temp + str(line)
            #print temp
        except:
            pass
    doc_set.append(temp)

print len(doc_set)

# compile sample documents into a list
#doc_set = [doc_a, doc_b, doc_c, doc_d, doc_e]
print type(doc_set)

# list for tokenized documents in loop
texts = []

# loop through document list
for i in doc_set:
    
    # clean and tokenize document string
    raw = i.lower()
    tokens = tokenizer.tokenize(raw)

    # remove stop words from tokens
    stopped_tokens = [i for i in tokens if not i in en_stop]
    
    # stem tokens
    stemmed_tokens = [p_stemmer.stem(i) for i in stopped_tokens]
    
    # add tokens to list
    texts.append(stemmed_tokens)

# turn our tokenized documents into a id <-> term dictionary
dictionary = corpora.Dictionary(texts)
    
# convert tokenized documents into a document-term matrix
corpus = [dictionary.doc2bow(text) for text in texts]

# generate LDA model
ldamodel = gensim.models.ldamodel.LdaModel(corpus, num_topics=2, id2word = dictionary, passes=20)

print(ldamodel.print_topics(num_topics=2))
