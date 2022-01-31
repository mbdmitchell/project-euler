total = 0

for i in range(1000):  # add numbers from 0-999 which are divisible by 3 or 5 to 'total'
    if i % 3 == 0 or i % 5 == 0:
        total += i

print(total)
