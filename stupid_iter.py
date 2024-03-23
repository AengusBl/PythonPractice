from itertools import takewhile

word_list = ["flower", "flooding", "floors"]

a = word_list[0][0:(len(list(takewhile(lambda z: z, map(lambda y: len(y) == 1, [{letter} for letter in zip(word_list)])))))]

print(a)