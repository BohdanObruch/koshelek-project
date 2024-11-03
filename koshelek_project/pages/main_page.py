from .base_page import BasePage
from playwright.sync_api import expect
import allure


class MainPage(BasePage):
    def __init__(self, page):
        super().__init__(page)
        self.registration_button = '[data-wi="widget-item-1"][class*="signup"]'
        self.header = '#app-header'

    def verify_headed_visible(self):
        with allure.step('Verify header is visible'):
            self.page.wait_for_selector(self.header)
            expect(self.page.locator(self.header)).to_be_visible()

    def click_on_registration_button(self):
        with allure.step('Click on registration button'):
            self.page.locator(self.registration_button).click()
