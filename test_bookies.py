from playwright.sync_api import sync_playwright
from pyvirtualdisplay import Display
from collections import namedtuple
from phunctions import *
from klasses import *
import pandas as pd
import agentql
import random
import pytest
import time


def test_bookies():
    URL = ["https://whatmyuseragent.com/", "https://www.betus.com.pa/sportsbook/", "https://sports.betmgm.com/en/sports", "https://sportsbook.draftkings.com/"]
    display = Display(visible=False, size=(1920, 1080))
    display.start()
    display_on()
    with sync_playwright() as p:        
        browser = p.chromium.launch(headless=False)

        #page = agentql.wrap(browser.new_page())
        page = browser.new_page()

        page.goto("https://whatmyuseragent.com/")
        page.wait_for_timeout(5000)
        page.screenshot(path=f"/app/screenshots/mua.png", full_page=True)

        page.goto("https://www.betus.com.pa/sportsbook/")
        page.wait_for_timeout(5000)
        page.screenshot(path=f"/app/screenshots/bus.png", full_page=True)

        page.goto("https://sports.betmgm.com/en/sports")
        page.wait_for_timeout(5000)
        page.screenshot(path=f"/app/screenshots/mgm.png", full_page=True)

        page.goto("https://sportsbook.draftkings.com/")
        page.wait_for_timeout(5000)
        page.screenshot(path=f"/app/screenshots/dfk.png", full_page=True)         

        time.sleep(5)
        browser.close()

    display_off(display)