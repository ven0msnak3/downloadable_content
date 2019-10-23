temperatures = [10, -20, -289, 100]
def celsius_fahrenhiet(celsius):
    if celsius < -273.15:
        return "That value is lower than absolute zero!"
    else:
        f = celsius * 9/5 + 32
        return f

for t in temperatures:
    print(celsius_fahrenhiet(t))
