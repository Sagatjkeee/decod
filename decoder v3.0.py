# This is just a demo version, it does not show full functionality | version: 3.0
# Sample : 25061 21931 11158 21171 30046 40079 54000 / 77172 80051  333 85713
kod = input("go: ")
kod_mass = kod.split()
print(kod_mass)


def visibility():
    Group_6_telegram_indicator = {'1': "Включена в 1й раздел", '2': "Включена в 3й раздел",
                                  '3': "Не включенна, т.к. осадков не было",
                                  '4': "Не включена, т.к. количество осадков не измерялось",
                                  '/': 'Включена в раздел 5'}
    Group_7_telegram_indicator = {'1': 'Включена', '2': 'Не включена', '3': 'Не включена',
                                  '4': 'Включена', '5': 'Не включена', '6': 'Не включена'}
    height = {'0': '<50', '1': '50-100', '2': '100-200', '3': '200-300', '4': '300-500', '5': '600-100',
              '6': '1000-1500', '7': '1500-2000', '8': '2000-2500', '9': 'облаков ниже 2500 нет', '/': '/'}
    visibility = {'00': '< 0.1', '01': '0.1', '02': '0.2', '03': '0.3', '04': '0.4', '05': '0.5', '06': '0.6',
                  '07': '0.7', '08': '0.8', '09': '0.9', '10': '1', '11': '1.1', '12': '1.2', '13': '1.3', '14': '1.4',
                  '15': '1.5', '16': '1.6', '17': '1.7', '18': '1.8', '19': '1.9', '20': '2', '21': '2.1', '22': '2.2',
                  '23': '2.3', '24': '2.4', '25': '2.5', '26': '2.6', '27': '2.7', '28': '2.8', '29': '2.9', '30': '3',
                  '31': '3.1', '32': '3.2', '33': '3.3', '34': '3.4', '35': '3.5', '36': '3.6', '37': '37.7','38': '3.8',
                  '39': '3.9', '40': '4.0', '41': '4.1', '42': '4.2', '43': '4.3', '44': '4.4', '45': '4.5','46': '4.6',
                  '47': '4.7', '48': '4.8', '49': '4.9', '50': '5', '56': '6', '57': '7', '58': '8', '59': '9','60': '10',
                  '61': '11', '62': '12', '63': '13', '64': '14', '65': '15', '66': '16', '67': '17', '68': '18','69': '19',
                  '70': '20', '71': '21', '72': '22', '73': '23', '74': '24', '75': '25', '76': '26', '77': '27','78': '28',
                  '79': '29', '80': '30', '81': '35', '82': '40', '83': '45', '84': '50', '85': '55', '86': '60','87': '65',
                  '88': '70', '89': '>70', '90': '<0.05km', '91': '0.05km', '92': '0.2km', '93': '0.5km',
                  '94': '1km', '95': '2km', '96': '4km', '97': '10km', '98': '20km', '99': '>=50km'}
    if kod_mass[0][0] in Group_6_telegram_indicator:
        print("Ir:" + kod_mass[0][0] + ' Группа 6 ' + Group_6_telegram_indicator[kod_mass[0][0]])
    if kod_mass[0][1] in Group_7_telegram_indicator:
        print("Ix:" + kod_mass[0][1] + ' Группа 7 ' + Group_7_telegram_indicator[kod_mass[0][1]])
        if kod_mass[0][2] in height:
            print("h:" + kod_mass[0][2] + ' Высота облаков: ' + height[kod_mass[0][2]])
    print("Видимость (VV): " + visibility[kod_mass[0][3] + kod_mass[0][4]] + ' метров(если больще 90, то..)')


def wind():
    cloud_cover ={'0':'◯', '1':'⊘','2':'◔','3':'◔+|','4':'◑','5':'◑+|','6':'◕','7':'◖◗','8':'●','9':'⊗','/':'⊜'}
    print('Количество облочности(N): ' + cloud_cover[kod_mass[1][0]] + " см. центр табл справа")

    wind = kod_mass[1][1] + kod_mass[1][2]
    wind = int(wind) * 10
    print("Направление ветра: " + str(wind) + " Градусов")

    speed = kod_mass[1][3] + '.' + kod_mass[1][4]
    speed = float(speed) * 10
    print("Скорость ветра : " + str(speed) + "м/c")
    print('но это не точно ¯\_(ツ)_/¯ ' + kod_mass[1][3] + kod_mass[1][4])


