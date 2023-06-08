import string


def read_lines_from_file(name_file: str) -> list:
    with open(name_file, 'r') as file:
        return file.readlines()


def sanitize_list(name_file: str) -> list:
    sym = string.punctuation
    lst = read_lines_from_file(name_file)

    def _sanitize(word: str) -> str:
        word = word.strip().lower()
        word = ''.join([a for a in word if a not in sym])
        return word

    head = lst[0].strip()
    lst = [head] + [_sanitize(word) for word in lst[1:]]

    return lst


def write_file(name_file: str):
    with open('result text.txt', 'w+') as new_file:
        lst = sanitize_list(name_file)
        for i in lst:
            new_file.write(i)
            new_file.write('\n')


def read_text(text: str) -> list[str]:
    lst = read_lines_from_file(text)
    return [word for line in lst for word in line.split()]


def create_dict(lst: list) -> dict:
    d = {}
    for key in lst:
        d.setdefault(key, 0)
        d[key] += 1
    return d


def give_me_quantity_words() -> int:
    lst = read_text('result text.txt')
    return len(lst)


def give_me_quantity_uniq_words() -> int:
    lst = read_text('result text.txt')
    d = create_dict(lst)
    return len(d.keys())


def give_me_list_popular_words(kol=20) -> list:
    lst = read_text('result text.txt')
    d = create_dict(lst)

    res = sorted(d.items(), reverse=True, key=lambda x: x[1])
    return [x[0] for x in res][:kol]


def write_filter_words():
    filter_lst = read_text('list words')

    write_file('original text')
    lst_result = read_text('result text.txt')

    res = [l for l in lst_result if l not in filter_lst]

    with open('result text.txt', 'w+') as file:
        for i in res:
            file.write(i)
            file.write('\n')