from concurrent.futures import ThreadPoolExecutor
from agentql.ext.playwright.sync_api import Page
from playwright.sync_api import sync_playwright
from pyvirtualdisplay import Display
from datetime import datetime 
import pandas as pd
import agentql
import random
import json
import time

# Set up logging

# Set the URL to the desired website

def test_main():
    urls = [
    "https://www.supabets.co.za/",
    "https://www.betway.co.za/sport"
    ]
    with ThreadPoolExecutor() as executor:
        # Map the scrape_data function to the list of URLs
        results = list(executor.map(scraper, urls))
        with open('match_data.json', 'w') as json_file:
            json.dump(results, json_file, indent=4)
  
def scraper(url):
    display = Display(visible=False, size=(1920, 1080))
    display.start()
    with sync_playwright() as p, p.chromium.launch(headless=False) as browser:
        # Create a new page in the browser and wrap it to get access to the AgentQL's querying API
        page = agentql.wrap(browser.new_page())

        # Navigate to the desired URL
        page.goto(url)
        time.sleep(3)
        timestamp = datetime.now().strftime('%Y%m%d_%H%M%S')
        filename = f"screenshot_{timestamp}.png"
        page.screenshot(path=f"/app/shots/{filename}", full_page=True)
        get_response(page)
        time.sleep(1)
        browser.close()
    display.stop

def get_response(page: Page):

    SPORTS_PAGE = """
{
  league_group_container {
    match_containers[] {
      league
      home
      away
      day
    }
  }
}
    """
    
    ODDS_PAGE = """
{
  page_url
  team_names(home v away)
  markets[] {
      market_name
      odd_type
      odd_value(decimal) 
      implied_probability(reciprocal of odds_value rounded to 2 decimal places)
  }
}
    """

    #page.screenshot(path="app/shots/before.png", full_page=True)
    time.sleep(1)
    #homepage = page.query_elements(SPORTS_PAGE)
    #matches = []
    #print(homepage)
    match_cont = len(homepage.league_group_container.match_containers)
    #counter = 0
'''   for index in range(match_cont):
        home_locator = homepage.league_group_container.match_containers[index].more
        home_class = home_locator.get_attribute("class")  # Get class attribute if needed
        #home_locator.click()
        #page.screenshot(path=f"/app/shots/supa_{index}.png", full_page=True)

        event = page.query_data(ODDS_PAGE)
        #ties = elements.league_group_container.league_containers.home[0:5]
        
        if event:
            matches.append(event)
        time.sleep(1)
        page.go_back()
        time.sleep(2)
    # Save data to a JSON file
'''
