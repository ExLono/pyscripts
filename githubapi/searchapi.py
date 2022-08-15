#! /usr/bin/env python3

# Поиск по звездам с самого большого значения, выставляется вручную
# Максимум возможного 1000 записей ?
# Можно сделать дополнительный цикл для автоматизации от 500000 звезд до минимального порога (смотри след скрипт)

from lib2to3.pgen2 import grammar
import requests
import json
import grab
import time
from lxml import html
from bs4 import BeautifulSoup
import selenium
import re

filename = "file.txt"
file = open(filename, 'w', encoding='utf-8')
newreposgits = open("newgit.txt", 'a', encoding='utf-8')

down = 590
up = 600
i = 1
while down >= 450:
    print(down)
# нужна пауза, так как ограничено количество запросов в минуту (максимум 10 страниц)
    time.sleep(61)
    while i <= 10:
        url = ("https://api.github.com/search/repositories?q=stars:" + str(down) + ".." + str(up) + "&per_page=100&page=" + str(i))
        # url = "https://api.github.com/search/repositories?q=stars:%3E100+created:%3E2018-01-01&per_page=100&page=1"
        response = requests.get(url, auth=('ExLono', '{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}')).text

        file.write(response)

        resultFree = re.findall('full_name":".*?"', response)

        for element in resultFree:
            newreposgits.write(element)
            newreposgits.write('\n')
        i += 1
    down = down - 5
    up = up - 5
    i = 1
