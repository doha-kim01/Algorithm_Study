#1000
while (True):
  num = input()
  A = int(num[0])
  B = int(num[-1])
  if (0<A and A<10) and (0<B and B<10) :
    print(A+B)
    break

#18108
while (True):
  y = int(input())
  if (1000 <= y) and (y <= 3000):
    print(y-543)
    break

#14681
while(True):
  x = int(input())
  y = int(input())
  if x*y > 0:
    if y > 0:
      print(1)
    else :
      print(3)
  if x*y < 0:
    if y > 0:
      print(2)
    else :
      print(4)
  if(-1000 <= x and x <= 1000 and x != 0) and (-1000 <= y and y <= 1000 and y != 0):
    break

#11021
T = int(input())
for i in range(T):
    a,b = map(int, input().split())
    ans = a + b
    print("Case #%s: %s"%(i+1, ans ))