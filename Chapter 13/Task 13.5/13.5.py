import random


def histogram(s):
    d = dict()
    for c in s:
        if c not in d:
            d[c] = 1
        else:
            d[c] += 1
    return d


def select_from_hist(s):
    h = histogram(s)
    d = {key: value/sum(h.values()) for key, value in h.items()}
    return random.choices(list(d.keys()), weights=list(d.values()))


print(*select_from_hist('aab'))
