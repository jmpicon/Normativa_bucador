import requests
from bs4 import BeautifulSoup
from werkzeug.urls import url_quote


def build_url(base_url, path):
    return f"{base_url}/{url_quote(path)}"


def scrape_website(url):
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')
    # Aquí agregas el código para extraer la información que necesitas
    return soup

# Ejemplo de uso
if __name__ == "__main__":
    url = 'https://www.incibe.es' # URL de ejemplo
    result = scrape_website(url)
    print(result)
