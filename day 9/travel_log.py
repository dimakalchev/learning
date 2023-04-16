#  =Nesting
# capitals = {
#     "France": "Paris",
#     "Germany": "Berlin",
#
# }
#
# travel_log = {
#     "France": ["Paris", "Lille", "Dijon", ],
#     "Germany": ["Berlin", "Hamburg", "Stuttgart", ]
# }
# # Dict in dict
# travel_log = {
#     "France": {"cities_visited": ["Paris", "Lille", "Dijon", ], "total_visits": "12" },
#     "Germany": {"cities_visited": ["Berlin", "Hamburg", "Stuttgart", ],"tjtal_visits": "8",  }
# }
#
#  Nesting a dictionare in a list
travel_log = [
    {
        "country": "France",
        "total_visits": 12,
        "cities_visited": ["Paris", "Lille", "Dijon", ],
    },
    {
        "country": "Germany",
        "total_visits": 5,
        "cities_visited": ["Berlin", "Hamburg", "Stuttgart", ],
    },
]
print(travel_log)
# country = input("input country have you been to?  ")
# how_often = input("How many times?  ")
# cities = input("What cities have you visited in this country?  ").split()
# travel_log.append({"country": country, "total_visits": how_often, "cities_visited": cities})
# print(travel_log)
def add_new_country(country_visited, times_visited, cities_visited):
    new_country = {}
    new_country["country"] = country_visited
    new_country["visits"] = times_visited
    new_country["cities"] = cities_visited
    travel_log.append(new_country)
print(travel_log)
