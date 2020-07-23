num = int(input('Enter a number, and its factorial will be printed: '))

if num < 0:
    raise ValueError('You must enter a non negative integer')

fact = 1

for i in range(2, num + 1):
    fact *= i

print(fact)
