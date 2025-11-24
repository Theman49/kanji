import requests
from bs4 import BeautifulSoup

def jlptPerLevel():
	result = ''
	level = 'n1'
	for i in range(1,63):
		filename = "./data/" + level + "_page_" + str(i) + ".html"
		r = requests.get('https://jisho.org/search/%23kanji%20%23jlpt-' + level + '?page=' + str(i))
		print(r)

		soup = BeautifulSoup(r.content, 'html.parser')
		content = soup.find('div', {'id':'page_container'})
		result += str(content)

		#write result into file
		with open(filename, "a") as f:
			f.write(str(content))

		print('Scraping Page', i, 'DONE')

	filename = "./data/" + level + "_all.html"
	with open(filename, "a") as f:
		f.write(str(result))

def search(value, page=1):
	genUrl = 'https://jisho.org/search/' + str(value) + '%20%23words?page=' + str(page)
	print(genUrl)
	r = requests.get(genUrl)
	soup = BeautifulSoup(r.content, 'html.parser')
	content = soup.find('div', {'id':'primary'})

	return content

def definition(query, searchType, x, y):
	genUrl = 'https://www.weblio.jp/content_find?query=' + str(query) + '&searchType=' + str(searchType) + '&x=' + str(x) + '&y=' + str(y)
	
	r = requests.get(genUrl)
	soup = BeautifulSoup(r.content, 'html.parser')
	content1 = soup.find('h2', {'class':'midashigo'})
	result = str(content1.find_next_siblings('div')[0])

	if not result.find('synonymsUnderDictWrp'):
		content2 = str(soup.find('div', {'class':'synonymsUnderDictWrp'}))
		result += content2

	return result.replace('。', '。<br/>')


def sentence(query):
	headers = {
		"User-Agent": 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/26.0.1 Safari/605.1.15',
		"Accept-Language": "en-US,en;q=0.9",
	}
	genUrl = 'https://www.kanshudo.com/searcht?q=' + str(query)

	return genUrl
