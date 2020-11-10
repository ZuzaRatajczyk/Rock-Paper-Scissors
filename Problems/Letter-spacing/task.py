word = input()
num_of_spaces = int(input())
spaces = num_of_spaces*' '
for char in word:
    print(char, end=spaces)
