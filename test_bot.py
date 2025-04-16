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

def test_main():
    urls = [
    "https://www.supabets.co.za/"
    ]
    POPUP = """
{
    popup {
        home_btn
        close_btn
    }
}
"""
    with ThreadPoolExecutor() as executor:
        results = list(executor.map(scraper, urls))
        with open('match_data.json', 'w') as json_file:
            
            json.dump(results, json_file, indent=4)
  
def scraper(url):
    display = Display(visible=False, size=(1920, 1080))
    display.start()
    with sync_playwright() as p, p.chromium.launch(headless=False) as browser:
        page = agentql.wrap(browser.new_page())
        page.goto(url)
        time.sleep(3)
        try:
            response = page.query_elements(POPUP)
            if close_button:
                response.popup.close_btn.click()
                time.sleep(1)
        except:
            pass
        time.sleep(1)
        get_response(page)
        time.sleep(1)
        print(matches)
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
  }
}
    """
    time.sleep(1)
    homepage = page.query_elements(SPORTS_PAGE)
    matches = []
    match_cont = len(homepage.league_group_container.match_containers)
    for index in range(match_cont):
        home_locator = homepage.league_group_container.match_containers[index].home
        home_class = home_locator.get_attribute("class")  # Get class attribute if needed
        home_locator.click() 
        time.sleep(1)
        event = page.query_data(ODDS_PAGE)
        
        if event:
            matches.append(event)
        time.sleep(1)
        page.go_back()
        time.sleep(2)
    return matches
    # Save data to a JSON file
