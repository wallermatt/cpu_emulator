old = 1
current = 0

for i in range(7):
    print(current)
    temp = current
    current = old + current
    old = temp
