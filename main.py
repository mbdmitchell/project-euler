# Euler 14 Which starting number, under one million, produces the longest Collatz sequence?

length = 1
longestNumber = 0
longestLength = 0

numPerm = 1

while numPerm <= 1000000:
    numTemp = numPerm

    while numTemp != 1:
        if numTemp % 2 == 0:
            numTemp /= 2
        else:
            numTemp = 3 * numTemp + 1
        length += 1

    if length > longestLength:
        longestLength = length
        longestNumber = numPerm

    length = 1
    numPerm += 1


print("Number: " + str(longestNumber))
print("Length: " + str(longestLength))

