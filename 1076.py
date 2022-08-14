val = {
    "black":0,
    "brown":1,
    "red":2,
    "orange":3,
    "yellow":4,
    "green":5,
    "blue":6,
    "violet":7,
    "grey":8,
    "white":9
}
n = [0,0,0]
for i in range(3):
    n[i] = val[input()]
print((10 * n[0] + n[1]) * (10 ** n[2]))