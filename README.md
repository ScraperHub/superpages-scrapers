# superpages-scrapers

## Description

This repository contains Python scrapers designed to extract business listings and detailed business information from SuperPages, a widely used online business directory. The scrapers help collect essential data for lead generation, market research, and competitive analysis.

➡ Read the full blog [here](https://crawlbase.com/blog/how-to-scrape-superpages-to-generate-leads/) to learn more.

## Scraper Overview

This repository includes two scrapers:

1. **SuperPages Listings Scraper** (`superpages_listings_scraper.py`) – Extracts business listings, including:

   - **Business Name**
   - **Address**
   - **Phone Number**
   - **Website URL**
   - **Business Profile Page Link**

   Scraper efficiently handle pagination.

2. **SuperPages Business Details Scraper** (`superpages_business_details_scraper.py`) – Extracts detailed business information from individual listing pages, including:

   - **Business Name**
   - **Operating Hours**
   - **Contact Information (e.g., email, additional phone numbers)**

## Environment Setup

Ensure that Python is installed on your system. Check the version using:

```bash
python --version
```

Install the required dependencies:

```bash
pip install requests beautifulsoup4
```

- **Requests** – Handles HTTP requests to retrieve web pages.
- **BeautifulSoup** – Parses and extracts structured data from HTML.

## Running the Scrapers

### 1. Running the SuperPages Listings Scraper

This scraper extracts multiple business listings from SuperPages.

1. **Modify the Target Search Query**
   Update the `fetch_listings()` function in `superpages_listings_scraper.py` with your desired search terms and location.

2. **Run the Scraper**

   ```bash
   python superpages_listings_scraper.py
   ```

3. **Extracted Data Format**
   The results are saved in superpages_listings.json as an array of business listings.

### 2. Running the SuperPages Business Details Scraper

This scraper extracts detailed information from individual business pages.

1. **Update the Business URLs**

   - Modify the **urls** list in `superpages_business_details_scraper.py` with the SuperPages business listing URLs you want to scrape.

2. **Run the Scraper**

   ```bash
   python superpages_business_details_scraper.py
   ```

3. **Extracted Data Format**
   The results are saved in business_details.json, containing structured details for each business.

## Optimizing SuperPages Scraper with Crawlbase Smart Proxy

To make our SuperPages scraper more robust and faster, we can use [Crawlbase Smart Proxy](https://crawlbase.com/smart-proxy). Smart Proxy provides IP rotation and anti-bot protection, helping us avoid rate limits and blocks during long data collection.

### Integrating Crawlbase Smart Proxy

Below example shows how to use Crawlbase Smart Proxy in Python.

```python
import requests

# Replace _USER_TOKEN_ with your Crawlbase Token
proxy_url = 'http://_USER_TOKEN_:@smartproxy.crawlbase.com:8012'

def request_with_crawlbase_smart_proxy(url):
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:131.0) Gecko/20100101 Firefox/131.0"
    }
    proxies = {"http": proxy_url, "https": proxy_url}

    try:
        response = requests.get(url=url, headers=headers, proxies=proxies, verify=False)
        response.raise_for_status()
        return response.text  # Return page content instead of full response object
    except requests.exceptions.RequestException as e:
        print(f"Request failed: {e}")
        return None
```

**Note:** Sign up on [Crawlbase](https://crawlbase.com/signup) and get an API token.

With Crawlbase Smart Proxy, requests appear to originate from different locations, ensuring uninterrupted scraping.

## To-Do List

1. Enhance scraping logic to extract additional business details (e.g., social media links, customer reviews).
2. Improve error handling for failed or slow requests.
3. Support automated discovery of business detail page links from search listings.

This project is ideal for businesses, marketers, and analysts looking to gather SuperPages data for lead generation and market insights. 🚀
