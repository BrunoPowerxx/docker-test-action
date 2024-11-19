from playwright.sync_api import sync_playwright
from pyvirtualdisplay import Display
from collections import namedtuple
from phunctions import *
from klasses import *
import pandas as pd
import pytest
import time
import agentql
#from dotenv import load_dotenv



def test_supaholly():
    #load_dotenv()
    #os.getenv('AGENTQL_API_KEY', default=None)

    URL = "https://new.hollywoodbets.net/"

    QUERY = """
    {
        popup_form {
            close_btn
        }
    }
    """
    
    display = Display(visible=False, size=(1920, 1080))
    display.start()
    display_on()

    with sync_playwright() as p:
        
        browser = p.chromium.launch(headless=False)
        page = agentql.wrap(browser.new_page())
        page.goto(URL)
        page.wait_for_timeout(5000)
        page.screenshot(path="shot1.png", full_page=True)
        response = page.query_elements(QUERY)
        response.popup_form.close_btn.click()
        page.wait_for_timeout(5000)
        page.screenshot(path="shot2.png", full_page=True)

        browser.close()

    display_off(display)
