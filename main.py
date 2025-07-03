from fastapi import FastAPI
import requests

app = FastAPI()

@app.get("/download_html")
async def download_html(urls: list):
    html_data = {}
    for url in urls:
        try:
            response = requests.get(url)
            if response.status_code == 200:
                html_data[url] = response.text  # Store the HTML content
            else:
                html_data[url] = f"Failed to fetch: {response.status_code}"
        except Exception as e:
            html_data[url] = f"Error: {str(e)}"
    
    return html_data
