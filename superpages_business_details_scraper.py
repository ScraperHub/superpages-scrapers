import requests
from bs4 import BeautifulSoup
import json

def get_business_details(url):
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:131.0) Gecko/20100101 Firefox/131.0"
    }
    response = requests.get(url, headers=headers)
    soup = BeautifulSoup(response.content, 'html.parser')

    # Extract the business name
    name = soup.find('h1', class_='business-name').text.strip() if soup.find('h1', class_='business-name') else ""

    # Extract operating hours in key-value pairs
    hours = {
        row.find('th', class_='day-label').text.strip(): row.find('td', class_='day-hours').text.strip()
        for row in soup.select('.biz-hours tr')
    }

    # Extract contact information as key-value pair
    contact_info = {
        dt.text.strip().replace(':', ''): dd.text.strip()
        for dt, dd in zip(soup.select('.details-contact dt'), soup.select('.details-contact dd'))
    }

    # Store the details in a dictionary
    details = {
        'name': name,
        'hours': hours,
        'contact_info': contact_info
    }
    return details

def save_to_json(data, filename='business_details.json'):
    with open(filename, 'w') as file:
        json.dump(data, file, indent=4)

def main():
    urls = [
        'https://www.superpages.com/los-angeles-ca/bpp/evergreen-cleaning-systems-540709574?lid=1002188497939',
        'https://www.superpages.com/van-nuys-ca/bpp/merry-maids-542022905?lid=1002108319143',
        # Add more product URLs here
    ]

    all_business_details = []
    for url in urls:
        business_details = get_business_details(url)
        all_business_details.append(business_details)

    # Save all details to a JSON file
    save_to_json(all_business_details)

if __name__ == '__main__':
    main()