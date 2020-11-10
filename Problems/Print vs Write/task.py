numbers = [1234, 5678, 90]
numbers = str(numbers)
# save this list in `file_with_list.txt`
file = open('file_with_list.txt', 'w')
file.write(numbers)
file.close()
