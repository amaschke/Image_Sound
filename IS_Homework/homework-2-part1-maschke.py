# Alena Maschke
# 02-07-16
# Homework 2, Part 1

# LISTS (Part 1)

#1
list1=[22, 90, 0, -10, 3, 22, 48]
#2
print(len(list1))
#3
print(list1[3])
#4
print(list1[1], list1[3])
#5
print (sorted(list1))
sorted_list = sorted(list1)
print(sorted(list1)[2])
#6
print(list1[-1])
#7: Do not understand 7. At all. 
#8
print(sum(list1)/2)

# DICTIONARIES (Part 1)
#9
movie = dict({'title': 'Leon the Professional', 'year': '1994', 'director': 'Luc Besson'})
print("My favorite movie is", movie['title'], "which was released in", movie['year'], "and was directed by", movie['director'])
#10
movie = dict({'budget': 16, 'box':46.1})
print("It had a budget of", movie['budget'], "million, and made", movie['box'], "million in box offices.")
#11
if movie['box'] >= (movie['budget']*5):
	print("It was a good investment.")
elif movie['box']<= movie['budget']:
	print("It was a flop.")
else:
	print("It did well.")
#12
population = dict({'Brooklyn': 2636735, 'Bronx': 1455444, 'Queens': 2339150, 'Staten Island': 474558, 'Manhattan': 1644518})
#13
print(population['Brooklyn'])
#14
print(sum(population.values()))
#15
print(population['Manhattan']/sum(population.values())*100, "%")
