import requests
from bs4 import BeautifulSoup
import warnings

def scrape_hotel_data():
    url = "https://www.comohotels.com/destinations"
    response = requests.get(url)
    if response.status_code != 200:
        warnings.warn(f"Failed to retrieve data: {response.status_code}")
        return []

    soup = BeautifulSoup(response.text, 'html.parser')
    properties = []

    for property_parent in soup.find_all("div", class_="property-parent"):
        property_info = property_parent.find("div", class_="property-info")
        name_tag = property_info.find("h3")
        location_tag = property_info.find("div", class_="location")
        description_tag = property_info.find("p")
        slug_tag = property_info.find("a", class_="button-tertiary iron")
        image_container = property_parent.find("div", class_="swiper-slide-active")
        image_tag = image_container.find("img") if image_container else None

        name = name_tag.text.strip() if name_tag else None
        location = location_tag.text.strip() if location_tag else None
        description = description_tag.text.strip() if description_tag else None
        slug = slug_tag['href'].strip() if slug_tag else None
        image_url = image_tag['src'].strip() if image_tag else None
        if image_url and not image_url.startswith("http"):
            image_url = "https:" + image_url

        if name and location and description and slug and image_url:
            properties.append({
                'name': name,
                'slug': slug,
                'location': location,
                'description': description,
                'image_url': image_url
            })

    if not properties:
        print("No properties found.")
        return []

    return properties

if __name__ == "__main__":
    scraped_data = scrape_hotel_data()
    print(scraped_data)
