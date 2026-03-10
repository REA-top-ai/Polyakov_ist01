from random import*
random_list = [randint(1, 100) for _ in range(101)]
print(random_list)
randomer_number = choice(random_list)
print(randomer_number)
