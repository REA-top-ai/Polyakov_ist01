def rang(grade):

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

grade = float(input("Введите ваш балл"))
rang(grade)