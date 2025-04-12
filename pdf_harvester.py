import os
import requests
from urllib.parse import urlparse
from googlesearch import search  # Install via `pip install googlesearch-python`

def download_pdf_from_overapi(folder_path, max_results=20):
    # Create folder if it doesn't exist
    os.makedirs(folder_path, exist_ok=True)

    # Google search query
    query = 'site:https://overapi.com/ filetype:pdf'
    print(f"Searching Google for: {query}")

    # Perform search
    pdf_links = []
    for result in search(query, num_results=max_results):
        if result.endswith(".pdf"):
            pdf_links.append(result)

    print(f"Found {len(pdf_links)} PDF(s). Starting download...\n")

    for link in pdf_links:
        try:
            filename = os.path.basename(urlparse(link).path)
            filepath = os.path.join(folder_path, filename)

            print(f"Downloading: {filename}")
            response = requests.get(link, stream=True)
            with open(filepath, 'wb') as f:
                for chunk in response.iter_content(chunk_size=8192):
                    f.write(chunk)
            print(f"Saved to: {filepath}\n")
        except Exception as e:
            print(f"Failed to download {link}. Error: {e}")

    print("Download complete.")

# === Change this to your desired path ===
save_folder = "C:\\Users\\penac\\OneDrive\\Documents\\Software Projects\\Python\\PDFHarvester"



# Run the app
download_pdf_from_overapi(save_folder)
