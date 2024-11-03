from .main_page import MainPage
from playwright.sync_api import expect
import re
import allure


class RegistrationPage(MainPage):
    def __init__(self, page):
        super().__init__(page)
        self.signup_url = '/authorization/signup'
        self.viewport = '[data-wi="viewport"]'
        self.shadow_root = self.page.locator(self.viewport)
        self.title_form = '[data-wi="title"]'
        self.form = '[data-wi="form"]'
        self.input = 'input'
        self.username = '[data-wi="user-name"]'
        self.email = '[data-wi="identificator"]'
        self.password = '[data-wi="password"]'
        self.referral_code = '[data-wi="referral"]'
        self.user_agreement = '[data-wi="user-agreement"] .v-input__control'
        self.submit_button = '[data-wi="submit-button"]'
        self.red_color_border = 'rgb(118, 118, 118)'
        self.red_color_checkbox = 'rgb(255, 255, 255)'
        self.alert_message = '[data-wi="message"]'
        self.error_message = '[data-wi="error"]'


    def verify_url_page_and_form_visible(self):
        with allure.step('Verify url page and form is visible'):
            self.page.wait_for_selector(self.form)
            expect(self.page).to_have_url(re.compile(self.signup_url))
            expect(self.shadow_root.locator(self.form)).to_be_visible()

    def fill_username(self, username):
        with allure.step(f'Fill username: {username}'):
            self.shadow_root.locator(f'{self.username} {self.input}').fill(username)

    def fill_email(self, email):
        with allure.step(f'Fill email: {email}'):
            self.shadow_root.locator(f'{self.email} {self.input}').fill(email)

    def fill_password(self, password):
        with allure.step(f'Fill password: {password}'):
            self.shadow_root.locator(f'{self.password} {self.input}').fill(password)

    def fill_referral_code(self, referral_code):
        with allure.step(f'Fill referral code: {referral_code}'):
            self.shadow_root.locator(f'{self.referral_code} {self.input}').fill(referral_code)

    def check_user_agreement(self):
        with allure.step('Check user agreement'):
            self.shadow_root.locator(self.user_agreement).click()

    def click_on_submit_button(self):
        with allure.step('Click on submit button'):
            self.shadow_root.locator(self.submit_button).click()

    def verify_alert_color(self, locator, color):
        with allure.step(f'Verify alert color: {color} for locator: {locator}'):
            expect(self.shadow_root.locator(locator).locator(self.input)).to_have_css('border-color', color)

    def verify_alert_message(self, locator, alert, message):
        with allure.step(f'Verify alert message: {message} for locator: {locator})'):
            expect(self.shadow_root.locator(locator).locator(alert)).to_have_text(message)