from playwright.sync_api import sync_playwright
from pyvirtualdisplay import Display
import concurrent.futues
import pandas as pd
import agentql
import random
import pytest
import time
import json

SPORTS_PAGE = """
{  league_container {
    match_containers[] {
      league
      home
      away
      day
    }
  }
}        """
URL = "https.supabets.co.za"


def click_game(game):
    """Opens a new page, clicks the game, and stores the resulting URL."""
    with sync_playwright() as p, p.chromium.launch(headless=False) as subbrowser:        # Create a new page in the browser and wrap it to get access to the AgentQL's querying API
        subpage = agentql.wrap(subbrowser.new_page())
        subpage.goto(URL, wait_until="networkidle")
        game.click()
        result_url = subpage.url  # Extract the navigated URL
        results.append(result_url)
        browser.close()
        
        return results
def test_supah():
    display = Display(visible=False, size=(1920, 1080))
    display.start()

    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False)
        context = browser.new_context()
        page = agentql.wrap(context.new_page())

        page.goto(URL, wait_until="networkidle")
        homepage = page.query_elements(SPORTS_PAGE)
        home_locator = homepage.league_group_container.match_containers.home
        games = home_locator.query_selector_all()
        results = []
        start_time = time.perf_counter()
        #Click each game link in a separate browser instance
        with concurrent.futures.ThreadPoolExecutor() as executor:
            results = list(executor.map(click_game, games))
        end_time = perf_counter()
        for result in results:
            
            print("Collected URL:", result)
        print(f"loop took {end_time - start_time}")

    display.stop()