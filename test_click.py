from pyvirtualdisplay import Display
import json
import time
import pandas as pd
import agentql
from agentql.ext.playwright.sync_api import Page
from playwright.sync_api import sync_playwright
import pytest

# Set the URL to the desired website
URL = "https://www.supabets.co.za/"


def test_main():
    display = Display(visible=False, size=(1920, 1080))
    display.start()
    with sync_playwright() as p, p.chromium.launch(headless=False) as browser:
        # Create a new page in the browser and wrap it to get access to the AgentQL's querying API
        page = agentql.wrap(browser.new_page())
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
        # Navigate to the desired URL
        #page.route("**", intercept_route)
        page.goto(URL)
        page.wait_for_load_state("networkidle")
        page.screenshot(path="/app/shots/before.png", full_page=True)
        homepage = page.query_elements(SPORTS_PAGE)
        home_teams = homepage.league_group_container.match_containers
        #get_response(page)
        start_time = time.perf_counter()
        supa_links = []
        for index, team in enumerate(home_teams):
            #new_page = browser.new_page()  # Open a new tab
            page.wait_for_load_state("networkidle")
            team.click()
# Store the new page object and URL
            link = page.url

            new_page.screenshot(path=f"/app/shots/img_{index}.png", full_page=True)
            supa_links.append(link)
            #new_page.close()

#time.sleep(2)

        end_time = time.perf_counter()
        for index, link in enumerate(supa_links):
            print(f"Page {index}: {link}")

            
       browser.close()
    display.stop
    print(f"for loop executed in {end_time - start_time:.2f} seconds")