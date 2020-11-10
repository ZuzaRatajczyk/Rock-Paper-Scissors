# read sample.txt and print the number of lines
sample = open('sample.txt', 'r')
print(len(sample.readlines()))

sample.close()