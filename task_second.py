numbers = str(input())
t = list(numbers)
subsidiary = []
other_num = []

for i in range(len(numbers)):
    if numbers[i] == ' ':
        part = numbers[i+1:]
        part_two = ''.join([str(m) for m in part])

        for letter in part_two:
            if letter == '?':
                subsidiary.append(letter)
            else:
                other_num.append(letter)

        if len(subsidiary) == 0:
            print(1)
        elif len(subsidiary) == 1 and len(other_num) == 0:
            print(10)
        elif len(subsidiary) == 1 and len(other_num) == 1:
            print(9)
        elif part[0] == '?' and len(subsidiary) > 1:
            print(9 * (10 ** (len(subsidiary) - 1)))
        else:
            print(10 ** len(subsidiary))
    i += 1
