# Aniamal Categories
# individuals_in_wild = 5500
# if individuals_in_wild < 1000:
#     print("Critically Endangered")
# elif individuals_in_wild > 1000:
#     print("Endangered")
# elif 5000 > individuals_in_wild <=20000:
#     print("Vulnerable")
# elif individuals_in_wild > 20000:
#     print("Safe")

# Weather per region.
# rainfall = 205 #mm
# population_density = 448

# if rainfall < 500 and population_density > 500:
#     print("Servere Scarcity")
# elif rainfall >= 500 and rainfall < 1000 and population_density <=200  and population_density >=500:
#     print("Moderate Scarcity")
# else:
#     print("No scarcity")

# Categorise items
# material = "paper", "plastic", "metal", "glass"
# size = "small", "medium", "large"
# if material == "glass" and size == "large":
#     print("Special Handling")
# elif size == "medium" and size =="small" or material == "glass":
#     print("Standard Recycling")
# elif size == "small":
#     print("Composting")
# else:
#     print("Landfill")

# Renewable energy usage.
# solar = True

# if not solar:
#     print("Needs Improvement")
# else:
#     print("Eco friendly")

# deforestation_rate = 0, 1
# if deforestation_rate > 0.1:
#     print("High alert")
# else:
#     pass

# # A program to check the air quality
# aqi = 250

# print("Poor air quality") if aqi > 250 else print("Good air quality")

animals_tuple = ('Great White Shark', 'Blue Whale', 'African Elephant',  'Bald Eagle', 'Orangutan', 'Tiger', 'Tiger', 'Panda', 'Koala')
animals_set= set(animals_tuple)
animal_string = "Great White Shark"
print("Tuple:")
for animal in animals_tuple:
    print(animal)
print("Set:")
for animal in animals_set:
    print(animal)
print("String:")
for letter in animal_string:
    print(letter)