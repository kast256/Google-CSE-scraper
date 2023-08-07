import requests
import csv
import os
import re
from urllib.parse import urlparse

# Define your API key and CSEHA ID
api_key = 'enter here'
cse_id = 'enter google cse id here'

# Define the query terms as a list of individual strings
query_terms = [
    'los2carnales',
    'chinchefercho',
    'alejandra217111',
    'alanzamudior',
    'amandamenamusic',
    'anabarbaramusic',
    'ashbrall',
    'reflejointimo',
    'abi_hernaandez',
    'nattinatasha',
    'alexisadictivo',
    'braggaomx',
    'vranalaura',
    'bizarrap',
    'galaxiaecuador',
    'dalumusica',
    'nerysdiaz',
    'fabiolagarzon',
    'gerardoortizoficial',
    'jerrycorraless',
    'gelenasolanotv',
    'guanamorrecords',
    'hijosdebarron',
    'spotifymexico',
    'delrecords',
    'evelyn_sicairos',
    'larryhernandez',
    'premiodelaradio',
    'zamoraliveoficial',
    'grupofirme',
    'yosoyyaco',
    'exafm',
    'jessytatianaoficial',
    'j_medina37',
    'lostigresdelnorte',
    'chapintv',
    'yamilet_bustillos',
    'keilarodas_',
    'kitziahermosillo',
    'lapoderosalg',
    'laz1073fm',
    'leninramirezmusic',
    'bmi',
    'broadcast music inc',
    'luiscoronelmusic',
    'marianoficialmx',
    'marissetvereni',
    'mazart.co',
    'mnldesigns',
    'bmarlener',
    'nuestromundo7',
    'palenqueculiacanoficial',
    'pedrocuevasgt',
    'venadosdemzt',
    'marthadebayle',
    'luisrconriquezoficial',
    'somosvevo',
    'soygruperomx',
    'missy.flow',
    'freddy_perezz',
    'keniaos',
    'chuperabuelotitorivera',
    '_lachupitos',
    'unotv_',
    'dalechama',
    'sexydulceg',
]

# Define the email domains to include in the query
email_domains = ['gmail.com', 'yahoo.com', 'aol.com', 'hotmail.com', 'outlook.com', 'icloud.com', 'comcast.net']

# Combine the query terms with email domains
queries = [f'{term} "{domain}"' for term in query_terms for domain in email_domains]

# Define the number of results per page and the total number of results to fetch
results_per_page = 10
total_results = 100  # Adjust as needed

# Function to download the image and save it locally
def download_image(image_url):
    try:
        response = requests.get(image_url)
        if response.status_code == 200:
            image_name = os.path.basename(urlparse(image_url).path)
            image_path = os.path.join('images', image_name)
            with open(image_path, 'wb') as image_file:
                image_file.write(response.content)
            return image_path
    except Exception as e:
        print(f'Error downloading image: {e}')
        return None

# Check if the CSV file already exists
file_exists = os.path.isfile('hacktheplanet.csv')

# Open the CSV file in append mode if it exists, otherwise create a new file
with open('hacktheplanet.csv', 'a', newline='', encoding='utf-8') as csv_file:
    csv_writer = csv.writer(csv_file)

    # Write the header row only if the file is newly created
    if not file_exists:
        csv_writer.writerow(['Title', 'Link', 'Description', 'Email', 'Follower Count', 'Country', 'ID', 'Status', 'Avatar', 'Contact', 'Images'])

    # Loop through the queries
    for query in queries:
        # Loop through the pages based on the desired number of results
        for start_index in range(1, total_results + 1, results_per_page):
            # Define the API endpoint URL with the API key, CSE ID, and query term
            url = f'https://www.googleapis.com/customsearch/v1?key={api_key}&cx={cse_id}&q={query}'

            # Modify the API URL to include the start index and number of results
            paginated_url = f'{url}&start={start_index}&num={results_per_page}'

            # Send the request to the API
            response = requests.get(paginated_url)

            # Check if the request was successful
            if response.status_code == 200:
                # Retrieve the search results from the response
                search_results = response.json()

                # Process and extract the desired information from the search results
                for item in search_results.get('items', []):
                    title = item.get('title', '')
                    link = item.get('link', '')
                    snippet = item.get('snippet', '')

                    # Extract email and follower count from the snippet
                    email = ''
                    follower_count = ''
                    email_parts = re.split(r'\bEmail\b', snippet, flags=re.IGNORECASE)
                    if len(email_parts) > 1:
                        email_match = re.search(r'([\w\.-]+@[\w\.-]+\.\w+)', email_parts[1])
                        if email_match:
                            email = email_match.group(1)

                    follower_count_match = re.search(r'Followers: (\d+)', snippet)
                    if follower_count_match:
                        follower_count = follower_count_match.group(1)

                    # Custom function to extract contact and images information from the snippet
                    def extract_contact_and_images(snippet):
                        contact = ''
                        images = []
                        # Custom logic to extract contact and images information from the snippet
                        # You can update this logic based on your requirements
                        # For example, if the contact information appears after 'Contact:', you can use:
                        contact_parts = re.split(r'\bContact\b', snippet, flags=re.IGNORECASE)
                        if len(contact_parts) > 1:
                            contact = contact_parts[1].split('\n', 1)[0].strip()

                        # If the image URLs appear after 'Image:', you can use:
                        image_parts = re.split(r'\bImage\b', snippet, flags=re.IGNORECASE)
                        if len(image_parts) > 1:
                            image_urls = re.findall(r'https?://\S+', image_parts[1])
                            images = [download_image(url) for url in image_urls if download_image(url)]
                        return contact, images

                    contact, images = extract_contact_and_images(snippet)

                    # Append the data to the CSV file
                    csv_writer.writerow([title, link, snippet, email, follower_count, '', '', '', '', contact, images])

            else:
                # Handle the case when the request was not successful
                print('Error: Request failed')

print('Data extraction completed and saved to hacktheplanet.csv.')
