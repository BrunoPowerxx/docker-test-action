from playwright.sync_api import sync_playwright
from agentql.ext.playwright.sync_api import Page
from pyvirtualdisplay import Display
import pytest
import agentql
import json
import time

from playwright.sync_api import sync_playwright
from agentql.ext.playwright.sync_api import Page
from pyvirtualdisplay import Display
import json

def test_requests():
    def intercept_route(route):  
        request = route.request  
        request_log.append(request.url)  # Append URL to list
        route.continue_()  

    request_log = []  # List to store all request URLs

    display = Display(visible=False, size=(1920, 1080))  
    display.start()  

    with sync_playwright() as p, p.chromium.launch(headless=True) as browser:
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
