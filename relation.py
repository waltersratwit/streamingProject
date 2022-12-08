# -*- coding: utf-8 -*-
"""
Created on Mon Nov 28 22:07:28 2022

@author: waltersr
"""
import title2 as title
# import title

class Relation:
    title1=title.Title
    title2=title.Title
    totalSim = 0
    
    def __init__(self, title1, title2, similarityList):
        self.title1 = title1
        # print (self.title1)
        self.title2 = title2
        self.similarityList = similarityList
        # print(similarityList)
        # print(self.similarityList)
        self.avgSim = {}
        for tag in self.similarityList:
            self.avgSim[tag] = sum(self.similarityList[tag])/len(self.similarityList[tag])
        # print(self.similarityList)
        # print(self.avgSim)
        self.updateTotalSim()
        # print(title1.getName())
        # print(title2.getName())
        self.title1.addRelation(self)
        self.title2.addRelation(self)
    
    def __str__(self):
        sims = ""
        for s in self.avgSim:
            sims = sims + s + ":" + str(self.avgSim[s]) + ", "
        sims = sims[:-2]
        return "{} and {} with similarities {}".format(self.title1.getName(), self.title2.getName(), sims)

    def addSim(self, tag, newValue):
        if (tag in self.similarityList.keys()):
            valueList = self.similarityList[tag]
            valueList.append(newValue)
        else:
            valueList = [newValue]
        self.similarityList[tag]=valueList
        self.avgSim[tag]=sum(valueList)/len(valueList)
        self.updateTotalSim()
        self.title1.sortRelations()
        self.title2.sortRelations()
        # print(self.similarityList)

    def updateTotalSim(self):
        top1=0
        top2=0
        top3=0
        for value in self.avgSim:
            if (self.avgSim[value] > top1):
                top3=top2
                top2=top1
                top1=self.avgSim[value]
            elif (self.avgSim[value] > top2):
                top2=top1
                top1=self.avgSim[value]
            elif (self.avgSim[value] > top3):
                top3=self.avgSim[value]
        self.totalSim = top1 + top2 + top3

    def getAvgSim(self):
        return self.avgSim

    def getTotalSim(self):
        return self.totalSim
    
    def getTitles(self):
        return (self.title1.getName(),self.title2.getName())