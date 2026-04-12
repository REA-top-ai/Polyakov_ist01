def done(user_name, ARM):
    if user_name == 'Дмитрий' and ARM == 1:
        return True
    if user_name == 'Ангелина' and ARM == 2:
        return True
    if user_name == 'Василий' and ARM == 3:
        return True
    if user_name == 'Екатерина' and ARM == 4:
        return True

    return False

user_name = input('Введите своё имя\n')
ARM = int(input('Введите свой APM'))

text_for_users = 'Добро пожаловать'
Dmitiy_check = 'Дмитрий, твое рабочее место находится в другой комнате. Отойди от чужого компьютера и займись работой!'

if done(user_name, ARM):
    print(text_for_users)

elif user_name == 'Дмитрий':
    print(Dmitiy_check)

else:
    print('Логин или пароль не верный, попробуйте еще раз')