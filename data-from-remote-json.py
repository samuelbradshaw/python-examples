# Python standard libraries
import os

# Third-party libraries
import requests

working_directory = os.path.abspath(os.path.dirname(__file__))

print('\nStarting…\n')

api_url = 'https://en.wikipedia.org/w/api.php?action=query&format=json&origin=*&titles={0}&prop=extracts|pageimages&exintro=&indexpageids=&pithumbsize=400'

article_name = 'Pizza'
request_url = api_url.format(article_name)

# Fetch data from the Wikipedia API
r = requests.get(request_url)
r.encoding = 'utf-8'
if r and r.status_code == 200:
  data = r.json()
  
  page_ids = data['query']['pageids']
  if page_ids:
    page_data = data['query']['pages'][page_ids[0]]
    print(page_data['title'])
    print('')
    print(page_data['extract'])
  
print('\nDone!')
