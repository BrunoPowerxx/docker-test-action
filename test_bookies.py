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
    display = Display(visible=False, size=(1920, 1080))
    display.start()
    display_on()
    host = "41.13.10.77"
    port = "8080"
    with sync_playwright() as p:        
        browser = p.chromium.launch(headless=False,                        proxy={"server": f"http://{host}:{port}"})
        #page = agentql.wrap(browser.new_page())
        page = browser.new_page()

        page.goto("https://whatmyuseragent.com/")
        page.wait_for_timeout(5000)
        page.screenshot(path="mua.png", full_page=True)

        page.goto("https://www.new.hollywoodbets.net/")
        page.wait_for_timeout(5000)
        page.screenshot(path="hwb.png", full_page=True)

        page.goto("https://www.betus.com.pa/sportsbook/")
        page.wait_for_timeout(5000)
        page.screenshot(path="bus.png", full_page=True)

        page.goto("https://sports.betmgm.com/en/sports")
        page.wait_for_timeout(5000)
        page.screenshot(path="mgm.png", full_page=True)

        page.goto("https://sportsbook.draftkings.com/")
        page.wait_for_timeout(5000)
        page.screenshot(path="dfk.png", full_page=True)         

        time.sleep(5)
        browser.close()

    display_off(display)