#! /usr/bin/env python3

# Нужно было найти список всех основных репозиториев
# Использовался драйвер для хрома, чтобы переходить по страницам
# API найдено не было


from selenium import webdriver
import time
import re
import sys

driver = webdriver.Chrome()
driver.set_window_position(0, 0)
driver.set_window_size(1920, 1080)
page = 83
while (page != 101):
    driver.get("https://hub.docker.com/search?q=&type=image&image_filter=store&architecture=amd64&page=" + str(page))
    # driver.get("https://hub.docker.com/search?q=&type=image&image_filter=store%2Cofficial&page=8")
    time.sleep(2)

    main_page = driver.page_source
    filetowrite = open("docker.txt", "w", encoding='utf-8')
    filetowrite.write(main_page)

    resultFree = re.findall('data-testid="imageSearchResult" href="/_/.*?>', main_page)
    resultResult = re.findall('data-testid="imageSearchResult" href="/r/.*?>', main_page)
    print(resultFree)
    print(resultResult)
    filetowrite.seek(0)

    dockerlist = open("dockerlist.txt", "a", encoding='utf-8')
    dockerlist.write(str(page))
    dockerlist.write("\n")
    for element in resultFree:
        dockerlist.write(element)
        dockerlist.write('\n')
    for element in resultResult:
        dockerlist.write(element)
        dockerlist.write('\n')
    page += 1

# data-testid="imageSearchResult" href="/_/.*?>
