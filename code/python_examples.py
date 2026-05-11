# Microsoftalion: 10^10000
MICROSOFTALION = 10 ** 10000

# Основные операции
def get_first_digits(number, n=50):
    """Возвращает первые n цифр числа."""
    return str(number)[:n]

def get_last_digits(number, n=50):
    """Возвращает последние n цифр числа."""
    return str(number)[-n:]

def count_digits(number):
    """Считает количество цифр в числе."""
    return len(str(number))

# Демонстрация
print(f"Первые 50 цифр: {get_first_digits(MICROSOFTALION)}...")
print(f"Последние 50 цифр: {get_last_digits(MICROSOFTALION)}")
print(f"Всего цифр: {count_digits(MICROSOFTALION)}")
