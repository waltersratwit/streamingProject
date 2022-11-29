# -*- coding: utf-8 -*-
"""
Created on Mon Nov 28 22:06:28 2022

@author: waltersr
"""

import title
import relation

title1 = title.Title("batman", ["comedy","action"])
title2 = title.Title("superman", ["comedy","action","fun"])
title3 = title.Title("spiderman", ["comedy","fun"])
sbrelation = relation.Relation(title1, title2, {"comedy":[5],"action":[3]})
# print(sbrelation)
ssrelation = relation.Relation(title2, title3, {"comedy":[1],"fun":[5]})
# print(ssrelation)

ssrelation.addSim("comedy",11)

# print(sbrelation.getTitles())
print(title1.getRelations())
print(title2.getRelations())
print(title3.getRelations())
print()

print(sbrelation.getAvgSim())
print(sbrelation.getTotalSim())