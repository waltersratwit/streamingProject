# -*- coding: utf-8 -*-
"""
Created on Mon Nov 28 22:06:28 2022

@author: waltersr
"""

import title
import relation

title1 = title.Title("batman", 5, ["comedy","action"], "file path")
title2 = title.Title("superman", 5, ["comedy","action","fun"], "file path")
title3 = title.Title("spiderman", 5, ["comedy","fun"], "file path")
sbrelation = relation.Relation(title1, title2, {"comedy":[5],"action":[3]})
# print(sbrelation)
ssrelation = relation.Relation(title2, title3, {"comedy":[1],"fun":[5]})
# print(ssrelation)

# print(title2.getRelations())

ssrelation.addSim("comedy",11)

# print(sbrelation.getTitles())
# print(title1.getRelations())
# print()
print(title2.getRelations())
# print()
# print(title3.getRelations())
# print()
# print(title1.relatedTitles)
# print()
# print(sbrelation.getAvgSim())
# print(sbrelation.getTotalSim())