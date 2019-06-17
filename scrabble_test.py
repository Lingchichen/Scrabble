""" The assertions in this module are known to be accurate but errors are
always possible. If you get differing results please make a note of them.
"""

from __future__ import print_function

import string
import sys

import scrabble_challenge

def test_functionality():
    tile_pool = scrabble_challenge.TilePool()
    word_finder = scrabble_challenge.WordFinder()
    while len(tile_pool):
        letters = tile_pool.pop()
        for cross_letter in string.ascii_lowercase:
            for word, score in word_finder.list_words(letters, cross_letter):
                print(word, score)


def test_accuracy():
    letters = list('sdipwnv')
    cross_letter = 'g'
    word_finder = scrabble_challenge.WordFinder()
    results = list(word_finder.list_words(letters, cross_letter))
    assert len(results)
    word, score = results[0]
    assert word in ('swing', 'wings')
    assert score == 7


def test_accuracy_one_blank():
    letters = list('t huray')
    cross_letter = 'z'
    word_finder = scrabble_challenge.WordFinder()
    results = list(word_finder.list_words(letters, cross_letter))
    assert len(results)
    word, score = results[0]
    assert word == 'hazy'
    assert score == 9


def test_accuracy_two_blanks():
    letters = list('nd ui w')
    cross_letter = 'b'
    word_finder = scrabble_challenge.WordFinder()
    results = list(word_finder.list_words(letters, cross_letter))
    assert len(results)
    word, score = results[0]
    #word assertion error
    #there is no such word windburn in results
    assert word == 'windburn'
    assert score == 9


if __name__ == '__main__':
    test_functionality()
    test_accuracy()
    test_accuracy_one_blank()
    test_accuracy_two_blanks()
    sys.exit(0)
