Python 3.12.3 (tags/v3.12.3:f6650f9, Apr  9 2024, 14:05:25) [MSC v.1938 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> DATABASE = {
...     'Серёга': 'Омск',
...     'Соня': 'Москва',
...     'Миша': 'Москва',
...     'Дима': 'Челябинск',
...     'Алина': 'Красноярск',
...     'Егор': 'Пермь',
...     'Коля': 'Красноярск'
... }
... 
... def process_anfisa(query):
...     if query == 'Сколько у меня друзей?':
...         count = len(DATABASE)
...         return 'У тебя ' + str(count) + ' друзей.'
...     # Проверяем, если запрос о друзьях
...     elif query == 'Кто все мои друзья?':
...         friends_string = ''
...         for friend in DATABASE.keys():
...             friends_string += friend + ' '
...         return 'Твои друзья: ' + friends_string
...     else:
...         return '<неизвестный запрос>'
... 
... # Не изменяйте следующий код
... print('Привет, я Анфиса!')
... print(process_anfisa('Сколько у меня друзей?'))
