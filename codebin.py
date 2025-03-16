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

URL = "https://www.supabets.co.za"
'''
def test_supabets():
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
        
        home_loc = homepage.league_group_container.match_containers[0].home
        if home_loc:
            home_class = home_loc.get_attribute("class")
            home_loc.click()
            page.wait_for_load_state("load")
            print("After click:", page.url)
            page.screenshot(path="after.png", full_page=True)

        #game = homepage.league_group_container.match_containers[0].home
        #game.click()
        browser.close
    display.stop()
'''
