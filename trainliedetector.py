from sys import stdin

p = False
train_capacity, train_stations = map(int, stdin.readline().split())
v = 0

for i in range(train_stations):
    left, entered, stayed = map(int, stdin.readline().split())
    v -= left
    if v < 0:
        break
    v += entered
    if v > train_capacity:
        break
    if stayed and v < train_capacity:
        break
else:
    p = (v == 0)

if p:
    print("possible")
else:
    print("impossible")
