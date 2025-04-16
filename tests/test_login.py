import time
import os
import sys
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))
import pytest
from dotenv import load_dotenv
from playwright.sync_api import Playwright, sync_playwright, expect
from steps.steps_login import login, confirm_login, confirm_user_locked, confirm_invalid_information

load_dotenv()

unactivated_account_username = os.getenv("UNACTIVATED_ACCOUNT_USERNAME")
unactivated_account_password = os.getenv("UNACTIVATED_ACCOUNT_PASSWORD")
activated_account_username = os.getenv("ACTIVATED_ACCOUNT_USERNAME")
activated_account_password = os.getenv("ACTIVATED_ACCOUNT_PASSWORD")
locked_account_username = os.getenv("LOCKED_ACCOUNT_USERNAME")
locked_account_password = os.getenv("LOCKED_ACCOUNT_PASSWORD")



BASE_URL = os.getenv("BASE_URL")
if BASE_URL:
    BASE_URL = f"{BASE_URL}"
else:
    raise ValueError("BASE_URL not set in .env file.")


LOGIN_URL = os.getenv("LOGIN_URL")
if LOGIN_URL:
    LOGIN_URL = f"{LOGIN_URL}"
else:
    raise ValueError("LOGIN_URL not set in .env file.")

# Browser launching

@pytest.fixture(scope="session")
def browser():
    with sync_playwright() as playwright:
        browser = playwright.chromium.launch(executable_path="/Applications/Google Chrome.app/Contents/MacOS/Google Chrome",
                                        headless=False
                                        )
        yield browser
        browser.close()

@pytest.fixture(scope="function")
def page(browser):
    context = browser.new_context()

    page = context.new_page()
    page.goto(f"{LOGIN_URL}")

    yield page

    page.close()
    context.close()




@pytest.mark.parametrize(
    "username, password",
    [
        (activated_account_username, activated_account_password)
    ]
)
def test_activated_account_login(page, username, password):

    time.sleep(2)

    login(page, username, password)

    time.sleep(2)

    confirm_login

    time.sleep(2)



@pytest.mark.parametrize(
    "username, password",
    [
        (unactivated_account_username, unactivated_account_password)
    ]
)
def test_unactivated_account_login(page, username, password):

    time.sleep(2)

    login(page, username, password)

    time.sleep(2)

    confirm_invalid_information(page)

    time.sleep(2)



@pytest.mark.parametrize(
    "username, password",
    [
        ("nepostojiovajaccountjuraj", "nekipassword")
    ]
)
def test_unregistered_account_login(page, username, password):

    time.sleep(2)

    login(page, username, password)

    time.sleep(2)

    confirm_invalid_information(page)

    time.sleep(2)




@pytest.mark.parametrize(
    "username, password",
    [
        (locked_account_username, locked_account_password)
    ]
)
def test_is_user_locked(page, username, password):

    time.sleep(2)

    login(page, username, password)

    time.sleep(2)

    confirm_user_locked(page)

    time.sleep(2)




@pytest.mark.parametrize(
    "username, password",
    [
        (activated_account_username, activated_account_password)
    ]
)
def test_is_username_case_sensitive(page, username, password):

    time.sleep(2)

    login(page, username.upper(), password)

    time.sleep(2)

    confirm_login(page, username)

    time.sleep(2)

