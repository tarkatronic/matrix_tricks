#!/usr/bin/env python

# This is the original implementation, when the data was defined as "matrix" and only requested a single print
#matrix = [[1, 2, 3],[4, 5, 6], [7, 8, 9]]
#print [a for b in [[y ** 2 for y in x] for x in matrix[::-1]] for a in b if a > 25]

lol = [[1, 2, 3],[4, 5, 6], [7, 8, 9]]
# "Invert" wasn't clearly defined, so I went with [[a,b,c],[d,e,f]] -> [[d,e,f],[a,b,c]],
# as opposed to the alternate interpretation of [[a,b,c][d,e,f]] -> [[c,b,a],[f,e,d]]
inverse = [[y ** 2 for y in x] for x in lol[::-1]]
print(inverse)
print([a for b in inverse for a in b if a > 25])
