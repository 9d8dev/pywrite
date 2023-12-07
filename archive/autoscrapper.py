from autoscraper import AutoScraper

url = 'https://www.comohotels.com/destinations'

# We can add one or multiple candidates here.
# You can also put urls here to retrieve urls.
wanted_list = ["COMO PARROT CAY"]

scraper = AutoScraper()
result = scraper.build(url, wanted_list)
print(result)
