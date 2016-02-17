#author ranjanmanish
import os
'''
script which takes directory as input and move them to another directory with changed extension of file
'''
cwd = os.getcwd()
lst=os.listdir(cwd +"/DownloadForAll")

#print type(lst)

for fileName in lst:
    newName = fileName.split("\\")[0]
    #print newName
    old = cwd + "/DownloadForAll/"+fileName
    new = cwd + "/CSVs/" + newName+".csv"
    print old 
    print new
    os.rename(old,new)

