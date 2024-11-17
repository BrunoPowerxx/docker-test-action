from playwright.sync_api import sync_playwright
from pyvirtualdisplay import Display
from collections import namedtuple
from phunctions import *
from klasses import *
import pandas as pd
import pytest
import time
import agentql

URL = "https://new.hollywoodbets.net/"

QUERY = """
{
    cookies_form {
        reject_btn
    }
}
"""

def test_supaholly():
    display = Display(visible=False, size=(1920, 1080))
    display.start()
    display_on()

    with sync_playwright() as p:
      browser = p.chromium.launch(headless=False)
      page = agentql.wrap(browser.new_page())
      page.goto(URL)


      browser.close()

    display_off(display)

# Set the URL to the desired website



