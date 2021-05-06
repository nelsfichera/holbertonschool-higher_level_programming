#!/usr/bin/python3
def best_score(a_dictionary):
    if a_dictionary and a_dictionary.get:
        best = sorted(a_dictionary, key=a_dictionary.get, reverse=True)
        return (best[0])
    else:
        return None
