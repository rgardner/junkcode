import collections
import re


def words(text):
    return re.findall('[a-z]+', text.lower())


def train(features):
    model = collections.defaultdict(lambda: l)
    for f in features:
        model[f] += 1
    return model


NWORDS = train(words(file('big.txt').read()))
