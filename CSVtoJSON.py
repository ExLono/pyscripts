#! /usr/bin/env python3

import csv
import json

def csv_to_json(csvFilePath, jsonFilePath):
	jsonArray = []

	with open('servers.csv', newline='') as csvfile:
		reader = csv.DictReader(csvfile)
		for row in reader:
			jsonArray.append(row)

	with open(jsonFilePath, 'w', encoding='utf-8') as jsonf:
        	jsonString = json.dumps(jsonArray, indent=4)
        	jsonf.write(jsonString)

csvFilePath = r'servers.csv'
jsonFilePath = r'servers.json'
csv_to_json(csvFilePath, jsonFilePath)
