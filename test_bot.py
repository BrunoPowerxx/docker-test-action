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

        page.goto(URL)
        page.wait_for_load_state("load")
        homepage = page.query_elements(SPORTS_PAGE)
        games_cont = homepage.league_container.match_containers
        links = []
        for index in range(len(games_count)):
            print("Before click:", page.url)
            game = homepage.league_container.match_containers[index].home
            home.click()
            page.wait_for_load_state("load")
            print("After click:", page.url)
            link = page.url
            links.append(link)
            page.go_back()
            page.wait_for_load_state("load")
        for link in links:
            
            print("Collected URL:", link)
        #print(f"loop took {end_time - start_time}")

    display.stop()