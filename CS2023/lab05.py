## Lab 5: Required Questions - Dictionaries  ##

_author_ = "Andrew Pipo"
_credits_ = "https://stackoverflow.com/questions/24101524/finding-median-of-list-in-python"
_email_ = "pipoat@mail.uc.edu" # Your email address

# imports for all RQs

import random
import os
from urllib.request import urlopen
from statistics import median
import doctest


# RQ1
def merge(dict1, dict2):
    """Merges two Dictionaries. Returns a new dictionary that combines both. You may assume all keys are unique.

    >>> new =  merge({1: 'one', 3:'three', 5:'five'}, {2: 'two', 4: 'four'})
    >>> new == {1: 'one', 2: 'two', 3: 'three', 4: 'four', 5: 'five'}
    True
    """
    dictnew = {}
    for i in dict1:
        dictnew[i] = dict1[i]
    for j in dict2:
        dictnew[j] = dict2[j]
    return dictnew


# RQ2
def counter(message):
    """ Returns a dictionary where the keys are the words in the message, and each
    key is mapped (has associated value) equal 
    to the number of times the word appears in the message.
    >>> x = counter('to be or not to be')
    >>> x['to']
    2
    >>> x['be']
    2
    >>> x['not']
    1
    >>> y = counter('run forrest run')
    >>> y['run']
    2
    >>> y['forrest']
    1
    """
    dictnew2 = {}
    for i in message.split():
       dictnew2[i] = 0
    for i in message.split():
       dictnew2[i] += 1
    return dictnew2


# RQ3
def replace_all(d, x, y):
    """ Returns a dictionary where the key/value pairs are the same as d, 
    except when a value is equal to x, then it should be replaced by y.
    >>> d = {'foo': 2, 'bar': 3, 'garply': 3, 'xyzzy': 99}
    >>> replace_all(d, 3, 'poof')
    >>> d == {'foo': 2, 'bar': 'poof', 'garply': 'poof', 'xyzzy': 99}
    True
    """
    
    
    for i in d:
        if d[i] == x:
            d[i] = y

# RQ4
def sumdicts(lst):
   """ 
   Takes a list of dictionaries and returns a single dictionary which contains all the keys/value pairs found in list. And 
   if the same key appears in more than one dictionary, then the sum of values in list of dictionaries is returned 
   as the value mapped for that key
   >>> d = sumdicts ([{'a': 5, 'b': 10, 'c': 90, 'd': 19}, {'a': 45, 'b': 78}, {'a': 90, 'c': 10}] )
   >>> d == {'b': 88, 'c': 100, 'a': 140, 'd': 19}
   True
   """
   dictnew3 = {}
   for i in lst:
       for j in i:
           dictnew3[j] = 0
   for k in lst:
      for x in k:
           dictnew3[x] += k[x]
   return dictnew3

def build_successors_table(tokens):
    """Takes in a list of words or tokens. Return a dictionary: keys are words; values are lists of successor words. By default, we set the first word in tokens to be a successor to "."
    >>> text = ['We', 'came', 'to', 'investigate', ',', 'catch', 'bad', 'guys', 'and', 'to', 'eat', 'pie', '.']
    >>> table = build_successors_table(text)
    >>> sorted(table)
    [',', '.', 'We', 'and', 'bad', 'came', 'catch', 'eat', 'guys', 'investigate', 'pie', 'to']
    >>> table['to']
    ['investigate', 'eat']
    >>> table['pie']
    ['.']
    >>> table['.']
    ['We']
    """
    tbl = {}
    prev = '.'
    for word in tokens:
        if prev not in tbl:
            tbl[prev] = []
        tbl[prev] += [word]
        prev = word
    return tbl

def construct_tweet(word, tbl):
    
    result = ' '
    while word not in ['.','!','?']:
        result += word + ' '
        word = random.choice(tbl[word])
    return result + word

def shakespeare_tokens(path='shakespeare.txt', url='http://composingprograms.com/shakespeare.txt'):
    
    
    if os.path.exists(path):
        return open('shakespeare.txt', encoding='ascii').read().split()
    else:
        shakespeare = urlopen(url)
        return shakespeare.read().decode(encoding='ascii').split()

def random_tweet(table):
    
    return construct_tweet(random.choice(table['.']), table)

#RQ5
def middle_tweet(table):
    """ Calls the function random_tweet() 5 times (see Interactive Worksheet) and 
    returns the one string which has length in middle value of the 5.
    Returns a string that is a random sentence of average length starting with word, and choosing successors from table.
    """
    tweets = []
    tweetsize = []
    for i in range(5):
        tweets.append(random_tweet(table))
        tweetsize.append(len(tweets[i]))
        print(f"{tweets[i]} - length: {tweetsize[i]}\n")

                   
    return f"\n\nMedian Sentence:\n{tweets[tweetsize.index(median(tweetsize))]}" 



if __name__ == "__main__":
    doctest.testmod(verbose=True)
    print("")
    shakestokens = shakespeare_tokens()
    shakestable = build_successors_table(shakestokens)
    print(middle_tweet(shakestable))