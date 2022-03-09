#!/usr/bin/env python3


"""Eric Tedford | Alta3 Training - Python Basics
   Challenge: for loop - Lab 29"""


#Create List
farms = [{"name": "NE Farm", "agriculture": ["sheep", "cows", "pigs", "chickens", "llamas", "cats"]},
         {"name": "W Farm", "agriculture": ["pigs", "chickens", "llamas"]},
         {"name": "SE Farm", "agriculture": ["chickens", "carrots", "celery"]}]

for farm in farms:
    print(farm.get("name"))
    for agri in farm.get("agriculture"):
        print(" -", agri)


