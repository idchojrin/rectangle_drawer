length = int(input("Enter a base "))
height = int(input("Enter a height "))
sequence = "*"
for i in range(0, height):
    for j in range(0, length):
        print(sequence, end='')
    print()