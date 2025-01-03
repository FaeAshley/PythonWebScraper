# PythonWebScarper
Web Scraper: Quotes to Scrape

This web scraper is a Python-based application that extracts quotes, authors, and tags from the website Quotes to Scrape. It uses the requests library to fetch the webpage's HTML content and BeautifulSoup for parsing and extracting the desired data.

Features

Scrapes the following data for each quote:

The text of the quote.

The author of the quote.

Tags associated with the quote.

Collects all quotes from the first page of the website.

Displays the scraped data as a list of dictionaries in the console.

Requirements

Python 3.x

Required libraries:

requests

beautifulsoup4

Install the libraries using pip:

pip install requests beautifulsoup4

How It Works

Fetches the Webpage:

Sends an HTTP GET request to https://quotes.toscrape.com/.

Retrieves the HTML content of the page.

Parses the HTML:

Locates the second <div> with the class row.

Within this, finds the <div> with the class col-md-8, which contains all the quotes.

Extracts Data:

Iterates through each <div> with the class quote to extract:

Quote text: From <span class="text">.

Author name: From <small class="author">.

Tags: From <div class="tags"> containing <a class="tag"> elements.

Displays the Data:

Collects all the quotes in a list of dictionaries and prints them to the console.

Code Overview

get_request()

Fetches the webpage and parses its content.

Locates the required HTML elements to extract quotes, authors, and tags.

Appends the extracted data to a list and prints the result.

main()

Calls the get_request() function to execute the scraping process.

Example Output

When you run the program, it prints a list of dictionaries like this:

[
    {
        'text': '“The world as we have created it is a process of our thinking. It cannot be changed without changing our thinking.”',
        'author': 'Albert Einstein',
        'tags': ['change', 'deep-thoughts', 'thinking']
    },
    {
        'text': '“It is our choices, Harry, that show what we truly are, far more than our abilities.”',
        'author': 'J.K. Rowling',
        'tags': ['abilities', 'choices']
    }
]

How to Run

Clone the repository or copy the script into a Python file (e.g., app.py).

Run the script:

python app.py

The output will display in the console.

Troubleshooting

Empty Output:

Verify that the website’s structure matches the scraper’s logic.

Check for network issues or site restrictions.

Website Blocking:

Add headers to mimic a browser request (e.g., User-Agent).

Potential Enhancements

Pagination Support: Scrape multiple pages to gather all quotes from the site.

Save Data: Store the scraped quotes in a CSV or JSON file for further use.

Error Handling: Add robust error handling for network issues or missing elements.

License

This project is open-source and available for learning and personal use.

Happy scraping! 🐾
