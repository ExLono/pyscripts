#! /usr/bin/env python3

# Сравнить два файла и сделать один без повторов

s = set()
s2 = set()
with open('20-400000.txt', 'r', encoding='UTF8') as iz_chego_rezhem:  # Откуда будем вырезать
    for line in iz_chego_rezhem:
        s.add(line.rstrip())

with open('Очищенный лям (потеря 5000).txt', 'r', encoding='UTF8') as chto_virezaem:  # Что будем вырезать
    for line in chto_virezaem:
        if line.rstrip() in s:
            continue
        else:
            s2.add(line.rstrip())

with open('result1.txt', 'w', encoding='UTF8') as result:
    for i in s2:
        result.write(i.rstrip())
        result.write('\n')
