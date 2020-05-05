#!/usr/bin/python3
def multiple_returns(sentence):
    firstchar = sentence[0] if sentence else None
    sentlen = len(sentence)
    return (sentlen, firstchar)
