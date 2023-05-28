import string

sym = string.punctuation


def give_me_list(name_file: str) -> list:
    with open(name_file, 'r') as file:
        return file.readlines()


def change_list(name_file: str) -> list:
    lst = give_me_list(name_file)
    lst[0] = lst[0].replace('\n', '')
    for i in range(1, len(lst)):
        lst[i] = lst[i].lower()
        lst[i] = lst[i].strip()
        for j in sym:
            if j in lst[i]:
                lst[i] = lst[i].replace(j, '')
        lst[i] = lst[i].replace('\n', '')
    return lst


def write_file(name_file: str):
    new_file = open('result text.txt', 'w+')
    lst = change_list(name_file)
    for i in lst:
        new_file.write(i)
        new_file.write('\n')


def give_me_quantity_words(uniq=False) -> int:
    with open('result text.txt', 'r') as file:
        lst = file.readlines()
        lst = [lst[i].split() for i in range(len(lst))]
        lst = [lst[i][j] for i in range(len(lst))
               for j in range(len(lst[i]))]

    if uniq:
        d = {}
        key = 0
        for i in lst:
            if i not in d.keys():
                key = i
                d[key] = 1
            else:
                d[key] += 1
        count = 0
        for value in d.values():
            if value == 1:
                count += 1
        return count
    return len(lst)


my_file = 'original text'
write_file(my_file)
print(give_me_quantity_words())
