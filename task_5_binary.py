number = int(input("Enter a number: "))
binary = bin(number)[2:]  
# Convert to binary and remove '0b'
print("Binary:", binary)