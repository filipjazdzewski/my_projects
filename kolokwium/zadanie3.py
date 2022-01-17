hexadecimal_file = open('szesnastkowo.txt', 'r')
decimal_file = open('dziesietnie.txt', 'w')
octal_file = open('osemkowo.txt', 'w')

hexadecimal = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9', 'A', 'B', 'C', 'D', 'E', 'F']
binary = ['0000', '0001', '0010', '0011', '0100', '0101', '0110', '0111',
          '1000', '1001', '1010', '1011', '1100', '1101', '1110', '1111']

for num in hexadecimal_file:
    binary_num = ''
    decimal_num = 0
    octal_num = 0
    for character in num:
        for i in range(len(hexadecimal)):
            if hexadecimal[i] == character:
                binary_num += binary[i]

    for i in range(len(binary_num) - 1, -1, -1):
        if binary_num[i] == '1':
            decimal_num += 2 ** (len(binary_num) - i - 1)
    decimal_file.write(str(decimal_num) + '\n')
    i = 1
    while decimal_num != 0:
        octal_num += (decimal_num % 8) * i
        decimal_num = decimal_num // 8
        i *= 10
    octal_file.write(str(octal_num) + '\n')

hexadecimal_file.close()
decimal_file.close()
octal_file.close()
