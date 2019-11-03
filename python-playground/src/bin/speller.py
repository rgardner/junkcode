import collections
import re


def words(text):
    return re.findall("[a-z]+", text.lower())


def train(features):
    model = collections.defaultdict(lambda: 1)
    for f in features:
        model[f] += 1
    return model


def main():
    NWORDS = train(words(open("big.txt").read()))


if __name__ == "__main__":
    main()
