from playwright.sync_api import sync_playwright
from pyvirtualdisplay import Display
from time import perf_counter
import concurrent.futures
import pandas as pd
import agentql
import random
import pytest
import json
import time

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


def test_supabets():
    display = Display(visible=False, size=(1920, 1080))
    display.start()

    with sync_playwright() as p:
        
        browser = p.chromium.launch(headless=False)
        context = browser.new_context()
        page = agentql.wrap(context.new_page())

        page.goto(URL, wait_until="networkidle")
        homepage = page.query_elements(SPORTS_PAGE)
        games_cont = homepage.league_container.match_containers
        games = [homepage.league_container.match_containers[i].home for i in range(len(games_cont))]
        links = []
        for game in games:
            game.click()
            page.wait_for_load_state("networkidle")
            link = page.url
            links.append(link)
            page.go_back()
            page.wait_for_load_state("networkidle")
        for link in links:
            
            print("Collected URL:", link)
        #print(f"loop took {end_time - start_time}")

    display.stop()