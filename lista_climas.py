def lista_climas(city):
    url = f"http://Wttr.in/{city}"
    response = requests.get(url)
    return response.text 