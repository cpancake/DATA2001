import csv
import re

def clean_street_name(name):
	name = re.sub(r'[^A-Za-z0-9]', '', name).strip().capitalize()
	name = name.replace("road", "rd")
	name = name.replace("street", "str")
	name = name.replace("avenue", "ave")
	name = name.replace("lane", "ln")
	return name

with open("dirty_data.csv", newline='') as infile:
	with open("clean_data.csv", 'w', newline='') as outfile:
		reader = csv.reader(infile, delimiter=',', quotechar='"')
		writer = csv.writer(outfile, delimiter=',', quotechar='"')
		data = list(reader)
		for row in data:
			row[2] = clean_street_name(row[2])
			row[3] = clean_street_name(row[3])
			if row[2] == row[3]:
				row[3] = ""
			writer.writerow(row[:4])