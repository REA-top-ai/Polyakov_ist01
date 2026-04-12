caffeine_level = {"espresso": 64, "chai": 40, "decaf": 0, "drip": 120}
try :
    print(caffeine_level["matcha"])
except KeyError:
    print("Неизвестный уровень кофеина")

#=========================================

caffeine_level["matcha"] = 30
print(caffeine_level["matcha"])