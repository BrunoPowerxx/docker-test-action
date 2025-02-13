from playwright.sync_api import sync_playwright
from agentql.ext.playwright.sync_api import Page
from pyvirtualdisplay import Display
import pytest
import agentql

def test_requests(url):
    def intercept_route(route):  # Playwright automatically provides `route`
        request = route.request  # Get the request object
        print(request.url)  # Print the full request URL
        route.continue_()   # Let the request proceed

    with sync_playwright() as p, p.chromium.launch(headless=False) as browser:
        context = browser.new_context()
        page = agentql.wrap(context.new_page())

        # Intercept all network requests
        page.route("**", intercept_route)

        # Load the page completely
        page.goto("https://www.supabets.co.za/", wait_until="networkidle")

        browser.close()