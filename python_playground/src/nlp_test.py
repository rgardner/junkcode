#!/usr/bin/env python3

from nltk.corpus import wordnet as wn


def test_multiple_synsets():
    result = wn.synsets("dog")
    result_names = [r.name() for r in result]
    assert result_names == [
        "dog.n.01",
        "frump.n.01",
        "dog.n.03",
        "cad.n.01",
        "frank.n.02",
        "pawl.n.01",
        "andiron.n.01",
        "chase.v.01",
    ]


def test_synset_definition():
    result = wn.synset("dog.n.-1").definition()

    assert (
        result
        == "a hinged catch that fits into a notch of a ratchet to move a wheel forward or prevent it from moving backward"
    )
