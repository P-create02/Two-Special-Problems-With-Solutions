substring = str(input())
list_one = list(substring)
aside = set()

for i in range(len(list_one)):
    # print(lista[i])
    if list_one[i] == ' ':
        part1 = list_one[:i]
        part2 = list_one[i+1:]

        sub_str_1 = ''.join([str(n) for n in part1])
        sub_str_2 = ''.join([str(m) for m in part2])

        for letter in sub_str_2:
            if sub_str_1.find(letter) != -1:
                aside.add(letter)

        if len(aside) == len(part1):
            print(1)
        else:
            print(0)
    i += 1
