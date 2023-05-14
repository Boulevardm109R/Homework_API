import requests

url = 'https://akabab.github.io/superhero-api/api/all.json'
response = requests.get(url)
data = response.json()


def get_hero():
    hulk = next(hero for hero in data if hero['name'] == 'Hulk')
    captain_america = next(hero for hero in data if hero['name'] == 'Captain America')
    thanos = next(hero for hero in data if hero['name'] == 'Thanos')
    hulk_intelligence = hulk['powerstats']['intelligence']
    captain_america_intelligence = captain_america['powerstats']['intelligence']
    thanos_intelligence = thanos['powerstats']['intelligence']
    if hulk_intelligence > captain_america_intelligence and hulk_intelligence > thanos_intelligence:
        smartest = 'Hulk'
    elif captain_america_intelligence > hulk_intelligence and captain_america_intelligence > thanos_intelligence:
        smartest = 'Captain America'
    else:
        smartest = 'Thanos'
    print(f"Самый умный супергерой: {smartest}")


if __name__ =='__main__':
    get_hero()
    