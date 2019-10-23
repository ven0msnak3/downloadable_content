result = []
for i in range(1, 5):
    x = 5000 * 225
    z = x*3
    print('{}: {} x3: {} x8: {}'.format(i, x, z, x*8))
    result.append(x)

y = sum(int(x) for x in result)
print('The total is: {} x3 is: {} and x8 is: {}'.format(y, y*3, y*8))
