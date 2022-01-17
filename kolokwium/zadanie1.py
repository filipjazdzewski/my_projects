def how_many_b(string):
    if len(string) == 0:
        return 0
    if string[0] == 'b':
        return 1 + how_many_b(string[1:])
    else:
        return how_many_b(string[1:])


print(how_many_b('Alamabota'))
