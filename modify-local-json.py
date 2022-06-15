# Python standard libraries
import os
import json
import shutil
from datetime import datetime

working_directory = os.path.abspath(os.path.dirname(__file__))
output_directory = os.path.join(working_directory, '_output')

json_input_path = os.path.join(working_directory, 'sample-data', 'articles.json')
json_output_path = os.path.join(output_directory, 'articles.json')

print('\nStarting…\n')

# Remove (if needed) and create a new output directory
shutil.rmtree(output_directory, ignore_errors=True)
os.makedirs(output_directory)

# Load data from a JSON file
articles_data = None
with open(json_input_path, 'r', encoding='utf-8') as f:
  articles_data = json.load(f)

# Get the current date
current_timestamp = datetime.now()
formatted_date = current_timestamp.isoformat().split('T')[0]

# Add an article
new_article = {
  'title': 'My new article',
  'date': formatted_date,
  'tags': ['fun', 'writing']
}
articles_data['articles'].append(new_article)

# Update metadata (number of articles)
number_of_articles = len(articles_data['articles'])
articles_data['numberOfArticles'] = number_of_articles

# Update metadata (available tags)
unique_tags = set()
for article in articles_data['articles']:
  unique_tags.update(article['tags'])
articles_data['availableTags'] = sorted(unique_tags)

# Write to output file
with open(json_output_path, 'w', encoding='utf-8') as f:
  json.dump(articles_data, fp=f, indent=2, ensure_ascii=False, sort_keys=False)

print('Done! (see output folder)')
