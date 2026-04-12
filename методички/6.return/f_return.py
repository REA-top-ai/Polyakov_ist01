def calc_age(current_year,birth_year):
    return current_year - birth_year
my_age = calc_age(2049,1993)
dads_age = calc_age(2049,1953)
print("Мне ",my_age," лет, а моему отцу ",dads_age," лет")

#===============================================================================

def get_boundaries(target,margin):
    low_limit = target - margin
    high_limit = target + margin
    return low_limit,high_limit
low_limit,high_limit = get_boundaries(100,20)
print("Нижний предел:",low_limit,", верхний предел:",high_limit)

#===============================================================================

def repeat_stuff(stuff,num_repeats = 10):
    return stuff * num_repeats
lyrics = repeat_stuff("Row",3) + "Your Boat"
song = repeat_stuff("Row")
print(song)