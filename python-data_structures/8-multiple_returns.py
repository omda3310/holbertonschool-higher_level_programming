#!/usr/bin/python3
def multiple_returns(sentence):
    if len(sentence) == 0:
        return 0, None
    a = len(sentence)
    b = sentence[0]
    new_sentence = (a, b)
    return new_sentence
