#requires download of nltk in python
import os
import nltk
from nltk.corpus import *
import string
from textblob import TextBlob

def main():
    # prints all corpora in NLTK
    print("\nHere are the corpora built into nltk:")
    for h in os.listdir(nltk.data.find("corpora")):
        if '.zip' not in h:
            print(h)
    print()

    # stores user's corpus choice
    chosen_corpus = input("Enter corpus name (copy the name EXACTLY as listed): ")
    function_string = "nltk.corpus." + chosen_corpus + ".fileids()"

    # shows all files within user's corpus choice
    print("\nHere are the options from", chosen_corpus + ": \n")
    for corpus in eval(function_string):
        print(str(corpus))
    print()
 # tags all words with corresponding part-of-speech in user's text file choice
    punctuations = ";,.:"
    text_function = chosen_corpus + ".raw(str(input('Enter text file name (with .txt): ')))"
    text = eval(text_function)

    #text_test = "Hello world! Today is a good day to die young."
    #tokens_test = nltk.word_tokenize(text_test)
    #tagged_test = nltk.pos_tag(tokens_test)

    # tokens = nltk.word_tokenize(text)
    # words = [word for word in tokens if word.isalpha()]
    # tagged_corpus = nltk.pos_tag(tokens)
    update_corpus = ""
    s = ""
    wiki = TextBlob(text)
    #wiki_test = TextBlob(text_test)
    #wiki_tagged_test = wiki_test.tags
    wiki_tagged = wiki.tags
    wiki_tagged_corpus = wiki.words
    tagged_corpus = nltk.pos_tag(wiki_tagged_corpus)

    # current issue: POS tagged lists aren't the same
    # i think i removed the punctuations... but i need the pos tagged lists to be the same
    print(len(wiki_tagged_corpus))
    print(len(tagged_corpus))
    print(len(wiki_tagged))
    if len(tagged_corpus) == len(wiki_tagged):
        print("yay they're the same list!")
    else:
        print("they're diff bro")
    """
    for i in range(len(wiki_tagged)):
        if wiki_tagged[i] != tagged_corpus[i]:
            print("wiki_tagged: " + str(wiki_tagged[i]) + " and " + "tagged_corpus: " + str(tagged_corpus[i]))
    """
    

"""
    print(tagged_test)
    print()
    print(wiki_tagged_test)
    print()
    print("length of NLTK base: " + str(len(tagged_test)))
    print("length of TextBlob: " + str(len(wiki_tagged_test)))
"""
    
# check for POS discrepancies
"""
    for i in range(len(tagged_test) - 1):
        if wiki_tagged_test[i][1] != tagged_test[i][1]:
            s += "NLTK's base POS tagger tagged (" + str(tagged_test[i][0]) + ") as "
            s += str(tagged_test[i][1]) + "\n"
            s += "TextBlob's POS tagger tagged (" + str(wiki_tagged_test[i][0]) + ") as "
            s += str(wiki_tagged_test[i][0]) + "\n" + "\n"
    print(s)
"""

# check for same list

"""
    for i in range(len(tagged_corpus) - 1):
        if wiki_tagged[i][0] == tagged_corpus[i][0]:
            print("good check: " + str(wiki_tagged[i][0] + " " + str(tagged_corpus[i][0])))
"""

while True:
    answer = input("Run the 'POS Comparison' program? (y/n): ")
    if answer not in ('y', 'n'):
        print("Invalid input.")
        break
    if answer == 'y':
        main()
    else:
        print("Goodbye.")
        break