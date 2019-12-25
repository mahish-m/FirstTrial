# #Mahish Mahendarkar
# #Python Phase 1 Heartrate proj
# hr max - heartrate maximum
# 208-.7(h)
# 65yr old - 163 bpm

# Part 1 -  simple app in ios/android
# which can make the heartrate calculaiton

# Part 2 -  use the age from a wearable app (eg apple health) collected age 

# Part 3 - create graph shows HR max rate 
# if you want to hit your hr max use the graph to see if you are hitting HR max - hourly update, 

#Working Logic: collect age input from user via number entry, 
#collect which output user wants (max heart rate(high end , low end), target heart rate), 
#calculate desired 
#display results



#overview 
#	heart rate calculation calculator
#	
#	input: age
#	output: max beats per minute, target heart rate
#	calculate: max heart rate/target heart rate
#
#	max heart rate (age)
#		return (220 - age)
#
#	*high and low percent are user set 
#- what percentage of max heart rate do you want to check for - 
#	default = 70,85*
#	target heart rate (resting heart rate, max heart rate(age), low percent, high percent)
#
#	- check for resting heart rate in the morning
#
#	- for target heart rate return both average and range
#		- Heart rate resevre = (max heart rate - resting)
#		- low range = (Heart rate reserve * low percent) + resting
#		- high range = (Heart rate reserve * high percent) + resting
#		- average = (high range - low range)/2 + low range

def calculate(data):
	outputStr = ""
	if("target" in data):
		
	elif("max" in options):
		outputStr = 220 - data['AGE']
	return outputStr
def intake():
	age = int(input("Age: "))
	options = str(input("Do you want Max Heart Rate(1) or Target Heart Rate(2)? \nType the numbers corresponding to the calculation: "))
	if('2' in options):
		default = str(input("Default range or custom range? For default enter Y for custom enter N: "))
		if("Y" in default or "y" in default):
			data["Range"] = [70,85]
		elif("N" in default or "n" in default):
			low = int(input("Low end range: "))
			high = int(input("High end range: "))
			data["Range"] = [low,high]
	data = {"Age": age, "Tests": options}
	return data
