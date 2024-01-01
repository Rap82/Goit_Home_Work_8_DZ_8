# ===================  Home work 8 ========================

# =================   Можливості деяких вбудованих пакетів Python =================

# =================== Робота з датою і часом (datetime)  ==========================

# Робота з датою і часом у Python реалізована у пакеті datetime. Основні можливості datetime:



# визначення поточної дати і часу;
# обчислення інтервалу між двома подіями;
# визначення дня тижня, високосного року для будь-якої дати у минулому не раніше року datetime.MINYEAR
# або в майбутньому не пізніше року datetime.MAXYEAR;
# порівняння дати і часу декількох подій за допомогою операторів порівняння;
# робота з часовими зонами, порівняння подій з урахуванням часових зон та переходу на літній/зимовий час;
# перетворення дати/часу в рядок і навпаки.
# Щоб отримати поточну дату і час без урахування часового пояса, можна викликати метод now() у datetime:



# from datetime import datetime

# current_datetime = datetime.now()
# print(current_datetime) # 2020-10-09 22:13:35.053819


# У результаті виклику now() ми отримуємо об'єкт datetime, у якого є ряд корисних атрибутів:



# from datetime import datetime

# current_datetime = datetime.now()

# print(current_datetime.year)        # 2020
# print(current_datetime.month)       # 10
# print(current_datetime.day)         # 09
# print(current_datetime.hour)        # 22
# print(current_datetime.minute)      # 32
# print(current_datetime.second)      # 22
# print(current_datetime.microsecond) # 819366


# В об'єкта datetime є методи, щоб отримати дату (без часу) та час (без дати):



# from datetime import datetime

# current_datetime = datetime.now()
# print(current_datetime.date())  # 2020-10-09
# print(current_datetime.time())  # 22:13:35.053819


# Щоб створити об'єкт datetime з будь-якою вибраною датою, можна зробити так:



# from datetime import datetime

# d1 = datetime(year=2012, month=1, day=7, hour=14)
# print(d1) # 2012-01-07 14:00:00


# Щоб дізнатися день тижня, можна скористатися методом weekday:



# from datetime import datetime

# seventh_day_2020 = datetime(year=2020, month=1, day=7, hour=14)
# print(seventh_day_2020.weekday())   # 1


# Дні тижня у Python починаються з понеділка і він буде 0. У прикладі вище 7 Січня 2020 року було вівторком.



# Щоб порівняти два об'єкти datetime, достатньо скористатися оператором порівняння:



# from datetime import datetime

# current_datetime = datetime.now()

# future_month = (current_datetime.month % 12) + 1
# future_year = current_datetime.year + int(current_datetime.month / 12)
# future_datetime = datetime(future_year, future_month, 1)

# print(current_datetime < future_datetime)    # True


# ================================ Звдання 1 / Task 1 ======================================

# ++++++++   Робота з датою і часом у Python реалізована у пакеті datetime +++++++++++++++

# Основні можливості datetime:

# визначення поточної дати і часу;
# обчислення інтервалу між двома подіями;
# визначення дня тижня, високосного року для будь-якої дати у минулому не раніше року datetime.MINYEAR 
# або майбутньому не пізніше року datetime.MAXYEAR;
# порівняння дати і часу декількох подій за допомогою операторів порівняння;
# робота з часовими зонами, порівняння подій з урахуванням часових зон та переходу на літній/зимовий час;
# перетворення дати/часу в рядок і навпаки.
# DATETIME
# Щоб отримати поточну дату і час без урахування часового пояса, можна викликати метод now() у datetime:

# from datetime import datetime

# current_datetime = datetime.now()
# print(current_datetime) # 2020-10-09 22:13:35.053819
# У результаті виклику now() ми отримуємо об'єкт datetime, у якого є ряд корисних атрибутів:

# from datetime import datetime

# current_datetime = datetime.now()

