def get_force(train_mass,train_acceleration):
    return train_acceleration * train_acceleration

def get_energy(bomb_mass, c = 3 * 10 ** 8):
    return bomb_mass * c ** 2

def get_work(mass,yskr,distant):
    return get_force(mass,yskr) * distant


train_mass = 22680
train_acceleration = 10
train_distance = 100

train_force = get_force(train_mass,train_acceleration)
print(train_force)
print("Поезд GE поставляет",train_force," ньютонов силы")

bomb_energy = get_energy(1)
print("1 кг бомбы составляет",bomb_energy," Джоулей")
train_work = get_work(train_mass,train_acceleration,train_distance)
print("Поезд выполняет",train_work," Джоулей за",train_distance," метров.")