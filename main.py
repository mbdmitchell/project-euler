# https://projecteuler.net/problem=40

constant = ""
num = 1
while len(constant) < 1000000:
    constant += str(num)
    num += 1

print(int(constant[0]) * int(constant[9]) * int(constant[99]) * int(constant[999]) * 
int(constant[9999]) * int(constant[99999]) * int(constant[999999]))
