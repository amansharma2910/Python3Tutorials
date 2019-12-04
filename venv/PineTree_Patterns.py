height= int(input("How tall is the tree: "))
spacesI= height-1
hashes=1
spacesF= height-1
while height!=0:
    for i in range(spacesI):
        print(" ", end="")
    for i in range(hashes):
        print("#", end="")
    print()
    hashes += 2
    spacesI -= 1
    height -= 1
for i in range(spacesF):
        print(" ", end="")
print("#")
