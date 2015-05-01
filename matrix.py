matrix = [[1, 2, 3],[4, 5, 6], [7, 8, 9]]
print [a for b in [[y ** 2 for y in x] for x in matrix[::-1]] for a in b if a > 25]
