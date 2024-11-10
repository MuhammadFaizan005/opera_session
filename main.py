import time
import opera_on
from tqdm import tqdm
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException

port_no = 9226
session = 6
browser = opera_on.OperaBrowser(port_no, session)
driver = browser.get_driver()

# Open the desired URL
driver.get("https://www.cyberbackgroundchecks.com/address/13050-e-47th-ave/denver/co")
time.sleep(5)
try:
    # Check if content is present
    check = driver.find_element(By.ID, "content")
    if check:
        print("Check Found")
    else:
        print("No check detected")
except NoSuchElementException:
    print("No check detected")

# Find the card divs and extract name
card_divs = driver.find_elements(By.CLASS_NAME, "card-header")
if card_divs:
    print(f"Div Found {len(card_divs)}\n{card_divs[0]}")
    
    # # Convert dictionary to WebElement if necessary
    # for idx, div in enumerate(card_divs):
    #     # Check if div is a dict and convert it to a WebElement
    #     if isinstance(div, dict) and 'ELEMENT' in div:
    #         # Convert dictionary to WebElement using the ELEMENT key
    #         div = driver.execute_script("return arguments[0]", div)
    #         card_divs[idx] = div  # Replace dict with WebElement in the list
    #     print(f"Item {idx} type: {type(div)} - Content: {div}")
        
    for div in tqdm(card_divs):
        try:
            # Check if div is a WebElement, otherwise skip
            # if isinstance(div, dict):
            #     print("Unexpected dict found, skipping this item")
            #     continue
            # Wait to ensure content within div is fully loaded
            time.sleep(0.5)
            ele = div.values()
            # Attempt to locate the name within the h2 element
            name_element = ele.find_element(By.CLASS_NAME, "name-given")
            name = name_element.text
            print("\nName Found:", name)
        except NoSuchElementException:
            print("\nName not found in this card div (name-given class missing)")
        except Exception as e:
            print(f"\nAn error occurred: {e}")

# Wait for 5 seconds


# Print the title of the page

# Close the Opera browser window
driver.quit()  # Close the Opera browser window
print("Opera Session-6 closed")
