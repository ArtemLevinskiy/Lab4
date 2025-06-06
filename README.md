# Опис класу  `Date`
`Date` - це власна реалізація класу для роботи з календарними датами. Клас надає базові можливості створення, форматування, порівняння дат і виконання простих операцій з ними.
# Можливості
- Створення об'єктів дати з необов'язковим описом
- Перевірка правильності введення дати
- Додавання і віднімання днів
- Порівняння дат (==, >)
- Визначення різниці між датами у днях
- Отримання повної назви місяця і дня тижня
- Перевірка високосності року
- Виведення дати у зрозумілому форматі
# Використання
Створення дат
```python
d1 = Date(16, 4, 2025)
d2 = Date(29, 2, 2025)
d3 = Date(29, 4, 2025)
d4 = Date(12, 2,4)
```
Віднімання від сьогоднішньої дати
```python
d2 - d3  # Повертає 153
```
Додає до дати n днів
```python
d2 + d4  # Повертає 10.12.2029
```
Перевірка на рівність дат 
```python
d1 == d3  # Повертає False
```
Перевірка на рівність дат (чи є перша дата раніше іншої)
```python
d2 > d1  # Не порівнюється бо дата (d2) не можу бути стоворена
d3 > d1  # Повертає True
```
Перевірка на високосний рік
```python
d1.is_leap_year()  # Повертає False
```
Повертає назву місяця з датою і роком
```python
d2.month_name()  # Повертає 12 лютого 4 рік
```
Повертає деть тижня
```python
d3.day_of_week()  # Повертає Вівторок
```
Повертає форматовану відформатовану дату
```python
print(d1)  # 16.04.2025
print(d3)  # 29.04.2025
```
# Параметри:
- day (int) - день
- month (int) - місяць
- year (int) - рік
# Помилки
- TypeError - введення дані не відповідають типам
- ValueError - не коректне введення даних
# Методи:
Перевірка на високосний рік

`is_leap_year()`

Повертає назву місяця з датою та роком

`month_name()`

Повертає день тижня

`day_of_week()`
# Інструкція щодо використання
1. Імпортувати через Clone Repository
2. Обрати свій репозиторій або інший репозиторій використавши посилання

Левінський Артем Максимович
11ІПЗ
