#! /usr/bin/env python3

# После определенного значения на страницу получается большое количество значенией в месяц
# Приходится разделять на месяца
# В итогом вариате можно использовать и на весь промежуток до 5000000 звезд, проблема заключается в скорости

from lib2to3.pgen2 import grammar
import requests
import time
import re

filename = "file.txt"
file = open(filename, 'w', encoding='utf-8')
newreposgits = open("newgitTEST55-70.txt", 'a', encoding='utf-8')

down = 160
i = 1
k = 1
year = 2019
month = {
    1:  '01',
    2:  '02',
    3:  '03',
    4:  '04',
    5:  '05',
    6:  '06',
    7:  '07',
    8:  '08',
    9:  '09',
    10: '10',
    11: '11',
    12: '12'
}
while year >= 2008:
    print(year)
    while k <= 12:
        time.sleep(61)
        while i <= 10:
            url = ("https://api.github.com/search/repositories?q=stars:55..70+created:" + str(year) + "-" + str(month[k]) + "&per_page=100&page=" + str(i))
            print(url)
            # url = "https://api.github.com/search/repositories?q=stars:%3E100+created:%3E2018-01-01&per_page=100&page=1"
            response = requests.get(url, auth=('ExLono', '{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}')).text

            file.write(response)
            print(re.findall('total_count":".*?"', response))
            resultFree = re.findall('full_name":".*?"', response)

            for element in resultFree:
                newreposgits.write(element)
                newreposgits.write('\n')
            i += 1
        k +=1
        i = 1
    year = year - 1
    k = 1
