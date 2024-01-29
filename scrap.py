from bs4 import BeautifulSoup
import requests
import os

with open('urls_old.txt', 'r') as file:
    urls = file.read().splitlines()

if not os.path.exists('data_url'):
    os.makedirs('data_url')

failed_urls = []  # List to store the failed URLs

for i, url in enumerate(urls):
    success = False
    try:
        response = requests.get(url)
        content = response.content

        soup = BeautifulSoup(content, 'html.parser')

        etiquetas = soup.find_all('p', {'dir': 'auto'})

        if etiquetas:
            # Generate a unique filename using the iteration index
            nombre_archivo = os.path.join('data_url/', f'data_url_{i+26297}.txt')

            with open(nombre_archivo, 'w') as file:
                for etiqueta in etiquetas:
                    file.write(etiqueta.get_text() + '\n')

            success = True
    except Exception as e:
        print(f"Error al procesar el URL: {url}")
        print(f"Detalle del error: {str(e)}")

        # Store the failed URL, index, error, and details in the list
        failed_urls.append((i, url, str(e)))

# Save the failed URLs and their details to a file
failure_file = 'failures.txt'
with open(failure_file, 'w') as file:
    for failure in failed_urls:
        file.write(f"URL Index: {failure[0]}\n")
        file.write(f"URL: {failure[1]}\n")
        file.write(f"Error Details: {failure[2]}\n")
        file.write('\n')