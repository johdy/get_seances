import re 

def parse_time(str_time):
	str_time = re.split(':', str_time)
	return (60 * int(str_time[0]) + int(str_time[1]))

def check_time(str_hours, str_time_deb, str_time_fin, str_length):
	time_deb = parse_time(str_time_deb)
	time_fin = parse_time(str_time_fin)
	try:
		length = int(str_length[0][0]) * 60 + int(str_length[1][0]) * 10 + int(str_length[1][1])
	except:
		length = 0
	good_hours = []
	for hour in str_hours:
		parsed_hour = parse_time(hour)
		if parsed_hour >= time_deb and parsed_hour + length <= time_fin:
			good_hours.append(hour)
	return (good_hours)