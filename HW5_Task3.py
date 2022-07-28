#  3-Создайте два списка — один с названиями языков программирования, другой — с числами от 1 до длины первого.
# ['python', 'c#']
# [1,2]
# Вам нужно сделать две функции: первая из которых создаст список кортежей, состоящих из номера и языка,
# написанного большими буквами.
# [(1,'PYTHON'), (2,'C#')]
# Вторая — которая отфильтрует этот список следующим образом: если сумма очков слова имеет в делителях номер,
# с которым она в паре в кортеже, то кортеж остается, его номер заменяется на сумму очков.
# [сумма очков c# = 102, в делителях есть 2 с которым в паре. Значит список будет]
# [(1,'PYTHON'), (102,'C#')]
# Если нет — удаляется. Суммой очков называется сложение порядковых номеров букв в слове.
# Порядковые номера смотрите в этой таблице, в третьем столбце: https://www.charset.org/utf-8
# Это — 16-ричная система, поищите, как правильнее и быстрее получать эти символы.
# Cложите получившиеся числа и верните из функции в качестве ответа вместе с преобразованным списком


program_language = ['python', 'c#', 'pascal']
num_list = [i for i in range(1, len(program_language)+1)]

program_language = [program_language[i].upper()
                    for i in range(len(program_language))]
# program_language = map(lambda i: program_language[i].upper(), program_language)  В случае приминения функции "map", функция "upper()" не работает(


def get_tuple(language, numbers):
    find_tuple = [(numbers[i], language[i]) for i in range(len(numbers))]
    return find_tuple


def get_point(prog):
    point_list = []
    for i in range(len(prog)):
        summa = 0
        for j in range(len(prog[i])):
            summa += ord(prog[i][j])
        point_list.append(summa)
    return point_list


# def filter_list(tup, points):
#     for i in range(len(points)):
#         tup = list(filter(lambda x: points[i] % tup[()], points))
#     return tup


point = get_point(program_language)
print(point)
find_tuple = get_tuple(program_language, num_list)
print(find_tuple)
# sort_list = filter_list(find_tuple, point)
# print(sort_list)