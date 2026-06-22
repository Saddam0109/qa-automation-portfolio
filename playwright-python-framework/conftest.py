import os
import pytest
import allure
from playwright.sync_api import sync_playwright
from config.config import load_environment
from utils.screenshot_helper import save_screenshot
from utils.logger import get_logger

logger = get_logger()


def pytest_addoption(parser):
    parser.addoption(
        "--browser-name",
        action="store",
        default="chromium",
        help="Browser: chromium, firefox, webkit"
    )
    parser.addoption(
        "--env",
        action="store",
        default="qa",
        help="Environment: qa, staging"
    )


@pytest.fixture(scope="session")
def config(request):
    os.environ["TEST_ENV"] = request.config.getoption("--env")
    return load_environment()


@pytest.fixture(scope="function")
def page(request, config):
    browser_name = request.config.getoption("--browser-name")

    if browser_name not in ["chromium", "firefox", "webkit"]:
        raise ValueError(f"Unsupported browser: {browser_name}")

    with sync_playwright() as p:
        browser_launcher = getattr(p, browser_name)
        browser = browser_launcher.launch(headless=config["headless"])
        context = browser.new_context()
        page = context.new_page()
        page.goto(config["base_url"])
        logger.info(f"Opened application: {config['base_url']} on {browser_name}")
        yield page
        browser.close()


@pytest.hookimpl(hookwrapper=True)
def pytest_runtest_makereport(item, call):
    outcome = yield
    report = outcome.get_result()

    if report.when == "call" and report.failed:
        page = item.funcargs.get("page")
        if page:
            screenshot_path = save_screenshot(page, item.name)
            logger.error(f"Test failed: {item.name}")
            allure.attach.file(
                screenshot_path,
                name="Failure Screenshot",
                attachment_type=allure.attachment_type.PNG
            )