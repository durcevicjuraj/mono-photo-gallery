import time
from playwright.sync_api import Page, expect

def login(page: Page, email: str, password: str) -> None:
    
    page.get_by_role("textbox", name="Enter your email or username").click()
    page.get_by_role("textbox", name="Enter your email or username").fill(email)

    time.sleep(2)

    page.get_by_role("textbox", name="Password").click()
    page.get_by_role("textbox", name="Password").fill(password)

    time.sleep(2)

    page.get_by_role("button", name="Login").click()

def confirm_login(page: Page, expected_username: str)-> None:

    username_element = page.locator("xpath=/html/body/app/master-layout/div/main/div/loader-component/div/profile-detail/baasic-album-list/div/div/div[1]/h2")

    time.sleep(2)

    expect(username_element).to_have_text(expected_username)

def confirm_user_locked(page: Page) ->None:

    expect(page.get_by_text("User is locked.")).to_be_visible()

def confirm_invalid_information(page: Page) -> None:

    expect(page.get_by_text("Invalid email, username or password")).to_be_visible()


