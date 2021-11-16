travel_log = [
{
  "country": "France",
  "visits": 12,
  "cities": ["Paris", "Lille", "Dijon"]
},
{
  "country": "Germany",
  "visits": 5,
  "cities": ["Berlin", "Hamburg", "Stuttgart"]
},
]
#🚨 Do NOT change the code above

#TODO: Write the function that will allow new countries
#to be added to the travel_log. 👇
def add_new_country(country, times, cities):
    new_dict = {}
    travel_log.append(new_dict)
    new_dict["country"] = country
    new_dict["visits"] = times
    new_dict["cities"] = cities




#🚨 Do not change the code below
add_new_country("Russia", 2, ["Moscow", "Saint Petersburg"])
add_new_country("Nepal", 100, ["KTM", "DHK"])
print(travel_log)
