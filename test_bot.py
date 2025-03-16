from pyvirtualdisplay import Display
import json
import time
import pandas as pd
import agentql
from agentql.ext.playwright.sync_api import Page
from playwright.sync_api import sync_playwright
import pytest
# Set up logging

# Set the URL to the desired website
#URL = "https://www.supabets.co.za/"
URL = "https://www.betway.co.za/sport"

def test_main():
    display = Display(visible=False, size=(1920, 1080))
    display.start()
    with sync_playwright() as p, p.chromium.launch(headless=False) as browser:
        # Create a new page in the browser and wrap it to get access to the AgentQL's querying API
        page = agentql.wrap(browser.new_page())

        # Navigate to the desired URL
        page.goto(URL)
        time.sleep(5)
        #page.screenshot(path="/app/shots/before.png", full_page=True)
        get_response(page)
        time.sleep(5)
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
    homepage = page.query_elements(SPORTS_PAGE)
    matches = []
    #print(homepage)
    match_cont = len(homepage.league_group_container.match_containers)
    #counter = 0
    for index in range(match_cont):
        home_locator = homepage.league_group_container.match_containers[index].home
        home_class = home_locator.get_attribute("class")  # Get class attribute if needed
        home_locator.click()
        #page.screenshot(path=f"/app/shots/supa_{index}.png", full_page=True)

        event = page.query_data(ODDS_PAGE)
        #ties = elements.league_group_container.league_containers.home[0:5]
        
        if event:  # Ensure event data is not empty

            print(event)
            print(page.url)
        time.sleep(1)
        page.go_back()
        time.sleep(3)
