from random import*

name = input() #"Леха Картоха"
question = input()#"Ты когда-нибудь видел(а), чтобы снег падал вверх, а не вниз?"
answer = ""
random_number = randint(1,9)

if random_number == 1:
    answer = "Да, безусловно"

elif random_number == 2:
    answer = " Это решительно так"

elif random_number == 3:
    answer = "Без сомнения"

elif random_number == 4:
    answer = "Ответ туманный, попробуйте еще раз"

elif random_number == 5:
    answer = "Спросите еще раз позже"

elif random_number == 6:
    answer = "Лучше не говорить вам сейчас"

elif random_number == 7:
    answer = "Мои источники говорят "нет""

elif random_number == 8:
    answer = "Прогноз не очень хороший"

elif random_number == 9:
    answer = "Очень сомнительно"
else :
    print("Ошибка")

if name == "":
    print("Вопрос:",question)
else :
    print(name,"спрашивает:",question)
if question == "":
    print("Magic 8-Ball не может принести удачу, иначе ткань реальности окажется под угрозой!")
else :
    print("Магический шар отвечает:",answer)
