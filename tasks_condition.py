# import textwrap as wr


loc = locals()
width_screen = 40


def get_task(num_task):
    num_task_text = 'num_' + str(num_task)
    try:
        condition = loc[num_task_text]

        # condition = wr.dedent(condition)
        # condition = wr.indent(condition, '\n')
        # condition = wr.fill(condition, width_screen)

        print(condition)

    except KeyError:
        print('Условие не написано')


num_96 = """
Летело стадо гусей, а навстречу им летит один гусь и говорит:

- Здравствуйте, сто гусей!
- Нас не сто, - отвечает ему вожак стада, - если бы нас было столько, сколько теперь, да ещё столько, да полстолька, да четверть столька, да ещё ты, гусь, с нами, так тогда нас было бы сто гусей
ы
Сколько было в стаде гусей?
"""

num_101 = """
Периметр равнобедренного треугольника равен 28 см. Основание его на 2 см меньше боковой стороны. 

Найти стороны треугольника.
"""

if __name__ == '__main__':
    print('Этот файл существует не для исполнения!!\nЗдесь находятся тексты условий задач)')
