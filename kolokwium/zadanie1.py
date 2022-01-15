def howManyA(string):
    if len(string) == 0:
        return 0
    if string[0] == 'a':
        return 1 + howManyA(string[1:])
    else:
        return howManyA(string[1:])


print(howManyA('Alamakota'))
