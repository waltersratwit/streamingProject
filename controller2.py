# -*- coding: utf-8 -*-
"""
Created on Thu Dec  8 14:16:50 2022

@author: waltersr
"""

import title2 as title
import relation

titleFile = open("titles.txt")
titleFileList = titleFile.readlines()
titleFile.close()
titleFileList = [t.strip() for t in titleFileList]

titles = []
for t in titleFileList:
    x = t.split("|")
    titles.append(title.Title(x[0], x[1]))

for t in titles:
    print(t)
    print()

titles.append(title.Title(557,"spider-man"))

relationFile = open("relations2.txt")
relationFileList = relationFile.readlines()
relationFile.close()
relationFileList = [r.strip() for r in relationFileList]

relations = []
for r in range(int(len(relationFileList)/3)):
    # print(r)
    title1 = title.Title
    title2 = title.Title
    for t in titles:
        if t.getName().lower() == relationFileList[r * 3].lower():
            title1 = t
        elif t.getName().lower() == relationFileList[r * 3 + 1].lower():
            title2 = t
    tags = relationFileList[r * 3 + 2].split()
    sims = {}
    for t in tags:
        t2 = t.split("|")
        # print(t2[0])
        sims[t2[0]] = [int(t3) for t3 in t2[1].split(",")]
    relations.append(relation.Relation(title1, title2, sims))

for r in relations:
    print(r)
    print()

relations.append(relation.Relation(titles[1], titles[2], {"comedy":[1],"fun":[5]}))
# relations[1].addSim("fun", 3) # no way to avoid this being spammed

# print(titles)
titleFile = open("titles.txt", "w")
titleFileList = []
for t in titles:
    titleFileList.append("{}|{}\n".format(t.getID(), t.getName()))
titleFileList = list(dict.fromkeys(titleFileList)) # removes duplicates
for t in titleFileList:
    titleFile.write(t)
titleFile.close()

relationFile = open("relations2.txt", "w")
relationFileList = []
for r in relations:
    sims = ""
    for s in r.similarityList:
        sims = sims + s + "|" + ",".join(map(str,r.similarityList[s])) + " "
    sims = sims[:-1]
    relationFileList.append("{}\n{}\n{}\n".format(r.getTitles()[0], r.getTitles()[1], sims))
relationFileList = list(dict.fromkeys(relationFileList)) # removes duplicates
for r in relationFileList:
    relationFile.write(r)
relationFile.close()