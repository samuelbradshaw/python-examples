# Python standard libraries
import os
import csv

working_directory = os.path.abspath(os.path.dirname(__file__))
csv_input_path = os.path.join(working_directory, 'sample-data', 'articles.csv')

print('\nStarting…\n')

# Load data from a CSV file
articles_list = []
with open(csv_input_path, newline='') as f:
  csv_reader = csv.DictReader(f)
  for row in csv_reader:
    row['tags'] = row['tags'].split(', ')
    articles_list.append(row)

# Do something with the articles
for article in articles_list:
  print(article['title'])

print('\nDone!')
