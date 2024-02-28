import json
import csv

# Carrega os dados do arquivo JSON
with open('scholar_results_raw.json', 'r', encoding='utf-8') as file:
    data = json.load(file)

# Prepara a lista para armazenar os dados extraídos
extended_data = []

for page in data:
    for result in page.get('organic_results', []):
        title = result.get('title', 'N/A')
        official_url = result.get('link', 'N/A')
        citation_count = result.get('inline_links', {}).get('cited_by', {}).get('total', 0)
        publication_info = result.get('publication_info', {}).get('summary', 'N/A')
        authors = [author.get('name', 'N/A') for author in result.get('publication_info', {}).get('authors', [])]

        # Extrair o ano de publicação da informação da publicação
        year = 'N/A'
        if ' - ' in publication_info:
            year = publication_info.split(' - ')[-1]
            if year.isdigit():
                year = year[:4]
            else:
                year = 'N/A'

        # Extrair links de recursos
        resource_links = [resource.get('link', 'N/A') for resource in result.get('resources', [])]

        extended_data.append([title, official_url, citation_count, publication_info, '; '.join(authors), year, '; '.join(resource_links)])

# Salva os dados em um arquivo CSV
with open('extended_scholar_results.csv', 'w', newline='', encoding='utf-8') as file:
    writer = csv.writer(file)
    writer.writerow(['Title', 'URL', 'Citation Count', 'Publication Info', 'Authors', 'Year', 'Resource Links'])
    writer.writerows(extended_data)

print("Extended data extraction complete.")
