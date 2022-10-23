# import textwrap as wr


loc = locals()
width_screen = 40


def get_task(num_task):
    num_task_text = 'num_' + str(num_task)
    condition = loc[num_task_text]

    # condition = wr.dedent(condition)
    # condition = wr.indent(condition, '\n')
    # condition = wr.fill(condition, width_screen)

    print(condition)



num_96 = """
Летело стадо гусей, а навстречу им летит один гусь и говорит:

- Здравствуйте, сто гусей!
- Нас не сто, - отвечает ему вожак стада, - если бы нас было столько, сколько теперь, да ещё столько, да полстолька, да четверть столька, да ещё ты, гусь, с нами, так тогда нас было бы сто гусей

Сколько было в стаде гусей?
"""

if __name__ == '__main__':
    print('Этот файл существует не для исполнения!!\nЗдесь находятся тексты условий задач)')
