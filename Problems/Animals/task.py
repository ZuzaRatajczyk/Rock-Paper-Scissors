# read animals.txt
# and write animals_new.txt
file_1 = open('animals.txt', 'r')
animals_1 = file_1.readlines()
file_2 = open('animals_new.txt', 'w')
animals_2 = [animal.replace('\n', ' ') for animal in animals_1]
for animal in animals_2:
    file_2.writelines(animal)
file_1.close()
file_2.close()
