from playwright.sync_api import Page
import allure


class BasePage:
    def __init__(self, page: Page):
        self.page = page

    def navigate(self, url: str = '/'):
        with allure.step(f'Open page: {url}'):
            self.page.goto(url)
