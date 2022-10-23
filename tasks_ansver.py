loc = locals()


def get_ansver(num_task):
    num_task_ansver = 'code_' + str(num_task)
    ansver = num_task_ansver
    print(loc[ansver]())


def code_96():

    ansver = 'Hello!!'
    return ansver


if __name__ == '__main__':
    print('Этот файл существует не для исполнения!!\nЗдесь находится код решения задач)')

