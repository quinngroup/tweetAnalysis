import math
import os
import sys
from textblob import TextBlob as tb

def tf(word, blob):
	return (float)(blob.words.count(word)) / (float)(len(blob.words))

def n_containing(word, bloblist):
    return sum(1 for blob in bloblist if word in blob)

def idf(word, bloblist):
    return math.log(len(bloblist) / (float)(1 + n_containing(word, bloblist)))

def tfidf(word, blob, bloblist):
    return tf(word, blob) * idf(word, bloblist)

'''document3 = tb("""The Colt Python is a .357 Magnum caliber revolver formerly
manufactured by Colt's Manufacturing Company of Hartford, Connecticut.
It is sometimes referred to as a "Combat Magnum".[1] It was first introduced
in 1955, the same year as Smith & Wesson's M29 .44 Magnum. The now discontinued
Colt Python targeted the premium revolver market segment. Some firearm
collectors and writers such as Jeff Cooper, Ian V. Hogg, Chuck Hawks, Leroy
Thompson, Renee Smeets and Martin Dougherty have described the Python as the
finest production revolver ever made.""")'''


def getTFIDF(bloblist, fileList):
    for blob, user in zip(bloblist, fileList):
        path = os.getcwd()
        #fileForOP = path+"/TFIDF_F/"+user+".csv"
        #sys.stdout = open(fileForOP,'w')
        print("USER::{}".format(user))
        scores = {word: tfidf(word, blob, bloblist) for word in blob.words}
        sorted_words = sorted(scores.items(), key=lambda x: x[1], reverse=True)
        for word, score in sorted_words[:50]:
            print("Word: {}".format(word))


# main here
if __name__ == '__main__':
    documentList = []
    fileList = []
    path = os.getcwd()
    #path = path + "/OUT_F/"
    path = path + "/TEMP_POS/"
    lst = os.listdir(path)
    for fileName in lst:
        temp = ""
        fileAdd = path + fileName
        fileContent = open(fileAdd)
        for line in fileContent:
            try:
                temp = temp + " " + line.lower()
            except:
                pass

        document1 = tb(temp)
        documentList.append(document1)
        fileList.append(fileName.split(".")[0])
    getTFIDF(documentList, fileList)
