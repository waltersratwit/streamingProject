# -*- coding: utf-8 -*-
"""
Created on Mon Nov 28 22:08:04 2022

@author: waltersr
"""


class Title:
    

    def __init__(self, name, rating, tags, image):
        self.name = name
        self.rating = rating
        # print(self.rating)
        self.tags = tags
        # print(self.tags)
        self.image = image
        # print(self.image)
        self.relations = []
        # print(self.relations)
        self.relatedTitles = []
    
    def addRelation(self, relation):
        self.relations.append(relation)
        if (relation.getTitles()[0] is self.name):
            self.relatedTitles.append(relation.getTitles()[1])
        else:
            self.relatedTitles.append(relation.getTitles()[0])
        self.sortRelations()
        
    def sortRelations(self):
        self.relations.sort(key=lambda x: x.getTotalSim(), reverse=True)

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
    
    def getTags(self):
        return self.tags