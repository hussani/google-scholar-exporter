import os
import csv
import json
import time
from serpapi import GoogleSearch

serpapi_api_key = os.getenv("SERPAPI_API_KEY")
max_results = 250
results_per_page = 20
total_requests = max_results // results_per_page

query_string = "\"software testing education\""
publish_since = "2018"

all_results = []
csv_data = []

def fetch_results(start_index):
    params = {
        "api_key": serpapi_api_key,
        "engine": "google_scholar",
        "num": str(results_per_page),
        "as_ylo": publish_since,
        "q": query_string,
        "hl": "en",
        "as_sdt": "0,5",
        "start": str(start_index)
    }
    search = GoogleSearch(params)
    return search.get_dict()

for i in range(total_requests):
    try_count = 0
    while try_count < 3:
        try:
            start_index = i * results_per_page
            results = fetch_results(start_index)
            all_results.append(results)

            for result in results.get('organic_results', []):
                title = result.get('title', 'N/A')
                official_url = result.get('link', 'N/A')
                citation_count = result.get('inline_links', {}).get('cited_by', {}).get('total', 0)
                publication_info = result.get('publication_info', {}).get('summary', 'N/A')
                authors = [author.get('name', 'N/A') for author in result.get('publication_info', {}).get('authors', [])]
                csv_data.append([title, official_url, citation_count, publication_info, '; '.join(authors)])

            break
        except Exception as e:
            print(f"Warning: Failed to fetch data for page {i + 1}. Attempt {try_count + 1}. Error: {e}")
            try_count += 1
            time.sleep(5)  # Espera 5 segundos antes de tentar novamente

    if try_count == 3:
        print(f"Error: Skipping page {i + 1} after 3 failed attempts.")

# Salvando os dados em CSV
with open('scholar_results.csv', 'w', newline='', encoding='utf-8') as file:
    writer = csv.writer(file)
    writer.writerow(['Title', 'URL', 'Citation Count', 'Publication Info', 'Authors'])
    writer.writerows(csv_data)

# Salvando os dados brutos em JSON
with open('scholar_results_raw.json', 'w', encoding='utf-8') as file:
    json.dump(all_results, file, ensure_ascii=False, indent=4)

print("Data extraction complete.")
