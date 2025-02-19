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
        game.click()
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

        #context_2 = browser.new_context()
        start_time = time.perf_counter()

        tasks = [click_game_async(game, browser) for game in games]
        results = await asyncio.gather(*tasks)
 
        
        #with concurrent.futures.ThreadPoolExecutor() as executor:
            #results = list(executor.map(lambda game: click_game(game, context_2), games))

        end_time = perf_counter()
        for result in results:
            
            print("Collected URL:", result)
        print(f"loop took {end_time - start_time}")

    display.stop()