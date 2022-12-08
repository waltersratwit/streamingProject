# -*- coding: utf-8 -*-
"""
Created on Mon Dec  5 15:29:03 2022

@author: waltersr
"""

# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.


import requests as rq

class Title:

    def __init__(self, id, name):
        self.movie = True
        results = rq.get('https://api.themoviedb.org/3//movie/{}?api_key=ec0c9cf926c79f5c0a1ecf728d746601'.format(id)).json()
        # print(results)
        self.name = results.get('title')
        if "{}".format(results.get('title')).lower() != name.lower(): # the format and lower are to account for incorrect capitalization
            results = rq.get('https://api.themoviedb.org/3//tv/{}?api_key=ec0c9cf926c79f5c0a1ecf728d746601'.format(id)).json()
            self.name = results.get('name')
            self.movie = False

        self.id = id
        self.poster_image = results.get('poster_path')
        self.description = results.get('overview')
        self.rating = results.get('vote_average')
        self.tags = []
        for tag in results.get('genres'):
            self.tags.append(tag["name"])
        self.relations = []
        self.relatedTitles = []
        # print(results)
    
    def __str__(self): # formats printing the object
        return "{} {:.1f}/10\nGenres: {}\n{}".format(self.name, self.rating, ", ".join(self.tags), self.description)

    def addRelation(self, relation):
        self.relations.append(relation)
        if (relation.getTitles()[0] == self.name):
            self.relatedTitles.append(relation.getTitles()[1])
        else:
            self.relatedTitles.append(relation.getTitles()[0])
        self.sortRelations()
    
    def sortRelations(self):
        self.relations.sort(key=lambda x: x.getTotalSim(), reverse=True)

    def getName(self):
        return self.name
    
    def getID(self):
        return self.id

    def getRelations(self):
        output = []
        for x in self.relations:
            titles = x.getTitles()
            print(titles)
            if (titles[0] is self.name):
                output.append((titles[1], x.getAvgSim()))
            else:
                output.append((titles[0], x.getAvgSim()))
        return output

# title1 = Title(1399, "Game of Thrones")

# title2 = Title(550, "Fight Club")

# title3 = Title(268, "Batman")

# print(title1)
# print()
# print(title2)
