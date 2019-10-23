import requests
import sys
import webbrowser
import bs4

print('Googling...') # display text while downloading the Google Page
res = requests.get('https://www.google.com/search?q=trading+algo&ie=utf-8&oe=utf-8&client=firefox-b-ab' + ' '.join(sys.argv[1:]))
res.raise_for_status()

# Retrieve top search result links.
soup = bs4.BeautifulSoup(res.text,'lxml')

#  Open a browser tab for each result.
link_elems = soup.select('.r a')
num_open = min(5, len(link_elems))
for i in range(num_open):
    webbrowser.open('https://www.google.com' + link_elems[i].get('href'))
