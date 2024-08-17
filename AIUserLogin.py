from playwright.sync_api import Playwright, sync_playwright, expect
from datetime import datetime


def run(playwright: Playwright) -> None:
    #creates browser
    browser = playwright.chromium.launch(headless=False)
    #makes browser linked so that any extra pages one page opens are connected
    context = browser.new_context()
    page = context.new_page()
    #grants microphone permission to get past popup
    context.grant_permissions(["microphone"])
    #goes to page
    page.goto("https://chadwellcon.maxcontact.com/ManagerPortal/Home/Login")
    #login info
    page.get_by_placeholder("Username").click()
    page.get_by_placeholder("Username").fill("AIAgent")
    page.get_by_placeholder("Password").click()
    page.get_by_placeholder("Password").fill("AIuser123!")
    page.get_by_placeholder("Password").press("Enter")
    #finds campaign (can be adjusted if fail during testing)
    with page.expect_popup() as page1_info:
        page.locator("#campaign_53 span").click()
    page1 = page1_info.value
    #once button available presses go ready
    page.get_by_role("button", name="Go Ready!").click()
    #while loop to stop browser from closing
    running=True
    while(running):
        #closes browser at 6pm
        if(datetime.strftime("%H")>=18):
            running=False

            
    

    # ---------------------
    context.close()
    browser.close()


with sync_playwright() as playwright:
    run(playwright)
