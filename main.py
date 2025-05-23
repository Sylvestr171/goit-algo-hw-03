from datetime import datetime
from random import randint
import re

#->->->->->->->->->->***FIRST TASK***<-<-<-<-<-<-<-<-<-<

print ('\n\tFIRST TASK\n')

# Function for calculating the number of days between two dates
def get_days_from_today(date:str) -> int:
    
    """
    Function for calculating the number of days between two dates:
        - takes one parameter in date format 'YYYY-MM-DD';
        - outputs integer number of days betwen some days to today (if the some date is later then the current one, the result is negative);
        - only days are taken into account, hours, min. etc. are ignored;
        - function should handle incorrect input data format.

    Input:
    :param date: string

    Output:
    :return: integer
    """

    try: #перехоплення помилки неправильного формату даних
        date_in_datetime = (datetime.strptime(date, '%Y-%m-%d').date()) #перетворення рядка дати в об'єкт datetime
    except ValueError:
        print (f"\nUnknown format of date: '{date}'.\nPlease correct it and try againe!\n") #вивід повідомлення при перехопленні помилки
    else:
#        today_date = datetime.strptime('2021.05.05', '%Y.%m.%d').date() #ДЛЯ ТЕСТУВАННЯ, Вказання конкретної дати
        today_date = datetime.now().date() #створення змінної з поточною датою
        diff_day = (date_in_datetime - today_date).days #визначення різниці між датами в днях
#        print (date_in_datetime, type(date_in_datetime), today_date, type(today_date), diff_day, type(diff_day), sep='\t-----\t') #ДЛЯ ТЕСТУВАННЯ, перевірка виводу і типу даних
        return diff_day

'''Початок тестового блоку'''
test_date = ['2021-10-09', '2asd', '2025-10-09', '23.01.2202'] #ДЛЯ ТЕСТУВАННЯ, тестові дані
days_from_today = []
for date in test_date:
    days_from_today.append(get_days_from_today(date))
print (days_from_today) #ДЛЯ ТЕСТУВАННЯ, тестовий вивід
'''Кінець тестового блоку'''

#->->->->->->->->->->***SECOND TASK***<-<-<-<-<-<-<-<-<-<

print ('\n\tSECOND TASK\n')

# A function that return a set of random unique (within the same set) numbers within the specified parametres
def get_numbers_ticket(min:int, max:int, quantity:int) -> list:

    """
    A function that return a set of random unique (within the same set) numbers within the specified parametres
        - min - the minimum possible number in the set (not less than 1);
        - max - the maximum possible number in the set (not more than 1000);
        - quantity - the number of numbers to be selected (value between min and max);
        - the function  generates the specified number of unique numbers in the specified range;
        - the function returns a list of randomly selected, sorted numbers;
        - the numbers in the set must not be repeated;
        - if the parameters do not meet the specified restrictions, the function returns an empty list.
    
    Input:
    :param min: integer
    :param max: integer
    :param quantity: integer

    Output:
    :return: list
    """

    if 1 <= min <= max <= 1000 and quantity <= (max-min): #Перевірка умов параметрів 
        '''
        Умова quantity <= (max-min) потрібна щоб цикл while не піщов в нескінченність так як не можливо
        заповнити множину quantity унікальними числами якщо між max та min цих чисел менше ніж quantity
        '''
        set_of_random_number = set() #ініціалізуємо множину в яку будемо генерувати числа
        while len(set_of_random_number) != quantity: #запускаємо цикл який працюватиме до досягнення множиною визначеної довжини
            set_of_random_number.add(randint(min, max)) #власне генерація значень
#        print(sorted(list(set_of_random_number)), type(set_of_random_number))   #ДЛЯ ТЕСТУВАННЯ, перевірка сформованої множни і типів даних
        list_of_sorted_random_number = list(sorted(set_of_random_number)) #перетворення множини на список
    else:
        list_of_sorted_random_number = [] #створює пустий список
    
    return list_of_sorted_random_number

