# Find the largest palindrome made from the product of two 3-digit numbers

i, j = 999
pal_list = []

while i > 100: 
    while j > 100:
        if str(i * j) == str(i * j)[::-1]:
            pal_list.append(i*j)
        j -= 1
    j = 999
    i -= 1

print(sorted(pal_list, reverse=True)[0])
