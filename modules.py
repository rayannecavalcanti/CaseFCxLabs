from random import randint, choice
from datetime import datetime
import requests
from faker import Faker

faker = Faker('pt_BR')

def username():
    username = f"user{randint(1000, 9999)}"
    return username

def email():
    return faker.email()

def password():
    return faker.password(length=12, special_chars=True, digits=True, upper_case=True, lower_case=True)

def first_name():
    return faker.first_name()

def last_name():
    return faker.last_name()

def phone_number():
    return faker.phone_number()

def country():
    return "Brasil"

def city():
    url = "https://servicodados.ibge.gov.br/api/v1/localidades/municipios"
    resposta = requests.get(url)

    if resposta.status_code == 200:
        resposta.encoding = 'utf-8'  # Garante que a resposta seja interpretada corretamente
        cidades = [cidade["nome"] for cidade in resposta.json()] [:25]
        return choice(cidades)
    else:
        return "Erro ao buscar cidades"

def address():
    return faker.street_address()

def state():
    url = "https://servicodados.ibge.gov.br/api/v1/localidades/estados"
    resposta = requests.get(url)

    if resposta.status_code == 200:
        resposta.encoding = 'utf-8'
        estados = [estado["nome"] for estado in resposta.json()] [:10]
        return choice(estados)
    else:
        return "Erro ao buscar estados"

def postal_code():
    return faker.postcode()

def categories():
    categories = [
        {"id": "tabletsTxt", "name": "Tablets"},
        {"id": "laptopsTxt", "name": "Laptops"},
        {"id": "miceTxt", "name": "Mice"},
        {"id": "headphonesTxt", "name": "Headphones"},
        {"id": "speakersTxt", "name": "Speakers"}
    ]

    chosen_category = choice(categories)
    print(f"Selecionando a categoria: {chosen_category['name']}")
    return chosen_category

def card_number():
    return ''.join([str(randint(0, 9)) for _ in range(16)])

def cvv():
    return randint(1000, 9999)

def month_exp():
    return randint(1, 12)

def year_exp():
    actual_data = datetime.now().year
    return randint(actual_data+1, actual_data+10)