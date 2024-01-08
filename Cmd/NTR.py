import random as rd
import requests as rq
from bs4 import BeautifulSoup as bs
from pathlib import Path
from urllib.parse import urljoin

headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36"}

directory = Path('Cmd/Cache')

file_path = Path('Cmd/NTR_list.txt')

try:
	with file_path.open('r') as file:
		Title_list = file.read().splitlines()
except FileNotFoundError:
	Title_list = []
	for page in range(1, 86):
		url = f"https://hentai2read.com/hentai-list/category/netorare/all/last-added/{page}"
		response = rq.get(url, headers)
		
		if response.status_code == 200:
			data = bs(response.text, 'html.parser')
			titles = data.find_all(class_="title-text")
			for title in titles:
				Title_list.append(title.text)
			print(f'Scraped {page} page')
		else:
			print(f"Error: {response.status_code}")
	with open('Cmd/NTR_list.txt', 'w') as file:
		file.write('\n'.join(Title_list))

def RandomSeries():
	mxrange = len(Title_list) - 1
	index = rd.randint(0, mxrange)
	title = Title_list[index]
	return title

def download(title):
	url_S = f"https://hentai2read.com/hentai-list/search/{title}"
	response_S = rq.get(url_S)
	
	if response_S.status_code == 200:
		data_S = bs(response_S.text, 'html.parser')
		picture_tag = data_S.find('picture')
		source_tag = picture_tag.find('source', {'type': 'image/avif'})
		if source_tag:
			srcset = source_tag.get('srcset')
			img_url_relative = srcset.split(',')[0].split()[0].strip()
			img_url_absolute = urljoin(url_S, img_url_relative)
			img_response = rq.get(img_url_absolute)
			filename = directory / Path(img_url_absolute).name
			if img_response.status_code == 200:
			     with open(filename, 'wb') as img_file:
			     	img_file.write(img_response.content)
			     return filename
			else:
				return "Something went wrong"
		else:
			return "No image found"
#			for source_tag in source_tags:
#				srcset = source_tag.get('srcset')
#				if srcset:
#					print(srcset)
#				else:
#					print("No links found")
	elif response_S.status_code == 404:
		return "better luck next time"
	else:
		return f"Error: {response_S.status_code}"