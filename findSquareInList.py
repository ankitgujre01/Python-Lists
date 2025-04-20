num = list(map(int, input("Enter numbers separated by space: ").split()))

square = list(map(lambda x: x**2, num))
print("Square of numbers:", square)