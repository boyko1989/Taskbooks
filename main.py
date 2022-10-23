import tasks_condition as c
import tasks_ansver as n
import argparse

parser = argparse.ArgumentParser()

parser.add_argument("num")
parser.add_argument("-a", "--all", action='store_true', help="Выведет и условие и решение задачи")
parser.add_argument("-c", action='store_true', help="Выведет только условие (condition)")
parser.add_argument("-n", "--ans", action='store_true', help="Выведет только ответ")
parser.add_argument("-i", "--isit", action='store_true', help="Проверка наличия задачи")

args = parser.parse_args()

header_1 = f'\nЗадача {args.num}'
len_und = len(header_1) - 1

if args.all:
    print(header_1)
    print('=' * len_und + '\n\nУСЛОВИЕ:\n---------------------------------')
    c.get_task(args.num)
    print('\nОТВЕТ:\n---------------------------------')
    n.get_ansver(args.num)
    print()

elif args.c:
    print(header_1)
    print('=' * len_und)
    c.get_task(args.num)
    print()

elif args.ans:
    print(header_1)
    print('=' * len_und)
    n.get_ansver(args.num)
    print()

else:
    print(header_1)
    print('=' * len_und)
    print(args.isit + '\n')
