#1
with open('file.txt', 'r') as file:
    text = file.read()
numbers = (r'\d+', text)
print(numbers)
#2
text = input('Введіть текст: ')

with open('data.txt', 'w') as file:
    file.write(text)
#3
N = int(input('Введіть число N: '))
with open('numbers.txt', 'w') as file:
    for i in range(N):
        number = input('Введіть число: ')
        file.write(number)
#4
import random
with open('random_numbers.txt', 'w') as file:
    for _ in range(100):
        number = random.randint(1, 1000)
        file.write(str(number))
#5
with open('file.txt', 'r') as file:
    text = file.read()
word_count = len(text.split())
print('Кількість слів у файлі: ', word_count)
#6
with open('numbers.txt', 'r') as file:
    text = file.read()
    numbers = text.split()
sum_numbers = 0
for number in numbers:
    sum_numbers += int(number)
print('Сума чисел: ', sum_numbers)
#7
from collections import Counter
import re
with open('file.txt', 'r') as file:
     text = file.read()
words = re.findall(r'\d+', text)
word_counts = Counter(words)