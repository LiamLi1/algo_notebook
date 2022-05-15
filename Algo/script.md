
```
T[0][0] = 1
For i = 1 to n
	T[i][0] = 0
For j = 1 to m
	T[0][j] = 0
For i = 1 to n
    For j = 1 to m
        if (j >= 2):
            T[i][j] += T[i - 1][j -2]
        if (i >= 2):
            T[i][j] += T[i - 2][j - 1]
return T[n][m]
```

```
for i = 1 to n:
    T[i][0] = 0
B = sum(p[i])
for i = 1 to n:
    for j = 1 to B:
        T[i][j] = T[i - 1][j]
        if j >= p[i]:
            T[i][j] = max(T[i][j], T[i][j - p[i]] + v[i])
return T[n][B]
```

my_map = {}
randInt(1, 15)  return 4  map:{4:15}  res = [4]
randInt(1, 14)  return 6  map:{4:15, 6:14} res = [4,6]
randInt(1, 13)  return 4  map:{4:13, 6:14} res = [4,6,15]
randInt(1, 12)  return 6  map:{4:15, 6:12} res = [4,6,15,14]
randInt(1, 11)  return 4  map:{4:11, 6:14} res = [4,6,15,14,13]

