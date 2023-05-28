import string

sym = string.punctuation


def give_me_list(name_file):
    with open(name_file, 'r') as file:
        return file.readlines()


def change_list(name_file):
    lst = give_me_list(name_file)
    for i in range(len(lst)):
        lst[i] = lst[i].lower()
        lst[i] = lst[i].strip()
        for j in sym:
            if j in lst[i]:
                lst[i] = lst[i].replace(j, '')
        lst[i] = lst[i].replace('\n', '')
    return lst


def write_file(name_file):
    new_file = open('result text.txt', 'w+')
    lst = change_list(name_file)
    for i in lst:
        new_file.write(i)
        new_file.write('\n')


my_file = 'original text'
print(write_file(my_file))


