def convert_date_time_to_seconds(date_time):
	""" Format dd/MM/YYYY HH:mm:ss return seconds if everthings ok
		return -1 if day, month, year, hour, minute, seconds are not integers
		return -2 if the date time is not well formated"""
	days = 0
	months = 0
	years = 0
	hours = 0
	minutes = 0
	seconds = 0
	days_in_month = [31, (28, 29), 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
	try:
		date_time = date_time.split(" ")
		date = date_time[0].split("-")
		time = date_time[1].split(":")
		if len(date) != 3:
			raise DateTimeFormatError
		if len(time) < 2 or len(time) > 3:
			raise DateTimeFormatError
	except DateTimeFormatError:
		return "Error: The date_time needs to be in this format:  dd/MM/YYYY HH:mm:ss"
	
	try:
		days = int(date[0])
		months = int(date[1])
		years = int(date[2])
		hours = int(time[0])
		minutes = int(time[1])
		if len(time) == 3:
			seconds = int(time[2])
		elif len(time) == 1:
			seconds = 0
	except:
		return "Error: Day, month, year, hour, minute and seconds needs to be integers with the following format: dd/MM/YYYY hh:mm:ss"
	
	if days < 1 or days > 31:
		return "Warning: Day need to be between 1 and 31"
	if months < 1 or months > 12:
		return "Warning: Month need to be between 1 and 12"
	if years < 0:
		return "Warning: Year need to be positive"
	if hours < 0 or hours > 24:
		return "Warning: Hour need to be between 0 and 24"
	if minutes < 0 or minutes > 60:
		return "Warning: Minutes need to be between 0 and 60"
	if seconds < 0 or seconds > 60:
		return "Warning: Minutes need to be between 0 and 60"

	minutes = minutes * 60
	hours = hours * 3600
	
	tmp = 0
	save_years = years
	for x in range(0,years+1):
		if x%4 != 0:
			tmp += 365*24*3600
		elif x%4 == 0:
			tmp += 366*24*3600
	years = tmp 
	
	tmp = days_in_month[months-1]
	if months != 2:
		months = months*tmp*24*3600
	else:
		if save_years%4 != 0:
			months = months*tmp[0]*24*3600
		else:
			months = months*tmp[1]*24*3600
	
	days = days*24*3600
	result = seconds + minutes + hours + years + months+ days	
	return str(result)


def main():
	date_time = "01-11-2021 21:38"
	result = convert_date_time_to_seconds(date_time)
	print(result)

if __name__ == '__main__':
	main()