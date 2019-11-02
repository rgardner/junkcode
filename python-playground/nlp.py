#!/usr/bin/env python3

snippet = "the fox jumped over the lazy brown dog slowly"


# Wordnet
from nltk.corpus import wordnet as wn

print(wn.synsets('dog'))
print(wn.synset('dog.n.-1').definition())
