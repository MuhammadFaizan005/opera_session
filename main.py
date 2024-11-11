import time
from tqdm import tqdm
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException
import opera_on
from bs4 import BeautifulSoup
# Set up browser session
port_no = 9226
session = 6
browser = opera_on.OperaBrowser(port_no, session)
driver = browser.get_driver()

# Open the desired URL
driver.get("https://www.cyberbackgroundchecks.com/address/13050-e-47th-ave/denver/co")
time.sleep(10)

page_source = driver.page_source
soup = BeautifulSoup(page_source, 'html.parser')

# Close the browser
driver.quit()

# Parsing the required data
try:
    # Extract Name from each card div
    cards = soup.find_all('div', class_='card')
    if cards:
        # Iterate through each card and extract the name
        for card in cards:
            name_tag = card.find('span',class_='name-given')
            if name_tag:
                name = name_tag.get_text(strip=True)
                c_d = card.find('p',class_="address-current")
                current_address = c_d.get_text(strip=True)
                profile_link = card.find('a',class_="btn")
                profile_href = profile_link.get("href") if profile_link else "No link found"
                link_final = f"https://www.cyberbackgroundchecks.com{profile_href}"
                print(f"Name: {name},\nCurrent Address : {current_address}\nLink : {link_final}\n\n")
            else:
                print("Name not found in this card.")
    else:
        print("No card divs found.")

except Exception as e:
    print("An error occurred during scraping:", e)