from playwright.sync_api import sync_playwright

def run():
    with sync_playwright() as p:
        browser = p.chromium.launch()
        page = browser.new_page()
        page.goto("file:///app/index.html")
        page.wait_for_timeout(1000)
        page.screenshot(path="dashboard_new.png")

        # Click Campaigns
        page.evaluate("document.querySelectorAll('.nav-item')[1].click()")
        page.wait_for_timeout(500)
        page.screenshot(path="campaigns_new.png")

        # Click Tasks
        page.evaluate("document.querySelectorAll('.nav-item')[3].click()")
        page.wait_for_timeout(500)
        page.screenshot(path="tasks_new.png")

        browser.close()

if __name__ == "__main__":
    run()
