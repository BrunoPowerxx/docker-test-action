from playwright.sync_api import sync_playwright
from chrome_extension_python import Extension
from pyvirtualdisplay import Display
from collections import namedtuple
from phunctions import *
from klasses import *
import pandas as pd
import agentql
import random
import pytest
import time

def test_user():
    URL = "https://whatmyuseragent.com/"
    display = Display(visible=False, size=(1920, 1080))
    display.start()
    display_on()
    with sync_playwright() as p:        
        browser = p.chromium.launch(headless=False)
        page = agentql.wrap(browser.new_page())
        page.goto(URL)
        page.wait_for_timeout(10000)
        page.screenshot(path="ua.png", full_page=True)
        time.sleep(5)
        browser.close()

    display_off(display)