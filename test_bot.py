from playwright.async_api import async_playwright
from pyvirtualdisplay import Display
from time import perf_counter
import concurrent.futures
import pandas as pd
import agentql
import random
import asyncio
import pytest
import json
import time

SPORTS_PAGE = """
{  league_container {
    match_containers[] {
      league
      home
      away
      day
    }
  }
}        """
URL = "https://www.supabets.co.za"

async def click_game(game, browser):
        context_2 = await browser.new_context()
        subpage = agentql.wrap(await context_2.new_page())
        await subpage.goto(URL, wait_until="networkidle")
        await game.click()
        result_url = subpage.url  # Extract the navigated URL
        await subpage.close()
        
        return result_url

async def supabets_urls():
    display = Display(visible=False, size=(1920, 1080))
    display.start()

    async with async_playwright() as p:
        browser = await  p.chromium.launch(headless=False)
        context = await browser.new_context()
        page = agentql.wrap(await context.new_page())

        await page.goto(URL, wait_until="networkidle")
        homepage = await  page.query_elements(SPORTS_PAGE)
        games_cont = homepage.league_container.match_containers
        games = [homepage.league_container.match_containers[i].home for i in range(len(games_cont))]
        links = []
        for game in games:
            await game.click()
            link = page.url
            links.append(link)
            page.go_back()
        for link in links:
            
            print("Collected URL:", link)
        #print(f"loop took {end_time - start_time}")

    display.stop()

def test_links():
    asyncio.run(supabets_urls())