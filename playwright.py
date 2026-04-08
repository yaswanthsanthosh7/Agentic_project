# app/tools/playwright_tools.py

from playwright.sync_api import sync_playwright

class PlaywrightManager:

    def __enter__(self):
        self.p = sync_playwright().start()
        self.browser = self.p.chromium.launch(headless=True)
        self.page = self.browser.new_page()
        return self.page

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.browser.close()
        self.p.stop()


# app/tools/transport_scraper.py

#from playwright_tools import PlaywrightManager

def search_redbus(from_city: str, to_city: str):
    with PlaywrightManager() as page:
        page.goto("https://www.redbus.in")

        page.fill("#src", from_city)
        page.fill("#dest", to_city)

        page.keyboard.press("Enter")
        page.wait_for_timeout(5000)

        buses = page.query_selector_all(".bus-item")

        results = []
        for bus in buses[:5]:
            text = bus.inner_text()
            results.append(text)

        return "\n".join(results) if results else "No buses found"

def get_uber_info():
    with PlaywrightManager() as page:
        page.goto("https://www.uber.com/in/en/")
        return page.title()