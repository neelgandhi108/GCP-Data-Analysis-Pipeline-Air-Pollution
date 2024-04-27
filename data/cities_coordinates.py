import json
import requests

cities = [
    "Warszawa",
    "Kraków",
    "Łódź",
    "Wrocław",
    "Poznań",
    "Gdańsk",
    "Szczecin",
    "Bydgoszcz",
    "Lublin",
    "Katowice",
    "Białystok",
    "Gdynia",
    "Częstochowa",
    "Radom",
    "Sosnowiec",
    "Toruń",
    "Kielce",
    "Rzeszów",
    "Gliwice",
    "Zabrze",
    "Olsztyn",
    "Bielsko-Biała",
    "Bytom",
    "Ruda Śląska",
    "Rybnik",
    "Tychy",
    "Dąbrowa Górnicza",
    "Opole",
    "Elbląg",
    "Płock",
    "Wałbrzych",
    "Gorzów Wielkopolski",
    "Włocławek",
    "Tarnów",
    "Chorzów",
    "Kalisz",
    "Koszalin",
    "Legnica",
    "Grudziądz",
    "Słupsk",
    "Jaworzno",
    "Jastrzębie-Zdrój",
    "Pruszków",
    "Nowy Sącz",
    "Mielec",
    "Ostrowiec Świętokrzyski",
    "Siemianowice Śląskie",
    "Stargard Szczeciński",
    "Pabianice",
    "Świdnica",
    "Skierniewice",
    "Kędzierzyn-Koźle",
    "Zgierz",
    "Łomża",
    "Ełk",
    "Przemyśl",
    "Starachowice",
    "Krotoszyn",
    "Gniezno",
    "Kołobrzeg",
    "Świnoujście",
    "Jarosław",
    "Zduńska Wola",
    "Żyrardów",
    "Namysłów",
    "Łask",
    "Augustów",
    "Kraśnik",
    "Pszczyna",
    "Ostrołęka",
    "Głogów",
    "Sandomierz",
    "Suwałki",
    "Goleniów",
    "Złotów",
    "Rawicz",
    "Sanok",
    "Lębork",
    "Nakło nad Notecią",
    "Nysa",
    "Chojnice",
    "Świebodzice",
    "Wągrowiec",
    "Brzeg",
    "Luboń",
    "Wieluń",
    "Łaziska Górne",
    "Węgrów",
    "Ostrzeszów",
    "Łęczyca",
    "Dzierżoniów",
    "Bartoszyce",
    "Olecko",
    "Bieruń",
    "Skarszewy",
    "Zwoleń",
    "Chodzież",
    "Rydułtowy",
    "Bogatynia",
    "Lidzbark Warmiński",
    "Lubniewice",
    "Jasło",
    "Pszczyna",
]

# empty lists for storing coordinates
locations = []

# loop over cities to get their coordinates
for id, city in enumerate(cities):
    url = f"https://nominatim.openstreetmap.org/search?q={city},+Poland&format=json"
    response = requests.get(url).json()
    location = {
        "City_index": id,
        "Latitude": response[0]["lat"],
        "Longitude": response[0]["lon"],
        "City": city,
    }
    locations.append(location)

# write locations to a json file
with open("locations.json", "w") as f:
    json.dump(locations, f, ensure_ascii=False)
