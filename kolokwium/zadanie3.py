hexadecimal_file = open('szesnastkowo.txt', 'r')
decimal_file = open('dziesietnie.txt', 'w')
octal_file = open('osemkowo.txt', 'w')

for num in hexadecimal_file:
    decimal = int(num, 16)
    octal = oct(decimal)[2:]
    decimal_file.write(str(decimal) + '\n')
    octal_file.write(str(octal) + '\n')
