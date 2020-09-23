import urllib3
import bs4
from bs4 import BeautifulSoup
import sys
import get
import parse
import utils

manager = urllib3.PoolManager()
str_time_deb = parse.get_time_flag(sys.argv, 1)
str_time_fin = parse.get_time_flag(sys.argv, 0)
urls = parse.parse_args(sys.argv, str_time_deb, str_time_fin)
for url in urls:
	print ('')
	print ('-----------', urls[url], '------------')
	print('')
	ressource = manager.request('GET', url)
	contenu = ressource.data
	soupe = BeautifulSoup(contenu, 'html.parser')
	titles = soupe.find_all('h2', { 'class' : 'meta-title' })
	hours = soupe.find_all('div', { 'class' : 'hours'})
	real = soupe.find_all('div', { 'class' : 'meta-body-item meta-body-direction'})
	length = soupe.find_all('div', { 'class' : 'meta-body-item meta-body-info'})
	nb_entries = min(len(titles), len(real), len(hours), len(length))
	for i in range(nb_entries):
		str_title = get.title(titles[i])
		str_real = get.real(real[i])
		str_length = get.length(length[i])
		str_hours = get.hours(hours[i])
		str_hours = utils.check_time(str_hours, str_time_deb, str_time_fin, str_length)
		if len(str_hours) > 0:
			print (str_real, '-', str_title, '-', str_hours)