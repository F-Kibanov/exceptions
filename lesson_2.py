# Реализуйте метод, который запрашивает у пользователя ввод дробного числа 
# (типа float), и возвращает введенное значение. Ввод текста вместо числа 
# не должно приводить к падению приложения, вместо этого, необходимо повторно 
# запросить у пользователя ввод данных.
def echo_float():
    while True:
        n = input('n = ')
        if '.' in n:
            try:
                return float(n)
            except ValueError:
                print("Введите дробное число!")
                continue
        print("Введите дробное число!")

# Разработайте программу, которая выбросит Exception, когда пользователь 
# вводит пустую строку. Пользователю должно показаться сообщение, что пустые 
# строки вводить нельзя.
def not_empty():
    while True:
        n = input('Введите что-нибудь: ')
        if n:
            for char in n:  # Добавил проверку на символ пробела
                if ord(char) == 32:
                    continue
                return 'Очень хорошо!'
        raise Exception('Пустые строки и пробелы вводить нельзя!')


if __name__  == "__main__":
    print(echo_float())
    print(not_empty())
    