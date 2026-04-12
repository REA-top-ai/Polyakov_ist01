first_name = "Виталий"
last_name = "Красилов"
new_account = last_name[:5]
temp_password = last_name[2:6]
#----------------------------- Конкатенация

def account_generator(a,b):

    return a[:3] + b[:3]

new_account = "".join(account_generator(first_name,last_name))
#print(new_account)
#------------------------------ 3 задание

def password_generator(a,b):
    return a[len(a)-3:] + b[len(b)-3:]
temp_password = "".join(password_generator(first_name,last_name))
#print(temp_password_2)

#------------------------------ 4 task

company_motto= "Мечты сбываются"
second_to_last = company_motto[-2]
final_word = company_motto[-4:]

#------------------------------ 5 task

first_name = "Роб"
last_name = "Дейли"
fixed_first_name = "P" + first_name[1:] + " " + last_name

#------------------------------ 6 task

Robe_password = "theycallme\"crazy\"91"

#------------------------------ 7 task
poem_title = "spring storm"
poem_title_fixed = poem_title.title()
print(poem_title,poem_title_fixed)