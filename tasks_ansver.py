loc = locals()


def get_ansver(num_task):
    num_task_ansver = 'code_' + str(num_task)

    try:
        ansver = num_task_ansver
        print(loc[ansver]())

    except KeyError:
        print('Решение пока не найдено...')


def code_96():
    for a in range(20, 100):
        res = (2 * a) + (a / 2) + (a / 4) + 1
        if res == 100:
            a = int(a)
            ansver = f'Гусей в стаде было {a}'
            break

    return ansver


def code_101():
    for a in range(2, 11):
        base = a - 2
        Per = base + a * 2
        if Per == 28:
            ansver = f'Сторона равнобедренного треугольника равна {a}, а основание - {base}'
            break

    return ansver


if __name__ == '__main__':
    print('Этот файл существует не для исполнения!!\nЗдесь находится код решения задач)')
