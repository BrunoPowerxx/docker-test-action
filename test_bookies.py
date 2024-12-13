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
    URL = ["https://whatmyuseragent.com/", "https://www.betus.com.pa/sportsbook/", "https://sports.betmgm.com/en/sports"]
    display = Display(visible=False, size=(1920, 1080))
    display.start()
    display_on()
    with sync_playwright() as p:        
        browser = p.chromium.launch(headless=False)
        page = agentql.wrap(browser.new_page())
        for index in range(len(URL)):
            page.goto(URL[index])
            page.wait_for_timeout(10000)
            page.screenshot(path=f"/app/screenshots/shot{index + 1}.png", full_page=True)
            time.sleep(5)
        browser.close()

    display_off(display)