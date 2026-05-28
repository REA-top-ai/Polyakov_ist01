
def is_allive(func):
    def wrapper(self,*args,**kwargs):
        health = self.health
        if health <= 0:
            print(f"{self.name} мертв")
            return None
        else:
            return func(self, *args, **kwargs)
    return wrapper

def log_action(func):
    def wrapper(self, *args):
        print(f'[LOG] Action starts: {func.__name__}')
        result = func(self, *args)
        print(f'[LOG] Action is ended')
        return result
    return wrapper

def ivent(func):
    def wrapper(self, *args, **kwargs):
        print(f'ur health and mana is improved twise')
        self.health *= 2
        self.mana *= 1.5
        print(f'for this event now u have staff')
        self.items['священный посох'] = {'mana':5}
        if self.hero_class == 'mid_liner':
            self.mana += 5
        result = func(self, *args, **kwargs)
        return result
    return wrapper

def use_taunt(func): #испоьлозвать насмешку 
    def wrapper(self,*args,**kwargs):
        #print(f'{self.name} использовал ')
        result = func(self, *args, **kwargs)
        return result
    return wrapper

class Hero:
    def __init__(self,name,health,mana,hero_class,spell_names,items):
        self.name = name
        self.health = health
        self.mana = mana
        self.hero_class = hero_class
        self.spell_names = spell_names
        self.items = items
    
    @is_allive
    def attack(self,damage):
        print(f"{self.name} нанес урон {damage} единиц")
    
    @log_action
    def heal(self,amount):
        self.health += amount
        print(f"{self.name} вылечил на {amount} единиц здоровья")
        return self.health

    @is_allive
    def cast_spell(self,spell_name):
        mana_cost = self.spells_name[spell_name]['mana_cost']
        self.mana -= mana_cost
        print(f"{self.name} использовал заклинание {spell_name}")
        return self.mana

    
    def add_spell(self,spell_name):
        self.spells_name.update(spell_name)
        return self.spells_name
    def add_item(self,item_name):
        if len(self.items) >= 6:
            print("Нельзя добавить больше 6 предметов")
            return None
        self.items.update(item_name)
        return self.items
    @use_taunt
    def taunt(self,taunt_name):
        print(f'{self.name} использовал: {taunt_name}')

    @ivent    
    def event_check(self):
        print('Corespondently with a celebration u will have a new item = twise, improved mana and improved health')
        print(self.items)
        print(self.mana)
        print(self.health)

Pudge = Hero('Stray228', 100, 50, 'mid_liner', {'disamber': {'mana_cost': 10}}, {'hook': {'damage': 5}})
Pudge.attack(20)
Pudge.taunt('Насмешка')