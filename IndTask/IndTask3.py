from math import sqrt

one = [12, 25, 3, 48, 71]
two = [5, 18, 40, 62, 98]
three = [4, 21, 37, 56, 84]
maxe = (max(one) + max(two) +max(three)) / 2
mine = (min(one) + min(two) +min(three)) / 2
maxSquare = sqrt(maxe * (maxe - max(one)) * (maxe - max(two)) * (maxe - max(three)))
minSquare = sqrt(mine * (mine - min(one)) * (mine - min(two)) * (mine - min(three)))
print(maxSquare)
print(minSquare)