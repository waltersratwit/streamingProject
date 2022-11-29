# -*- coding: utf-8 -*-
"""
Created on Mon Nov 28 22:08:04 2022

@author: waltersr
"""


class Title:
    

    def __init__(self, name, tags):
        self.name = name
        self.rating = 5 #will pull from service
        self.tags = tags #will pull from service
        self.image = "file path for image" #will pull from service
        self.relations = []
        self.relatedTitles = []
    
    def addRelation(self, relation):
        self.relations.append(relation)
        if (relation.getTitles()[0] is self.name):
            self.relatedTitles.append(relation.getTitles()[1])
        else:
            self.relatedTitles.append(relation.getTitles()[0])
        self.relations.sort(key=lambda x: x.getTotalSim())
        
    def getName(self):
        return self.name
    
    def getRelations(self):
        output = []
        for x in self.relations:
            titles = x.getTitles()
            # print(titles)
            if (titles[0] is self.name):
                output.append((titles[1],x.getAvgSim()))
            else:
                output.append((titles[0],x.getAvgSim()))
        return output