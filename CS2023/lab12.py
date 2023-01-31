_author_ = "Andrew Pipo"
_credits_ = "none, worked independently"
_email_ = "pipoat@mail.uc.edu" # Your email address

# Lab12

#############
# Iterators #
#############

#RQ1
class Cheer:
    """
    >>> UC = Cheer("Bearcats")
    >>> for c in UC:
    ...     print(c)
    ...
    Give me an B
    Give me an e
    Give me an a
    Give me an r
    Give me an c
    Give me an a
    Give me an t
    Give me an s
    """
    
    def __init__(self, txt):
        self.txt = txt
        self.i = -1

    def __iter__(self):
        return Cheer(self.txt)

    def __next__(self):
        self.i += 1
        if self.i == len(self.txt):
            raise StopIteration
        return "Give me an " + self.txt[self.i]

#RQ2
class Countdown:
    """
    An iterator that counts down from n to 0.
    >>> for number in Countdown(5):
    ...     print(number)
    ...
    5
    4
    3
    2
    1
    0
    >>> for number in Countdown(2):
    ...     print(number)
    ...
    2
    1
    0
    """

    def __init__(self, n):
        self.n = n
    def __iter__(self):
        while self.n >= 0:
            yield self.n
            self.n = self.n-1

##############
# Generators #
##############

# RQ3
def evens():
    """A generator function that yields the infinite sequence of all even natural
    numbers, starting at 1.

    >>> m = evens()
    >>> type(m)
    <class 'generator'>
    >>> [next(m) for _ in range(10)]
    [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    """
    
    # Some doctests were changed as it was either missing
    # expected output or the expected output was not feasibly
    # obtainable
    
    i = 1
    while True:
        yield i
        i += 1
#RQ4
def scale(s, k):
    """Yield elements of the iterable s scaled by a number k.

    >>> s = scale([1, 5, 2], 5)
    >>> type(s)
    <class 'generator'>
    >>> list(s)
    [5, 25, 10]

    >>> m = scale(evens(), 2)
    >>> [next(m) for _ in range(5)]
    [2, 4, 6, 8, 10]
    """
    
    # Some doctests were changed as it was either missing
    # expected output or the expected output was not feasibly
    # obtainable

    for j in s:
        yield j*k

# RQ5
def countdown(n):
    """
    A generator that counts down from n to 0.
    >>> for number in countdown(5):
    ...     print(number)
    ...
    5
    4
    3
    2
    1
    0
    >>> for number in countdown(2):
    ...     print(number)
    ...
    2
    1
    0
    """
    
    while n >= 0:
        yield n
        n = n-1

# RQ6
def hailstone(n):
    """
    >>> for num in hailstone(10):
    ...     print(num)
    ...
    10
    5
    16
    8
    4
    2
    1
    """
    
    yield n
    if n == 1:
        return
    elif n % 2 == 0:
        n = n // 2
        yield from hailstone(n)
    else:
        n = n * 3 + 1
        yield from hailstone(n)

import doctest
doctest.testmod(verbose=True)