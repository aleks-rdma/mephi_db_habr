import csv

section_article = []
sections_from_file = []
article_arr = [i for i in range(1, 5 + 1)]
with open('sections.csv', newline='\n', encoding='utf-8') as csvfile:
    reader = csv.reader(csvfile)
    for row in reader:
        sections_from_file.append(row[0])
print(sections_from_file)
