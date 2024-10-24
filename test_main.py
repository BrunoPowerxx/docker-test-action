from playwright.sync_api import sync_playwright
from pyvirtualdisplay import Display
from collections import namedtuple
from Functions import *
from Classes import *
import pytest
import time


def test_supaholly():
    display = Display(visible=False, size=(1920, 1080))
    display.start()
    display_on()

    with sync_playwright() as p:
      browser = p.chromium.launch(headless=False)
      context = browser.new_context()

      supa = context.new_page()
      holly = context.new_page()

      goto_sb(supa)
      get_sb(supa)

      goto_hwb(holly)
      get_hwb(holly)
      
      arbs()
      
      #print_hbgames()
      #print_sbgames()

      browser.close()

    display_off()
