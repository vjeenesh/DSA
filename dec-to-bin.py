def DecimalToBinary(decNum):
    
    pow = 1
    bin = 0

    while (decNum > 0):
        rem = decNum % 2
        decNum //= 2
        bin += (rem * pow)
        pow *= 10
    
    return bin


for i in range(0, 11):
    print(f"{i} in binary is {DecimalToBinary(i)}")


print(4 & 8) # Bitwise AND
print(4 | 8) # Bitwise OR

# print(DecimalToBinary(10))
# print(DecimalToBinary(42))
# print(DecimalToBinary(2))
# print(DecimalToBinary(69))
# print(DecimalToBinary(246))
# print(DecimalToBinary(1225))
