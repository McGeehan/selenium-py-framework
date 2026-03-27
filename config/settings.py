import os
BASE_URL = os.getenv("BASE_URL", 
"https://www.selenium.dev/selenium/web/web-form.html")
# Chrome flags tuned for Linux VMs and CI containers
HEADLESS = os.getenv("HEADLESS", "true").lower() == "true"
NO_SANDBOX = os.getenv("NO_SANDBOX", "true").lower() == "true"
DISABLE_DEV_SHM = os.getenv("DISABLE_DEV_SHM", "true").lower() == 
"true"
WINDOW_SIZE = os.getenv("WINDOW_SIZE", "1920,1080")