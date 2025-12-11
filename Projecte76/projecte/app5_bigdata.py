# app5_bigdata.py
import requests
from bs4 import BeautifulSoup

def aplicacio_bigdata():
    print("\n--- APLICACIÓ 5: Web Scraping ---")

    url = "https://www.wikipedia.org/"

    resposta = requests.get(url)
    html = BeautifulSoup(resposta.text, "html.parser")

    titol = html.find("strong").text

    print("Títol principal de Wikipedia:")
    print(titol)

