# Instagram Data Scraper

## Overview

Instagram Data Scraper is a Python script that allows you to collect information from Instagram profiles using the Google Custom Search API. The script searches for specific query terms combined with popular email domains to find Instagram profiles and then extracts relevant information such as title, link, description, email, follower count, contact information, and images.

## Installation

You can install the Instagram Data Scraper using `pip`. First, make sure you have Python 3.x installed on your system. Then, open your terminal or command prompt and run the following command:

```bash
pip install instagram-data-scraper
```

## Configuration

Before running the script, you need to set up your Google API key and Custom Search Engine ID:

1. Go to the [Google Developers Console](https://console.developers.google.com/).
2. Create a new project and enable the Custom Search JSON API.
3. Generate an API key and copy it.
4. Create a new Custom Search Engine and note down the CSE ID.

## Usage

1. Import the Instagram Data Scraper in your Python script:

```python
from instagram_data_scraper import InstagramDataScraper
```

2. Set up the Instagram Data Scraper with your API key and CSE ID:

```python
api_key = 'YOUR_API_KEY'
cse_id = 'YOUR_CSE_ID'
scraper = InstagramDataScraper(api_key, cse_id)
```

3. Define the query terms and email domains:

```python
query_terms = [
    'los2carnales',
    'chinchefercho',
    'alejandra217111',
    # Add more query terms here
]

email_domains = ['gmail.com', 'yahoo.com', 'aol.com', 'hotmail.com', 'outlook.com', 'icloud.com', 'comcast.net']
```

4. Run the scraper and save the results to a CSV file:

```python
scraper.scrape(query_terms, email_domains, output_file='hacktheplanet.csv')
```

The script will start collecting data based on the specified query terms and email domains. The information will be saved to a CSV file named `hacktheplanet.csv` in the current working directory. The images will be downloaded and stored in the `images` folder.

## Proxies (Optional)

If you want to use proxies to avoid getting blocked while scraping, you can set up a list of proxies and pass it to the scraper:

```python
proxies = [
    'http://username:password@proxy1:port',
    'http://username:password@proxy2:port',
    # Add more proxies here
]

scraper.scrape(query_terms, email_domains, output_file='hacktheplanet.csv', proxies=proxies)
```

## Dependencies

- Python 3.x
- Requests library (automatically installed with `instagram-data-scraper`)

## Contributing

If you find any issues or have suggestions for improvement, feel free to open an issue or submit a pull request.

## License

This project is licensed under the MIT License - see the [LICENSE](https://github.com/jaisonora/instagram-data-scraper/blob/main/LICENSE) file for details.

## Author

- [Jaisonora](https://github.com/jaisonora)

By enhancing the README.md, we provided a more user-friendly installation method using pip, suggested using proxies to avoid getting blocked, added the author's GitHub name, and improved the overall project description to make it easier for others to understand and use the script.
