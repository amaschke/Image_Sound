# Alena Maschke
# January 29, 2016
# Homework 1
year_of_birth = input ("What year were you born in? ")
age = 2016 - int(year_of_birth)
print("You are roughly " + str(age) + " years old.")
heartbeat = (age) * int(365) * int(24) * int(60) * int(80)
print("You're heart has beaten about " + str(heartbeat) + " times so far.")
# this is assuming that a resting heart rate of 60 to 100 is considered normal, 80 being the golden middle.
heartbeat_whale = (age) * int(365) * int(24) * int(60) * int(10)
print("If you were a blue whale, your heart would have beaten only " + str(heartbeat_whale) + " times so far.")
heartbeat_rabbit = (age) * int(365) * int(24) * int(60) * int(150)
if heartbeat_rabbit < 1000000000:
	print("Wow! If you were a rabbit, your heart could have beaten " + str(heartbeat_rabbit) + " times already!")
else:
	heartbeat_rabbit_in_billions = (heartbeat_rabbit) / 1000000000
	print("Wow! If you were a rabbit, your heart could have beaten ", (round(heartbeat_rabbit_in_billions, 2)), " billion times already!") 
venus_years = (age) * int(365) / int(224)
print("On Venus, you would be " + str(venus_years) + " years old.")
neptune_years = (age) * int(365) / int(60190)
print("On Neptune, you would be " + str(neptune_years) + " years old.")
if age == 24:
    print("Awesome, we're the same age then!")
elif age < 24:
    print("Cute, you're such a baby!")
    younger = 24 - age
    print ("Ugh I wish I was still ", younger, " years younger than I am today.")
else:
    print("Damn, you are old!")
    older = age - 24
    print (older, " years older than me, actually.")
if int(year_of_birth) % 2 == 0:
	print ("We're even.")
else:
	print ("You're odd.")
if int(year_of_birth) <= 1975:
	print ("The Pittsburgh Steelers won six NFL championships since you were born. What have you done?")
elif int(year_of_birth) >= 1976:
	print ("The Pittsburgh Steelers won five NFL championships since you were born. What have you done?")
elif int(year_of_birth) >= 1979:
	print ("The Pittsburgh Steelers won four NFL championships since you were born. What have you done?")
elif int(year_of_birth) >= 1980:
	print ("The Pittsburgh Steelers won three NFL championships since you were born. What have you done?")
elif int(year_of_birth) >= 2006:
	print ("You could have seen the Pittsburgh Steelers win two NFL championships.")
elif int(year_of_birth) <= 2009:
	print ("You were probably to young to see it, but the Pittsburgh Steelers won the NFL championships once since you were born.")
else:
	print ("Fingers crossed for the Pittsburgh Steelers. You should get a chance to see Steely McBeams Superbowl victory dance.")
# This is not working correctly yet.
if int(year_of_birth) >= 2009:
	print ("In case you were wondering: Yes, we can.")
elif int(year_of_birth) >= 2001:
	print ("No child left behind, amirite?")
elif int(year_of_birth) >= 1993:
	print ("You really shouldn't have stopped thinking about tomorrow. Look where we're at now.")
elif int(year_of_birth) >= 1989: 
	print ("I'm sure you had a kind, gentle childhood.")
elif int(year_of_birth) >= 1981:
	print ("Are you better of than you were as a kid? Huh?")
elif int(year_of_birth) >= 1977:
	print ("Come here, you little peanut!")
elif int(year_of_birth) >= 1974:
	print ("I don't know what to tell you, your president flew away in a helicopter.")
elif int(year_of_birth) >= 1969:
	print ("Hate to break it to you, but: He wasn't the one.")
elif int(year_of_birth) >= 1963:
	print ("Did you have a stay-at-home mom? Didn't she know what was at stake?")
elif int(year_of_birth) >= 1961:
	print ("Born for greatness.")
elif int(year_of_birth) >= 1953:
	print ("Did you like Ike? Yeah, me neither.")
elif int(year_of_birth) >= 1945:
	print ("Oh weren't we all just wild about little Harry!")
elif int(year_of_birth) >= 1933:	
	print ("Happy days are here again! At least for your parents. Maybe.")
else:
	("You're too old for this shit.")
# Since you love riddles so much, I though you might enjoy some campaign slogan jokes instead of just boring names.
