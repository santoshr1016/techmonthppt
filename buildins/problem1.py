from functools import reduce
# Use map to create a function which finds the length of each word in the phrase (broken by spaces) and return the values in a list.

# The function will have an input of a string, and output a list of integers.
# use len() function for strings
# [3, 4, 3, 3, 5, 2, 4, 6]


def word_lengths(phrase):
    return list(map(len, phrase.split()))

ret = word_lengths('How long are the words in this phrase')
print(ret)


# Use filter to return the words from a list of words which start with a
# target letter.
# 34321
def digits_to_num(digits):
    return reduce(lambda x,y: x*10 + y, digits)

print(digits_to_num([3,4,3,2,1]))


# Use filter to return the words from a list of words which start with a
# target letter.
# ['hello', 'ham', 'hi', 'heart']

def filter_words(word_list, letter):
    # return list(filter(lambda x: x.startswith(letter), word_list))
    return list(filter(lambda word: word[0] == letter, word_list))

l = ['hello','are','cat','dog','ham','hi','go','to','heart']
print(filter_words(l,'h'))

# Use zip and list comprehension to return a list of the same length where each value is the two strings
# from L1 and L2 concatenated together with connector between them. Look at the example output below:
# concatenate(['A','B'],['a','b'],'-')
# ['A-a', 'B-b']

def concatenate(L1, L2, connector):
    return [word1+connector+word2 for (word1, word2) in zip(L1, L2)]
# [(A,a), (B,b)]
print(concatenate(['A','B'],['a','b'],'-'))

# Use enumerate and other skills to return a dictionary which has the values of the list as keys
# and the index as the value. You may assume that a value will only appear once in the given list.
# d_list(['a','b','c'])
# {'a': 0, 'b': 1, 'c': 2}

def d_list(L):
    return {key:value for key,value in enumerate(L)}

print(d_list(['a','b','c']))