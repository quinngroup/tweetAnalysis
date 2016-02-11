import os
'''
script which takes directory as input and move them to 
'''
cwd = os.getcwd()
lst=os.listdir(cwd +"/DownloadTweetForAll")

#print type(lst)

for fileName in lst:
    newName = fileName.split("\\")[0]
    #print newName
    old = cwd + "/DownloadTweetForAll/"+fileName
    new = cwd + "/CSVs/" + newName+".csv"
    print old 
    print new
    os.rename(old,new)

