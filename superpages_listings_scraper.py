import requests
from bs4 import BeautifulSoup
import json

# Function to fetch listings from a single page
def fetch_listings(page_number):
    url = f"https://www.superpages.com/search?search_terms=Home%20Services&geo_location_terms=Los%20Angeles%2C%20CA&page={page_number}"
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:131.0) Gecko/20100101 Firefox/131.0"
    }
    response = requests.get(url, headers=headers)
    if response.status_code == 200:
        soup = BeautifulSoup(response.content, "html.parser")
        listings = []

        for business in soup.select("div.search-results > div.result"):
            name = business.select_one("a.business-name span").text.strip() if business.select_one("a.business-name span") else ""
            address = business.select_one("span.street-address").text.strip() if business.select_one("span.street-address") else ""
            phone = business.select_one("a.phone.primary").text.strip() if business.select_one("a.phone.primary") else ""
            website = business.select_one("a.weblink-button")["href"] if business.select_one("a.weblink-button") else ""
            detail_page_link = 'https://www.superpages.com' + business.select_one("a.business-name")["href"] if business.select_one("a.business-name") else ""

            listings.append({
                "name": name,
                "address": address,
                "phone": phone,
                "website": website,
                "detail_page_link": detail_page_link
            })

        return listings
    else:
        print("Failed to retrieve page.")
        return []

# Function to fetch listings from multiple pages
def fetch_all_listings(total_pages):
    all_listings = []
    for page in range(1, total_pages + 1):
        print(f"Scraping page {page}...")
        listings = fetch_listings(page)
        all_listings.extend(listings)
    return all_listings

# Function to save listings data to a JSON file
def save_to_json(data, filename="superpages_listings.json"):
    with open(filename, "w") as file:
        json.dump(data, file, indent=4)
    print(f"Data saved to {filename}")

# Main function to run the complete scraper
def main():
    total_pages = 5  # Define the number of pages you want to scrape
    all_listings_data = fetch_all_listings(total_pages)
    save_to_json(all_listings_data)

# Run the main function
if __name__ == "__main__":
    main()