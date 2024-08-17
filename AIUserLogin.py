from playwright.sync_api import Playwright, sync_playwright, expect


def run(playwright: Playwright) -> None:
    browser = playwright.chromium.launch(headless=False)
    context = browser.new_context()
    page = context.new_page()
    context.grant_permissions(["microphone"])
    page.goto("https://chadwellcon.maxcontact.com/ManagerPortal/Home/Login")
    page.get_by_placeholder("Username").click()
    page.get_by_placeholder("Username").click()
    page.get_by_placeholder("Username").fill("AIAgent")
    page.get_by_placeholder("Password").click()
    page.get_by_placeholder("Password").fill("AIuser123!")
    page.get_by_placeholder("Password").press("Enter")
    with page.expect_popup() as page1_info:
        page.locator("#campaign_53 span").click()
    page1 = page1_info.value
    page.get_by_role("button", name="Go Ready!").click()

    # ---------------------
    context.close()
    browser.close()


with sync_playwright() as playwright:
    run(playwright)
