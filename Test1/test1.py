import os
import json

inverDict = {}

def readText():
    textList = []
    with open("tweets.txt", 'r+') as f:
        content = f.readlines()
    for i in content:
        textList.append(json.loads(i.replace('\n', '')))
    return textList

def create_inverIndex(textList):
    for Dict in textList:
        index = Dict["tweetId"]
        for words in Dict["text"].split(" "):
            if words.lower() in inverDict: inverDict[words.lower()].append(index)
            else: inverDict[words.lower()] = [index]
    return inverDict

def selectSec(k):
    return k[1]

def searchFor(string):
    indexSetAll = set()
    strList_or = string.split(", ")
    for str_or in strList_or:
        sortList = []
        for words in str_or.split(" "):
            betList = [words.lower(), len(inverDict[words.lower()]) if words.lower() in inverDict else 0]
            sortList.append(betList)
        sortList.sort(key = selectSec)
        indexSet = inverDict[sortList[0][0]] if sortList[0][1] != 0 else []
        for words, num in sortList[1:]:
            if num == 0: break
            nowSet = set()
            for i in indexSet:
                if i in inverDict[words]: nowSet.add(i)
            indexSet = nowSet
        for i in indexSet: indexSetAll.add(i)
    return indexSetAll

if __name__ == "__main__":
    create_inverIndex(readText())
    print(searchFor("National Zoo Panda, insemination"))