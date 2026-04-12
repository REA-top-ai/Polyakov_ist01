print("для орентации ответов и заданий вам надо выбратиь номер задания, всего заданий 7,введя число 1 - 7 вам выйдет ответ на конкретное задание , но ввидя число 0 код остановиться ")
n = int(input("укажите номер задания "))
while n != 0 :
   
    if n == 1:
        # проверка выражения на True & False (первый тип задания)
        print((6 * 6) - 1 == 8 + 1)
        print(13 - 7 != (3 * 2) + 1)
        print(3 * (2 - 1) == 4 - 1)
        
    if n == 2:
        # проверка выражения на True & False (второй тип задания)
        print((6 * 6) - 1 >= 8 + 1)
        print(13 - 7 <= (3 * 2) + 1)
        print(3 * (2 - 1) > 4 - 1)
    if n == 3:
        # я закоментировал две следущих строки тк они мешали но задания с нимим сделал
            #bool_variable = true
            #print(bool_variable)
        # NameError: name 'true' is not defined. Did you mean: 'True'? ----------- проблема в регистре тк t!=T
        bool_variable = 'true'
        print(type(bool_variable))
        #Ошибка - <class 'str'>    это не лог переменная тк она заключена в ковычки и является стрингой - строкой 
        bool_variable_2 = True # такая запись позволит сделать переменную логической тк правильный регистр и нет ковычек
        print(type(bool_variable_2))
    if n == 4:
        user_name = input("Введите имя пользователя")
        Dmitriy_check = "Дмитрий, твое рабочее место находится в другой комнате. Отойди от чужого компьютера и займись работой!"
        Welcome_user = "Добро пожаловать"
        enter_number = 0
        if user_name != "Дмитрий":
            print(Welcome_user)
        else :
            print(Dmitriy_check)
            enter_number += 1                # тут от димы кол попыток не должно влиять но пока не к чему привзять 
            if enter_number <= 3:
                p = 3 - enter_number
                print("Попробуйте еще раз. У вас осталось",p,"попыток")
            else :
                print("Вы привысели количество попыток")
    if n == 5:
        statement_one = ((2 + 2 + 2 >= 6) and (-1 * -1 < 0))
        statement_two = ((4 * 2 <= 8) and (7 - 1 == 6))
        #Дмитрий номер АРМ 1
        #Ангелина номер АРМ 2
        #Василий номер АРМ 3
        #Екатерина номер АРМ 4

        user_name = input("Введите имя пользователя")
        ARM = int(input("Введите номер АРМ"))

        if user_name == "Ангелина" and ARM == 2:
            print("Добро пожаловать!")
        if user_name == "Василий" and ARM == 3:
            print("Добро пожаловать!")
        if user_name == "Екатерина" and ARM == 4:
            print("Добро пожаловать!")
        
        if user_name != "Дмитрий" and user_name == "Ангелина" and ARM != 2 :
            print("Логин или пароль не верный, попробуйте еще раз")
        if user_name != "Дмитрий" and user_name == "Василий" and ARM != 3 :
            print("Логин или пароль не верный, попробуйте еще раз")
        if user_name != "Дмитрий" and user_name == "Екатерина" and ARM != 4 :
            print("Логин или пароль не верный, попробуйте еще раз")
        if user_name == "Дмитрий"  and ARM != 1 :
            print("Дмитрий, твое рабочее место находится в другой комнате. Отойди от чужого компьютера и займись работой!")
    if n == 6:
        print((2 - 1 > 3) or (-5 * 2 == -10))
        print((9 + 5 <= 15) or (7 != 4 + 3))
    if n == 7:
        grade = float(input("Введите ваш балл"))
        if grade >= 4.0:
            print("A")
        elif grade >= 3.0:
            print("B")
        elif grade >= 2.0:
            print("C")
        elif grade >= 1.0:
            print("D")
        else :
            print("F")

    n = int(input("укажите номер задания "))
