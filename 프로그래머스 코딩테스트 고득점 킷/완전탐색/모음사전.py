from itertools import product

def solution(word):
    words = []
    for i in range(1, 6):
        words += [''.join(w) for w in (product("AEIOU", repeat=i))]
    words = sorted(words)
    print(len(words))
    return words.index(word) + 1

word = "AAAAE"
print(solution(word))