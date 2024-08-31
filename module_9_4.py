first = 'Мама мыла раму'
second = 'Рамена мало было'

func1 = lambda x, y: x == y                  # Передаем функцию lambda для переменных х и у, где сравниваются элементы
                                            # строк first и second
result = list(map(func1, first, second))    # Создаем список с результатами поэлементного сравнения срок first и second

print(result)                               # Выводим результат (список) в консоль

def get_advanced_writer(file_name):
    def write_everything(*data_set):
        with open(file_name, 'a', encoding='utf-8') as file:      # Отрываем файл file_name (если его нет, то он
                                                                  # создается) в режиме "а" (режим добавления в файл)
                                                                  # в кодировке utf-8 (для двух языков), как file
            for i in data_set:                                    # Записываем в file поэлементно список на отдельных
                file.write(str(i) + '\n')                         # строчках
                                                                  # Здесь автоматически закрывается файл file
    return write_everything                                       # Возвращаем функцию write_everything

write = get_advanced_writer('example.txt')
write('Это строчка', ['А', 'это', 'уже', 'число', 5, 'в', 'списке'])


from random import choice             # Импортируем из модуля random функцию choice (случайный выбор)
class MysticBall:                     # Создаем класс
    def __init__(self, *words):       # Создаем объект self.words
        self.words = list(words)
    def __call__(self):               # Функция случайного выбора
        return choice(self.words)     # Возвращаем случайно выбранный элемент из списка self.words

first_ball = MysticBall('Да', 'Нет', 'Наверное')
print(first_ball())
print(first_ball())
print(first_ball())