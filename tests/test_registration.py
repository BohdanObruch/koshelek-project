from koshelek_project.data.user_data import *
import pytest
import allure


class TestRegistration:

    @pytest.fixture(autouse=True)
    def setup(self, registration):
        self.registration = registration
        self.registration.verify_url_page_and_form_visible()

    def alert_info_message(self, locator, message):
        self.registration.verify_alert_message(locator, self.registration.alert_message, message)

    def fill_data(self, username, email, password, referral_code, alert_message=None):
        self.registration.fill_username(username)
        if alert_message:
            self.alert_info_message(self.registration.username, alert_message)
        self.registration.fill_email(email)
        self.registration.fill_password(password)
        self.registration.fill_referral_code(referral_code)

    def submit_registration(self):
        self.registration.check_user_agreement()
        self.registration.click_on_submit_button()

    def verify_field(self, field, expected_color, message_type, expected_message):
        self.registration.verify_alert_color(field, expected_color)
        self.registration.verify_alert_message(field, message_type, expected_message)



    @pytest.mark.parametrize(
        "username, email, password, referral_code, username_message, email_message, password_message", [
            (invalid.username, invalid.email, invalid.password,
             invalid.referral_code,
             'Допустимые символы (от 6 до 32): a-z, 0-9, _. Имя должно начинаться с буквы',
             'Формат e-mail: username@test.ru',
             'Пароль должен содержать минимум 8 символов'),
            (empty.username, empty.email, empty.password,
             empty.referral_code,
             'Поле не заполнено',
             'Поле не заполнено',
             'Поле не заполнено'),
            (with_spase.username, with_spase.email, with_spase.password,
                with_spase.referral_code,
             'Поле не заполнено',
             'Поле не заполнено',
             'Поле не заполнено')
        ],ids=['invalid_data', 'empty_data', 'with_space_data'])
    def test_registration_with_various_data(self, request, registration, username, email, password, referral_code,
                                            username_message, email_message, password_message):
        allure.dynamic.title(f'Registration with various data: {request.node.callspec.id}')
        self.fill_data(username, email, password, referral_code)
        self.submit_registration()

        self.verify_field(registration.username, registration.red_color_border, registration.alert_message,
                            username_message)
        self.verify_field(registration.email, registration.red_color_border, registration.alert_message,
                            email_message)
        self.verify_field(registration.password, registration.red_color_border, registration.error_message,
                            password_message)


    @allure.title('Registration with correct data and without user agreement')
    def test_registration_without_user_agreement_and_correct_data(self, registration):
        self.fill_data(correct.username, correct.email, correct.password, correct.referral_code)
        registration.click_on_submit_button()

        registration.verify_alert_color(registration.user_agreement, registration.red_color_checkbox)

    @pytest.mark.parametrize(
        "user_data, username_message", [
            (max_count_and_one, 'Превышен лимит символов: 32 максимум'),
            (with_hyphen, f'Введены недопустимые символы: {with_hyphen.username}'),
        ], ids=['max_count_and_one', 'with_hyphen']
    )
    def test_registration_with_max_count_data_and_one(self, request, registration, user_data, username_message):
        allure.dynamic.title(f'Registration with various data: {request.node.callspec.id}')
        self.fill_data(user_data.username, user_data.email, user_data.password, user_data.referral_code,
                       alert_message=username_message)
        self.submit_registration()

        self.verify_field(registration.username, registration.red_color_border, registration.alert_message,
                            'Допустимые символы (от 6 до 32): a-z, 0-9, _. Имя должно начинаться с буквы')
        self.verify_field(registration.password, registration.red_color_border, registration.error_message,
                            'Пароль должен содержать от 8 до 64 символов, включая заглавные буквы и цифры')
        self.verify_field(registration.referral_code, registration.red_color_border, registration.alert_message,
                            'Неверный формат ссылки')

    @allure.title('Registration with hebrew data')
    def test_registration_with_hebrew_data(self, registration):
        self.fill_data(with_hebrew.username, with_hebrew.email, with_hebrew.password,
                       with_hebrew.referral_code, alert_message=f'Введены недопустимые символы: {with_hebrew.username}')
        self.submit_registration()

        self.verify_field(registration.username, registration.red_color_border, registration.alert_message,
                            'Допустимые символы (от 6 до 32): a-z, 0-9, _. Имя должно начинаться с буквы')
        self.verify_field(registration.password, registration.red_color_border, registration.error_message,
                            'Пароль должен содержать от 8 до 64 символов, включая заглавные буквы и цифры')

    @allure.title('Registration with cross script data')
    def test_registration_with_cross_script_data(self, registration):
        self.fill_data(with_cross_script.username, with_cross_script.email, with_cross_script.password,
                       with_cross_script.referral_code,
                       alert_message='Введены недопустимые символы: &lt;&gt;(&quot;)&#x2F;')
        self.submit_registration()

        self.verify_field(registration.username, registration.red_color_border, registration.alert_message,
                            'Допустимые символы (от 6 до 32): a-z, 0-9, _. Имя должно начинаться с буквы')
        self.verify_field(registration.email, registration.red_color_border, registration.alert_message,
                          'Формат e-mail: username@test.ru')
        self.verify_field(registration.referral_code, registration.red_color_border, registration.alert_message,
                          'Неверный формат ссылки')

    @allure.title('Registration with sql injection data')
    def test_registration_with_sql_injection_data(self, registration):
        self.fill_data( with_sql_injection.username, with_sql_injection.email, with_sql_injection.password,
                          with_sql_injection.referral_code,
                       alert_message='Введены недопустимые символы: ;')
        self.submit_registration()

        self.verify_field(registration.username, registration.red_color_border, registration.alert_message,
                            'Допустимые символы (от 6 до 32): a-z, 0-9, _. Имя должно начинаться с буквы')
        self.verify_field(registration.email, registration.red_color_border, registration.alert_message,
                            'Формат e-mail: username@test.ru')
        self.verify_field(registration.password, registration.red_color_border, registration.error_message,
                            'Пароль должен содержать от 8 до 64 символов, включая заглавные буквы и цифры')
        self.verify_field(registration.referral_code, registration.red_color_border, registration.alert_message,
                            'Неверный формат ссылки')


    @pytest.mark.parametrize(
        "user_data, password_message, referral_message", [
            (max_count,
             'Пароль должен содержать от 8 до 64 символов, включая заглавные буквы и цифры',
             'Неверный формат ссылки'),
            (with_max_number,
             'Пароль должен содержать от 8 до 64 символов, включая заглавные буквы и цифры',
             'Неверный формат ссылки')
        ], ids=['max_count', 'with_max_number'])
    def test_registration_with_max_values(self, request, registration, user_data, password_message, referral_message):
        allure.dynamic.title(f'Registration with various data: {request.node.callspec.id}')
        self.fill_data(user_data.username, user_data.email, user_data.password, user_data.referral_code)
        self.submit_registration()

        self.verify_field(registration.password, registration.red_color_border, registration.error_message,
                            password_message)
        self.verify_field(registration.referral_code, registration.red_color_border, registration.alert_message,
                            referral_message)