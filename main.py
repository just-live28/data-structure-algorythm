d=[]
for i in range(11) :
  d.append([])
  for j in range(11) : 
    d[i].append(0)

n = int(input())
for i in range(n):
  l, dir, x, y = map(int, input().split())

  if dir == 0:
    for j in range(l):
      d[x][y+j] = 1
  else:
    for j in range(l):
      d[x+j][y] = 1








for i in range(1, 11) :
  for j in range(1, 11) :
    print(d[i][j], end=' ')
  print()