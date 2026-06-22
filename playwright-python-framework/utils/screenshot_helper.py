from datetime import datetime
import os


def save_screenshot(page, test_name):
    os.makedirs("screenshots", exist_ok=True)
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    path = f"screenshots/{test_name}_{timestamp}.png"
    page.screenshot(path=path, full_page=True)
    return path