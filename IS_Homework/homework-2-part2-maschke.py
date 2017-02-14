# Alena Maschke
# 02-07-16
# Homework 2, Part 2

# Lists
#1
countries=["Somalia", "Denmark", "China", "Laos", "Argentina", "Russia", "South Africa"]
#2
for country in countries:
	print ("Country: %s" % country)
#3
countries.sort()
#4
print (countries)
#5
print (countries[0])
#6
print (countries[-2])
#7
countries.remove('Denmark')
print (countries)

#Dictionaries

#1
tree = { "name": "Sunland Baobab", "species": "Baobab", "age": 1060, "location_name": "Limpop Province, South Africa", "latitude": -23.3716, "longitude": 30.1153 }
#2
print(tree["name"], "is a", tree["age"], "year old tree, that is in", tree["location_name"])
#3
if tree["latitude"] < 40.7128:
	print("The tree",tree["name"],"in",tree["location_name"],"is south of NYC.")
else:
	print("The tree",tree["name"],"in",tree["location_name"],"is north of NYC.")
#4
user_age = input ("How old are you?")
if int(user_age) > tree["age"]:
    print("Are you sure? That would mean you are",(int(user_age) - tree["age"]),"older than this crazy old tree.")
else:
	print(tree["name"],"was",(tree["age"] - int(user_age)),"years old when you were born.")
	
#Lists of dictionaries

#1
dictList = [{"name": "Moscow", "latitude": 55.7558, "longitude": 37.6173},
{"name": "Tehran", "latitude": 35.6892, "longitude": 51.3890},
{"name": "Falkland Islands", "latitude": -51.7963, "longitude": -59.5236},
{"name": "Seoul", "latitude": 37.5665, "longitude": 126.9780},
{"name": "Santiago", "latitude": -33.4489, "longitude": -70.6693}]
#2
for city in dictList:
	print (city["name"])
	if city["latitude"] < 0:
		print("This city is below the equator")
	else:
		print("This city is north of the equator")
	if city["name"] == "Falkland Islands":
		print("The Falkland Islands are a biogeographical part of the mild Antarctic zone")
#3		
for city in dictList:
	if city["latitude"] < tree["latitude"]:
		print("This city is south of the Sunland Baobab")
	if city["latitude"] > tree["latitude"]:
		print("This city is north of the Sunland Baobab")