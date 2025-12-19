#!/usr/bin/env python3
# -*- coding:utf-8 -*-

NormKG = {"MATCH":("minimal_unit", 2),
          "SOLO":("minimal_unit", 1),
          "TEAM_UP_3":("minimal_unit", 3)}

FactDB = {"that_six_young_persons":{"quantity":6,
                                    "unit":"person"},
          "that_single_pianist":{"quantity":1,
                                 "unit":"person"}
          }

def STANDARD(dimension):
    if dimension in NormKG.keys():
        return NormKG[dimension]
    else:
        return None

def FactAccess(key, dimension):
    if key=="":
        pass
    else:
        return FactDB[key][dimension]

def NamedEntity(entity=""):
    return entity

def OUTSIDERS(n, z):
    return n * z

def MATCH_EVENT(d="", entity="", n=0):
    entity_name = NamedEntity(entity)
    norm = d
    
    z = norm[1]
    y = FactAccess(entity_name, dimension="quantity")
    
    tu_count = (y / z) + n
    outsiders = OUTSIDERS(n, z)
    
    return int(tu_count), int(outsiders)

if __name__ == "__main__":
    
    verb_standard = STANDARD("MATCH")
    target_entity = "that_six_young_persons"

    print("--- Internal Reading (n=0) ---")
    results = MATCH_EVENT(d=verb_standard, entity=target_entity, n=0)
    print(results)

    print("\n--- External Reading (n=3) ---")
    results = MATCH_EVENT(d=verb_standard, entity=target_entity, n=3)
    print(results)

    print("\n--- Mixed Reading (n=1) ---")
    results = MATCH_EVENT(d=verb_standard, entity=target_entity, n=1)
    print(results)