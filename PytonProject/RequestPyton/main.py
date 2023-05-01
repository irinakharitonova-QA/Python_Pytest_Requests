import requests

# Покемоны у тренера
# response = requests.get("https://pokemonbattle.me:9104/pokemons",
#                        params={"trainer_id":"4167"})

# print(response.text)

url = "https://pokemonbattle.me:9104/trainers"
header = {"Content-Type": "application/json"}
response = requests.get(url, headers=header)
print(response.text)

# Создание покемона
# header = {"trainer_token": "147960980c6dad9942d02a2eeab5deba", "Content-Type": "application/json"}

# data_pok = {
#     "name":"Clop",
#     "photo":"https://dolnikov.ru/pokemons/albums/033.png"
# }

# response = requests.post("https://pokemonbattle.me:9104/pokemons", 
#                          headers=header,
#                          json=data_pok)

# print(response.text)

#Поменять имя
# header = {"trainer_token": "147960980c6dad9942d02a2eeab5deba", "Content-Type": "application/json"}
# data_pok = {
#     "pokemon_id": "9735",
#     "name": "Clop2",
#     "photo": "https://dolnikov.ru/pokemons/albums/056.png"
# }
# response = requests.put("https://pokemonbattle.me:9104/pokemons",
#                         headers=header,
#                         json=data_pok)
# print(response.text)

# headers = {"trainer_token": "147960980c6dad9942d02a2eeab5deba", "Content-Type": "application/json"}

# data_pok = {
#     "pokemon_id": "9735"
# }

# response = requests.post("https://pokemonbattle.me:9104/trainers/add_pokeball", 
#                           headers=headers,
#                           json=data_pok)

# print(response.text)