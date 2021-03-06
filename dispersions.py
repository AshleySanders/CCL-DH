#! /usr/bin/env python

from sys import nltk

# First, let's get input from the user:

print "Enter the word for which you would like to see a dispersion graph:",
word = raw_input()

# I can't get this to work for multiple words
# words = raw_input().split(",")


# Then we need to transform the base text using a series of steps.
# Please note this could be one line:

thefile = open('memoir.txt')
rawtext = thefile.read()
tokens = nltk.word_tokenize(rawtext)
text = nltk.Text(tokens)

# Now we can actually look at a word:

graphed = text.dispersion_plot([words])

# print(similarwords)