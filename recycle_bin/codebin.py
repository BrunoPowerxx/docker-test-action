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


from pyvirtualdisplay import Display
import json
import time
import pandas as pd
import agentql
from agentql.ext.playwright.sync_api import Page
from playwright.sync_api import sync_playwright
import pytest

# Set the URL to the desired website
URL = "https://www.supabets.co.za/"


def test_main():
    display = Display(visible=False, size=(1920, 1080))
    display.start()
    with sync_playwright() as p, p.chromium.launch(headless=False) as browser:
        # Create a new page in the browser and wrap it to get access to the AgentQL's querying API
        page = agentql.wrap(browser.new_page())
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
        # Navigate to the desired URL
        #page.route("**", intercept_route)
        page.goto(URL)
        print(page.content())
        page.wait_for_load_state("load")
        page.screenshot(path="/app/shots/before.png", full_page=True)
        homepage = page.query_elements(SPORTS_PAGE)
        home_teams = homepage.league_group_container.match_containers
        #get_response(page)
        start_time = time.perf_counter()
        supa_links = []
        for index in range(len(home_teams)):
            home_teams[index].home.click()
            page.wait_for_load_state("load")
# Store the new page object and URL
            link = page.url

            page.screenshot(path=f"/app/shots/img_{index}.png", full_page=True)
            supa_links.append(link)
            page.goto(URL)
            page.wait_for_load_state("load")

#time.sleep(2)

        end_time = time.perf_counter()
        for index, link in enumerate(supa_links):
            print(f"Page {index}: {link}")


        browser.close()
    display.stop
    print(f"for loop executed in {end_time - start_time:.2f} seconds")


from playwright.sync_api import sync_playwright
from agentql.ext.playwright.sync_api import Page
from pyvirtualdisplay import Display
import pytest
import agentql
import json
import time

def test_requests():
    def intercept_route(route):  
        request = route.request  
        request_log.append(request.url)  # Append URL to list
        route.continue_()  

    request_log = []  # List to store all request URLs

    display = Display(visible=False, size=(1920, 1080))  
    display.start()  

    with sync_playwright() as p, p.chromium.launch(headless=False) as browser:
        context = browser.new_context()
        page = agentql.wrap(context.new_page())

        # Intercept all network requests
        page.route("**", intercept_route)

        # Load the page completely
        page.goto("https://www.supabets.co.za/", wait_until="networkidle")

        browser.close()
    display.stop()

    # Save network requests to a JSON file
    with open("network_requests.json", "w") as file:
        json.dump(request_log, file, indent=2)

    print("Network requests saved to network_requests.json")

if __name__ == "__main__":
    test_requests()
