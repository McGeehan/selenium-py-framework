import os
import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from config import settings
from dotenv import load_dotenv

load_dotenv(override=True)

def build_options():
    opts = Options()
    if settings.HEADLESS:
        opts.add_argument("--headless=new")
    if settings.NO_SANDBOX:
        opts.add_argument("--no-sandbox")
    if settings.DISABLE_DEV_SHM:
        opts.add_argument("--disable-dev-shm-usage")
        opts.add_argument(f"--window-size={settings.WINDOW_SIZE}")
        opts.add_argument("--disable-gpu")
        return opts

@pytest.fixture
def driver():
    opts = build_options()
    driver = webdriver.Chrome(options=opts)
    yield driver
    driver.quit()