# print(current_datetime.year)        # 2020
# print(current_datetime.month)       # 10
# print(current_datetime.day)         # 09
# print(current_datetime.hour)        # 22
# print(current_datetime.minute)      # 32
# print(current_datetime.second)      # 22
# print(current_datetime.microsecond) # 819366
# У об'єкту datetime є методи, щоб отримати дату (без часу) та час (без дати):

# from datetime import datetime

# current_datetime = datetime.now()
# print(current_datetime.date())  # 2020-10-09
# print(current_datetime.time())  # 22:13:35.053819
# Щоб створити об'єкт datetime з будь-якою вибраною датою, можна зробити так:

# from datetime import datetime

# d1 = datetime(year=2012, month=1, day=7, hour=14)
# print(d1) # 2012-01-07 14:00:00
# Щоб дізнатися день тижня, можна скористатися методом weekday:

# from datetime import datetime

# seventh_day_2020 = datetime(year=2020, month=1, day=7, hour=14)
# print(seventh_day_2020.weekday())   # 1
# Дні тижня у Python починаються з понеділка і він буде 0. У прикладі вище 7 Січня 2020 року було вівторком.

# Щоб порівняти два об'єкти datetime, досить скористатися оператором порівняння.

# TIMEDELTA
# Якщо відняти від одного datetime об'єкту інший, то отримаємо timedelta об'єкт. Він відповідає за відрізок часу між двома датами.

# from datetime import datetime

# seventh_day_2019 = datetime(year=2019, month=1, day=7, hour=14)
# seventh_day_2020 = datetime(year=2020, month=1, day=7, hour=14)

# difference = seventh_day_2020 - seventh_day_2019
# print(difference)                   # 365 days, 0:00:00
# print(difference.total_seconds())   # 31536000.0
# Об'єкти timedelta можна створювати самостійно щоб отримати дату/час віддалену від початкової:

# from datetime import datetime, timedelta

# seventh_day_2020 = datetime(year=2020, month=1, day=7, hour=14)
# four_weeks_interval = timedelta(weeks=4)

# print(seventh_day_2020 + four_weeks_interval)   # 2020-02-04 14:00:00
# print(seventh_day_2020 - four_weeks_interval)   # 2019-12-10 14:00:00
# Об'єкт timedelta можна створити, задаючи тижні, дні, години, хвилини, секунди, мілісекунди і мікросекунди:

# from datetime import timedelta
# delta = timedelta(
#     days=50,
#     seconds=27,
#     microseconds=10,
#     milliseconds=29000,
#     minutes=5,
#     hours=8,
#     weeks=2
# )
# Якщо якийсь параметр не заданий, то він дорівнює 0 за умовчанням.

# Робота з часовими поясами припускає знання класів у Python і ми розглянемо її пізніше.

# TIMESTAMP
# Окремо треба сказати про timestamp. timestamp — це кількість секунд, що пройшло з 00 годин 00 хвилин 1 Січня 1970 року 
# у UTC (часовий пояс Грінвіча). Це просто прийнята константа і нічого особливого вона не означає. 
# Просто для зручності колись почали відлічувати час в секундах з цієї миті і це виявилося дуже зручно. 
# Адже порівняти два числа завжди легше і швидше, чим порівняти складну структуру дат і часів.

# Звичайно можна з timestamp отримати дату/час і навпаки:

# from datetime import datetime

# seventh_day_2020 = datetime(year=2020, month=1, day=7, hour=14)
# ts = seventh_day_2020.timestamp()
# print(ts)   # 1578398400.0

# ts += 100_000
# print(datetime.fromtimestamp(ts))   # 2020-01-08 17:46:40

# ++++++++++++++++++++++++++++++++++++++Умова / Condition ++++++++++++++++++++++++++++++++++++++++

# Розробіть функцію get_days_from_today(date), яка повертатиме кількість днів від поточної дати,
# де параметр date - це рядок формату '2020-10-09' (рік-місяць-день).

# Підказки:

