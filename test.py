
n = 611954591

x = 24738

while True:
    if n % x == 0:
        print("x is " + str(x))
        break
    x -= 1

x = 23333
y = 10000
while True:
    if x * y == n:
        print("y is " + str(y))
        break
    y += 1