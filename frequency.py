""" Analyzes the word frequencies in a book downloaded from
Project Gutenberg """

import string
import requests


def get_word_list(file_name):
    """ Reads the specified project Gutenberg book.  Header comments,
    punctuation, and whitespace are stripped away.  The function
    returns a list of the words used in the book as a list.
    All words are converted to lower case.
    """
    f = open(file_name)
    lines = f.readlines()
    text=""
    words = []
    final_words = []
    letters = ['A','a','B','b','C','c','D','d','E','e','F','f','G','g','H','h','I',
               'i','J','j','L','l','M','m','N','n','O','o','P','p','Q','q','R','r',
               'S','s','T','t','U','u','V','v','W','w','X','x','Y','y','Z','z']
    for i in lines:
        if i[0:len("*** START")] == "*** START":
            begin = lines.index(i)+1
            break
    for el in reversed(lines):
        if el[0:len("*** END")] == "*** END":
            end = lines.index(el)
            break
    text_lines = lines[begin:end]
    #guttenburg info has been stripped.
    for o in text_lines:
        text = text+o
    liney = text.splitlines()
    for stuff in liney:
        j = stuff.split(" ")
        words += j
    for word in words:
        newword = ""
        for character in word:
            if character not in letters:
                newword += ""
            else:
                newword += character
        if newword != "":
            final_words.append(newword.lower())
    return final_words



def get_top_n_words(word_list, n):
    """ Takes a list of words as input and returns a list of the n most frequently
    occurring words ordered from most to least frequently occurring.

    word_list: a list of words (assumed to all be in lower case with no
    punctuation
    n: the number of words to return
    returns: a list of n most frequently occurring words ordered from most
    frequently to least frequentlyoccurring

    """
    freqdict = {}
    unique_words = []
    for i in word_list:
        if i in unique_words:
            freqdict[i] +=1
        if i not in unique_words:
            freqdict[i] = 1
            unique_words.append(i)
    Try1 = (sorted(freqdict, key = freqdict.get))
    return (Try1[-n:])



if __name__ == "__main__":
    print("Running WordFrequency Toolbox")
    print(string.punctuation)
    r=get_word_list("astudyinscarlet.txt.utf-8")
    print(get_top_n_words(r,10))