# Параметр date розбити на рік, місяць та день можна використовуючи метод рядків split.
# datetime приймає аргументи типу int, використовуйте перетворення типів.
# ігноруйте години, хвилини та секунди для вашої дати, важливі повні дні.
# кількість днів ви можете отримати відніманням з поточної дати, заданої в змінній date (без часу).
# Наприклад: Якщо поточна дата - '5 травня 2021', то виклик get_days_from_today("2021-10-09") поверне нам -157.


# ++++++++++++++++++++ Код / Code ++++++++++++++++++++++++++++++++++++

# from datetime import datetime  # З бібліотеки *datetime  імпортуємо функцію *datetime . Бібліотека для роботи з датою і часом.


# def get_days_from_today ( date ) : # Функція яка приймає оди аргумент . *date (тип *str ) формату 'Рік-Місяць-День' # '2024-10-09'
#                                    # Повертає ціле число днів (тип *int) від поточної дати до вказаної в *date .
#                                    # якщо *date -містить майбутню дату (та яка має настати від поточної) То повертає відємне число днів.
#                                    # якщо *date -містить минулу дату (та яка вже відбулась  від поточної) То повертає додатнє число днів

#     list_some_date = date.split ('-')  # Передану у функцію дату *date типу рядок . Розділяємо методом *.split ('-') - по знаку тире "-"
#                                        # отримаємо у *list_some_date список із 3 елементів ,для ашого тестового значення - *['2024', '10', '09']. 
#                                        #  Де перший елемент списку '2024'- це рік, Другий - '10' -місяць, Третій '09' - день 

#     some_date =  datetime ( year = int ( list_some_date [0] ), month = int ( list_some_date [1] ), day = int ( list_some_date [2] ) ) # 
#                         # За допомогою вбудованої функції *datetime ( year = *int , month = *int, day = *int ) в зміну *some_date передаєм обєкт типу *datetime 
#                         #  В *year передаєм перший елемент з списку *list_some_date приведений до типу *int .  *int ( list_some_date [0] ) = 2024
#                         #  В *month передаєм другий елемент з списку *list_some_date приведений до типу *int .  *int ( list_some_date [1] ) = 10
#                         #  В *day передаєм третій  елемент з списку *list_some_date приведений до типу *int . *int ( list_some_date [2] ) = 09
#                         # Функція *datetime - містить ще інші парметри зокрема години , хв , секунди , мікросекунди . Але для нашого завдання ці дані непотрібні.
#                         # Всі параметри які не передані у фцнкцію замінняються 00 - нулями .
#                         # Тому для нашого випадку *some_date = 2024-10-09 00:00:00
    
#     # print ( list_some_date)
#     # print ( some_date )

#     data_now = datetime.now() # Предаєм у зміну *data_now поточне значення дати і часу за допомогою вбудованої функції *datetime і методу *.now() . 
#                               # Для нашого тестового значення 2023-12-30 07:34:52.039276 ( точний час на момент запуску коду)

#     # print (data_now )

#     data_diferent_curent = data_now.date() - some_date.date() # Порівнюємо два обєкти *datetime віднімаючи їх і результат передаємо в *data_diferent_curent
#                                                               # *data_diferent_curent = -284 days, 0:00:00
#     print ( data_diferent_curent)


#     return  data_diferent_curent.days  # повертаємо з нашої функції значення *data_diferent_curent - приведеного до форми *.days . 
#                                        # Метод *.days застосований до обєкта *datetime повертає з обєкта ціле число днів. 
#                                        # Якщо дата з майбутнього то відємне число. В нашому прикладі вказано майбутню дату ому поверне 
#                                        # -284

   


# date = '2024-10-09'  #  Тестове значення


# print ( get_days_from_today ( date ) )  # Принтимо результат роботи нашої функції  * get_days_from_today ( date ) = -284


# ================================ Звдання 2 / Task 2 ======================================

#   КІЛЬКІСТЬ ДНІВ НА МІСЯЦЬ

# ++++++++++++++++++++++++++++++++++++++Умова / Condition ++++++++++++++++++++++++++++++++++++++++

