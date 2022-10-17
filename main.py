import math
import random
from rich.progress import track
import time
from time import sleep
from rich.console import Console

console = Console()
print('Привет ты зашел на калькулятор PIP')





variable = input('Что делаем M или G или P или gams: ' )


def maths ():
   var = input('Что делаем M или G или P или gams: ')
   if var == 'gams':
      GAMS()
   if var == 'P':
      generator ()
   if var == 'G':
      geomer()
   if var == 'M':
    a = input('Что делаем -, *, +, / или же возводим в степень **:   ')
   if a == '**':
      h = int(input('Введите число: '))
      j = int(input('Введите в какую степень хотите возвести: '))
      print('ответ ' + str(h**j))
   if a == '-':
      g = int(input('Введите первое число:' ))
      f = int(input('Введите второе число:' ))
      print('Ответ ', g - f )
   if a == '+':
      g = int(input('Введите первое число:' ))
      f = int(input('Введите второе число:' ))
      print('Ответ ', g + f )
   if a == '/':
      g = int(input('Введите первое число:' ))
      f = int(input('Введите второе число:' ))
      print('Ответ ', g / f )
   if a == '*':
      g = int(input('Введите первое число:' ))
      f = int(input('Введите второе число:' ))
      print('Ответ ', g * f,)
   var = input('Хотите продолжить пиши yes: ' )
   if var == 'yes' or var == 'Да' or var == 'Yes' or var == 'да':
      maths ()
   else:
      print('Хорошо завершаю процес ')


def geomer ():
   print('Рассчитаем геометрические параметры прямоугольника')
   print('_________________________________________________')
   a = float(input('Введите длинну прямоугольника..'))
   b = float(input('Отлично,теперь ширину ..'))
   perimeter = 2 * (a + b)
   diagonal = math.sqrt(a**2 + b**2)
   square = a * b
   print('Периметр прямоугольника равен', perimeter, sep=' --> ')
   print('Диагональ прямоугольника равна', diagonal, sep=' --> ')
   print('Площадь прямоугольника равна', square, sep=' --> ')
   var = input('Хотите продолжить пиши yes: ' )
   if var == 'yes' or var == 'да' or var == 'Yes' or var == 'Да':
      maths ()
   else:
      print('Хорошо завершаю процес')

def generator ():
 chars = 'qwertyuiopasdfghjklzxcvbnmQWERTYUIOPASDFGHJKLZXCVBNM1234567890'

 number = int(input('Кол-во паролей: '))
 lenght =  int(input('Длина строки: '))




 for i in track(range(20), description="Генерирую..."):
    time.sleep(0.5)
 for x in range(number):
    password = ''

    for i in range(lenght):
        password += random.choice(chars)
    console.print(password, style="bold blue")   

    file = open( 'password.txt', 'a' )
    file.write('\n' + password)
    file.close()
 var = input('Хотите продолжить пиши yes: ' )
 if var == 'yes' or var == 'да' or var == 'Yes' or var == 'Да':
   maths ()
 else:
   print('Хорошо завершаю процес')


def GAMS ():

 city_list = ['Манго', 'Виноград', 'Манго', 'Арбуз', 'Манго', 'бомба+10', 'Манго', 'Манго']

 s = int(input('Хотите поиграть жми 1: '))

 r = 0
 y = int(input('Сколько крутите:'))
 console = Console()
 tasks = [f"Ваш результат:  {n}" for n in range(1, y)]

 def gems ():

    with console.status("[bold green]Кручу колесо --> ") as status:
        while tasks:
            task = tasks.pop(0)
            sleep(2)
            console.log(f"{task} " + random.choice(city_list))
    var = input('Хотите продолжить пиши yes: ' )
    if var == 'yes' or var == 'да' or var == 'Yes' or var == 'Да':
      maths ()
    else:
      print('Хорошо завершаю процес')


 if s == 1:
    gems ()
 else:
    print('Ок я заканчиваю')





#Жизнь странная штука,то хорошая,то плохая....Мне бывает тяжело... :( Hо бывает весело  когда я вижу улыбку Егора Сергеевича ;) Хаха Егор привет вам если вы это видите ;)

# Lil peep "Life Is Beautiful" 



















if variable == str('gams'):
   GAMS ()
if variable == str('M'):
   maths()
if variable == str('G'):
   geomer()
if variable == str('P'):
   generator()




#Рынок плохой если на нём нет конкурентов
