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
from pyvirtualdisplay import Display
import json
import time
import pandas as pd
import agentql
from agentql.ext.playwright.sync_api import Page
from playwright.sync_api import sync_playwright
import pytest
# Set up logging

# Set the URL to the desired website
URL = "https://www.supabets.co.za/"


def test_main():
    display = Display(visible=False, size=(1920, 1080))
    display.start()
    with sync_playwright() as p, p.chromium.launch(headless=False) as browser:
        # Create a new page in the browser and wrap it to get access to the AgentQL's querying API
        page = agentql.wrap(browser.new_page())

        # Navigate to the desired URL
        page.goto(URL)
        time.sleep(5)
        page.screenshot(path="before.png", full_page=True)
        get_response(page)
        time.sleep(5)
        browser.close()
    display.stop

def get_response(page: Page):

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
}
    """
    ODDS_PAGE = """
{
  subevent_details {
    match_tracker {
      home_v_away
      day
      time
    }
    list_cgq {
      all
      popular
    }
    subevent_panel {
      head_to_head(1x2) {
        market_type
        home {
          odd_type
          odd_value
        }
        draw {
          odd_type
          odd_value
        }
        away {
          odd_type
          odd_value
        }
      }
      first_goal("1st goal", odds values) {
        market_type
        None {
          odd_type
          odd_value
        }
        home {
          odd_type
          odd_value
        }
        away {
          odd_type
          odd_value
        }
      }
      first_half_first_goal {
        market_type
        None {
          odd_type
          odd_value
        }
        home {
          odd_type
          odd_value
        }
        away {
          odd_type
          odd_value
        }
      }
      first_half_away_over_under(0.5, odds vales) {
        market_type
        over {
          odd_type
          odd_value
        }
        under {
          odd_type
          odd_value
        }
      }
    }
  }
}"""

    #page.screenshot(path="hwb.png", full_page=True)
    time.sleep(1)
    homepage = page.query_elements(SPORTS_PAGE)
    matches = []
    #print(homepage)
    match_cont = len(homepage.league_group_container.match_containers)
    #counter = 0
    for index in range(match_cont):
        home_locator = homepage.league_group_container.match_containers[index].home
        home_class = home_locator.get_attribute("class")  # Get class attribute if needed
        home_locator.click()
        #page.screenshot(path=f"swb_{index}.png", full_page=True)

        event = page.query_data(ODDS_PAGE)
        #ties = elements.league_group_container.league_containers.home[0:5]

        if event:  # Ensure event data is not empty

            print(event)
            #print(event)
        time.sleep(1)
        page.go_back()
        time.sleep(3)'''