# Напишіть функцію визначення кількості днів у конкретному місяці. Ваша функція повинна приймати два параметри: 
# month - номер місяця у вигляді цілого числа в діапазоні від 1 до 12 і year - рік, що складається із чотирьох цифр. 
# Перевірте, чи функція коректно обробляє місяць лютий високосного року.

# ++++++++++++++++++++ Код / Code ++++++++++++++++++++++++++++++++++++

from datetime import date  #  З бібліотеки *datetime  імпортуємо функцію *datetime  . Бібліотека для роботи з датою і часом.

DAYS_in_MONTH = { '1': 31, '2': 28, '3': 31, '4': 30, '5': 31, '6': 30, '7': 31, '8': 31, '9': 30, '10': 31, '11': 30, '12': 31
   
                    }  # Словник який містить ключами місяці а значеннями кількість днів в цьому місяці . Для невисокосних років.

DAYS_in_MONTH_VYSOKOS = { '1': 31, '2': 29, '3': 31, '4': 30, '5': 31, '6': 30, '7': 31, '8': 31, '9': 30, '10': 31, '11': 30, '12': 31
   
                            }  # Словник який містить ключами місяці а значеннями кількість днів в цьому місяці . Для високосних років.

def vysokosnyj_year ( year ) : # Допоміжна функція . яка визначає чи перданий в функцію рік високосний.
                               # Приймає один аргумент . Ціле число . Повертає *True -якщо високосний і *False якщо ні.
    
    if  ( ( year % 4 == 0 ) and ( year % 100 != 0 ) or ( year % 400 == 0 ) ) : #Високочний рік повинен бути кратним 4 і не кратним 100 або кратним 400 .
       
       vysokosnyj_year  = True  # Якщо виконалась умова *if ... Значить рік високосний присвоюємо в *vysokosnyj_year = *True

    else:
      
      vysokosnyj_year  = False  #  Якщо не виконалась умова *if ... Значить рік не високосний присвоюємо в *vysokosnyj_year = *False
    
    return vysokosnyj_year  #  Повертаємо значення присвоюємо в *vysokosnyj_year . 


def get_days_in_month ( month, year ) :  # Основна фінкція . В ній перевіряємо чи переданий рік в *year високисний чи ні за допомогою функції *vysokosnyj_year ( year )
                                         #  Далі якщо високосний то повертаємо відповідне значення днів за ключем *month  з нашого словника *DAYS_in_MONTH_VYSOKOS
                                         #  якщо не високосний то повертаємо відповідне значення днів за ключем *month  з нашого словника *DAYS_in_MONTH
    
    month = str ( month )  #  Приводимо наш month до типу *str і переприсовоюємо це значення в *month

     
    if vysokosnyj_year ( year ) :  #  перевіряємо повернутий результат з функції *vysokosnyj_year ( year ) якщо високосний поверне *True
                                   

        days_in_month = DAYS_in_MONTH_VYSOKOS.get ( month )  # Якщо виконалась умова *if... То повертаємо відповідне значення для ключа * month з нашого словника *DAYS_in_MONTH_VYSOKOS 
                                                            #  для тестових значень *year = 2020 і *month = 2  Поверне -  29

        
     
        return days_in_month   # Повертаємо з функції значення *days_in_month
    
    else :
       
       days_in_month = DAYS_in_MONTH.get ( month )  # # Якщо не виконалась умова *if... То повертаємо відповідне значення для ключа * month  з нашого словника *DAYS_in_MONTH
                                                    #  для тестових значень *year = 2020 і *month = 2  Поверне -  28
       
       return days_in_month    #
       

month = 2  #  Тестове значення місяць Лютий . Для високосного року 29 днів 

year = 2020  # Тестове значення високосний рік . 

month = 2  # Тестове значення місяць Лютий . Для звичного  року 28 днів 

year = 2021  # Не вискосний рік

print ( get_days_in_month ( month, year ) )   # Прінтимо значення повернуті в результаті виконання нашої фцнкції *get_days_in_month ( month, year )
                                            #  Для звчайного року Лютий ( 2 місяць року) видасть 28 .
                                            #  Для високосного року Лютий ( 2 місяць року) видасть 29 .
