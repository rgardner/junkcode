def pigify(word: str):
    vowels = ["a", "e", "i", "o", "u"]
    for i, letter in enumerate(word):
        if letter not in vowels:
            continue
        return word[i:] + "-" + word[:i] + "way"


def test_piglatin():
    words = "This is a test".split()
    pigified = [pigify(word) for word in words]
    assert pigified == ["is-Thway", "is-way", "a-way", "est-tway"]
