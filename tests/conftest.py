import pytest
from playwright.sync_api import Page, Browser, BrowserContext
from koshelek_project.pages.main_page import MainPage
from koshelek_project.pages.registration_page import RegistrationPage
import allure

from koshelek_project.utils.registration_helpers import RegistrationHelpers


def pytest_addoption(parser):
    parser.addoption("--size", action="store", default="1920,1080", help="browser window size")


@pytest.fixture(scope="session")
def browser_context_args(browser_context_args, request):
    device = request.config.getoption("--device")
    if device:
        return {
            **browser_context_args
        }
    else:
        width, height = map(int, request.config.getoption("--size").split(","))
        return {
            **browser_context_args,
            "viewport": {"width": width, "height": height},
            "screen": {"width": width, "height": height}

        }



@pytest.fixture(scope="function")
def page(context: BrowserContext) -> Page:
    page = context.new_page()
    yield page
    page.close()


@pytest.fixture(scope="function")
def context(browser: Browser, browser_context_args) -> BrowserContext:
    context = browser.new_context(**browser_context_args)
    yield context
    context.close()


@pytest.hookimpl(tryfirst=True, hookwrapper=True)
def pytest_runtest_makereport(item, call):
    outcome = yield
    rep = outcome.get_result()

    setattr(item, "rep_" + rep.when, rep)

@pytest.fixture(autouse=True)
def allure_attach(request, page: Page, context: BrowserContext):
    yield context

    # Get device or screen size info
    device = request.config.getoption("--device")
    size = request.config.getoption("--size")

    viewport_size = page.viewport_size
    width = viewport_size['width']
    height = viewport_size['height']

    if device:
        screen_size_info = f"Device: {device}, Screen Size: {width}x{height}"
    elif size:
        width, height = map(int, size.split(","))
        screen_size_info = f"Screen Size: {width}x{height}"
    else:
        screen_size_info = f"Screen Size: {width}x{height}"

    # Attach screen size info
    allure.attach(screen_size_info, name="Screen Size Info", attachment_type=allure.attachment_type.TEXT)

    if request.node.rep_call.failed:
        # Capture screenshot
        screenshot_path = f"reports/{request.node.name}.png"
        page.screenshot(path=screenshot_path)
        allure.attach.file(screenshot_path, name="Screenshot", attachment_type=allure.attachment_type.PNG)

        # Capture stack trace
        allure.attach(str(request.node.rep_call.longreprtext), name="Stack Trace",
                      attachment_type=allure.attachment_type.TEXT)

        # Handle video recording
        context.close()
        page.video.save_as(f"reports/videos/{request.node.name}.webm")
        video_path = page.video.path()
        allure.attach.file(video_path, name="Video", attachment_type=allure.attachment_type.WEBM)

@pytest.fixture
def main(page):
    return MainPage(page)

@pytest.fixture
def registration(page):
    return RegistrationPage(page)

@pytest.fixture(autouse=True)
def go_to_registration_page(main):
    main.navigate()
    main.verify_headed_visible()
    main.click_on_registration_button()


@pytest.fixture
def registration_helpers(registration):
    return RegistrationHelpers(registration)