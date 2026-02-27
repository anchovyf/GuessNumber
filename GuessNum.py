import random
def GuessTheNumber(max_num):
     num = random.randint(1, max_num)
     attempt = 0
     while True:
        attempt += 1
        try:
         answer = int(input(f'===========================\n Введите число от 1 до {max_num}: \n\n '))
        except ValueError:
          print('\n===========================\n Емае! Принимаю только числа, без остальных символов!')
          continue
        if answer < 1 or answer > max_num:
          print(f' Лээээ, сказал же, от 1 до {max_num}\n===========================\n\n dayum\n')
          continue
        if answer == num:
          print(f'\n===========================\n Вы угадали за {attempt} попыток!\n===========================')
          break
        elif answer < num:
          print('\n===========================\n Вы не угадали, число должно быть больше ')
        elif answer > num:
          print('\n===========================\n Вы не угадали, число должно быть меньше ')
try:
    difficult = int(input('\n===========================\n Выберите сложность: \n 1. Легкая \n 2. Нормальная \n 3. Тяжелая \n '))
except ValueError:
    print('\n===========================\n Ой-ой. Надо ввести цифру от 1 до 3\n===========================')
    exit()
if difficult == 1:
    GuessTheNumber(10)
elif difficult == 2:
    GuessTheNumber(100)
elif difficult == 3:
    GuessTheNumber(1000)
else:
    print('\n===========================\n Такой сложности нету, перезапускай игру\n===========================')