def temp():
    if kod_mass[2][0] in '1':
        if kod_mass[2][1] in '0':
            sign = '-'
        else:
            sign = '+'
        if kod_mass[2][2] in '0':
            number_3 = ''
        else:
            number_3 = kod_mass[2][2]
    print('температура: ' + sign + number_3 + kod_mass[2][3] + ',' + kod_mass[2][4])


def dew_point():  # точка росы
    if kod_mass[3][0] == '2':
        if kod_mass[3][1] == '0':
            sign = '-'
        else:
            sign = '+'
        if kod_mass[3][2] == '0':
            number_3 = ''
        else:
            number_3 = kod_mass[3][2]
        print('точка росы: ' + sign + number_3 + kod_mass[3][3] + ',' + kod_mass[3][4])


def station_lvl_pressure():  # давление на уровне станции
    if kod_mass[4][0] in '3':
        if kod_mass[4][1] in '0':
            number_1 = '1'
            Plus_number = '0'
        elif kod_mass[4][1] in '234567':
            number_1 = kod_mass[4][1]
            Plus_number = ''
            print("но это не точно")
        elif kod_mass[4][1] in '89':
            number_1 = kod_mass[4][1]
            Plus_number = ''
        else:
            number_1 = kod_mass[4][1]
            Plus_number = '0'

        print('P на уровне станции: ' + number_1 + Plus_number + kod_mass[4][2] + kod_mass[4][3] + ',' + kod_mass[4][4])


def sea_lvl_pressure():
    if kod_mass[5][0] == '4':
        if kod_mass[5][1] in '0':
            number_1 = '1'
            Plus_number = '0'
        elif kod_mass[5][1] in '234567':
            number_1 = '0'
            Plus_number = '0'
            print("ERROR! Второе число мб только 0,8,9")
        elif kod_mass[5][1] in '89':
            number_1 = kod_mass[5][1]
            Plus_number = ''
        else:
            number_1 = kod_mass[5][1]
            Plus_number = '0'

        print('P на уровне моря: ' + number_1 + Plus_number + kod_mass[5][2] + kod_mass[5][3] + ',' + kod_mass[5][4])


def barometric_trend():
    if kod_mass[6][0] in '5':
        if kod_mass[6][1] in '01234':
            number_1 = '+'
        else:
            number_1 = '-'
        if kod_mass[6][2] in '0':
            number_2 = ''
        else:
            number_2 = kod_mass[6][2]
        print('барометрическая тенденция:' + number_1 + number_2 + kod_mass[6][3] + ',' + kod_mass[6][4])
        print('a = {} чекай в центральной таблице'.format(kod_mass[6][1]))


def weather_phenomenon():  # явление погоды
    past_weather = {'0':'Ясно или облачно','1':'Меняющаяся облачность','2':'Облачность не более 5 баллов',
                    '3':'!Песчанная буря...','4':'☰ Туман или сильная мгла','5':', Морось','6':'● Дождь',
                    '7':'* Снег или дождь со снегом','8':'∇ Ливневые осадки','9':'R Гроза с осадками или без них'}
    if kod_mass[8][0] == '7':
        print("Смотри в центр табл слева")
        print("погода в срок наблюдений(WW): " + kod_mass[8][1] + kod_mass[8][1] + 'см. в центр. табл. слева')
        print("Смотри в центр табл справа")
        print("W1: " + past_weather[kod_mass[8][3]])  # позже добавим словарь
        print("W2: " + past_weather[kod_mass[8][4]])


def overcast():
    if kod_mass[9][0] == '8':
        number_of_clouds = {'0':'0','1':'1','2':'2-3','3':'4','4':'5','5':'6','6':'7-8','7':'9','8':'10',}
        print("Центра справа")
        print("Nh: " + number_of_clouds[kod_mass[9][1]])
        print("Cl: " + kod_mass[9][2])
        print("Cm: " + kod_mass[9][3])
        print("Ch: " + kod_mass[9][4])


def last():
    if kod_mass[11][0] == '8':
        print("Центра справа")
        print("Nh: " + kod_mass[11][1])
        print("Cl: " + kod_mass[11][2])
        print("hh: " + kod_mass[11][3] + kod_mass[11][4])


visibility()
wind()
temp()
dew_point()
station_lvl_pressure()
sea_lvl_pressure()
barometric_trend()
weather_phenomenon()
overcast()
last()
