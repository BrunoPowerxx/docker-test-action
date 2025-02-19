from playwright.sync_api import sync_playwright
from pyvirtualdisplay import Display
from time import perf_counter
import concurrent.futures
import pandas as pd
import agentql
import random
import pytest
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
URL = "https://www.supabets.co.za"

def click_game(game, context_2):
        subpage = agentql.wrap(context_2.new_page())
        subpage.goto(URL, wait_until="networkidle")
        game.click()
        result_url = subpage.url  # Extract the navigated URL
        subpage.close()
        
        return result_url

def test_supah():
    display = Display(visible=False, size=(1920, 1080))
    display.start()

    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False)
        context = browser.new_context()
        page = agentql.wrap(context.new_page())

        page.goto(URL, wait_until="networkidle")
        homepage = page.query_elements(SPORTS_PAGE)
        games_count = len(homepage.league_group_container.match_containers)
        games = [homepage.league_group_container.match_containers[i].home for i in range(games_count)]

        context_2 = browser.new_context()
        start_time = time.perf_counter()
        
        with concurrent.futures.ThreadPoolExecutor() as executor:
            results = list(executor.map(lambda game: click_game(game, context_2), games))

        end_time = perf_counter()
        for result in results:
            
            print("Collected URL:", result)
        print(f"loop took {end_time - start_time}")

    display.stop()