import requests
import json

# Required to get api key, you may instead enter your api key later in api_key
import apiKey

# Enter your own api key
api_key = apiKey.API_KEY

url_search = 'https://api.nal.usda.gov/fdc/v1/foods/search?api_key=' + api_key

query = input('Enter the food you wish to search for - ')

print('\nSearching...\n')

# Can include "Foundation", "SR Legacy", "Survey", "Branded", "Experimental"
dataType = ["Foundation", "SR Legacy", "Survey"]

data = {"query": query, "dataType": dataType}

response = requests.post(url_search, json = data)

result = json.loads(response.text)

num_results = len(result['foods'])

print(str(num_results) + ' results found\n')

for i in range(num_results):
    a = str(i+1)
    nutrient_length = len(result['foods'][i]['foodNutrients'])
    print(a + '. ' + result['foods'][i]['description'] + '\n\t' + 'Category - ' + result['foods'][i]['foodCategory'])
    print('\t Food Nurtrients - ')
    for n in range(nutrient_length):
        nutrient = result['foods'][i]['foodNutrients'][n]
        print('\n\t\t' + nutrient['nutrientName'] + '\n\t\t\t' + str(nutrient['value']) + ' ' + nutrient['unitName'])