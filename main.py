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

if args.all:
    print(f'\nЗадача {args.num}\n\nУСЛОВИЕ:\n---------------------------------')
    c.get_task(args.num)
    print('\nОТВЕТ:\n---------------------------------')
    n.get_ansver(args.num)

elif args.c:
    print(f'\nЗадача {args.num}\n\n')
    c.get_task(args.num)

elif args.ans:
    print(f'\nЗадача {args.num}\n\n')
    n.get_ansver(args.num)

else:
    print(f'\nЗадача {args.num}\n\n')
    print(args.isit)
