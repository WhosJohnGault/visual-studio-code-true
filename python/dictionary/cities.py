# Make a dictionary called cities Use the names of three cities as
# keys in your dictionary Create a dictionary of information about each city and
# include the country that the city is in, its approximate population, and one fact
# about that city The keys for each city’s dictionary should be something like
# country, population, and fact Print the name of each city and all of the infor-
# mation you have stored about it
cities={
    'Chicago': {'state' : 'Illinois',
                'population' : 'atleast 5',
                'fun fact' : 'there is no gabby here',
                },
    'Los Angeles':{'state' : 'California',
                'population' : 'atleast 10',
                'fun fact' : 'Gabby used to live in a nearby county',
                },
    'Gabbyville':{'state' : 'Wisconsin',
                'population' : 'less than 3',
                'fun fact' : 'Gabby currently lives here',},
}
for city,facts in cities.items():
    print("\n City name: " + city)
    city_info = facts['state'] + ": population size: " + facts['population']
    funfact=facts['fun fact']

    print("\t City Information: " + city_info.title())
    print("\t Fun Fact: " + funfact.capitalize())