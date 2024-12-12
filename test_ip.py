

def rest_supaholly():
    URL = "https://whatmyuseragent.com/"
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
        page.wait_for_timeout(10000)
        page.screenshot(path="before.png", full_page=True)
        response = page.query_elements(QUERY)
        if response.popup_form.close_btn != None:
            response.popup_form.close_btn.click()

        page.wait_for_timeout(10000)

        page.screenshot(path="after.png", full_page=True)
        time.sleep(5)
        browser.close()

    display_off(display)