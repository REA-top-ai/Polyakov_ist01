car_brand = input('Введите марку машины, на которой хотите поехать(Volkswagen Polo / BMW X1)\n')
age_of_driver = int(input('Введите возраст водителя, с которым хотели бы поехать(20 - 34)\n'))
experience_of_driver = int(input('Введите стаж водителя, с которым хотели бы поехать(2 - 15)\n'))
reputation_of_driver = int(input('Введите репутацию водителя, с которым хотели бы поехать(1 - 5)\n'))
traffic_jams = int(input('Введите загруженность дорог в данный момент(1 - 7)\n'))
trip_duration = int(input('Введите длительность поездки(в минутах)\n'))

rate_per_minute = 0
if car_brand == 'Volkswagen Polo':
    if 20 <= age_of_driver <= 27:
        if 2 <= experience_of_driver <= 9:
            if 1 <= reputation_of_driver <= 2:
                if 1 <= traffic_jams <= 3:
                    rate_per_minute = 8
                elif 4 <= traffic_jams <= 7:
                    rate_per_minute = 8.5
            elif 3 <= reputation_of_driver <= 5:
                if 1 <= traffic_jams <= 3:
                    rate_per_minute = 7.5
                elif 4 <= traffic_jams <= 7:
                    rate_per_minute = 7.4
    elif 27 <= age_of_driver <= 34:
        if 2 <= experience_of_driver <= 9:
            if 1 <= reputation_of_driver <= 2:
                if 1 <= traffic_jams <= 3:
                    rate_per_minute = 7.2
            elif 3 <= reputation_of_driver <= 5:
                if 1 <= traffic_jams <= 3:
                    rate_per_minute = 7
                elif 4 <= traffic_jams <= 7:
                    rate_per_minute = 7.2
        elif 10 <= experience_of_driver <= 15:
            if 1 <= reputation_of_driver <= 2:
                if 1 <= traffic_jams <= 3:
                    rate_per_minute = 6.9
                elif 4 <= traffic_jams <= 7:
                    rate_per_minute = 6.7
            elif 3 <= reputation_of_driver <= 5:
                if 4 <= traffic_jams <= 7:
                    rate_per_minute = 6.6

elif car_brand == 'BMW X1':
    if 20 <= age_of_driver <= 27:
        if 2 <= experience_of_driver <= 9:
            if 1 <= reputation_of_driver <= 2:
                if 1 <= traffic_jams <= 3:
                    rate_per_minute = 12
                elif 4 <= traffic_jams <= 7:
                    rate_per_minute = 12.5
            elif 3 <= reputation_of_driver <= 5:
                if 1 <= traffic_jams <= 3:
                    rate_per_minute = 11.6
                elif 4 <= traffic_jams <= 7:
                    rate_per_minute = 11.3
    elif 27 <= age_of_driver <= 34:
        if 2 <= experience_of_driver <= 9:
            if 1 <= reputation_of_driver <= 2:
                if 1 <= traffic_jams <= 3:
                    rate_per_minute = 11.4
            elif 3 <= reputation_of_driver <= 5:
                if 1 <= traffic_jams <= 3:
                    rate_per_minute = 11.7
                elif 4 <= traffic_jams <= 7:
                    rate_per_minute = 11.9
        elif 10 <= experience_of_driver <= 15:
            if 1 <= reputation_of_driver <= 2:
                if 1 <= traffic_jams <= 3:
                    rate_per_minute = 10.8
                elif 4 <= traffic_jams <= 7:
                    rate_per_minute = 11
            elif 3 <= reputation_of_driver <= 5:
                if 4 <= traffic_jams <= 7:
                    rate_per_minute = 10.9

price = rate_per_minute * trip_duration
if price == 0:
    print('Проверьте введённые вами данные, где-то допущена ошибка')
else:
    print(f'Стоимость вашей поездки составит {price}')
