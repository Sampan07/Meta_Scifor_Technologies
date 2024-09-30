# -*- coding: utf-8 -*-
"""08/07

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/16yeYEHVAuzYL3yaphGflEjJSm6jq9hRG

create a dictionary with all the operations
"""

team = {
    "Captain": "Rohit",
    "Bowler": "Bumrah",
    "Wicketkeeper": "Pant",
    "Vice Captain": "Hardik",
    "Batsman": "Virat",
    "Coach": "Dravid"
}
for i in team.items():
    print(i)

for i in team.keys():
    print(i)

for i in team.values():
    print(i)



# print(team.items())
# print(team.keys())
# print(team.values())
team.pop("Wicketkeeper")
print(team)
team.update({"Wicketkeeper": "Samson"})
print(team)
print(team.get("Batsman"))
del team["Coach"]
print(team)
team.popitem()
print(team)
team.clear()
print(team)

"""sets and its functions

"""

shapes = {"Ellipse","Circle","Cylinder","Cone","Square","Rectangle","Triangle","Parallelogram","Pyramid","Cube","Star","Rhombus","Hexagon","Octagon","Decagon","Diamond"}
shapes_upto_four_sides = {"Triangle","Rhombus","Parallelogram","Rectangle","Square"}
shapes_more_than_four_sides = {"Octagon","Pentagon","Hexagon","Cube","Star","Pyramid","Decagon","Diamond"}
shapes.add("Pentagon")
print(shapes)
d = shapes.difference(shapes_upto_four_sides)
print(d)
e = shapes.intersection(shapes_more_than_four_sides)
print(e)
f = shapes.union(shapes_upto_four_sides)
print(f)
g = shapes_more_than_four_sides.issubset(shapes)
print(g)
h = shapes.issuperset(shapes_upto_four_sides)
print(h)

shapes.remove("Rhombus")
print(shapes)
item = shapes.pop()
print(item)
print(shapes)
shapes.clear()
print(shapes)