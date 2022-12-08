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
        print(results)
        if results.get('title') != name:
            results = rq.get('https://api.themoviedb.org/3//tv/{}?api_key=ec0c9cf926c79f5c0a1ecf728d746601'.format(id)).json()
            self.movie = False

        self.id = id
        self.name = name
        self.poster_image = results.get('poster_path')
        self.description = results.get('overview')
        self.rating = results.get('vote_average')
        self.relations = []
        self.relatedTitles = []
        print(results)

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
            print(titles)
            if (titles[0] is self.name):
                output.append((titles[1], x.getAvgSim()))
            else:
                output.append((titles[0], x.getAvgSim()))
        return output

title = Title(1399, "Game of Thrones")

title = Title(550, "Fight Club")
