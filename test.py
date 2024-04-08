
mapAdjacencyList = {}
n = 0
l = -1
r = 1
u = 1
d = -1

for n in range(10):
    for j in range(10):
        mapAdjacencyList[(n,j)] = [(n-1,j),(n,j+1),(n+1,j),(n,j-1)]

print(mapAdjacencyList)