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
{
   league_group_container {
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
        page.screenshot(path="before.png", full_page=True)
        homepage = page.query_elements(SPORTS_PAGE)
        links = []
        more_markets = page.locator("div.more-markets a").first
        # Get the href attribute
        link = more_markets.get_attribute("href")
        if link:
            print("Extracted link:", link)
        if more_markets:
            more_markets.click()
            print("After click:", page.url)

        #game = homepage.league_group_container.match_containers[0].home
        #game.click()
        page.wait_for_load_state("load")
        page.screenshot(path="after.png", full_page=True)

    display.stop()