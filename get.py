import re
import parse

def length(length):
	str_length = str(length)
	str_length = re.split('<span class="spacer">/</span>', str_length)[1]
	str_length = re.split('<span class="spacer">', str_length)[0]
	return (str_length.split())

def title(title):
	str_title = str(title)
	str_title = re.split('.html">', str_title)[1]
	str_title = re.split ('</a>', str_title)[0]
	str_title = parse.transform_s(str_title)
	return (str_title)

def real(real):
	str_real = str(real)
	str_real = re.split('blue-link">',str_real)[1]
	str_real = re.split('</span>',str_real)[0]
	str_real = parse.transform_s(str_real)
	return (str_real)

def hours(hours):
	fussy_string = str(hours)
	fussy_string = re.split('-item-value">', fussy_string)[1:]
	str_hours = [0] * len(fussy_string)
	for j in range(len(fussy_string)):
		str_hours[j] = re.split('</span>', fussy_string[j])[0]
	return (str_hours)

def cinema(soupe):
	cinema = soupe.find_all('div', { 'class' : 'theater-cover-informations' })
	str_cinema = str(cinema)
	str_cinema = re.split('theater-cover-title">',str_cinema)[1]
	str_cinema = re.split('</span>',str_cinema)[0]
	str_cinema = parse.transform_s(str_cinema)
	return (str_cinema)
	
