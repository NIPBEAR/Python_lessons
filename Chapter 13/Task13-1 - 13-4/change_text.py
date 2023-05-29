import string


def give_me_list(name_file: str) -> list:
    with open(name_file, 'r') as file:
        return file.readlines()


def change_list(name_file: str) -> list:
    sym = string.punctuation
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


def read_text(text) -> list:
    with open(text, 'r') as file:
        lst = file.readlines()
    lst = [lst[i].split() for i in range(len(lst))]
    return [lst[i][j] for i in range(len(lst))
            for j in range(len(lst[i]))]


def create_dict(lst: list) -> dict:
    d = {}
    for i in lst:
        key = i
        if i not in d.keys():
            d[key] = 1
        else:
            d[key] += 1
    return d


def give_me_quantity_words() -> int:
    lst = read_text('result text.txt')
    return len(lst)


def give_me_quantity_uniq_words() -> int:
    lst = read_text('result text.txt')
    d = create_dict(lst)
    count = 0
    for value in d.values():
        if value == 1:
            count += 1
    return count


def give_me_list_popular_words(kol=20) -> list:
    lst = read_text('result text.txt')
    d = create_dict(lst)
    sort_values = sorted(d.values(), reverse=True)
    res = []
    for i in range(len(sort_values)):
        for key, values in d.items():
            if sort_values[i] == values and key not in res:
                res.append(key)
                break
    return [res[i] for i in range(kol)] if len(res) > kol \
        else [res[i] for i in range(len(res))]


def write_filter_words():
    filter_lst = read_text('list words')

    write_file('original text')
    lst_result = read_text('result text.txt')

    res = list(filter(lambda x: x not in filter_lst, lst_result))

    with open('result text.txt', 'w+') as file:
        for i in res:
            file.write(i)
            file.write('\n')
