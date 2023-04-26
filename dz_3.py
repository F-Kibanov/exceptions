import datetime


def get_surname():
    while True:
        surname = input('Введите фамилию: ')
        if surname:
            if surname.isalpha():
                return surname
        print('Введите корректную фамилию!')

def get_name():
    while True:
        name = input('Введите имя: ')    
        if name:
            if name.isalpha():
                return name
        print('Введите корректное имя!')

def get_patronymic():
    while True:
        patronymic = input('Введите отчество: ')
        if not patronymic or patronymic.isalpha():
            return patronymic
        print('Введите корректное отчество или оставьте поле пустым')

def get_borndate():
    while True:
        try:
            borndate = datetime.datetime.strptime(input
                ('Введите дату рождения в формате "дд.мм.гггг": '), 
                "%d.%m.%Y").date()
            return str(borndate)
        except ValueError:
            print('Некорректная дата, попробуйте еще раз')

def get_phonenumber():
    while True:
        phonenumber = input('Введите номер телефона: ')
        if phonenumber.isdigit():
            try:
                return int(phonenumber)
            except ValueError:
                pass
        print('Некорректный номер, попробуйте еще раз')

def get_sex():
    while True:
        sex = input('Введите пол (f или m): ')
        if sex in ['f', 'm']:
            return sex
        print('Некорректный пол, попробуйте еще раз')


if __name__ == "__main__":
    surname = get_surname()
    name = get_name()
    patronymic = get_patronymic()
    borndate = get_borndate()
    phonenumber = get_phonenumber()
    sex = get_sex()

    with open(surname, 'a') as f:
        f.writelines(f'{surname}, {name}, {patronymic}, {borndate}, {phonenumber}, {sex}\n')
