from nltk.tokenize import RegexpTokenizer
from stop_words import get_stop_words
from nltk.stem.porter import PorterStemmer
from collections import defaultdict
from gensim import corpora, models
from pprint import pprint

import gensim

tokenizer = RegexpTokenizer(r'\w+')

# create English stop words list
en_stop = get_stop_words('en')

# Create p_stemmer of class PorterStemmer
p_stemmer = PorterStemmer()
    
# create sample documents
doc_a = "Brocolli is good to eat. My brother likes to eat good brocolli, but not my mother."
doc_b = "My mother spends a lot of time driving my brother around to baseball practice."
doc_c = "Some health experts suggest that driving may cause increased tension and blood pressure."
doc_d = "I often feel pressure to perform well at school, but my mother never seems to drive my brother to do better."
doc_e = "Health professionals say that brocolli is good for your health."

doc_f = "I was playing sport and it was sexy sports"

doc_g = "health professionals always suggest my mother  to play sportss and eat brocoli for his increased tension as well as sport"

doc_h = "health sports mother brocolli "

doc_i = "politician statements are doing rumble in the jungle"

doc_j = "machine learning bigdata logistic regression svm regression"
doc_k = "machine learning bigdata youtube regression abc def logistic sample statistics svm regression"

#compile sample documents into a list

doc_set = [doc_a, doc_b, doc_c, doc_d, doc_e]

#doc_test = [doc_f, doc_g, doc_h, doc_i, doc_j]
doc_test = [doc_i, doc_j, doc_k]

# list for tokenized documents in loop
texts = []

# loop through document list
for i in doc_set:
    # initialize fre
    #frequency = defaultdict(int)
    
    # clean and tokenize document string
    raw = i.lower()
    tokens = tokenizer.tokenize(raw)
    # remove stop words from tokens
    stopped_tokens = [i for i in tokens if not i in en_stop]
    
    # stem tokens
    stemmed_tokens = [p_stemmer.stem(i) for i in stopped_tokens]

    
    # add tokens to list
    texts.append(stemmed_tokens)

'''for text in texts:
    for token in text:
        frequency[token] += 1

texts = [[token for token in text if frequency[token] > 1] for text in texts]'''


pprint(texts)

# turn our tokenized documents into a id <-> term dictionary
dictionary = corpora.Dictionary(texts)

print dictionary

# convert tokenized documents into a document-term matrix
corpus = [dictionary.doc2bow(text) for text in texts]

# generate LDA model
ldamodel = gensim.models.ldamodel.LdaModel(corpus, num_topics=5, id2word = dictionary, passes=20)

print(ldamodel.print_topics(num_topics=5, num_words=10))

texts = []

stopeed_tokens = []
stemmed_tokens = []

for i in doc_test:

    raw = i.lower()
    tokens = tokenizer.tokenize(raw)

    # remove stop words from tokens
    stopped_tokens = [i for i in tokens if not i in en_stop]

    # stem tokens
    stemmed_tokens = [p_stemmer.stem(i) for i in stopped_tokens]

    texts.append(stemmed_tokens)


'''for text in texts:
    for token in text:
        frequency[token] += 1

texts = [[token for token in text if frequency[token] > 1] for text in texts]'''

pprint (texts)

dictionary = corpora.Dictionary(texts)

#doc_bow = [(0, 1), (1, 1)]

corpus_test = [dictionary.doc2bow(text) for text in texts]
# To get the scores for each document, you can run the document. as a bag of words, through a trained LDA mode
for item in corpus_test:
    print ldamodel[item]
print ("*********************Comparing now***********************")
# Here I am going to run it on the same documents against which model was trained and see how well  they show the expected behavior
for item in corpus:
    print ldamodel[item]


