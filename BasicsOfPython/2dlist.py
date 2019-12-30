number_grid = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9],
    [0]
]
print(number_grid[0][0])
"""
for row in number_grid:
    for col in row:
     #   print(number_grid)
"""

def trans_langauge(sentence):
    ret_sentence=""
    for letter in sentence:
        if letter in "AEIOUaeiou":
            ret_sentence=ret_sentence+"g"
        else:
            ret_sentence=ret_sentence +letter
    return ret_sentence

print(trans_langauge(input("enter a vlaue for translation : ")))



