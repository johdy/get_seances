import re

def transform_s(s):
	s = s.replace('ç','c')
	s = s.replace('é','e')
	s = s.replace('ê','e')
	s = s.replace('è','e')
	s = s.replace('ě','e')
	s = s.replace('à','a')
	s = s.replace('â','a')
	s = s.replace('ã','a')
	s = s.replace('ô','o')
	s = s.replace('î','i')
	s = s.replace('ì','i')
	s = s.replace('ò','o')
	s = s.replace('õ','o')
	s = s.replace('ù','u')
	s = s.replace('û','u')
	s = s.replace('ä','a')
	s = s.replace('ë','e')
	s = s.replace('ï','i')
	s = s.replace('ö','o')
	s = s.replace('ü','u')
	s = s.replace('ÿ','y')
	s = s.replace('á','a')
	s = s.replace('í','i')
	s = s.replace('ó','o')
	s = s.replace('ú','u')
	s = s.replace('œ','oe')
	s = s.replace('æ','ae')
	return s

def display_usage():
	print('Usage :')
	print('')
	print("1er argument : décalage de jour par rapport à aujourd'hui")
	print('2e argument : zone de cinémas')
	print('-all, -old, -new, -latin, -st_denis, -public, -champollion, -21, -filmo, -reflet, -champo, -grand_action, -desperado, -christine, -brady, -archipel, -cinematheque, -pompidou, -forum, -beaubourg, -halles, -odeon, -3lux, -luminor, -maxlinder')
	print('')
	print('Flag -td : Horaire de début des séances au jour choisi au format HH:MM')
	print('Flag -tf : Horaire de fin des séances au jour choisi au format HH:MM')
	print('\n')
	print('Exemple : get_seances.py 0 -all -td 15:00 -tf 20:00')

def get_time_flag(argv, deb):
	i = 0
	if deb == 1:
		lookfor = '-td'
		init = '00:00'
	else:
		lookfor = '-tf'
		init = '23:59'
	while (i < len(argv)):
		if argv[i] == lookfor:
			break
		else:
			i = i+1
	if i == len(argv):
		return init
	check_arg = re.split(':', argv[i + 1])
	if len(check_arg) != 2 or len(check_arg[0]) != 2 or len(check_arg[1]) != 2:
		return -1
	if check_arg[0].isnumeric() == 0 or check_arg[1].isnumeric() == 0:
		return -1
	if check_arg[0][0] > '2' or (check_arg[0][0] == '2' and check_arg[0][1] > '3') or check_arg[1][0] > '5':
		return -1
	else:
		return argv[i + 1]


def parse_args(argv, str_time_deb, str_time_fin):
	file = open("/Users/john/Dev/get_seances/config.txt", "r")
	urls = []
	if len(argv) <= 2 or str_time_deb == -1 or str_time_fin == -1 or argv[1].isnumeric() == 0:
		display_usage()
		return (urls)
	day = 'd-%s/' % argv[1]
	argv = argv[2:]
	lien = 'http://www.allocine.fr/seance/%ssalle_gen_csalle=' % (day)
	for line in file:
		line = re.split('\n', line)[0]
		id_salle = re.split(' ', line)[0]
		id_salle = re.split('gen_csalle=', id_salle)[1]
		lien = 'http://www.allocine.fr/seance/%ssalle_gen_csalle=%s' % (day, id_salle)
		flags = re.split(' ', line)[1:]
		for arg in argv:
			if arg == '-all':
				urls.append(lien)
			else:
				for flag in flags:
					if flag == arg:
						urls.append(lien)
	if (len(urls) == 0):
		display_usage()
	return (urls)
