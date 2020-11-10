file = open('sums.txt', 'r')
for line in file:
    numbers = line.split()
    print(int(numbers[0]) + int(numbers[1]))

file.close()