'''Початок тестового блоку'''
lottery_numbers = get_numbers_ticket(1, 49, 6)    #ДЛЯ ТЕСТУВАННЯ, тестовий виклик1, відповідає параметрам
print('Тест 1 (Параметри ОК)')
print("Ваші лотерейні числа:", lottery_numbers)    #ДЛЯ ТЕСТУВАННЯ, тестовий виклик1
lottery_numbers = get_numbers_ticket(10, 15, 10)    #ДЛЯ ТЕСТУВАННЯ, тестовий виклик2, quantity > max-min
print('Тест 2 (quantity > max-min), коли унікальних чисел min та max менше ніж розмір вибірки')
print("Ваші лотерейні числа:", lottery_numbers)    #ДЛЯ ТЕСТУВАННЯ, тестовий виклик2
lottery_numbers = get_numbers_ticket(0, 10, 5)    #ДЛЯ ТЕСТУВАННЯ, тестовий виклик3, min < 1
print('Тест 3 (min < 1)')
print("Ваші лотерейні числа:", lottery_numbers)    #ДЛЯ ТЕСТУВАННЯ, тестовий виклик3
lottery_numbers = get_numbers_ticket(2, 10000, 5)    #ДЛЯ ТЕСТУВАННЯ, тестовий виклик4, max > 1000
print('Тест 4 (max > 1000)')
print("Ваші лотерейні числа:", lottery_numbers)    #ДЛЯ ТЕСТУВАННЯ, тестовий виклик4
lottery_numbers = get_numbers_ticket(30, 15, 10)    #ДЛЯ ТЕСТУВАННЯ, тестовий виклик5, min > max
print('Тест 5 (min > max)')
print("Ваші лотерейні числа:", lottery_numbers)    #ДЛЯ ТЕСТУВАННЯ, тестовий виклик5
lottery_numbers = get_numbers_ticket(36, 537, 20)    #ДЛЯ ТЕСТУВАННЯ, тестовий виклик6, відповідає параметрам
print('Тест 6 (Параметри ОК)')
print("Ваші лотерейні числа:", lottery_numbers)    #ДЛЯ ТЕСТУВАННЯ, тестовий виклик6
'''Кінець тестового блоку'''

#->->->->->->->->->->***THIRD TASK (optional)***<-<-<-<-<-<-<-<-<-<

print ('\n\tTHIRD TASK\n')

#Function for normilize phone number format
def normalize_phone(phone_number:str) -> str:
    
    """
    Function for normilize phone number format
        - phone_number is a string with a phone number in various formats;
        - the function removes all characters except digits and the ‘+’ symbol;
        - if the international code is missing, the function adds the code ‘+38’. 
          This takes into account cases when the number begins with '380' (only the '+' is added) and when the number begins without a code (the '+38' is added);
        - the function returns a normalized phone number as a string.
    
    Input:
    :param phone_number: string
   
    Output:
    :return: string
    """
    cleaned_number = re.sub(r'[^0-9,+]', '', phone_number) #прибираємо все крім цифр і знака '+'
    if not cleaned_number.startswith('+'): #перевіряємо якщо номер починається не з '+'
        if cleaned_number.startswith('38'): #перевіряємо якщо на посатку '38' то даємо '+'
            cleaned_number = '+' + cleaned_number
        else:
            cleaned_number = '+38' + cleaned_number #в іншому разі '+38'

    return cleaned_number #повертаємо рядок з чистим номером

'''Початок тестового блоку'''
raw_numbers = [    "067\\t123 4567",    "(095) 234-5678\\n",    "+380 44 123 4567",    "380501234567",    "    +38(050)123-32-34",
    "     0503451234",    "(050)8889900",    "38050-111-22-22",    "38050 111 22 11   ",]     #ДЛЯ ТЕСТУВАННЯ, тестові дані

sanitized_numbers = [normalize_phone(num) for num in raw_numbers]    #ДЛЯ ТЕСТУВАННЯ, тестовий виклик
print("Нормалізовані номери телефонів для SMS-розсилки:\n", sanitized_numbers)     #ДЛЯ ТЕСТУВАННЯ, тестовий виклик
'''Кінець тестового блоку'''