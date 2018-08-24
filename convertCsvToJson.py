import csv
import json
import codecs

csvfile = codecs.open('fundos_temp.csv', 'r', encoding="utf8")
jsonfile = codecs.open('fundos_temp.json', 'w', encoding="utf8")

fieldnames = ('''here you put the field names of your JSON file''')
reader = csv.DictReader( csvfile, fieldnames)
for row in reader:
    json.dump(row, jsonfile, ensure_ascii=False)
    jsonfile.write('\n')