loc = locals()


def get_ansver(num_task):
    num_task_ansver = '_code_' + str(num_task)

    try:
        ansver = num_task_ansver
        print(loc[ansver]())

    except KeyError:
        print('Решение пока не найдено...')


def _proc_task_1(
        reduced_value,
        reduction_percentage
):
    initial_value = (reduced_value * 100) / (100 - reduction_percentage)

    return initial_value


def _code_96():
    for a in range(20, 100):
        res = (2 * a) + (a / 2) + (a / 4) + 1
        if res == 100:
            a = int(a)
            ansver = f'Гусей в стаде было {a}'
            break

    return ansver


def _code_101():
    for a in range(2, 11):
        base = a - 2
        Per = base + a * 2
        if Per == 28:
            ansver = f'Сторона равнобедренного треугольника равна {a}, а основание - {base}'
            break

    return ansver


def _code_105():
    fresh_width = _proc_task_1(4.4, 12)
    ansver = f'Свежего кофе нужно взять {fresh_width:.0f} кг'

    return ansver


def _code_106():
    fresh_apples = _proc_task_1(16, 84)
    ansver = f'Свежих яблок нужно взять {fresh_apples:.0f} кг'

    return ansver


def _code_107():
    total = 900

    en_dict = {
        'oak': 'Eiche',
        'maple': 'Ahorn',
        'linden': 'Linde',
    }

    for oak in range(1, 900):
        maple = 2 * oak
        linden = 3 * maple

        if (oak + maple + linden) == total:
            ansver = 'Отдельно было выращено следующее количество саженцев:\n'
            for a in en_dict:
                ansver += f'\t{en_dict[a]}: {locals()[a]}\n'

    return ansver


def _code_108():
    a, b = 40, 30
    Per = a * 2 + b * 2
    # sq_side = int(Per / 4)
    sq_side = 0
    sq_Per = 1

    while Per != sq_Per:
        sq_side += 1
        sq_Per = sq_side * 4

    ansver = f'Квадрат со стороной {sq_side}'

    return ansver


if __name__ == '__main__':
    print('Этот файл существует не для исполнения!!\nЗдесь находится код решения задач)')
