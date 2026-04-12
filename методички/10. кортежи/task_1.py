correct = (1, 2, 3, 2, 1, 2, 1, 3, 1, 2, 1, 2, 3, 3, 2, 1, 2, 1, 2, 1)
ans = input("введите ответы:")
ans = [int(x) for x in ans]
if tuple(ans) == correct:
    print("Экзамен сдан")
else :
    print("Экзамен провален")