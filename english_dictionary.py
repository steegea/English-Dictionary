
"""
An app that lets the user check whether a word exists or not
in a supplied JSON dictionary
"""

import json
from difflib import get_close_matches

def dict_search(w):
    data = json.load(open("data.json", "r"))
    w = w.lower()
    
    #If the user's word is in the JSON file
    if(w in data):
        return data[w]

    #If the user checks a proper noun
    elif(w.title() in data):
        return data[w.title()]

    #If the user checks an acronym
    elif(w.upper() in data):
        return data[w.upper()]

    #If the user enters a word that is not in the JSON file
    #but has some close matches
    elif len(get_close_matches(w, data.keys())) > 0:
        user_response = input("Did you mean %s instead? Enter Y/y if yes or N/n if no: " % get_close_matches(word, data.keys())[0])
        
        if user_response == "Y" or user_response == "y":
            return data[get_close_matches(w, data.keys())[0]]
        
        elif user_response == "N" or user_response == "n":
            return "The word does not exist. Please double-check it."
        
        else:
            return "You entered an invalid entry!"
    
    #If a user enters a word that does not exist in the JSON file
    #and there are no close matches for the user's word
    else:
        return "The word does not exist. Please double-check it."

word = input("Enter word: ")

output = dict_search(word)

#If the output is a list
if isinstance(output, list):
    for item in output:
        print(item)

#If the output is a string
else:
    print(output)