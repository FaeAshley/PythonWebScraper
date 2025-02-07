import json

import jsonify as jsonify
import requests
import gspread
from bs4 import BeautifulSoup
import os
from google.oauth2.service_account import Credentials


SCOPES = [
    "https://www.googleapis.com/auth/spreadsheets",
    "https://www.googleapis.com/auth/drive"  # Add Drive access
]

creds = Credentials.from_service_account_file("credentials.json", scopes=SCOPES)
client = gspread.authorize(creds)

spreadsheet = client.open("WebScrape")  # Make sure this is the correct sheet name
worksheet = spreadsheet.sheet1


def get_request():
    url = "https://quotes.toscrape.com/"
    r = requests.get(url)
    soup = BeautifulSoup(r.content, 'html.parser')

    rows = soup.find_all('div', class_='row')
    parent_div = rows[1]  # The second row contains the quotes
    target_div = parent_div.find('div', class_='col-md-8')

    quotes = []
    for row in target_div.find_all('div', attrs={'class': 'quote'}):
        quote = {}  # Ensure it's a dictionary
        quote["text"] = row.find('span', class_='text').text.strip()
        quote["author"] = row.find('small', class_='author').text.strip()
        quote["tags"] = [tag.text.strip() for tag in row.find('div', class_='tags').find_all('a', class_='tag')]

        print("DEBUG:", quote)  # Debugging
        quotes.append(quote)

    # Convert list of dicts into list of lists
    data = [["Text", "Author", "Tags"]]  # Header row
    for quote in quotes:
        if isinstance(quote, dict):  # Ensure it's a dictionary before accessing keys
            data.append([quote["text"], quote["author"], ", ".join(quote["tags"])])
        else:
            print("Skipping invalid entry:", quote)

    # Send data to Google Sheets
    worksheet.update(data)
    print("Data successfully written to Google Sheets!")


def main():
    get_request()


if __name__ == "__main__":
    main()