maximum = int(input("Введите максимум:"))
minimum = int(input("Введите минимум:"))
srednei = int(input("Введите среднее:"))
otclan = int(input("Введите отклонение:"))
if (maximum > srednei + otclan * 3) or (minimum < srednei + otclan * 3):
    print("В ваших данных имеются выбросы и требуют предобработки")
if (maximum > srednei + otclan * 5) or (minimum < srednei+ otclan * 5):
    print("В ваших данных имеются экстремальные значения и требуют предобработки")
if (maximum < srednei + otclan * 3) or (minimum > srednei + otclan * 3):
    print("Ваши данные пригодны для анализа")