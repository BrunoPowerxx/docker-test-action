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
        page.goto(URL)
        page.wait_for_load_state("networkidle")
        page.screenshot(path="before.png", full_page=True)
        homepage = page.query_elements(SPORTS_PAGE)
        home_teams = homepage.league_group_container.match_containers
        #get_response(page)
        for index, team in enumerate(home_teams):
            home = homepage.league_group_container.match_containers[index].home
            home.click(button="right")
            page.screenshot(path=f"img_{index}.png", full_page=True)
            time.sleep(2)
        browser.close()
    display.stop
