
numbers = [1, 3, 4, 5, 7, 8, 9, 10, 11, 13, 15, 16, 18, 19, 20]

i = 0

while i < len(numbers):
    if(numbers[i] % 2 == 0):
        print("Even Number : " + str(numbers[i]))
    else:
        print("Odd Number : " + str(numbers[i]))
    i = i+1
