import re

def display_usage():
	print('Usage :')
	print('')
	print("1er argument : décalage de jour par rapport à aujourd'hui")
	print('2e argument : zone de cinémas')
	print('-all, -old, -new, -latin, -st_denis, -public, -champollion, -21, -filmo, -reflet, -champo, -grand_action, -desperado, -christine, -brady, -archipel, -cinematheque, -pompidou, -forum, -beaubourg, -halles, -odeon, -3lux, -luminor, -maxlinder')
	print('')
	print('Flag -td : Horaire de début des séances au jour choisi au formar HH:MM')
	print('Flag -tf : Horaire de fin des films au jour choisi au formar HH:MM')
	print('\n')
	print('Exemple : get_seances 0 -all -t 15:00')

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

	urls = {}
	if len(argv) <= 2 or str_time_deb == -1 or str_time_fin == -1 or argv[1].isnumeric() == 0:
		display_usage()
		return (urls)
	day = 'd-%s/' % argv[1]
	argv = argv[2:]
	lien = 'http://www.allocine.fr/seance/%ssalle_gen_csalle=' % (day)
	for arg in argv:
		if arg == '-latin' or arg == '-all' or arg == '-old' or arg == '-filmo' or arg == '-champollion':
			urls['%sC0020.html' % lien] = 'Filmothèque du Quartier latin'
		if arg == '-latin' or arg == '-all' or arg == '-old' or arg == '-reflet' or arg == '-champollion':
			urls['%sC0074.html' % lien] = 'Reflet Medicis'
		if arg == '-latin' or arg == '-all' or arg == '-old' or arg == '-champo' or arg == '-champollion':
			urls['%sC0073.html' % lien] = 'Champo Espace Jacques Tati'

		if arg == '-latin' or arg == '-all' or arg == '-old' or arg == '-grand_action' or arg == '-21':
			urls['%sC0072.html' % lien] = 'Grand action'
		if arg == '-latin' or arg == '-all' or arg == '-old' or arg == '-desperado' or arg == '-21':
			urls['%sC0071.html' % lien] = 'Ecoles cinéma club'
		if arg == '-latin' or arg == '-all' or arg == '-old' or arg == '-christine' or arg == '-21':
			urls['%sC0015.html' % lien] = 'Christine Cinéma Club'

		if arg == '-latin' or arg == '-all' or arg == '-old' or arg == '-3lux':
			urls['%sC0095.html' % lien] = 'les 3 Luxembourgs'
		if arg == '-latin' or arg == '-all' or arg == '-odeon' or arg == '-old':
			urls['%sC0041.html' % lien] = 'Nouvel Odéon'
		if arg == '-latin' or arg == '-all' or arg == '-luminor' or arg == '-old':
			urls['%sC0013.html' % lien] = 'Luminor'


		if arg == '-st_denis' or arg == '-all' or arg == '-old' or arg == '-brady':
			urls['%sC0023.html' % lien] = 'Le Brady'
		if arg == '-st_denis' or arg == '-all' or arg == '-old' or arg == '-archipel':
			urls['%sC0134.html' % lien] = "L'archipel"
		if arg == '-st_denis' or arg == '-all' or arg == '-new' or arg == '-maxlinder':
			urls['%sC0089.html' % lien] = "Max Linder Panorama"

		if arg == '-public' or arg == '-all' or arg == '-old' or arg == '-cinematheque':
			urls['%sC1559.html' % lien] = 'La Cinémathèque Française'
		if arg == '-public' or arg == '-all' or arg == '-old' or arg == '-pompidou':
			urls['%sC0127.html' % lien] = 'Centre Georges Pompidou'
		if arg == '-public' or arg == '-all' or arg == '-forum':
			urls['%sC0119.html' % lien] = 'Le Forum des Images'

		if arg == '-beaubourg' or arg == '-all' or arg == '-new':
			urls['%sC0050.html' % lien] = 'MK2 Beaubourg'
		if arg == '-halles' or arg == '-all' or arg == '-new':
			urls['%sC0159.html' % lien] = 'UGC Ciné Cité les Halles'
	if (len(urls) == 0):
		display_usage()
	return (urls)