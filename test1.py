# A Simple Python function to compute sum of digits in numbers from 0 to number input
print(60 * "*")
while True:
    try:
        n = int(input('Enter a number to perform the operation: '))
        break
    except ValueError:
        print('Please enter a whole number')


'''
Returns sum of all digits in numbers from 1 to n
Two models
'''

# Progression = (a1 + an).n / 2.
def x1(n):
    return (n * (n + 1)) // 2

# Sum range
def x2(n):
  return sum(range(n+1))

print(60 * "*")
print("Sum of digits in numbers from 0 to", n)
print("Method 1:", x1(n))
print("Method 2:", x2(n))
print(60 * "*")
